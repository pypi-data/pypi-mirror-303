import polars as pl
import pandas as pd
import re
import boto3
from dataclasses import dataclass
import os
import pkg_resources
import numpy as np

from z_score_target_engagement.class_process_utils import ProcessUtils


pd.options.mode.chained_assignment = None

module_dir = os.path.dirname(__file__)


# Read in list of high abundance batches to ignore

bad_batch_path = pkg_resources.resource_filename('z_score_target_engagement', 
                                                 'data/bad_batches.txt')

with open(bad_batch_path, 'r') as file:
    bad_batches = file.read()
bad_batches = bad_batches.strip()
bad_batches = bad_batches.split("\n")

@dataclass
class DataContainer:
    path: str

    # To be computed
    filetype: str = None # diann or encyclopedia
    datatype: str = None # protein or peptide
    raw_df: pd.DataFrame = None
    batches: list = None
    normalized_df: pd.DataFrame = None
    z_scores: pd.DataFrame = None
    median_z_scores: pd.DataFrame = None # only for peptide data
    melted_z_scores: pd.DataFrame = None
    all_data: pd.DataFrame=None

    def __post_init__(self):
        self._detect_filetype()
        self._detect_datatype()

    def _detect_filetype(self):
        if self.filetype is None:
            if "encyclopedia" in self.path:
                self.filetype = "encyclopedia"
            # Otherwise keep the default of "diann"
            else:
                self.filetype = "diann"
            
    def _detect_datatype(self):
        if self.datatype is None:
            if "pr_matrix" in self.path or "peptides" in self.path:
                self.datatype = "peptide"
            elif "pg_matrix" in self.path or "proteins" in self.path:
                self.datatype = "protein"
            else:
                raise ValueError("Unable to determine data type from path.")

@dataclass
class DataLoader(ProcessUtils):


    def load_data(self, path,
                  filetype=None,
                  datatype=None,
                  target=None,
                  batch=None,
                  get_batches=False,
                  include_stripped_sequence=False,
                  merge_type='left'):
        
        if isinstance(path, list) and len(path) == 2:
            merge_data = True
        else:
            merge_data = False

        if isinstance(path, list) and len(path) > 2:
            raise ValueError("Data loading is only supported with max 2 paths.")
        
        # Instantiate DataContainer
        data_container = DataContainer(path,
                                       filetype=filetype,
                                       datatype=datatype)
        
        if data_container.datatype == "protein" and include_stripped_sequence:
            raise TypeError("Stipped sequences are only available for peptide"
                            " files.")

        if merge_data:
            path_list = path
            path = path_list[0]

        if get_batches:
            data_container.batches = self.get_batches(data_container.path)
        
        lazy_df = self._load_lazy_df(path)

        # Filter for targets, if provided
        if target is not None:
            lazy_df = self._filter_targets(data_container.filetype, 
                                           lazy_df,
                                           target)

        # Collect all column names for filtering
        df = self._select_columns_of_interest(data_container, 
                    lazy_df,
                    include_stripped_sequence=include_stripped_sequence,
                    batch=batch)
        
        # If a second path is given, load and merge that path
        if merge_data:
            # collect the smaller df to get info on targets. Convert to 
            # diann style if encyclopedia
            data_container.raw_df = df.collect(streaming=True).to_pandas()
            if data_container.filetype == "encyclopedia":
                data_container = self._convert_encyclopedia_file(data_container)
            df = data_container.raw_df
            merge_targets = df["Genes"].unique()
            df = pl.from_pandas(df).lazy() # back to lazy dataframe

            second_lazy_df = self._load_lazy_df(path_list[1])
            second_lazy_df = self._filter_targets("diann",
                                                  second_lazy_df,
                                                  merge_targets)
            second_lazy_df = self._select_columns_of_interest(data_container, 
                                                              second_lazy_df,
                                                              batch=batch)

            df = df.join(second_lazy_df,
                         on=DataLoader._detect_id_columns(data_container),
                         how=merge_type)

        # Collect the DataFrame
        df = df.collect(streaming=True).to_pandas()

        if "Genes" in df.columns:
            df["Genes"] = df["Genes"].astype("category")

        data_container.raw_df = df

        return data_container
    
    @staticmethod
    def extract_unique_genes(df):
        return list(set(gene for genes in df["Genes"] \
                         for gene in genes.split(";")))
    

    def _filter_targets(self, filetype, lazy_df, target):
        if not isinstance(target, (list, str, set, np.ndarray)):
            raise TypeError("Target must be a string, list, set, or array.")
        
        if isinstance(target, str):
            target = [target]

        #TODO: sort this out for diann vs encyclopedia
        if filetype == "diann" and target is not None:
            lazy_df = lazy_df.filter(pl.col("Genes").is_in(target))
        elif filetype == "encycolopedia" and target is not None:
            raise NotImplementedError("Target filtering for encyclopedia data" \
                                      " has yet to be implemented.")
        return lazy_df
    
    def _get_run_columns(self, all_columns, batch):
        if not isinstance(batch, (list, str)):
            raise TypeError("Target should be string or list of strings.")
        if isinstance(batch, str):
            batch = [batch]
        return [col for col in all_columns \
                if any(b in col for b in batch) and col not in bad_batches]
        

    def _select_columns_of_interest(self,
                                    data_container,
                                    lazy_df,
                                    include_stripped_sequence=False,
                                    batch=None):
        #TODO: There's probably a more elegant way of sharing datatype info...
        id_cols = DataLoader._detect_id_columns(data_container)

        all_columns = lazy_df.collect_schema().names()

        if batch:
            selected_cols = id_cols + self._get_run_columns(all_columns, batch)
        else: # get all columns
            selected_cols = id_cols + [col for col in all_columns \
                                      if (col.endswith(".d") \
                                          or col.endswith(".mzML")) \
                                        and col not in bad_batches]
        if data_container.filetype == "diann" and include_stripped_sequence:
            selected_cols.append("Stripped.Sequence")

        return lazy_df.select(selected_cols)
    
    @staticmethod
    def _detect_id_columns(data):
        # This seems like it can be simplified but both code blocks are 
        # needed for the case where the DataContainer is empty
        if not isinstance(data, (DataContainer, pd.DataFrame)):
            raise TypeError("Expected DataContainer or DataFrame. "
                            f"Got {type(data)}")
        
        if isinstance(data, DataContainer):
            if data.filetype == "diann":
                if data.datatype == "protein":
                    return ["Protein.Ids", "Genes"]
                else:
                    return ["Protein.Ids", "Genes", "Precursor.Id"]
            else: # encyclopedia
                if data.datatype == "protein":
                    return ["Protein"]
                else:
                    return ["Peptide", "Protein"]
                
        # If it's a dataframe        
        if "Protein.Ids" in data.columns:
            if "Precursor.Id" in data.columns:
                return ["Protein.Ids", "Genes", "Precursor.Id"]
            else:
                return ["Protein.Ids", "Genes"]
        elif "Peptide" in data.columns:
            return ["Peptide", "Protein"]
        else:
            return ["Protein"]

    @staticmethod
    def _detect_file_format(path):
        if path.endswith(".csv"):
            return "csv"
        elif path.endswith(".tsv") or path.endswith(".txt"): # encylopedia paths end with .txt despite being tsv
            return "tsv"
        else:
            raise ValueError(f"Unsupported file format for file: {path}")

    @staticmethod
    def _load_lazy_df(path):
        file_format = DataLoader._detect_file_format(path)
        sep = "," if file_format == "csv" else "\t"
        if path.startswith("s3"):
            storage=DataLoader.get_storage_options()
            lazy_df = pl.scan_csv(path,
                        separator=sep,
                        storage_options=storage,
                        infer_schema_length=10000,
                        )
        else:
            lazy_df = pl.scan_csv(path,
                        separator=sep,
                        infer_schema_length=10000,
                        )
        
        return lazy_df

    @staticmethod
    def get_batches(path):
        if isinstance(path, str):
            path = [path]
        batches = []
        for p in path:
            lazy_df = DataLoader._load_lazy_df(p)
            column_names = lazy_df.collect_schema().names()
            p_batches = []
            for column in column_names:
                batch = re.search(r'SET\d+(-\d+)?REP\d+(-\d+)?', column)
                if isinstance(batch, re.Match):
                    p_batches.append(batch[0])
            batches += list(set(p_batches))
        return batches

    @staticmethod
    def get_storage_options() -> dict[str, str]:
        """Get AWS credentials to enable polars scan_parquet functionality.
        """
        credentials = boto3.Session().get_credentials()
        return {
            "aws_access_key_id": credentials.access_key,
            "aws_secret_access_key": credentials.secret_key,
            "session_token": credentials.token,
            "aws_region": "us-west-2",
        }
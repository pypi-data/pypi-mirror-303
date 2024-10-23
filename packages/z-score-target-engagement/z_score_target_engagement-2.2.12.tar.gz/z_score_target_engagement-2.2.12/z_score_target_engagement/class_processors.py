import pandas as pd
import numpy as np
from dataclasses import dataclass
from tqdm import tqdm

from z_score_target_engagement.class_process_utils import ProcessUtils
from z_score_target_engagement.data_utils import *

@dataclass
class PeptideProcessor(ProcessUtils):

    progress_bar: bool=True

    def __post_init__(self):
        super().__post_init__()

    def process_and_normalize(self, data_container,
                              process_by_batch=False,
                              copy=True,
                              normalize_abundance=False):
        
        if data_container.datatype == "protein":
            raise ValueError("Function received protein data. \
                             Provide petide data or use ProteinProcessor.")

        if data_container.filetype == "encyclopedia":
            data_container = self._convert_encyclopedia_file(data_container)
        
        if copy:
            pep_df = data_container.raw_df.copy()
        else:
            pep_df = data_container.raw_df
            # raise Warning("Modiying raw_df. Set copy=True to avoid this.")
        
        pep_df["Genes"] = pep_df["Genes"].astype(str)
        if self.label_tfs:
            pep_df = self._label_tfs(pep_df)

        if process_by_batch:

            id_cols = DataLoader._detect_id_columns(data_container)

            processed_batch_dfs = []

            if data_container.batches is None:
                data_container.batches = ProcessUtils \
                    .get_batches(data_container.path)
            
            for batch in tqdm(data_container.batches, 
                              desc="Processing Batches", 
                              unit="batch"):
                """Yes this will extract batches from multiple screens if there
                are SET1REP1 in several batches for example. But the 
                _get_batch_compound_name will append the screen name to the 
                batch (if label_screens=True) so the true batches will be
                preserved for median normalization."""
                chunk_cols = [col for col in pep_df.columns if batch in col]
                subdf = pep_df[id_cols+chunk_cols]
                pivot_df = self._melt_pivot_df(subdf)
                pivot_df = self.log_transform(pivot_df)
                pivot_df = self._get_batch_compound_names(pivot_df)
                if normalize_abundance:
                    normalized_df = self._normalize_abundance(pivot_df)
                else:
                    normalized_df = self._median_normalize(pivot_df)
                processed_batch_dfs.append(normalized_df)

            normalized_df = pd.concat(processed_batch_dfs)
        else:
            pivot_df = self._melt_pivot_df(pep_df)
            pivot_df = self.log_transform(pivot_df)
            pivot_df = self._get_batch_compound_names(pivot_df)
            if normalize_abundance:
                    normalized_df = self._normalize_abundance(pivot_df)
            else:
                normalized_df = self._median_normalize(pivot_df)

        if self.label_screens:
            normalized_df = self._split_batch_screen(normalized_df)
        normalized_df = self._drop_nan_cols(normalized_df)

        if normalized_df.empty:
            raise Exception("Dataframe is empty after dropping NaNs. \
                            Try raising dropna_percent_threshold.")
        data_container.normalized_df = normalized_df
    

    def _is_tf_append(self, gene: str) -> str:
        """Check if a gene is a transcription factor or not.

        Example: 'STAT3' -> 'STAT3_True'
                 'NONO' -> 'NONO_False'

        Args:
            gene (str): gene ID

        Returns:
            str: gene ID appended with transcription factor status
        """
        gene_list = gene.split(';')
        is_tf = any(gene in self.tf_list for gene in gene_list)
        return f"{gene}_{str(is_tf)}"
    
    def _label_tfs(self, df: pd.DataFrame, 
                   new_column: bool=False) -> pd.DataFrame:
        """ Overwrite the superclass method to label genes with their 
        transcription factor status.

        Args:
            df (pd.DataFrame): A dataframe with a "Genes" column
            new_column (bool): If True, add a new column with the boolean 
                transcription factor status.
                If False (default), append the transcription factor status
                to the gene string.
        
        Returns:
            pd.DataFrame: The original dataframe with the genes labeled with
            their transcription factor status.
        """
        if not new_column:
            df["Genes"] = df["Genes"].apply(self._is_tf_append)
        else:
            df["Is TF"] = df["Genes"].apply(self._is_tf)
        return df

    @staticmethod
    def melt_raw_df(raw_df: pd.DataFrame) -> pd.DataFrame:
        """Melt a dataframe with mass spec runs as columns so that new 
        dataframe has "Compound" (filename for now) and "Abundance" as columns
        in addition to the ID columns.

        Args:
            raw_df (pd.DataFrame): Dataframe from diann or encyclopedia with 
            mass spec runs as columns

        Returns:
            pd.DataFrame: Melted dataframe with mass spec filenames as rows.
        """
        # Restructure df so columns are peptides
        id_vars = DataLoader._detect_id_columns(raw_df)    
        melt_df = raw_df.melt(id_vars=id_vars, # Melt so filename is col.
                                    var_name="Compound",
                                    value_name="Abundance")
        return melt_df

    @staticmethod
    def log_transform(df: pd.DataFrame) -> pd.DataFrame:
        """Take the log of all the quantitative columns in a dataframe

        Args:
            df (pd.DataFrame): A dataframe with linear scale abundance values.

        Returns:
            pd.DataFrame: The dataframe with abundance values in log scale.
        """
        # Get the quantitative column names
        try:
            quant_cols = [col for col in df.columns \
                        if (col.endswith(".d") or col.endswith(".mzML"))]
        except AttributeError: # occurs if the df is already multiindexed
            quant_cols = [col for col in df.columns if col not in \
                          [("Compound","",""),
                           ("batch", "", ""),
                           ("screen", "", "")]
            ]

        # Log transform 
        quant_pep_df = df.replace({None: np.nan,
                                       0: np.nan}).infer_objects(copy=False)
        quant_pep_df[quant_cols] = np.log(quant_pep_df[quant_cols] \
                                          .astype(float))
        return quant_pep_df

    @staticmethod
    def _melt_pivot_df(pep_df):

        melt_df = PeptideProcessor.melt_raw_df(pep_df)

        id_vars = DataLoader._detect_id_columns(pep_df)
        pivoted_df = melt_df.pivot(index="Compound", 
                                   columns=id_vars,
                                   values="Abundance")
        pivoted_df.reset_index(inplace=True) # Make compound a normal column
        return pivoted_df
    
    @staticmethod
    def get_quant_cols(df: pd.DataFrame) ->list:
        """Get a list of column names where the values are floats.

        Args:
            df (pd.DataFrame): A data frame with abundance values

        Returns:
            list: A list of column names for columns with float values.
        """
        non_quant_cols = [("Compound", "", ""),
                          ("batch", "",""),
                          ("screen", "", ""),
                          ("Filename", "", ""),
                          "Compound",
                          "batch",
                          "screen"
                          "Filename"]
        return [col for col in df.columns if col not in non_quant_cols]

    def _normalize_abundance(self, pivot_df):
        # Isolate the abundance columns
        quant_cols = PeptideProcessor.get_quant_cols(pivot_df)
        pivot_df_quant = pivot_df[quant_cols]

        # Get the median of the entire data frame
        overall_median = pivot_df_quant.median().median()

        # Median normalize by batch
        normalized = self._median_normalize(pivot_df)

        # Add back the overall median to every data point
        normalized[quant_cols] = normalized[quant_cols] + overall_median

        # Go back to linear scale for all abundance columns
        normalized[quant_cols] = np.exp(normalized[quant_cols])

        return normalized

    def melt_multiindex_df(self, multi_index_df, value_name="Abundance"):
        df = multi_index_df.copy()
        id_cols = ['screen__', 'batch__', 'Compound__']
        if "Compound__" not in df.columns: # Prevent splitting mutlitple times
            df.columns = ['_'.join([str(i) for i in col]).strip() \
                            for col in df.columns] # Combine mulitindex columns
        df_melted = pd.melt(
                    df, 
                    id_vars=id_cols,
                    value_vars=[col for col in df.columns \
                                if col not in id_cols],
                    var_name='multiindex', 
                    value_name=value_name
                )
        if len(df_melted.iloc[0]["multiindex"].split("_")) == 3:
            new_cols = ['Protein.Ids', 'Genes', 'Precursor.Id']
        else:
            new_cols = ['Protein.Ids', 'Genes', 'Is TF', 'Precursor.Id']
        df_melted[new_cols] = df_melted['multiindex'] \
            .str.split('_', expand=True)
        df_melted = df_melted.drop(columns=['multiindex'])
        df_melted = df_melted.rename(columns= \
                                    {key: key.rstrip("_") for key in id_cols})
        return df_melted

        

    def _median_normalize(self, pivot_df):
        batchcol = ("batch", "","") if ("batch", "","") in pivot_df.columns \
                    else "batch"

        # Drop empty batches
        pivot_df = pivot_df.groupby(batchcol, observed=False).filter( \
            lambda x: not x.iloc[:,2:].isna().all().all())
        if pivot_df.empty:
            return pivot_df

        def subtract_median(group):
            if group.empty:
                return group
            # Check if the group contains any non-NaN values
            non_nan_values = group.iloc[:, 2:]  # Skip the first two columns
            if non_nan_values.isna().all().all():
                return group  # Return group unchanged if all values are NaN
            return group - group.median().median()
            
        pivot_df.index = pivot_df["Compound"] # Temporarily make compound the index
        pivot_df.drop(columns=["Compound"], inplace=True)

        normalized_df = pivot_df.groupby(batchcol, observed=False) \
            .apply(subtract_median, include_groups=True)
        normalized_df = normalized_df.reset_index() # Remove batch from index
        return normalized_df


    def join_melted_dfs(self, data_container: DataContainer):
        # Process the raw df
        pivot_df = self._melt_pivot_df(data_container.raw_df)
        pivot_df = self._get_batch_compound_names(pivot_df)
        pivot_df = self._split_batch_screen(pivot_df)
        melt_raw = self.melt_multiindex_df(pivot_df, value_name="Raw Abundance")

        if self.label_tfs:
            melt_raw = self._label_tfs(melt_raw, new_column=True)

        # Process the normalized df if there is one
        if isinstance(data_container.normalized_df, pd.DataFrame):
            melt_normalized = self \
                .melt_multiindex_df(data_container.normalized_df)
            melt_raw["Normalized Abundance"] = \
                melt_normalized["Abundance"]

        # Process Z score df if there is one
        if isinstance(data_container.melted_z_scores, pd.DataFrame):
            melt_raw["Z Score"] = data_container.melted_z_scores["Z Score"]
            melt_raw["med Z Score"] = data_container \
                .melted_z_scores["med Z Score"]
        
        data_container.all_data = melt_raw.dropna()


@dataclass
class ProteinProcessor(ProcessUtils):
    

    def __post_init__(self):
        super().__post_init__()

    def process_and_normalize(self,
                              data_container,
                              keep_filenames=True,
                              normalize_abundance=False):
        # If normalize_abundance is true, then we'll median normalize,
        # add back in the median for the screen (as proxy for cell type) and 
        # then convert back to linear scale. Otherwise we'll just median 
        # normalized everything by batch so all medians will be 0 and everything 
        # remains log scale.
        if data_container.datatype == "peptide":
            raise ValueError("Function received peptide data. \
                Supply a protein DataContainer or use PeptideProcessor.")
        
        # Melt df so that columns are ["Protein.Ids", "Genes", "Compound",
        # "Abundance", and "batch"]
        prot_df = data_container.raw_df.copy()
        melt_df = self._melt_df(prot_df)
        melt_df = self._get_batch_compound_names(melt_df,
                                                 keep_filenames=keep_filenames)

        if self.label_tfs: # Add column "Is TF" with bools
            melt_df = self._label_tfs(melt_df)

        # Normalize
        if normalize_abundance:
            normalized = self._normalize_abundance(melt_df)
        else:
            normalized = self._median_normalize(melt_df)
            if self.label_screens:
                normalized = self._split_batch_screen(normalized)

        # Drop rows where abundance is nan and put in data_container
        data_container.normalized_df = normalized.loc \
            [normalized["Abundance"].notna()]

    def _normalize_abundance(self, melt_df):
        # Get the median (log) abundances
        overall_median = melt_df["Abundance"].median()
        
        # Median normalize per usual and separate batch and screen into columns
        normalized = self._median_normalize(melt_df)
        normalized = self._split_batch_screen(normalized)

        # Add back the overall median
        normalized["Abundance"] = normalized["Abundance"] + overall_median
        
        # Go back to linear scale
        normalized["Abundance"] = np.exp(normalized["Abundance"])

        return normalized

        
    def _melt_df(self, prot_df):

        quant_cols = [col for col in prot_df.columns \
                      if (col.endswith(".d") or col.endswith(".mzML"))]

        # Log transform 
        quant_pep_df = prot_df.replace({None: np.nan,
                                        0: np.nan}).infer_objects(copy=False)
        quant_pep_df[quant_cols] = np.log(quant_pep_df[quant_cols] \
                                          .astype(float))

        df = quant_pep_df[["Protein.Ids", "Genes"] + quant_cols]
        df = self._drop_nan_cols(df)
        if df.empty:
            raise Exception("Dataframe is empty after dropping NaNs. \
                            Try lowering dropna_percent_threshold.")
        melt_df = df.melt(id_vars=["Protein.Ids", "Genes"],
                          var_name="Compound",
                          value_name="Abundance")
        melt_df = melt_df.loc[melt_df["Abundance"].notna()]
        return melt_df

    def _median_normalize(self, melt_df):
        def subtract_median(group):
            # For a protein in a batch, subtractract the median abundance
            group["Abundance"] = group["Abundance"] - \
                group["Abundance"].median()
            return group
        normalized_df = melt_df.groupby(["Genes", "batch"], observed=False) \
            .apply(subtract_median, include_groups=False).reset_index()
        dropcol = [col for col in normalized_df.columns \
                   if col.startswith("level")][0]
        normalized_df = normalized_df.drop(columns=dropcol)
        return normalized_df
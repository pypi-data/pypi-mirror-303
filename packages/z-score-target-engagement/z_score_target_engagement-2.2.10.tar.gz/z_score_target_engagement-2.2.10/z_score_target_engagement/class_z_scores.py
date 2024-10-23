import pandas as pd
from dataclasses import dataclass
import os
from tqdm import tqdm



# Turn off annoying pandas warnings
pd.options.mode.chained_assignment = None
pd.set_option("future.no_silent_downcasting", True)

module_dir = os.path.dirname(__file__)


@dataclass
class ProteinZScoreCalculator:

    
    def _compute_z_score(self, subdf):
        # Get the median abundance for the current screen
        med = subdf["Abundance"].median()

        # Get median absolute deviation
        subdf["abs dev"] = abs(subdf["Abundance"] - med)
        MAD = subdf["abs dev"].median()
        subdf.drop(columns=["abs dev"], inplace=True)

        # Calculate Z Score
        subdf["Z Score"] = (subdf["Abundance"] - med) / MAD
        return subdf

    def _get_median_z_score(self, z_scores):
        if "screen" in z_scores.columns.to_list():
            groups = ["screen", "Genes", "Compound"]
        else:
             groups = ["Genes", "Compound"]
        z_scores["med Z Score"] = z_scores.groupby(groups)["Z Score"] \
            .transform('median')
        return z_scores

    def compute_z_score(self, data_container):
        if data_container.datatype == "peptide":
            raise ValueError("Function received peptide data. \
                Provide protein data or use PeptideZScoreCalculator.")
        
        data = data_container.normalized_df.copy()
        if "screen" in data.columns.to_list():
            groups = ["screen", "Genes"]
        else:
             groups = ["Genes"]
        z_scores = data.groupby(groups).apply(self._compute_z_score, 
                                              include_groups=False) \
                                              .reset_index()
        z_scores = self._get_median_z_score(z_scores)

        dropcol = [col for col in z_scores if col.startswith("level")]
        z_scores = z_scores.drop(columns=dropcol)
        data_container.z_scores = z_scores


@dataclass
class PeptideZScoreCalculator:

    def _compute_z_score(self, subdf):
        # Get median abundance for all peptides in the protein
        quant_cols = [col for col in subdf.columns \
                      if col not in [('batch', '', ''),\
                                      ('Compound', '', ''), ('screen', '', '')]]

        for column in tqdm(quant_cols, 
                            desc="Computing peptide z scores", 
                            unit="peptide"):
            MAD = abs(subdf[column] - subdf[column].median()).median()
            subdf[column] = (subdf[column] - subdf[column].median())/MAD
        return subdf
    
    @staticmethod
    def _check_data_type(data_container):
        if data_container.datatype == "protein":
            raise ValueError("Function received protein data. \
                Provide peptide data or use ProteinZScoreCalculator.")


    def compute_z_score(self, data_container):

        self._check_data_type(data_container)
        
        data = data_container.normalized_df
            
        if ("screen", "", "") in data.columns.to_list():
            groups = [("screen", "", "")]
            z_scores = data.groupby(groups).apply(self._compute_z_score, 
                                                  include_groups=False) \
                                                  .reset_index()
        else:
            z_scores = self._compute_z_score(data)

        dropcol = [col for col in z_scores.columns \
                   if col[0].startswith("level")]
        z_scores = z_scores.drop(columns=dropcol)
        data_container.z_scores = z_scores

        self.melt_z_score_df(data_container)

    @staticmethod
    def _get_median_z_score(melted_z_scores):
        if "screen" in melted_z_scores.columns.to_list():
            groups = ["screen", "Genes", "Compound", "Precursor.Id"]
        else:
             groups = ["Genes", "Compound", "Precursor.Id"]
        melted_z_scores["med Z Score"] = melted_z_scores \
            .groupby(groups)["Z Score"].transform('median')
        return melted_z_scores
    
    @staticmethod
    def melt_z_score_df(data_container):
        PeptideZScoreCalculator._check_data_type(data_container)

        z_scores_copy = data_container.z_scores.copy()
        if ("screen", "", "") in z_scores_copy.columns.to_list():
            id_cols = ['screen__', 'batch__', 'Compound__']
        else:
            id_cols = ['batch__', 'Compound__']

        z_scores_copy.columns = ['_'.join([str(i) for i in col]).strip() \
                                 for col in z_scores_copy.columns] # Combine mulitindex columns
        df_melted = pd.melt(
            z_scores_copy, 
            id_vars=id_cols,
            value_vars=[col for col in z_scores_copy.columns \
                        if col not in id_cols],
            var_name='multiindex', 
            value_name='Z Score'
        )
        if len(df_melted['multiindex'].iloc[0].split('_')) == 3:
            new_cols = ['Protein.Ids', 'Genes', 'Precursor.Id']
            df_melted[new_cols] = df_melted['multiindex'] \
                .str.split('_', expand=True)
        else:
            new_cols = ['Protein.Ids', 'Genes', 'Is TF', 'Precursor.Id']
            df_melted[new_cols] = df_melted['multiindex'] \
                .str.split('_', expand=True)
            df_melted["Is TF"] = df_melted["Is TF"] \
                .replace({'True': True, 'False': False})
            df_melted["Is TF"] = df_melted["Is TF"].astype(bool)
        
        df_melted = df_melted.drop(columns=['multiindex'])
        df_melted = df_melted.rename(columns= \
                                     {key: key.rstrip("_") for key in id_cols})

        df_melted = PeptideZScoreCalculator._get_median_z_score(df_melted)

        dropcol = [col for col in df_melted if col.startswith("level")]
        df_melted = df_melted.drop(columns=dropcol)

        data_container.melted_z_scores = df_melted

# z_score_engagement_analysis

This module provides functions for analyzing peptide dropout using robust Z scores. 

## Biology Principle
Some compounds may be "silent binders," meaning they bind to a protein but do not cause it to detach from chromatin. In this case, the protein abundance may not drop, but within the protein, a single peptide's abundance may drop if a compound is bound to it. If we can identify peptides that have "dropped out", we may be identifying silent binders covalently binding to proteins.

## Analysis Principle
This module uses the robust z score to measure outliers in peptide abundance. First, all peptide abundances are coverted to a log scale. Then the robust z score is calculated. A larger negative value indicates that the peptides abundance is much lower than the other abundance values.

To find "hits," you can select a cutoff value and search for compound-peptides with z scores below this cutoff value. I do not yet have an official/automated way to pick a cutoff value, but the procedure I am using as is follows:
1. Look at the plot for all z scores for all peptides to get a rough idea of where outliers fall
2. Plot the false hit rate are various cutoff values
3. Calculate the precision at a few cutoff values (precision = "true positives"/total hits, in quotes here because they are just not KNOWN false positives, they could still be unknown false positives)
4. Pick a value that seems to capture the outliers and offers a "good" precision, 95% +

## FAQs
*Do you explicitly compare peptide dropout to DMSO?*

No, I do not. For each peptide, I compare each abundance value to all other abundance values for that peptide. I assume that almost all compounds will be ineffective and essentially act like DMSO, so by comparing each abundance to all other abundances, I am effectively comparing it to DMSO.

*Do you take batch effects into account?*

Yes, each batch is median normalized.


*Why use the robust Z score instead of the standard Z score?*

The standard Z score relies on averages. If you are looking for giant outliers, those can influence the average and lower the power of the test. By looking for medians instead, the test is more robust to the effects of outliers. I tested bnoth ways in the notebook comparison.ipynb (located in this repo) and found that the robust z score performed slightly better on synthetic data.

## TODO:
* Normalize "raw" abundance by cell type and add into data
* Create visualization tools
* Creat batch manager
* Update analysis script

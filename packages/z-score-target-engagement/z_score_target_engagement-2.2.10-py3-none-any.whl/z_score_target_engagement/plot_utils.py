import matplotlib.pyplot as plt

def plot_target_z_scores(df,
                         target,
                         compound,
                         peptide,
                         savefig=False,
                         show=True):
    """
    Plot robust z scores for a target by peptide, highlighting a specified peptide
    df should be a melted z score data frame
    """
    
    # Filter for the target, compound
    subdf = df.loc[(df["Genes"]==target) & (df["Compound"]==compound)]

    # Plot all peptides
    plt.scatter(subdf["Precursor.Id"], subdf["Z Score"],
                color='blue',
                alpha=0.5)

    # Highlight specific peptide
    if isinstance(peptide, str):
        peptide = [peptide]

    for p in peptide:
        peptide_df = subdf.loc[subdf["Precursor.Id"]==p]
        plt.scatter(peptide_df["Precursor.Id"], peptide_df["Z Score"],
                    color='red',
                    s=100,
                    edgecolor='black'
                   )

    plt.xticks(rotation=90)
    plt.ylabel("Robust Z Score")
    plt.xlabel("Peptides")
    plt.title(f"{target} - {compound}")

    if savefig:
        is_negative = peptide_df["Z Score"] < 0
        is_negative_sum = is_negative.sum()
        if is_negative_sum == len(peptide_df):
            status="good"
        else:
            status="bad"
        save_path = os.path.join(os.getcwd(), status, f"{target}_{compound}_{peptide}.png")
        plt.tight_layout()
        plt.savefig(save_path)
    if show:
        plt.show()
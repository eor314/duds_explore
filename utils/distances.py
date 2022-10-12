import pandas as pd
import numpy as np
from scipy.spatial.distance import braycurtis, dice
from sklearn.feature_selection import mutual_info_classif


def pairwise_bc(df):
    """
    Compute the Bray-Curtis dissimilarity between study regions or times
    
    :param df: Pandas dataframe of counts in a region or time. [concepts x regions]
    :return: dataframe of pairwise distances
    """

    # compute pairwise braycurtis
    outbc = {}

    # iterate over regions
    for item in df.columns:
        try:
            bc = df.apply(lambda xx: braycurtis(df[item].to_numpy(), xx.to_numpy()), axis=0)
            outbc[item] = bc
        except ZeroDivisionError:
            # catch any regions that have no items
            print(f'no entries in {item}')

    return pd.DataFrame(outbc)


def pairwise_L1_dist(df):
    """
    Compute the L1 distance between the normalized per-concept distribtuion in each region.
    c.f. Beery et al., 2022: https://openaccess.thecvf.com/content/CVPR2022/papers/\
        Beery_The_Auto_Arborist_Dataset_A_Large-Scale_Benchmark_for_Multiview_Urban_CVPR_2022_paper.pdf)

    :param df: Pandas dataframe of counts in a region or time. [concepts x regions]
    :return: dataframe of pairwise distances
    """
    nrmd = df/df.sum(axis=0)
    outL1 = {}

    # iterate over regions
    for item in nrmd.columns:
        L1dist = nrmd.apply(lambda xx: np.linalg.norm((nrmd[item].to_numpy()-xx.to_numpy()), ord=1), axis=0)
        outL1[item] = L1dist

    return pd.DataFrame(outL1)


def pairwise_mi(df):
    """
    Compute the mutual information between per-concept distributions
    :param df: Pandas dataframe of counts in a region or time. [concepts x regions]
    :return: dataframe of pairwise distances
    """
    
    outmi = {}

    for item in df.columns:
        mi = df.apply(
            lambda xx: mutual_info_classif(df[item].to_numpy().reshape(-1, 1), xx.to_numpy().ravel()), 
            axis=0
        )
        
        outmi[item] = mi.values.ravel()

    return pd.DataFrame(outmi)


def pairwise_dice(df):
    """
    Compute the dice between per-concept distributions
    :param df: Pandas dataframe of counts in a region or time. [concepts x regions]
    :return: dataframe of pairwise distances
    """

    outdice = {}

    for item in df.columns:
        dd = df.apply(
            lambda xx: dice(np.where(df[item].to_numpy()>0, 1, 0), np.where(xx.to_numpy()>0, 1, 0)), 
            axis=0
        )
        
        outdice[item] = dd

    return pd.DataFrame(outdice)


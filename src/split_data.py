import pandas as pd
from pandas import DataFrame

def split_train_test(data: DataFrame, test_ratio: float) -> tuple[DataFrame, DataFrame]:
    """
    This function splits the dataset into a training set and a test set based on the specified test ratio.

    Parameters:
    data (DataFrame): The dataset to be split.
    test_ratio (float): The proportion of the dataset to include in the test split.
    
    Returns:
    tuple: A tuple containing the training set and the test set.

    """

    shuffled_indices = pd.np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)

    train_indices = shuffled_indices[test_set_size:]
    test_indices = shuffled_indices[:test_set_size]

    train_set = data.iloc[train_indices]
    test_set = data.iloc[test_indices]

    return train_set, test_set
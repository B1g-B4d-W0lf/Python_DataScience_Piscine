import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Take a csv file and returns a dataset"""
    try:
        target = path
        if not target.lower().endswith(".csv"):
            raise AssertionError("Only 'csv'format supported.")
        if not os.path.exists(target):
            raise AssertionError("File does not exist / \
                is in the wrong directory.")

        dataset = pd.read_csv(target)
        print(f"Loading dataset of dimensions : {dataset.shape}")

        return dataset

    except AssertionError as e:
        print(e)
        return None

    except Exception as e:
        print(f"Exception :\n{e}\nHas been caught.")
        return None

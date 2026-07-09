"""
preprocess.py

Handles data preprocessing for the
Multi-Model ML Classification Visualizer.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_dataset(file):

    df = pd.read_csv(file)


    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")


    # Remove duplicate rows
    df = df.drop_duplicates()


    return df


def split_features_target(df, target_column):

    """
    Split features and target.
    """

    X = df.drop(columns=[target_column])

    y = df[target_column]

    return X, y


def split_data(X, y, test_size=0.2, random_state=42):

    try:

        return train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
            stratify=y
        )

    except ValueError:

        return train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state
        )


def scale_features(X_train, X_test):

    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler


    # Missing value handling

    imputer = SimpleImputer(
        strategy="mean"
    )


    X_train = imputer.fit_transform(
        X_train
    )


    X_test = imputer.transform(
        X_test
    )


    # Scaling

    scaler = StandardScaler()


    X_train_scaled = scaler.fit_transform(
        X_train
    )


    X_test_scaled = scaler.transform(
        X_test
    )


    return X_train_scaled, X_test_scaled, scaler
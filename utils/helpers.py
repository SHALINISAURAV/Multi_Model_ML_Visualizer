"""
helpers.py

Utility functions for the
Multi-Model ML Classification Visualizer.
"""

import joblib
import pandas as pd


def save_model(model, filepath):
    """
    Save trained model.
    """

    joblib.dump(model, filepath)


def load_saved_model(filepath):
    """
    Load saved model.
    """

    return joblib.load(filepath)


def save_results(results_df, filepath):
    """
    Save model comparison results.
    """

    results_df.to_csv(filepath, index=False)


def make_predictions(model, X):
    """
    Generate predictions.
    """

    return model.predict(X)


def get_class_label(prediction):
    """
    Convert numeric prediction into class label.
    """

    labels = {
        0: "Malignant",
        1: "Benign"
    }

    return labels.get(prediction, "Unknown")
"""
metrics.py

Handles evaluation of machine learning models.
"""

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


def evaluate_models(
    trained_models,
    X_test,
    y_test
):
    """
    Evaluate all trained models and return
    comparison DataFrame.
    """

    results = []

    for name, model in trained_models.items():

        # Predictions
        y_pred = model.predict(
            X_test
        )

        metrics = {
            "Model": name,
            "Accuracy": accuracy_score(
                y_test,
                y_pred
            ),
            "Precision": precision_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            ),
            "Recall": recall_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            ),
            "F1 Score": f1_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            )
        }

        # ROC AUC
        try:
            y_prob = model.predict_proba(
                X_test
            )[:, 1]

            metrics["ROC AUC"] = roc_auc_score(
                y_test,
                y_prob
            )

        except:
            metrics["ROC AUC"] = None

        results.append(metrics)

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="Accuracy",
        ascending=False
    ).reset_index(drop=True)

    results_df.iloc[:, 1:] = results_df.iloc[:, 1:].round(4)

    return results_df


def get_best_model(
    results_df,
    trained_models
):
    """
    Return best performing model.
    """

    best_model_name = results_df.iloc[0]["Model"]

    best_model = trained_models[
        best_model_name
    ]

    return best_model_name, best_model
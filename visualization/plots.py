"""
plots.py

Visualization functions for the
Multi-Model ML Classification Visualizer.
"""

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay
)


def plot_accuracy(results_df):
    """
    Plot model accuracy comparison.
    """

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=results_df,
        x="Model",
        y="Accuracy"
    )

    plt.title("Model Accuracy Comparison")
    plt.xlabel("Models")
    plt.ylabel("Accuracy")
    plt.xticks(rotation=30)

    plt.tight_layout()

    return plt


def plot_confusion_matrix(model, X_test, y_test):
    """
    Plot confusion matrix.
    """

    fig, ax = plt.subplots(figsize=(6, 5))

    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test,
        y_test,
        cmap="Blues",
        ax=ax
    )

    ax.set_title("Confusion Matrix")

    return fig


def plot_roc_curve(model, X_test, y_test):
    """
    Plot ROC Curve.
    """

    fig, ax = plt.subplots(figsize=(6, 5))

    RocCurveDisplay.from_estimator(
        model,
        X_test,
        y_test,
        ax=ax
    )

    ax.set_title("ROC Curve")

    return fig


def plot_feature_importance(model, feature_names):
    """
    Plot Top 10 Feature Importance.
    """

    if not hasattr(model, "feature_importances_"):
        return None

    importance = model.feature_importances_

    indices = importance.argsort()[::-1][:10]

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=importance[indices],
        y=[feature_names[i] for i in indices]
    )

    plt.title("Top 10 Important Features")
    plt.xlabel("Importance")
    plt.ylabel("Features")

    plt.tight_layout()

    return plt
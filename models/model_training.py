"""
model_training.py

Handles model creation and training for the
Multi-Model ML Classification Visualizer.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)


def get_models():
    """
    Create all classification models.
    """

    models = {

        "Logistic Regression": LogisticRegression(
            max_iter=1000
        ),

        "KNN": KNeighborsClassifier(),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Naive Bayes": GaussianNB(),

        "SVM": SVC(
            probability=True,
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

        "AdaBoost": AdaBoostClassifier(
            random_state=42
        ),

        "Gradient Boosting": GradientBoostingClassifier(
            random_state=42
        )

    }

    return models


def train_models(models, X_train, y_train):
    """
    Train all machine learning models.
    """

    trained_models = {}

    for name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

        trained_models[name] = model

    return trained_models
"""
Multi-Model ML Classification Visualizer

Streamlit Application
"""

import streamlit as st
import pandas as pd

from preprocessing.preprocess import (
    load_dataset,
    split_features_target,
    split_data,
    scale_features
)

from models.model_training import (
    get_models,
    train_models
)

from evaluation.metrics import (
    evaluate_models,
    get_best_model
)

# Step 1: Imports perfectly added
from visualization.plots import (
    plot_accuracy,
    plot_confusion_matrix,
    plot_roc_curve,
    plot_feature_importance
)

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Multi-Model ML Classification Visualizer",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------

st.title("🧠 Multi-Model ML Classification Visualizer")

st.markdown(
    """
Train and compare multiple Machine Learning classification models
using your own dataset.
"""
)

# -----------------------------------
# Sidebar Configuration
# -----------------------------------

st.sidebar.header("⚙️ Configuration")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

# -----------------------------------
# Dataset Loading
# -----------------------------------

if uploaded_file is not None:

    df = load_dataset(uploaded_file)

    st.success("Dataset loaded successfully!")

    # -------------------------------
    # Dataset Preview
    # -------------------------------

    st.subheader("📄 Dataset Preview")

    st.dataframe(df)

    # -------------------------------
    # Dataset Shape
    # -------------------------------

    st.subheader("📊 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    # -------------------------------
    # Target Selection
    # -------------------------------

    st.subheader("🎯 Select Target Column")

    target_column = st.selectbox(
        "Target Column",
        df.columns
    )

    # -------------------------------
    # Model Selection
    # -------------------------------

    st.sidebar.subheader(
        "🤖 Select Models"
    )

    selected_models = st.sidebar.multiselect(
        "Choose Models",
        [
            "Logistic Regression",
            "KNN",
            "Decision Tree",
            "Naive Bayes",
            "SVM",
            "Random Forest",
            "AdaBoost",
            "Gradient Boosting"
        ],
        default=[
            "Logistic Regression",
            "Random Forest",
            "SVM"
        ]
    )

    # -------------------------------
    # Training Configuration
    # -------------------------------

    test_size = st.sidebar.slider(
        "Test Size",
        min_value=0.1,
        max_value=0.4,
        value=0.2,
        step=0.05
    )

    random_state = st.sidebar.number_input(
        "Random State",
        value=42,
        step=1
    )

    train_button = st.sidebar.button(
        "🚀 Train Models"
    )

    # -------------------------------
    # Model Training Pipeline
    # -------------------------------

    if train_button:
        if df[target_column].nunique() == df.shape[0]:
            st.error(
                "Selected target column contains unique values. Please select a classification target column."
            )
            st.stop()

        if len(selected_models) == 0:
            st.warning(
                "Please select at least one model."
            )

        else:
            # Feature Target Split
            X, y = split_features_target(
                df,
                target_column
            )

            # Train Test Split
            X_train, X_test, y_train, y_test = split_data(
                X,
                y,
                test_size=test_size,
                random_state=random_state
            )

            # Scaling
            X_train_scaled, X_test_scaled, scaler = scale_features(
                X_train,
                X_test
            )

            # Get Models
            models = get_models()

            # Select User Models
            models = {
                name: model
                for name, model in models.items()
                if name in selected_models
            }

            # Train Models
            trained_models = train_models(
                models,
                X_train_scaled,
                y_train
            )

            st.success(
                "✅ Models trained successfully!"
            )

            # -------------------------------
            # Model Evaluation (Metrics Table)
            # -------------------------------

            st.subheader(
                "📊 Model Performance Comparison"
            )

            results_df = evaluate_models(
                trained_models,
                X_test_scaled,
                y_test
            )

            st.dataframe(
                results_df
            )

            # Step 2: Model Comparison Visualization
            # -----------------------------------
            # Model Comparison Visualization
            # -----------------------------------
            st.subheader("📊 Model Accuracy Comparison")
            accuracy_plot = plot_accuracy(
                results_df
            )
            st.pyplot(
                accuracy_plot
            )

            # Step 3: Best Model Selection
            # -----------------------------------
            # Best Model Selection
            # -----------------------------------
            best_model_name, best_model = get_best_model(
                results_df,
                trained_models
            )
            st.success(
                f"🏆 Best Model: {best_model_name}"
            )

            # Step 4: Confusion Matrix
            # -----------------------------------
            # Confusion Matrix
            # -----------------------------------
            st.subheader(
                "🔲 Confusion Matrix"
            )
            cm_plot = plot_confusion_matrix(
                best_model,
                X_test_scaled,
                y_test
            )
            st.pyplot(
                cm_plot
            )

            # Step 5: ROC Curve
            # -----------------------------------
            # ROC Curve
            # -----------------------------------
            st.subheader(
                "📈 ROC Curve"
            )
            roc_plot = plot_roc_curve(
                best_model,
                X_test_scaled,
                y_test
            )
            st.pyplot(
                roc_plot
            )

else:
    st.info(
        "Please upload a CSV dataset to continue."
    )
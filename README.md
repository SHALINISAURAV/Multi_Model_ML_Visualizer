# 🧠 Multi-Model ML Classification Visualizer

An interactive Machine Learning Classification Dashboard built using **Python, Scikit-Learn, and Streamlit** that allows users to upload datasets, preprocess data, train multiple classification algorithms, compare model performance, and visualize evaluation metrics.

## 🚀 Live Demo

Streamlit Application:
https://multimodelmlvisualizer-3xbjtvfke7tal9jqkvuymu.streamlit.app

---

# 📌 Project Overview

Machine Learning workflows usually require multiple stages:

- Dataset loading
- Data preprocessing
- Model training
- Evaluation
- Visualization
- Model comparison

This project converts the complete classification workflow into an interactive web application where users can experiment with different ML algorithms without writing code.

The application provides a complete ML experimentation environment.

---

# ✨ Features

## Dataset Upload

- Upload custom CSV classification datasets
- Dynamic dataset preview
- Automatic row and column information
- Select target column manually

## Data Processing Pipeline

Implemented preprocessing workflow:

- Feature-target separation
- Train-test splitting
- Feature scaling
- Handling preprocessing requirements before training

## Machine Learning Models

Implemented classification algorithms:

### Core Models

- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

### Additional Models

- K-Nearest Neighbors
- Decision Tree
- Naive Bayes
- AdaBoost
- Gradient Boosting

Users can select multiple models and compare their performance.

---

# 📊 Evaluation System

The application evaluates trained models using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

A model comparison table is generated automatically.

---

# 📈 Visualization Module

The dashboard provides:

## Model Accuracy Comparison

Bar chart comparing different algorithms.

## Confusion Matrix

Visual analysis of:

- True Positive
- True Negative
- False Positive
- False Negative

## ROC Curve

Performance comparison using classification threshold analysis.

## Feature Importance

Helps understand important features contributing to predictions.

---

# 🏗️ Project Architecture

```
Multi_Model_ML_Visualizer/
│
├── app.py
│
├── notebooks/
│   └── model_experiments.ipynb
│
├── data/
│   └── dataset.csv
│
├── preprocessing/
│   └── preprocess.py
│
├── models/
│   └── model_training.py
│
├── evaluation/
│   └── metrics.py
│
├── visualization/
│   └── plots.py
│
├── utils/
│   └── helpers.py
│
├── saved_models/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# 🔄 Application Workflow

```
Upload Dataset
      ↓
Dataset Exploration
      ↓
Select Target Column
      ↓
Select ML Models
      ↓
Preprocessing
      ↓
Train Models
      ↓
Evaluate Performance
      ↓
Visualize Results
      ↓
Select Best Model
```

---

# 🛠️ Technology Stack

## Programming Language

Python

## Machine Learning

- Scikit-Learn

## Data Handling

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Application Framework

- Streamlit

## Development Tools

- Jupyter Notebook
- Git
- GitHub

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/SHALINISAURAV/Multi_Model_ML_Visualizer.git
```

Navigate:

```bash
cd Multi_Model_ML_Visualizer
```

Create environment:

```bash
python -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧪 Dataset Used

The application was tested using classification datasets including:

- Breast Cancer Classification Dataset

The architecture supports any properly formatted CSV classification dataset.

---

# 📚 Learning Outcomes

This project demonstrates:

- End-to-end Machine Learning pipeline development
- Classification algorithm implementation
- Model evaluation techniques
- Data visualization
- Streamlit application development
- Modular software architecture
- ML deployment workflow

---

# 🔮 Future Improvements

- Hyperparameter tuning interface
- Prediction download feature
- SHAP based explainability
- Automated feature selection
- Model saving and loading workflow
- Advanced ensemble models

---

# 👩‍💻 Author

## Shalini Saurav

B.Tech Computer Science Engineering

AI / Machine Learning Enthusiast

---

⭐ Built to demonstrate practical Machine Learning engineering skills beyond model training.

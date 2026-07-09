# 🧠 Multi-Model ML Classification Visualizer

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)

![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red?style=for-the-badge&logo=streamlit)

![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)

![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy)

![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green?style=for-the-badge)

![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?style=for-the-badge&logo=github)

</p>

---

An interactive **Machine Learning Classification Dashboard** built using **Python, Scikit-Learn, and Streamlit** that enables users to upload custom datasets, preprocess data, train multiple machine learning classification models, compare their performance using various evaluation metrics, and visualize results through an intuitive web interface.

Rather than requiring users to write repetitive machine learning code, this application provides an end-to-end experimentation environment where multiple classification algorithms can be trained and evaluated within a few clicks.

Designed with a **modular software architecture**, the project separates preprocessing, model training, evaluation, and visualization into reusable components, making it scalable, maintainable, and deployment-ready.

# 🚀 Live Demo

### 🌐 Streamlit Application

https://multimodelmlvisualizer-3xbjtvfke7tal9jqkvuymu.streamlit.app

---

### 💻 GitHub Repository

https://github.com/SHALINISAURAV/Multi_Model_ML_Visualizer

---

### 📌 Built With

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

# 📖 Project Overview

Machine Learning experimentation typically involves multiple disconnected steps such as data preprocessing, model training, evaluation, visualization, and comparison. These tasks are often performed across different notebooks or scripts, making the workflow repetitive, time-consuming, and difficult to manage.

The **Multi-Model ML Classification Visualizer** was developed to simplify this process by bringing the complete classification pipeline into a single interactive application.

The dashboard allows users to upload their own classification datasets, perform preprocessing, train multiple machine learning models simultaneously, compare their performance using standard evaluation metrics, and visualize the results without writing additional code.

The application follows software engineering principles by organizing the project into separate modules for preprocessing, model training, evaluation, visualization, and utility functions. This modular design improves readability, maintainability, scalability, and future extensibility.

Whether used for learning machine learning concepts, experimenting with different algorithms, or rapidly comparing models on new datasets, the application provides a practical and user-friendly solution for classification tasks.

# 💼 Business Problem

In real-world organizations, selecting the most suitable machine learning model for a classification problem is rarely straightforward. Data scientists and analysts often need to experiment with multiple algorithms before identifying the one that delivers the best performance.

However, this process usually requires:

- Writing repetitive preprocessing code
- Training one model at a time
- Switching between multiple notebooks
- Manually calculating evaluation metrics
- Creating visualizations separately
- Comparing results across different experiments

These repetitive tasks increase development time and make machine learning experimentation less efficient.

For beginners, the process can be even more challenging because it requires understanding several libraries, workflows, and evaluation techniques before meaningful comparisons can be made.# 💼 Business Problem

In real-world organizations, selecting the most suitable machine learning model for a classification problem is rarely straightforward. Data scientists and analysts often need to experiment with multiple algorithms before identifying the one that delivers the best performance.

However, this process usually requires:

- Writing repetitive preprocessing code
- Training one model at a time
- Switching between multiple notebooks
- Manually calculating evaluation metrics
- Creating visualizations separately
- Comparing results across different experiments

These repetitive tasks increase development time and make machine learning experimentation less efficient.

For beginners, the process can be even more challenging because it requires understanding several libraries, workflows, and evaluation techniques before meaningful comparisons can be made.

# 💡 Proposed Solution

This project provides an interactive dashboard that automates the complete machine learning classification workflow.

Instead of manually writing preprocessing and training code for every experiment, users simply upload a CSV dataset, select the target column, choose one or more machine learning models, and train them through an intuitive graphical interface.

The application automatically performs:

- Dataset loading
- Data preprocessing
- Feature scaling
- Train-test splitting
- Multi-model training
- Performance evaluation
- Result comparison
- Visual analytics
- Best model identification

By integrating all these components into a single application, the project significantly reduces the effort required to compare machine learning models while improving accessibility for students, developers, educators, and data practitioners.

# ✨ Key Features

The application is divided into multiple functional modules, each responsible for a specific stage of the machine learning workflow.

---

## 📂 Dataset Management

- Upload custom CSV classification datasets
- Interactive dataset preview
- Display dataset dimensions (rows and columns)
- Dynamic target column selection
- Support for binary and multiclass classification datasets

---

## ⚙️ Data Preprocessing

The preprocessing pipeline prepares the dataset before model training by performing:

- Feature and target separation
- Missing value handling
- Train-test splitting
- Feature scaling using StandardScaler
- Consistent preprocessing across all selected models

---

## 🤖 Machine Learning Models

The dashboard currently supports multiple supervised classification algorithms:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest Classifier
- AdaBoost Classifier
- Gradient Boosting Classifier

Users can train one model or compare multiple models simultaneously.

---

## 📊 Model Evaluation

Automatically evaluates every trained model using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

The results are displayed in a comparison table, making it easier to identify the best-performing model.

---

## 📈 Visualization Dashboard

The application generates multiple visualizations, including:

- Model Accuracy Comparison
- Confusion Matrix
- ROC Curve
- Feature Importance (for supported models)

These visualizations help users better understand model performance beyond numerical metrics.

---

## 🏆 Best Model Identification

The application automatically identifies the best-performing model based on evaluation metrics, allowing users to quickly compare algorithms and select the most suitable one.

# 🔄 End-to-End Machine Learning Pipeline

The application follows a structured machine learning workflow from raw dataset to model comparison.

```text
                 User
                   │
                   ▼
          Upload CSV Dataset
                   │
                   ▼
          Dataset Exploration
                   │
                   ▼
        Target Column Selection
                   │
                   ▼
        Data Preprocessing
     (Cleaning • Scaling • Split)
                   │
                   ▼
       Machine Learning Models
                   │
                   ▼
        Model Training Pipeline
                   │
                   ▼
      Performance Evaluation
                   │
                   ▼
     Interactive Visualizations
                   │
                   ▼
      Best Model Identification
```

Every stage of the pipeline is modular, making the application easy to maintain and extend with additional preprocessing techniques, machine learning models, and evaluation methods.

# 🏗️ Project Architecture

The project follows a modular software engineering architecture where each component has a single responsibility.

```text
                        app.py
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
Preprocessing        Model Training      Evaluation
(preprocess.py)   (model_training.py)   (metrics.py)
        │                  │                  │
        └──────────────┬───┴──────────────────┘
                       │
                       ▼
                Visualization
                  (plots.py)
                       │
                       ▼
                 Streamlit UI
```

This architecture separates business logic from the user interface, improving maintainability, readability, scalability, and code reusability.

# 📁 Project Structure

```text
Multi_Model_ML_Visualizer/
│
├── app.py
│   ├── Main Streamlit application
│   ├── Handles user interaction
│   └── Connects all project modules
│
├── data/
│   └── Sample classification dataset
│
├── preprocessing/
│   └── preprocess.py
│       ├── Dataset loading
│       ├── Feature-target separation
│       ├── Train-test splitting
│       └── Feature scaling
│
├── models/
│   └── model_training.py
│       ├── Model initialization
│       ├── Model selection
│       └── Training pipeline
│
├── evaluation/
│   └── metrics.py
│       ├── Accuracy
│       ├── Precision
│       ├── Recall
│       ├── F1 Score
│       └── ROC-AUC
│
├── visualization/
│   └── plots.py
│       ├── Accuracy comparison
│       ├── Confusion Matrix
│       ├── ROC Curve
│       └── Feature Importance
│
├── utils/
│   └── Helper functions
│
├── notebooks/
│   └── Experimental notebooks
│
├── saved_models/
│   └── Generated comparison results
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Streamlit |
| Development Environment | Jupyter Notebook |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

## Libraries Used

- streamlit
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- joblib

# 🤖 Machine Learning Models Implemented

The dashboard currently supports eight supervised machine learning classification algorithms.

| Model | Purpose |
|--------|----------|
| Logistic Regression | Baseline linear classifier for binary classification |
| K-Nearest Neighbors | Instance-based learning using nearest neighbors |
| Decision Tree | Rule-based classification model |
| Naive Bayes | Probabilistic classifier based on Bayes' theorem |
| Support Vector Machine | Effective for high-dimensional datasets |
| Random Forest | Ensemble learning using multiple decision trees |
| AdaBoost | Boosting algorithm combining weak learners |
| Gradient Boosting | Sequential ensemble model for improved predictive performance |

The modular architecture allows additional machine learning algorithms to be integrated with minimal code changes.

# 📊 Model Evaluation

After training, each selected machine learning model is evaluated using multiple performance metrics to provide a comprehensive comparison.

| Metric | Description |
|----------|-------------|
| Accuracy | Measures the overall percentage of correctly classified instances. |
| Precision | Indicates how many predicted positive instances are actually positive. |
| Recall | Measures the model's ability to correctly identify positive instances. |
| F1 Score | Harmonic mean of Precision and Recall, useful for imbalanced datasets. |
| ROC-AUC Score | Evaluates the model's ability to distinguish between different classes across various classification thresholds. |

Instead of relying on a single metric, the application evaluates every model across multiple performance measures, enabling more informed model selection.

# 📈 Interactive Visualizations

To make model evaluation more intuitive, the dashboard provides several visual analytics.

## 📊 Accuracy Comparison

A bar chart compares the accuracy of all selected machine learning models, allowing quick identification of the best-performing algorithm.

---

## 📉 Confusion Matrix

The Confusion Matrix illustrates:

- True Positives
- True Negatives
- False Positives
- False Negatives

This helps users understand how well each model classifies different categories.

---

## 📈 ROC Curve

The Receiver Operating Characteristic (ROC) Curve demonstrates the trade-off between the True Positive Rate and False Positive Rate across different thresholds.

A higher Area Under Curve (ROC-AUC) generally indicates better classification performance.

---

## ⭐ Feature Importance

For tree-based algorithms such as Random Forest and Gradient Boosting, the dashboard displays the most influential features contributing to predictions.

This improves model interpretability by highlighting which variables have the greatest impact on classification.

# 📷 Application Screenshots

> **Note:** The screenshots below demonstrate the application's workflow.

| Screen | Description |
|----------|-------------|
| Home Page | Landing interface of the application |
| Dataset Upload | Uploading a CSV dataset |
| Dataset Preview | Preview of uploaded data |
| Target Selection | Selecting the target variable |
| Model Selection | Choosing machine learning algorithms |
| Model Comparison | Performance comparison table |
| Accuracy Chart | Model accuracy visualization |
| Confusion Matrix | Classification performance |
| ROC Curve | ROC-AUC visualization |
| Feature Importance | Top contributing features |

```
assets/
└── screenshots/
    ├── home.png
    ├── upload.png
    ├── preview.png
    ├── comparison.png
    ├── confusion_matrix.png
    ├── roc_curve.png
    └── feature_importance.png
```

# ⚙️ Engineering Decisions

Several design decisions were made during development to improve maintainability, usability, and scalability.

---

## Why Streamlit?

Streamlit enables rapid development of interactive data science applications while requiring minimal frontend code.

---

## Why Modular Architecture?

Instead of placing all logic inside a single script, the project was divided into dedicated modules:

- Preprocessing
- Model Training
- Evaluation
- Visualization
- Utility Functions

This separation improves code readability, testing, debugging, and future scalability.

---

## Why StandardScaler?

Many machine learning algorithms, such as Logistic Regression, Support Vector Machine, and K-Nearest Neighbors, are sensitive to feature magnitudes.

Applying feature scaling ensures fair comparison across models.

---

## Why Scikit-Learn?

Scikit-Learn provides reliable implementations of classical machine learning algorithms while maintaining a consistent API for training and evaluation.

---

## Why Multiple Evaluation Metrics?

Accuracy alone may not always represent model quality.

Using Precision, Recall, F1 Score, and ROC-AUC enables more robust performance comparison across different datasets.

# 🚧 Challenges Faced During Development

Developing this project involved solving several real-world engineering challenges beyond simply training machine learning models.

Some of the key challenges included:

- Handling missing values before model training.
- Preventing users from selecting invalid target columns.
- Managing feature scaling consistently across different algorithms.
- Supporting multiple machine learning models through a common training pipeline.
- Computing evaluation metrics for different classification outputs.
- Designing reusable preprocessing and evaluation functions.
- Integrating multiple visualization components within Streamlit.
- Structuring the project using modular software engineering principles.
- Preparing the application for cloud deployment using Streamlit Community Cloud.
- Debugging preprocessing, evaluation, and visualization issues during development.

Addressing these challenges helped improve both the robustness of the application and my understanding of practical machine learning engineering.

# 🧠 ML Engineering Skills Demonstrated

This project demonstrates practical Machine Learning Engineering concepts, including:

- End-to-end machine learning workflow development
- Modular Python project organization
- Data preprocessing pipelines
- Feature engineering workflow
- Model training automation
- Comparative benchmarking of multiple ML algorithms
- Performance evaluation using multiple metrics
- Interactive dashboard development
- Data visualization for model analysis
- Software engineering best practices
- Version control using Git & GitHub
- Deployment using Streamlit Community Cloud

Rather than focusing solely on model accuracy, this project emphasizes building reusable, maintainable, and deployment-ready machine learning software.

# 🎯 Learning Outcomes

Building this project provided hands-on experience across multiple stages of the Machine Learning lifecycle.

### Machine Learning

- Supervised Classification
- Model Selection
- Performance Comparison
- Evaluation Metrics
- Feature Scaling
- Data Preprocessing

---

### Software Engineering

- Modular Project Structure
- Code Reusability
- Function-Based Architecture
- Separation of Concerns
- Version Control using Git & GitHub

---

### Data Visualization

- Performance Comparison Charts
- Confusion Matrix Visualization
- ROC Curve Analysis
- Feature Importance Visualization

---

### Deployment

- Streamlit Application Development
- Streamlit Community Cloud Deployment
- Dependency Management
- GitHub Repository Management

---

Through this project, I gained practical experience in building machine learning applications that are interactive, reusable, and deployment-ready rather than focusing solely on notebook-based experimentation.

# 🔮 Future Enhancements

The current version establishes a strong foundation for machine learning experimentation. Several enhancements can further improve the application.

## Model Optimization

- Hyperparameter Tuning
- GridSearchCV Integration
- RandomizedSearchCV
- Cross Validation

---

## Explainable AI

- SHAP Explainability
- LIME Interpretability
- Feature Contribution Analysis

---

## Advanced Machine Learning

- XGBoost
- LightGBM
- CatBoost
- Voting Classifier
- Stacking Classifier

---

## User Experience

- Dark Mode Support
- Better Dashboard Design
- Download Evaluation Reports
- Export Trained Models
- Save Model Comparison Results

---

## Deployment Improvements

- Docker Containerization
- REST API Integration using FastAPI
- Authentication & User Management
- Cloud Storage Integration
- CI/CD Pipeline using GitHub Actions

---

The modular architecture of the project makes these future enhancements straightforward to integrate.

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SHALINISAURAV/Multi_Model_ML_Visualizer.git
```

Move into the project directory

```bash
cd Multi_Model_ML_Visualizer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

The application will open automatically in your default browser.

# 🚀 How to Use

Using the application is simple.

### Step 1

Upload a CSV classification dataset.

↓

### Step 2

Select the target column.

↓

### Step 3

Choose one or multiple machine learning models.

↓

### Step 4

Adjust the test size and random state if required.

↓

### Step 5

Click **Train Models**.

↓

### Step 6

Compare the evaluation metrics.

↓

### Step 7

Analyze the generated visualizations.

↓

### Step 8

Identify the best-performing model.

The application performs the complete machine learning workflow automatically.

# 🧪 Example Datasets

The application has been tested on standard classification datasets, including:

- Breast Cancer Wisconsin Dataset
- Iris Dataset
- Wine Dataset
- Heart Disease Dataset
- Pima Indians Diabetes Dataset

The dashboard supports any properly formatted CSV file designed for binary or multiclass classification.

# 🌟 Why This Project?

Many machine learning projects stop after training a model inside a Jupyter Notebook.

This project goes beyond notebook experimentation by transforming the complete machine learning workflow into a reusable, interactive, and deployment-ready application.

Rather than focusing on achieving the highest possible accuracy on a single dataset, the objective was to build a practical tool that demonstrates software engineering principles alongside machine learning concepts.

The project emphasizes:

- Modular Architecture
- Code Reusability
- Interactive User Experience
- Comparative Model Analysis
- Data Visualization
- Deployment Readiness

This reflects the type of engineering workflow commonly followed when developing production-oriented machine learning applications.

# ⭐ Repository Highlights

✔ Modular Project Structure

✔ End-to-End Machine Learning Workflow

✔ Multiple Classification Algorithms

✔ Interactive Streamlit Dashboard

✔ Comparative Model Evaluation

✔ Performance Visualization

✔ Deployment Ready

✔ Clean & Maintainable Codebase

✔ Beginner-Friendly UI

✔ Scalable Architecture

# 👩‍💻 Author

## Shalini Saurav

**B.Tech – Computer Science Engineering**

Aspiring **AI Engineer | Machine Learning Engineer | Generative AI Developer**

### Connect with Me

- GitHub: https://github.com/SHALINISAURAV

- LinkedIn: https://www.linkedin.com/in/shalini-saurav-649aa22b8/

---

I enjoy building practical AI and Machine Learning applications that combine software engineering principles with intelligent systems.

I am currently focused on developing projects in:

- Machine Learning
- Artificial Intelligence
- Generative AI
- NLP
- RAG Systems
- AI Engineering

# 📄 License

This project is intended for educational purposes and personal portfolio demonstration.

Feel free to fork the repository, explore the implementation, and build upon it for learning.

If you use this project as inspiration, appropriate attribution is appreciated.

---

<div align="center">

### ⭐ If you found this project helpful, consider giving it a star!

Built with ❤️ using **Python**, **Scikit-Learn**, and **Streamlit**

**Turning Machine Learning Workflows into Interactive Applications.**

</div>

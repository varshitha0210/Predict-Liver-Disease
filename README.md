# **Predict Liver Disease**

A **machine learning–based web application** that predicts the likelihood of **liver disease** based on patient medical data.

---

## **Overview**

**Predict-Liver-Disease** is a **machine learning project** that classifies whether a person is likely to suffer from liver disease using clinical attributes such as age, gender, and biochemical test results.  
The goal is to assist in **early detection of liver problems** using data-driven prediction.

**Built With:**
- **Python**
- **scikit-learn**, **pandas**, **numpy**
- **Flask** (for web interface)
- **HTML**, **CSS** (for front-end)

---

## **Features**

- User-friendly **web interface** to input medical data  
- Predicts whether the patient **may have liver disease**  
- Displays **probability score** and health insights  
- Can be **retrained** or extended with additional data  

---

## **Dataset**

- **Source:** [Kaggle Indian Liver Patient Dataset](https://www.kaggle.com/uciml/indian-liver-patient-records)  
- **File Used:** `HealthCareData.csv`  
- **Attributes include:**  
  - `Age`, `Gender`, `Place`, `Duration of Alcohol Consumption`, `Quantity of Alcohol Consumption`, `Type of Alcohol`, `Hepatitis B`,`Hepatitis C`, `Diabetes`, etc.  
- **Target Variable:** Presence or absence of liver disease  

---

## **Model Details**

### **Algorithms Used**
The project explores and compares multiple machine learning algorithms to predict liver disease based on clinical parameters:

1. **Logistic Regression**
2. **Decision Tree Classifier**
3. **Random Forest Classifier**  
4. **Support Vector Machine (SVM)**
5. **K-Nearest Neighbors (KNN)**  

Each model was trained, tested, and evaluated to determine which algorithm performs best for accurate and reliable prediction.

---

### **Libraries Used**
- `scikit-learn` – for ML model building and evaluation  
- `pandas` – for data preprocessing and manipulation  
- `numpy` – for numerical computations  
- `matplotlib` & `seaborn` – for visualization and EDA  

---

### **Preprocessing Steps**
- Handled missing values using **mean imputation**  
- Encoded **Gender** feature (Male/Female → 1/0)  
- Normalized and scaled numerical features for algorithms like SVM and KNN  
- Removed highly correlated and redundant features  
- Split dataset into **80% training** and **20% testing** data  

---

### **Model Configurations**

#### **1️.Logistic Regression**
- Solver: `liblinear`  
- Regularization: `L2`  
- Random State: `42`

#### **2️.Decision Tree Classifier**
- Criterion: `entropy`  
- Max Depth: `6`  
- Random State: `42`

#### **3️.Random Forest Classifier**
- n_estimators: `200`  
- Max Depth: `8`  
- Criterion: `entropy`  
- Random State: `42`

#### **4️.Support Vector Machine (SVM)**
- Kernel: `rbf`  
- C: `1.0`  
- Gamma: `scale`  
- Random State: `42`

#### **5️.K-Nearest Neighbors (KNN)**
- n_neighbors: `5`  
- Metric: `minkowski`  
- Weights: `uniform`

---

### **Evaluation Metrics**
All models were evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **ROC-AUC Curve**

---

### **Model Artifacts**
- **Training Notebook:** `liver_disease_prediction.ipynb`  
- **Trained Model File:** `model.pkl` (best performing model saved)  
- **Dataset:** `HealthCareData.csv`  

After comparing all models, the **Logistic Regression** is giving highest accuracy

## **Team Members**

| Name | Roll Number |
|------|--------------|
| **M Padma Varshitha** | **106123085** |
| **Hema Naidu** | **106123095** |
| **R Rajeswari** | **106123111** |


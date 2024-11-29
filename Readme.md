# UG Group 1: Machine Learning Portfolio
## Predicting Alzheimer’s with Machine Learning Models

## Group Members
- Harihar Thachapully (H00364363)
- Midhun Saminathan (H00383233)
- Mohammad Ibrahim (H00264865)
- Patson D’Souza (H00404212)

# Project Milestones
- Week 3: Dataset discovery and exploration.
- Week 4: Project pitch.
- Week 7: Completion of exploratory data analysis (EDA) and feature selection.
- Week 9: Implementation of clustering and baseline models.
- Week 10: Training and evaluation of neural network models.
- Week 11: Final report and code submission.
- Week 12: Project presentation and peer assessment.

# Dataset Sources
## Tabular Dataset
Source: https://www.kaggle.com/datasets/brsdincer/alzheimer-features \
License: Open Source

<!-- (Add example data here) -->

## Image Dataset
Source: https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset \
License: Open Source

<!-- (Add example data here) -->

# Data Preparation Pipeline
- Preprocess tabular data: handle missing values, outliers, encode categorical variables.

- Scale with StandardScaler and Reduce dimensionality of data with PCA

- Process images: convert to grayscale, resize to 128x128, normalize, and split into training, validation, and test sets.

- Perform feature selection on tabular data using chi2, f_classification, and Random Forest methods.

From project root folder, run:
```bash
cd scripts
python pre.py
```

## Description of Requirements (R2–R5)

### R2: Data Analysis and Exploration
- Performed EDA to identify patterns and correlations within the tabular dataset.
- Data was scaled using `StandardScaler` from `sklearn`
- Feature selection was performed using:
  - chi2
  - f_classification
  - Random Forest Classifier
- Applied PCA to reduce dimensionality and visualize feature clusters in a scatterplot.
- **Results**: Available in the [EDA Script](https://github.com/DarkEmbers/Dubai_UG-1/blob/main/notebooks/alzheimer.ipynb).

---

### R3: Clustering
- Implemented clustering algorithms on the tabular dataset:
  - **KMeans**: Used the elbow method to determine optimal clusters
  - **Expectation Maximization (EM) with Gaussian Mixture Models (GMM)**: Used Bayesian Information Criterion (BIC) and Akaike Information Criterion (AIC) to find optimal number of cluster.
- **Results**: Available in the [Clustering Script](https://github.com/DarkEmbers/Dubai_UG-1/tree/main/notebooks/Clustering).

---

### R4: Baseline Models
- Implemented baseline machine learning models on tabular data:
  - **Decision Trees**
  - **Naïve Bayes**
  - **Random Forest**
  - **Linear Classifier**
>- Implemented on tabular dataset
>- input: "MMSE", "M/F", "EDUC", "SES"
>- output: "Demented / "Non-Demented"
>- Implemented baseline machine learning models for tabular dataset:
- Implemented baseline machine learning models on Image data:
  - **SVM**
>- Implemented on tabular dataset
>- input: "MMSE", "M/F", "EDUC", "SES"
>- output: "Demented / "Non-Demented"
>- Implemented baseline machine learning models for tabular dataset:

#### Results:
| Model           | Accuracy | Precision | Recall | F1 Score |
|-----------------|----------|-----------|--------|----------|
| Decision Trees  | 85.00%   | 88.46%    | 71.87% | 79.31%   |
| Naïve Bayes     | 87.50%   | 88.60%    | 79.50% | 83.75%   |
| Random Forest   | 82.63%   | 85.10%    | 72.00% | 78.85%   |
| SVM (Average)	  | 79.06%   | 77%       | 82.5%  | 79.5%    |

**Code and Results**: Available in the [Baseline Models](https://github.com/DarkEmbers/Dubai_UG-1/tree/main/notebooks/Baseline_models).

---

### R5: Neural Networks
- Developed and trained neural networks:
  - **MLP for tabular dataset**:
    - Input: "MMSE", "M/F", "nWBV", "EDUC"
	- Output: "Demented" / "Non-Demented"
  - **MLP for image dataset**
    - Input: Image
	- Output: "MildDemented" / "ModerateDemented" / "VeryMildDemented" / "NonDemented"
  - **CNN**
    - Input: Image
	- Output: "MildDemented" / "ModerateDemented" / "VeryMildDemented" / "NonDemented"
  - **LSTM**
    - Input: Image
	- Output: "MildDemented" / "ModerateDemented" / "VeryMildDemented" / "NonDemented"
- Performance metrics for the best-performing CNN model:

**Code and Results**: Available in the [Neural Networks](https://github.com/DarkEmbers/Dubai_UG-1/tree/main/notebooks/Neural%20Networks).
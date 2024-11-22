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
Source: https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset
License: Open Source

<!-- (Add example data here) -->

# Data Preparation Pipeline
- Preprocess tabular data: handle missing values, outliers, encode categorical variables.

- Scale with StandardScaler and Reduce dimensionality of data with PCA

- Process images: convert to grayscale, resize to 128x128, normalize, and split into training, validation, and test sets.

- Perform feature selection on tabular data using chi2, f_classification, and Random Forest methods.

> Run from within notebook: notebooks/
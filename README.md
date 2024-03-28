# House-Prices-Advanced-Regression-Techniques
This project tackles the Kaggle challenge [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques), aiming to predict the sales prices of residential homes in Ames, Iowa. 


## Table of Contents
- [Competition Description](#competition-description)
- [Model Summary](#model-summary)
- [Repository Structure](#repository-structure)
- [Acknowledgments](#acknowledgments)

## Competition Description
Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges you to predict the final price of each home.

![House Prices Kaggle Banner](https://storage.googleapis.com/kaggle-media/competitions/House%20Prices/kaggle_5407_media_housesbanner.png)


## Model Summary

The table below provides an overview of the models developed and fine-tuned for this competition. To facilitate understanding, common acronyms from the fields of machine learning have been employed. These include Mean Squared Logarithmic Error (MSLE), Learning Rate (LR), Early Stopping (ES), Split Ratio (SR) and Batch Size (BS).

### Machine Learning Models

| Model              | R² | SR (%) | L. Score*   |
|--------------------|----------------|--------|-------|
| Linear Regression  | 0.9115        | 85/15  | 0.3539 |
| Regression Tree    | 0.8036        | 85/15  | 0.2336 |

### Ensembling Methods

| Model          | Estimators | R² | SR (%) | L. Score*   |
|----------------|------------|----------------|--------|-------|
| Random Forest  | 100        | 0.9076       | 85/15  | 0.1565 |

### Deep Learning Models

| Model   | EPOCHs | LR   | BS | ES  | Patience | Loss | R²     |SR (%) | L. Score* |
|---------|--------|------|-----|-----|----------|------|--------|-------|------|
| FFDNN   | 4000   | 1e-4 | 20  | Yes | 200      | MSLE | 0.7375 | 85/15 | 0.2133 |

**\*** Leaderboard Scores (LS) are based on the Root Mean Squared Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price. Lower scores indicate better performance.


## Repository Structure

Project files and folder structure:
- `models`: Models folder.
- `submission`: Submission files for each model.
- `data/train.csv`: Training data set.
- `data/test.csv`: Test data set.
- `data/data_description.txt`: Dataset feature description.
- `data/sample_submission.csv`: Sample submission file.

## Acknowledgments

The Ames Housing dataset was compiled by Dean De Cock for use in data science education. For detailed information about the code and its functionalities, please refer to the inline comments within the source files. Feel free to explore the codebase and contribute to further enhancements or bug fixes!

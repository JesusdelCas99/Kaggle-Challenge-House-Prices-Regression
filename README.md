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
The table below provides an overview of the models developed and fine-tuned for this competition. To facilitate understanding, common acronyms from the fields of machine learning and deep learning have been employed. These include Mean Squared Logarithmic Error (MSLE), Learning Rate (LR), Early Stopping (ES), Split Ratio (SR), and Batch Size (BS). The relevance of these terms to the current work will become evident as they appear throughout the text.

### Machine Learning Models

| Model              | R² (Val. Data) | SR (%) | Leaderboard Score\* |
|--------------------|-----------------|-----------------|-------------|
| Linear Regression  | 0.91152         |       85/15     | 0.35392     |
| Regression Tree    | 0.80361         |       85/15     | 0.23367     |

### Deep Learning Models

| Model    | EPOCHs | LR   | BS  | ES | Patience | Loss  | SR (%) | Leaderboard Score\* |
|----------|--------|------|-----|-------|----------|-------|----------|---------|
| FFDNN    | 4000   | 1e-4 |  20 |  Yes  | 200      | MSLE  |  85/15   | 0.21338 |

#### Deep Learning Models Training Metrics

| Model    | Loss | Loss (Train. Data) | Loss (Val. Data) | R² (Train. Data) | R² (Val. Data) |
|----------|------|---------------------|------------------|-------------------|----------------|
| FFDNN    | MSLE | 0.0393              |  0.0511          |  0.7510           |  0.2834        |

**\*** Leaderboard scores are based on the Root Mean Squared Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price. Lower scores indicate better performance.

## Repository Structure

Project files and folder structure:
- `models`: Models folder.
- `submission`: Submission files for each model.
- `data/train.csv`: Training data set.
- `data/test.csv`: Test data set.
- `data/data_description.txt`: Dataset feature description.
- `data/sample_submission.csv`: Sample submission file.

## Acknowledgments

For detailed information about the code and its functionalities, please refer to the inline comments within the source files. Feel free to explore the codebase and contribute to further enhancements or bug fixes!

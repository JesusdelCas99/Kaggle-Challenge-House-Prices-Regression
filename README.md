# House-Prices-Advanced-Regression-Techniques
This project tackles the Kaggle challenge [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques), aiming to predict the sales prices of residential homes in Ames, Iowa. 


## Table of Contents
- [Model Summary](#model-summary)
- [Repository Structure](#repository-structure)
- [Acknowledgments](#acknowledgments)

## Competition Description
Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges you to predict the final price of each home.

![House Prices Kaggle Banner](https://storage.googleapis.com/kaggle-media/competitions/House%20Prices/kaggle_5407_media_housesbanner.png)


## Model Summary
The table below provides an overview of the models developed for this competition:

| Model              | R²      | Leaderboard Score (*) | Training Split Ratio | Validation Split Ratio |
|--------------------|---------|-------------------|----------------------|------------------------|
| Linear Regression  | 0.91152 | 0.35392           | 0.85                 | 0.15                   |
| Regression Tree    | 0.80361 | 0.23367           | 0.85                 | 0.15                   |

(**\***) Submissions are evaluated on Root-Mean-Squared-Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price.

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

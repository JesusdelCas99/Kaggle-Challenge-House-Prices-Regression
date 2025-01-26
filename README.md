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

The table below provides an overview of the models developed and fine-tuned for this competition:

### Machine Learning Models

| <img width=38/>Model<img width=38/>               | KFold | RMSLE | R²   | L. Score* |
|:---------------------------------------------:|:-----:|:------:|:-----------:|:----------:|
| Linear Regression                             |   10  | 0.3507 | 0.7124 |    0.2004  |
| Regression Tree                               |   10  | 0.2161 | 0.7034 |   0.1734  |

### Ensembling Methods

| <img width=38/>Model<img width=38/>                 | KFold | RMSLE | R²    | L. Score* |
|:-----------------------------------------------:|:-----:|:------:|:-----------:|:----------:|
| Random Forest                                   |   10  | 0.1503 | 0.8593 |  0.1550  |

### Deep Learning Models

| <img width=38/>Model<img width=38/> | KFold | RMSLE | R²  | L. Score* |
|:--------------------------:|:-----:|:------:|:-----------:|:----------:|
| FFDNN                      |   10  | 0.2048 | 0.6872 |  0.2156  |  


**\*** Leaderboard Scores (LS) are based on the Root Mean Squared Logarithmic Error (RMSLE) between the predicted values and the observed sales price. Lower scores indicate better performance.


## Acknowledgments

The Ames Housing dataset was compiled by Dean De Cock for use in data science education. For detailed information about the code and its functionalities, please refer to the inline comments within the source files. Feel free to explore the codebase and contribute to further enhancements or bug fixes!

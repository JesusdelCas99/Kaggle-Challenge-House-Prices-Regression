import pandas as pd

def one_hot_encode_dataset(data: pd.DataFrame):
    # Identify categorical variables
    categorical_features = data.select_dtypes(include=['object']).columns

    # Apply one-hot encoding to the categorical variables
    encoded_data = pd.get_dummies(data, columns=categorical_features)

    return encoded_data


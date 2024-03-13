import pandas as pd

def one_hot_encode_dataset(data: pd.DataFrame):
    # Identificar variables categóricas
    categorical_features = data.select_dtypes(include=['object']).columns

    # Aplicar one-hot encoding a las variables categóricas
    encoded_data = pd.get_dummies(data, columns=categorical_features)

    return encoded_data


import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression


class Model:
    def __init__(self, data_path, model_path='model\\model.sav'):
        self.data_path = data_path
        self.model_path = model_path
        self.model = None

    def read_data(self):
        df = pd.read_csv(self.data_path, delimiter=',')
        df_numeric = df.select_dtypes(include=['number'])
        df_cleaned = df_numeric.dropna()
        self.X = df_cleaned[['upstream_water_level', 'downstream_water_level', 'inflow_rate']]
        self.y = df_cleaned['outflow_rate']

    def train(self):
        self.model = LinearRegression()
        self.model.fit(self.X, self.y)
        print("Model trained successfully.")

    def save_model(self):
        with open(self.model_path, 'wb') as file:
            pickle.dump(self.model, file)
        print(f"Model saved to {self.model_path}.")

    def create_model(self):
        self.read_data()
        self.train()
        self.save_model()


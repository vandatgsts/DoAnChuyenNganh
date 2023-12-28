import pickle


class RunModel:
    def __init__(self, model_path='model\\model.sav'):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        with open(self.model_path, 'rb') as file:
            self.model = pickle.load(file)
        print("Model loaded successfully.")

    def predict(self, input_data):
        if self.model is None:
            raise Exception("Model is not loaded. Please load the model first.")
        prediction = self.model.predict([input_data])
        return prediction




import numpy as np
import tensorflow.keras as kr
import rl_const as ct


class QNetwork:
    def __init__(self, input_dim=0, output_dim=0, model_path=None):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.prob = None

        self.model = kr.models.Sequential() 

        self.model.add(kr.layers.LSTM(128, input_shape=(1, input_dim), \
            dropout=0.3, kernel_initializer='random_normal', return_sequences=True))
        self.model.add(kr.layers.BatchNormalization())
        self.model.add(kr.layers.LSTM(64, \
            dropout=0.3, kernel_initializer='random_normal', return_sequences=True))
        self.model.add(kr.layers.BatchNormalization())
        self.model.add(kr.layers.LSTM(32, \
            dropout=0.3, kernel_initializer='random_normal'))
        self.model.add(kr.layers.BatchNormalization())
        # activation='linear', 'softmax'
        self.model.add(kr.layers.Dense(output_dim, \
            activation='linear', kernel_initializer='random_normal'))
        # optimizer='sgd', loss='mse'
        self.model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

        # self.model.summary()

        if model_path is not None:
            self.load_model(model_path)

    def reset(self):
        self.prob = None

    def predict(self, sample):
        self.prob = self.model.predict(np.array(sample).reshape((1, -1, self.input_dim)))[0]
        return self.prob

    def train_on_batch(self, x, y):
        return self.model.train_on_batch(x, y)

    def save_model(self, model_path):
        if model_path is not None and self.model is not None:
            self.model.save_weights(model_path, overwrite=True)

    def load_model(self, model_path):
        if model_path is not None:
            self.model.load_weights(model_path)


if __name__ == "__main__":
    qnet = QNetwork(ct.STATE_SIZE, ct.ACTION_SIZE, ct.MODEL_PATH)
    qnet.reset()
    print('init complete!!')
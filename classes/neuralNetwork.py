import tensorflow as tf


class NeuralNetwork:
    def __init__(self, a, b, c, d=None):
        self.model = None
        self.input_nodes = None
        self.hidden_nodes = None
        self.output_nodes = None

        if(isinstance(a, tf.keras.Sequential)):
            self.model = a
            self.input_nodes = b
            self.hidden_nodes = c
            self.output_nodes = d
        else:
            self.input_nodes = a
            self.hidden_nodes = b
            self.output_nodes = c
            self.createModel()

        return

    def createModel(self):
        self.model = tf.keras.Sequential()

        hidden = tf.keras.layers.Dense(
            self.hidden_nodes,
            input_shape=(self.input_nodes,)
        )

        output = tf.keras.layers.Dense(
            self.output_nodes,
            activation="softmax"
        )

        self.model.add(hidden)
        self.model.add(output)

        print(self.model.summary())

        return

    def predict(self, inputs):
        # Put input array into tensor variable
        xs = tf.Variable(inputs, tf.float32)
        # Make a prediction
        ys = self.model.predict(xs)

        return ys

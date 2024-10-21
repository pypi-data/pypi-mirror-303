import numpy as np

                         #THE MODEL

class linear_regression():
    #initiating the hyperparameters
    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations

    def fit(self, x, y):

        self.x = x
        self.y = y

        #number of training examples and n° of features
        self.n, self.f = x.shape  #n° of rows and columns

        #initiating the parameters (all slopes & one unique intercept)

        #  1."Zero initiation"
        self.weights = np.zeros(self.f)
        self.bias = 0.0

        #gradient descent to minimize the loss
        for i in range(self.iterations):
            self.upgrade_w()

    def upgrade_w(self):
        y_predicted = self.predict(self.x)

        #calculating the gradients
        dw = -(2 * np.sum((self.x.T).dot(self.y - y_predicted)) )/ self.n
        db = -(2 * np.sum(self.y - y_predicted))/ self.n

        #now the new weights
        self.weights = self.weights - (self.learning_rate * dw)
        self.bias = self.bias - (self.learning_rate * db)

    def predict(self, x):
        return x.dot(self.weights) + self.bias
                        #IMPLEMENTING THE MODEL
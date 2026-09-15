class Model:
    #__init__ is intialized automatically everytime model class is used
    def __init__(self, learning_rate):  #Here self is standardized to refer that any upcoming paramter will be assigned to the particular instance with which it is created
        self.learning_rate = learning_rate #this means that for m = Model(0.1) will make 0.1 LR as LR for instance m
        self.weights = None

    def fit(self, X, y): #standardized in Data science where X refers to 2D matrix like grid and y refers to 1D list/vector
        self.weights = X.T @ X #T is used in numpy to get transpose of a matrix wheresas @ is used to perform matrix multiplication (dot-product)
        return self #this hands back the new weights back when this method is called
    
    def predict(self, X):
        return X @ self.weights
    


    
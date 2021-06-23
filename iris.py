from sklearn import datasets
iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target
print(X_iris.shape,y_iris.shape)
# data - input & no of input instance ; target - 3 iris species (output)
print(X_iris[0],y_iris[0])

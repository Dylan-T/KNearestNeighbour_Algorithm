import numpy
from scipy.spatial import distance

"""Load the data"""
trainingText = open("part1/iris-training.txt", "r")
trainingData = []
for line in trainingText:
    tokens = line.split()
    trainingData.append(numpy.array((float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3]))))


testingText = open("part1/iris-test.txt", "r")
testingData = []
for line in testingText:
    tokens = line.split()
    testingData.append(numpy.array((float(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3]))))

"""Initialise the value of k"""
k = 1

"""For getting the predicted class, iterate from 1 to total number of training data points"""
for x in range(1, 10):

    """Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as 
    our distance metric since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, 
    etc. """
    dist = numpy.linalg.norm(testingData[0]-trainingData[0])
    dst = distance.euclidean(testingData[0], trainingData[0])
    print(dst)
    print(dist)

    """Sort the calculated distances in ascending order based on distance values"""

    """Get top k rows from the sorted array"""

    """Get the most frequent class of these rows"""

    """Return the predicted class"""


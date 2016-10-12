from numpy import *
import operator

# To generate sample data set
def createDataSet():
  group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
  labels = ['A', 'A', 'B', 'B']
  return group, labels

# To classify X
def classify0(inX, dataSet, labels, k):
  dataSetSize = dataSet.shape[0]
  print "dataSetSize: %r" % dataSetSize
  # Calculate the distance between X and the current point 
  diffMat = tile(inX, (dataSetSize, 1)) - dataSet
  print "diffMat: %r" % diffMat
  sqDiffMat = diffMat ** 2
  sqDistances = sqDiffMat.sum(axis=1)
  print "sqDistances: %r" % sqDistances
  distances = sqDistances ** 0.5
  print "distances: %r" % distances
  # Sort the distance in increasing order
  sortedDistIndicies = distances.argsort()
  print "sortedDistIndicies: %r" % sortedDistIndicies
  classCount = {}
  # Take k items with lowest distances to X
  for i in range(k):
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
  
  sortedClassCount = sorted(classCount.iteritems(), 
    key = operator.itemgetter(1), reverse=True)
  
  return sortedClassCount[0][0]
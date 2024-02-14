class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getData(self):
        return (self.x, self.y)

    def setData(self, x, y):
        self.x = x
        self.y = y
        

class Cluster:
    def __init__(self, data):
        self.data = data
        self.centroid = Data(0, 0)

    def getCentroid(self):
        return self.centroid

    def setCentroid(self, x, y):
        self.centroid.setData(x, y)

    def addData(self, data):
        self.data.append(data)

    def removeData(self, data):
        self.data.remove(data)

    def getData(self):
        return self.data

    def clearData(self):
        self.data.clear()

    def getClusterSize(self):
        return len(self.data)



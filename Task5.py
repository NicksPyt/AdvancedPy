import pandas as pd

data_dict = {
    "students": ["nika", "salome", "saba"],
    "grade": [72, 84, 74]
}


class dataClass:
    def __init__(self):
        pass

    def saveCsv(self, data, filename):
        self.data = data
        self.filename = filename
        df = pd.DataFrame(self.data)  # excepted .csv file extension
        df.to_csv(self.filename)

    def loadCsv(self, filename):
        self.filename = filename
        df = pd.read_csv(self.filename)
        print(df)

    def saveJson(self, data, filename):
        self.data = data
        self.filename = filename
        df = pd.DataFrame(self.data)
        df.to_json(self.filename)  # excepted .json file extension

    def loadJson(self, filename):
        self.filename = filename
        df = pd.read_json(self.filename)
        print(df.to_string())  # use to_string() to print the entire DataFrame.

    def savePickle(self, data, filename):
        self.data = data
        self.filename = filename
        df = pd.DataFrame(self.data)
        df.to_pickle(self.filename)

    def loadPickle(self, filename):
        self.filename = filename
        df = pd.read_pickle(self.filename)  # excepted .dump file extension
        print(df)

"""for csv file"""
csvFile = dataClass()
csvFile.saveCsv(data_dict, 'dataCsv.csv')
csvFile.loadCsv('dataCsv.csv')


"""for json file"""
jsonFile = dataClass()
jsonFile.saveJson(data_dict, 'JsonData.json') 
jsonFile.loadJson('JsonData.json')


"""for pickle file"""
pickleFile = dataClass()
pickleFile.savePickle(data_dict, 'pickleFile.dump')
pickleFile.loadPickle('pickleFile.dump')
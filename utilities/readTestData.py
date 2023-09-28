import json


class ReadTestData:
    @staticmethod
    def testdata():
        file = open(r"C:\Users\Geethanjali_Pasala\PycharmProjects\flipkart\testdata\data.json", "r")
        data = json.loads(file.read())
        return data

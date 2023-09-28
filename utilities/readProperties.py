import configparser

config = configparser.ConfigParser()
config.read(r"C:\Users\Geethanjali_Pasala\PycharmProjects\flipkart\configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common data", "baseURL")
        return url

    @staticmethod
    def get_browsers():
        browsers = [config.get("browsers", "chrome"), config.get("browsers", "edge")]
        print(browsers)
        return browsers


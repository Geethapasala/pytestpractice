import logging


class LogGenerator:

    @staticmethod
    def loggen():
        LogGenerator.logger = logging.getLogger()
        LogGenerator.logger.setLevel(logging.INFO)
        print("Handlers", LogGenerator.logger.handlers)
        file_handler = logging.FileHandler(r"C:\Users\Geethanjali_Pasala\PycharmProjects\flipkart\logs\logs.log", "w")
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        LogGenerator.logger.addHandler(file_handler)
        return LogGenerator.logger

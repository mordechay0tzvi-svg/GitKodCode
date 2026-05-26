import logging
def get_logger(name):
    new_logger = logging.getLogger(name)
    new_logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("file.log", encoding= "utf-8")
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(format)
    file_handler.setFormatter(format)
    new_logger.addHandler(stream_handler)
    new_logger.addHandler(file_handler)
    return new_logger


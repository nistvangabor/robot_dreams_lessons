import logging

#HANDLER: hová íródjon ki a log üzenet
#FORMATTER: mik jelenjenek meg a log üzenetben
#A formatter-t adjuk hozzá a handler-hez, így eltérő helyekre eltérő formátumban tudunk logolni. Ezután a loggerhez hozzáadjuk a handler-öket

file_handler = logging.FileHandler("app.log") #file-ba logol
stream_handler = logging.StreamHandler() #konzolra logol

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

#adjuk hozzá a formattert a handler-hez
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# logging level beállítása
file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.DEBUG)

#create a logger

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

#logging messages:
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("error message")
logger.critical("critical error")
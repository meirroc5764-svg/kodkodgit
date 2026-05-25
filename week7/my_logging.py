import logging
from datetime import datetime

#create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#create handler
file_handler = logging.FileHandler("my_logging.log", encoding="utf-8")
#create formate 
format = logging.Formatter("%(asctime)s| %(levelname)s|%(name)s|%(message)s")

file_handler.setFormatter(format)
logger.addHandler(file_handler)

#1)
def add(a,b):
    logger.info("start function add a=%s,b=%s",a,b)
    try:
        logger.info("the function successfully add a=%s, b=%s",a,b)
        return a + b
    except Exception as e:
        logger.error("adding eror %s",e)
add(5,6)

#2)
def user_id_and_time(user_id):
    time = datetime.now()
    logger.info("user id=%s ahd time=%s",user_id, time)
    return
user_id_and_time(1234)

#3)

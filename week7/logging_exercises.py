#1)✅ ❌
#1.❌
#2.✅
#3.❌
#4.❌
#5.✅
#6.✅
#7.❌

#2)
#1.INFO
#2.ERROR
#3.DEBUG
#4.WARNING
#5.WARNING
#6.INFO

#3)
# logger.info('User logged in successfully')

# logger.info('Login=%s password=%s', email, bool(password))

# logger.eror('ERROR: payment failed')

#4)
#%(asctime)s: data and time 
#%(levelname)s: type eror
#%(name)s: neme file program
#%(message)s: string messege 

#5)
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')

#6)
def process_payment(user_id, amount):
    logger.info('Starting payment for user=%s',user_id)
    if amount <= 0:
        logger.error('ERROR: Invalid amount')
        return
    if amount > 10000:
        logger.warning('WARNING: Large transaction')
    logger.info('Payment of amount=%s completed for user=%s',amount,user_id)

#7)
logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    encoding="utf-8",
                    format="%(asctime)s|%(levelname)s|%(name)s|%(message)s")
logger = logging.getLogger(__name__)

def add(a,b):
    logger.debug("Start login function")
    logger.info("start function add a=%s,b=%s",a,b)
    try:
        logger.info("the function successfully add a=%s, b=%s",a,b)
        return a + b
    except Exception as e:
        logger.error("adding eror %s",e)
add(5,6)

#8)
def read_config(filepath):
    logger.debug("Trying to open file: %s", filepath)
    try:
        with open(filepath) as f:
            data = f.read()
            logger.info("File opened successfully: %s", filepath)
        return data
    except FileNotFoundError:
        logger.exception("File not found: %s", filepath)
    return None

#9)
from datetime import datetime
import json

my_data = {"timestamp": datetime.utcnow().isoformat(),
    "level": "INFO",
    "module": "auth",
    "message": "User logged in",
    "user_id": 42}
json_data = json.dumps(my_data)
print(json_data)

#10)
#1. need more information info(function finish to do somthin)
#2. need more information error(function faled no have somthnik)
#3. need more information and dont print user information info(what to do with bool user id )

#11)
# 1. info
# 2. eror
# 3. debug
# 4. warning
# 5. info
# 6. eror
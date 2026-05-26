import json
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_payment(user_id, amount):
    logging.info(f'Starting payment for user {user_id}')
    if amount <= 0:
        logging.error('Invalid amount')
        return
    if amount > 10000:
        logging.warning('Large transaction')
    logging.info(f'Payment of {amount} completed for user {user_id}')



logger = logging.getLogger("write3logs")
logger.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('write_3_logs.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
def write_3_logs():
    logger.info('function starts')
    logger.debug("function runs")
    logger.info("function ends")

write_3_logs()



readlog = logging.getLogger("read_config_logs")
logger.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('read_config.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
log_handler.setFormatter(formatter)
readlog.addHandler(log_handler)

def read_config(filepath):
    readlog.debug('reading config file')
    try:
        with open(filepath) as f:
            data = f.read()
            readlog.info("successfully read config file")
        return data
    except FileNotFoundError:
        readlog.exception("could not find config file")
        return None



from datetime import datetime, timezone
def write_structured_log(message, level, module, **extra):
    log = {"timestamp": datetime.now(timezone.utc).isoformat(), "level": level, "module": module, "message": message, **extra}
    print(json.dumps(log))

write_structured_log("savage", "INFO", __name__, ip = "1234567")


import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def register_user(email, password, age):
    logger.debug('register')
    if age < 18:
        logger.error('age is under 18')
        return
    logger.info("email and password are acceptable")
    logger.info('user registered')



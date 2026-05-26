def build_log(name):
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("logs.logs", "utf-8")
    format = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
    handler.setFormatter(format)
    logger.addHandler(handler)
    return logger



import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)
def write_log(level, module_name, message, **extra):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "module": module_name,
        "message": message,
        **extra,
    }
    logger.info(json.dumps(entry, ensure_ascii=False))
    

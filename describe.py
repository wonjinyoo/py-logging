import sys
import logging
import pandas as pd

# 로그 구성 템플릿 (로거 이름, 로그 심각성 수준, 로그 메시지)
log_format = "[%(name)s][%(levelname)-6s] %(message)s"
logging.basicConfig(format=log_format)
logger = logging.getLogger("describe") # 로거 이름
logger.setLevel(logging.error) # 심각성 수준

argument = sys.argv[-1]
logger.debug("processing input files: %s", argument) # 로그 메시지

try:
    df = pd.read_csv(argument)
    print(df.describe())
except Exception:
    logger.exception("Had a problem trying to read the CSV file") # traceback

logger.info("the program continues, without issue")
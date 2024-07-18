import requests
import logging

logging.basicConfig()

# 루트 로거
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# 이 스크립트에 대한 새로운 로거
logger = logging.getLogger('http-app')

logger.warning('example.com에 요청을 전송합니다.')
requests.get('http://example.com')

# urllib3 package logger
urllib_logger = logging.getLogger('urllib3')
urllib_logger.setLevel(logging.ERROR)

logger.info('example.com에 요청을 전송합니다.')
requests.get('http://example.com')
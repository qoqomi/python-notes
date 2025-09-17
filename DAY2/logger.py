import logging
import os
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv


def setup_logger():
    """drink_order.log 로거 설정"""
    # .env 파일 로드
    load_dotenv()

    # 환경 변수에서 로그 레벨 가져오기 (기본값 INFO)
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level, logging.INFO)

    # logs 디렉토리 생성
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "drink_order.log")

    # 로거 생성
    logger = logging.getLogger("DrinkOrderApp")
    logger.setLevel(log_level)
    logger.handlers.clear()

    # 포맷 정의
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # 파일 핸들러 (자정마다 새 파일, 7일 보관)
    file_handler = TimedRotatingFileHandler(
        filename=log_file, when="midnight", interval=1, backupCount=7, encoding="utf-8"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # 핸들러 등록
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

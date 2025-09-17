"""
====================================
# 과제명: Logging 설정 및 사용 (간단한 리팩토링)
# 작성자: 유승연 / 2077
# 작성일: 2025-09-16
# 설명:
  .env 파일에서 로깅 레벨을 가져와 콘솔과 파일(app.log)에 동시에 출력하는 프로그램
  1) logs 디렉토리를 생성하고 app.log 파일에 로그 기록
  2) .env 파일에서 LOG_LEVEL 값을 읽어와 로깅 레벨 설정
  3) 콘솔 핸들러와 파일 핸들러를 동시에 추가하여 로그 출력
  4) 로그 포맷: 시간 [레벨] 메시지
  5) 파일 핸들러는 TimedRotatingFileHandler 사용 (매일 자정에 로테이션, 7일 보관)
  6) 4단계 - 로그 출력 테스트: INFO, DEBUG, ERROR 레벨 테스트 및 예외 처리
====================================
"""

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv


def setup_logger():
    """로거 설정 함수"""
    # .env 파일 로드
    load_dotenv()

    # 환경 변수에서 로그 레벨 읽기
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level, logging.INFO)

    # 로그 디렉토리 생성
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")

    # 로거 생성
    logger = logging.getLogger("MyApp")
    logger.setLevel(log_level)

    # 기존 핸들러 제거 (중복 방지)
    logger.handlers.clear()

    # 로그 포맷 정의
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # 파일 핸들러 (매일 자정에 로테이션, 7일 보관)
    file_handler = TimedRotatingFileHandler(
        filename=log_file, when="midnight", interval=1, backupCount=7, encoding="utf-8"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # 핸들러 추가
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def simulate_zero_division_error():
    """ZeroDivisionError 예외를 의도적으로 발생시키는 함수"""
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError as e:
        raise e


def main():
    """메인 실행 함수"""
    # 로거 설정
    logger = setup_logger()

    # === 4단계: 로그 출력 테스트 ===

    # INFO 레벨 메시지: "앱 실행 시작"
    logger.info("앱 실행 시작")

    # DEBUG 레벨 메시지: "환경 변수 로딩 완료"
    logger.debug("환경 변수 로딩 완료")

    # ERROR 레벨 메시지: ZeroDivisionError 예외 발생 시 출력
    try:
        simulate_zero_division_error()
    except ZeroDivisionError as e:
        logger.error(f"ZeroDivisionError 예외 발생: {str(e)}")

    # 추가 로깅 테스트
    logger.info("=== 로깅 테스트 시작 ===")
    logger.warning("경고 메시지")
    logger.critical("치명적 오류")
    logger.info("=== 로깅 테스트 완료 ===")


if __name__ == "__main__":
    main()

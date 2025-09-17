from logger import setup_logger
from order_system import BeverageOrderSystem


def main():
    logger = setup_logger()
    system = BeverageOrderSystem()

    logger.info("앱 실행 시작")
    system.setup_menu()
    logger.debug("메뉴 세팅 완료")

    # 주문 예시
    system.add_order("김철수", 1, 2)
    system.add_order("김철수", 2, 1)

    logger.info("주문 처리 완료")


if __name__ == "__main__":
    main()

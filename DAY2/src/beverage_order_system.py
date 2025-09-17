"""
====================================
# 과제명: 온라인 음료 주문 플랫폼 (추천 시스템 포함)
# 작성자: [유승연] / [2077]
# 작성일: 2025-09-17
# 설명:
  스타트업 온라인 음료 주문 플랫폼 개발 프로그램
  1) 다양한 음료 메뉴 정의 (이름, 가격, 태그)
  2) 사용자 주문 내역 저장 및 관리
  3) 최근 주문 기반 유사 태그 음료 추천
  4) 총 주문 금액 계산 (총합, 평균 등)
====================================
"""

from dataclasses import dataclass
from typing import List, Optional


# ---------------------------------
# 데이터 클래스 정의
# ---------------------------------
@dataclass
class Beverage:
    """음료 클래스: id, 이름, 가격, 태그(특징)"""

    id: int
    name: str
    price: int
    tags: List[str]


@dataclass
class Order:
    """주문 클래스: 사용자, 음료 객체, 수량"""

    user_id: int
    beverage: Beverage
    quantity: int


# ---------------------------------
# 음료 주문 시스템
# ---------------------------------
class BeverageOrderSystem:
    def __init__(self, menu: Optional[List[Beverage]] = None):
        self.menu: List[Beverage] = menu or []  # 음료 메뉴 리스트
        self.orders: List[Order] = []  # 주문 내역 리스트

    def setup_menu(self) -> None:
        """기본 메뉴 세팅"""
        self.menu = [
            Beverage(1, "아이스 아메리카노", 3000, ["커피", "차가운"]),
            Beverage(2, "카페라떼", 3500, ["커피", "밀크", "뜨거운"]),
            Beverage(3, "녹차", 2800, ["차", "뜨거운"]),
            Beverage(4, "허브티", 3000, ["차", "뜨거운"]),
            Beverage(5, "아이스티", 2500, ["차", "차가운"]),
            Beverage(6, "핫초콜릿", 4000, ["초콜릿", "뜨거운"]),
        ]

    def show_menu(self) -> None:
        """메뉴 출력"""
        for i, beverage in enumerate(self.menu, 1):
            tags_str = ", ".join(beverage.tags)
            print(f"{i}. {beverage.name} - {beverage.price}원 [{tags_str}]")

    def find_beverage(self, id: int) -> Optional[Beverage]:
        """id로 특정 음료 찾기"""
        for beverage in self.menu:
            if beverage.id == id:
                return beverage
        return None

    def add_order(self, user_id: str, beverage_id: int, quantity: int = 1) -> bool:
        """사용자 주문 추가"""
        beverage = self.find_beverage(beverage_id)
        if beverage:
            order = Order(user_id, beverage, quantity)
            self.orders.append(order)
            total_price = beverage.price * quantity
            print(f"✅ 주문 완료: {beverage.name} x{quantity} = {total_price}원")
            return True
        else:
            print(f"❌ 존재하지 않는 음료 ID: {beverage_id}")
            return False

    def get_user_orders(self, user_id: str) -> List[Order]:
        """특정 사용자의 주문 내역 조회"""
        return [order for order in self.orders if order.user_id == user_id]

    def calculate_total(self, user_id: str) -> dict:
        """사용자 총 주문 금액 및 평균 계산"""
        user_orders = self.get_user_orders(user_id)
        if not user_orders:
            return {"총액": 0, "평균": 0, "주문수": 0}

        total = sum(order.beverage.price * order.quantity for order in user_orders)
        count = len(user_orders)
        average = total / count

        return {"총액": total, "평균": round(average, 2), "주문수": count}

    def recommend_by_recent_tags(self, user_id: str, top_k: int = 3) -> List[Beverage]:
        """최근 주문 음료의 태그를 기준으로 유사한 음료 추천"""
        user_orders = self.get_user_orders(user_id)
        if not user_orders:
            return []

        # 가장 최근 주문 가져오기
        last_order = user_orders[-1]
        last_tags = set(last_order.beverage.tags)

        candidates = []
        for b in self.menu:
            if b.id == last_order.beverage.id:
                continue
            score = len(last_tags & set(b.tags))  # 태그 교집합 개수
            if score > 0:
                candidates.append((score, b))

        # 정렬 기준: 태그 겹치는 수 ↓, 가격 ↑
        candidates.sort(key=lambda x: (-x[0], x[1].price))

        return [b for _, b in candidates[:top_k]]


# ---------------------------------
# End of code
# ---------------------------------
def main():

    # 1. 시스템 초기화 + 메뉴 세팅
    system = BeverageOrderSystem()
    print("\n=== 메뉴 출력 ===")
    system.setup_menu()
    system.show_menu()

    # 2. 주문 처리 (테스트 시나리오)
    print("\n=== 주문 처리 ===")
    system.add_order("김철수", 1, 2)  # 아이스 아메리카노 2잔
    system.add_order("김철수", 2, 1)  # 카페라떼 1잔
    system.add_order("이영희", 3, 1)  # 녹차 1잔
    system.add_order("이영희", 99, 1)  # 없는 메뉴 테스트

    # 3. 사용자별 주문 내역 + 총액/평균 + 추천
    print("\n=== 주문 내역 & 추천 ===")
    for user in ["김철수", "이영희"]:
        orders = system.get_user_orders(user)
        if orders:
            print(f"\n{user}의 주문:")
            for order in orders:
                total = order.beverage.price * order.quantity
                print(f"  - {order.beverage.name} x{order.quantity} = {total}원")

            # 총 금액 계산
            total_info = system.calculate_total(user)
            print(f"  총 주문 통계: {total_info}")

            # 추천 메뉴 출력
            recs = system.recommend_by_recent_tags(user, top_k=3)
            if recs:
                rec_names = ", ".join(b.name for b in recs)
                print(f"  👉 최근 취향 기반 추천: {rec_names}")
            else:
                print("  👉 추천할 메뉴가 없습니다.")


if __name__ == "__main__":
    main()

"""
main_assignment.py - Menu chạy thử toàn bộ assignment POLY-SHIP

File này dùng để gọi demo từ 3 module:
- routing.py
- hashing_tools.py
- promo_optimizer.py

Chạy:
    python main_assignment.py
"""

from assingment.routing import demo_routing_shortest_path, demo_mst_network

from assingment.hashing_tools import (
    demo_order_hash_table,
    demo_group_coupon_anagrams,
    demo_longest_consecutive_days,
    demo_count_revenue_windows,
    demo_rolling_coupon_search,
)

from promo_optimizer import (
    demo_dp_basics,
    demo_combo_knapsack_2d,
    demo_combo_knapsack_1d,
)


def show_menu():
    """
    In menu chính cho người dùng chọn demo muốn chạy.
    """
    print("\n================ POLY-SHIP DSA ASSIGNMENT ================")
    print("1. Demo routing - shortest path giữa 2 kho")
    print("2. Demo MST - mạng kho tối thiểu")
    print("3. Demo hash table đơn hàng")
    print("4. Demo hashing: group anagrams, ngày liên tiếp, subarray sum = k")
    print("5. Demo rolling hash tìm pattern trong log")
    print("6. Demo DP cơ bản: fibonacci, climbing stairs")
    print("7. Demo combo khuyến mãi: knapsack 0/1 bản 2D và 1D")
    print("8. Thoát")
    print("===========================================================")


def run_choice(choice):
    """
    Nhận lựa chọn từ người dùng và gọi demo tương ứng.
    """
    if choice == "1":
        source = input("Nhập điểm bắt đầu, ví dụ WH1: ").strip()
        target = input("Nhập điểm kết thúc, ví dụ HN: ").strip()

        if source == "":
            source = "WH1"

        if target == "":
            target = "HN"

        demo_routing_shortest_path(source, target)

    elif choice == "2":
        demo_mst_network()

    elif choice == "3":
        demo_order_hash_table()

    elif choice == "4":
        demo_group_coupon_anagrams()
        demo_longest_consecutive_days()
        demo_count_revenue_windows()

    elif choice == "5":
        demo_rolling_coupon_search()

    elif choice == "6":
        demo_dp_basics()

    elif choice == "7":
        demo_combo_knapsack_2d()
        demo_combo_knapsack_1d()

    elif choice == "8":
        print("Kết thúc chương trình. Tạm biệt!")
        return False

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 8.")

    return True


def main():
    """
    Vòng lặp menu chính.
    Chương trình sẽ chạy cho đến khi người dùng chọn 8 để thoát.
    """
    running = True

    while running:
        show_menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()
        running = run_choice(choice)


if __name__ == "__main__":
    main()

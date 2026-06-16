from routing import demo_routing_shortest_path, demo_mst_network

from hashing_tools import (
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
    print("\n================ POLY-SHIP DSA ASSIGNMENT ================")
    print("1. Routing - shortest path")
    print("2. MST network")
    print("3. Hash table demo")
    print("4. Hashing algorithms demo")
    print("5. Rolling hash demo")
    print("6. DP basics")
    print("7. Knapsack demo")
    print("8. Thoát")
    print("===========================================================")


def run_choice(choice):
    if choice == "1":
        demo_routing_shortest_path("WH1", "HN")

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
        print("Thoát chương trình")
        return False

    else:
        print("Lựa chọn không hợp lệ")

    return True


def main():
    running = True
    while running:
        show_menu()
        choice = input("Chọn: ")
        running = run_choice(choice)


if __name__ == "__main__":
    main()
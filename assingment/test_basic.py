"""
tests/test_basic.py - Test đơn giản cho assignment POLY-SHIP

Chạy:
    python tests/test_basic.py
"""

import sys
from pathlib import Path

# Thêm thư mục cha vào sys.path để import được các file .py chính
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from assingment.routing import build_graph, shortest_route, get_sample_polyship_edges, kruskal_mst
from assingment.hashing_tools import (
    OrderHashTable,
    group_coupon_anagrams,
    longest_consecutive_days,
    count_revenue_windows,
    rolling_hash_search,
)
from promo_optimizer import fib_tab, climb_stairs, build_combo_dp_table, combo_knapsack_1d


def test_routing_shortest_path():
    edges = get_sample_polyship_edges()
    graph = build_graph(edges)

    cost, route = shortest_route(graph, "WH1", "HN")

    assert cost == 13
    assert route == ["WH1", "HCM", "DN", "HN"]


def test_kruskal_mst():
    edges = get_sample_polyship_edges()
    vertices = sorted({u for u, v, cost in edges} | {v for u, v, cost in edges})

    mst_edges, total_cost = kruskal_mst(vertices, edges)

    assert len(mst_edges) == len(vertices) - 1
    assert total_cost > 0


def test_order_hash_table():
    table = OrderHashTable(capacity=5)

    table.insert("ORD001", {"customer": "An"})
    table.insert("ORD002", {"customer": "Binh"})

    assert table.get("ORD001") == {"customer": "An"}
    assert table.get("ORD999") is None

    assert table.remove("ORD002") is True
    assert table.get("ORD002") is None


def test_group_coupon_anagrams():
    codes = ["SAVE10", "AVES10", "ABC", "CAB"]
    groups = group_coupon_anagrams(codes)

    sorted_groups = [sorted(group) for group in groups]

    assert sorted(["SAVE10", "AVES10"]) in sorted_groups
    assert sorted(["ABC", "CAB"]) in sorted_groups


def test_longest_consecutive_days():
    days = [10, 11, 12, 20, 30, 31]
    assert longest_consecutive_days(days) == 3


def test_count_revenue_windows():
    revenues = [100, 200, 300, 100, 200]
    k = 300

    assert count_revenue_windows(revenues, k) == 4


def test_rolling_hash_search():
    text = "ABC SAVE10 XYZ SAVE10"
    pattern = "SAVE10"

    assert rolling_hash_search(text, pattern) == [4, 15]


def test_dp_basics():
    assert fib_tab(8) == 21
    assert climb_stairs(5) == 8


def test_knapsack():
    prices = [3, 4, 5, 2, 1]
    scores = [30, 50, 60, 25, 15]
    B = 8

    dp = build_combo_dp_table(prices, scores, B)
    result_2d = dp[len(prices)][B]
    result_1d = combo_knapsack_1d(prices, scores, B)

    assert result_2d == result_1d


if __name__ == "__main__":
    test_routing_shortest_path()
    test_kruskal_mst()
    test_order_hash_table()
    test_group_coupon_anagrams()
    test_longest_consecutive_days()
    test_count_revenue_windows()
    test_rolling_hash_search()
    test_dp_basics()
    test_knapsack()

    print("Tất cả test đều chạy thành công!")

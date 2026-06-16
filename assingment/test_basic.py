import sys
from pathlib import Path

# add project root
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from routing import build_graph, shortest_route, kruskal_mst
from hashing_tools import (
    OrderHashTable,
    group_coupon_anagrams,
    longest_consecutive_days,
    count_revenue_windows,
    rolling_hash_search,
)
from promo_optimizer import fib_tab, climb_stairs, build_combo_dp_table, combo_knapsack_1d


# =========================
# ROUTING TEST
# =========================
def test_routing():
    edges = [
        ("WH1", "HCM", 5),
        ("HCM", "DN", 3),
        ("DN", "HN", 5),
        ("WH1", "DN", 20),
        ("HCM", "HN", 15),
    ]

    graph = build_graph(edges)
    cost, route = shortest_route(graph, "WH1", "HN")

    print("ROUTE:", route, "COST:", cost)

    assert route == ["WH1", "HCM", "DN", "HN"]


# =========================
# MST TEST
# =========================
def test_mst():
    edges = [
        ("A", "B", 1),
        ("B", "C", 2),
        ("A", "C", 3),
    ]

    vertices = ["A", "B", "C"]

    mst_edges, total_cost = kruskal_mst(vertices, edges)

    print("MST:", mst_edges, "COST:", total_cost)

    assert len(mst_edges) == 2


# =========================
# HASH TABLE TEST
# =========================
def test_hash_table():
    table = OrderHashTable(capacity=5)

    table.insert("A1", {"item": 100})
    table.insert("A2", {"item": 200})

    assert table.get("A1") == {"item": 100}
    assert table.get("A2") == {"item": 200}


# =========================
# ANAGRAM TEST
# =========================
def test_anagram():
    codes = ["ABC", "BCA", "XYZ"]
    res = group_coupon_anagrams(codes)

    print("ANAGRAM:", res)


# =========================
# CONSECUTIVE DAYS
# =========================
def test_consecutive():
    days = [1, 2, 3, 10, 11]
    assert longest_consecutive_days(days) == 3


# =========================
# REVENUE TEST (FIXED DEBUG)
# =========================
def test_revenue():
    revenues = [100, 200, 300, 100, 200]
    k = 300

    res = count_revenue_windows(revenues, k)

    print("REVENUE RESULT:", res)


# =========================
# ROLLING HASH
# =========================
def test_hash():
    text = "SAVE10 ABC SAVE10"
    pattern = "SAVE10"

    res = rolling_hash_search(text, pattern)
    print("ROLLING HASH:", res)


# =========================
# DP TEST
# =========================
def test_dp():
    assert fib_tab(8) == 21
    assert climb_stairs(5) == 8


# =========================
# KNAPSACK TEST
# =========================
def test_knapsack():
    prices = [3, 4, 5]
    scores = [30, 50, 60]
    B = 8

    dp = build_combo_dp_table(prices, scores, B)
    res = combo_knapsack_1d(prices, scores, B)

    print("KNAPSACK:", res)


# =========================
# RUN ALL
# =========================
if __name__ == "__main__":
    test_routing()
    test_mst()
    test_hash_table()
    test_anagram()
    test_consecutive()
    test_revenue()
    test_hash()
    test_dp()
    test_knapsack()

    print("\nALL TEST DONE")
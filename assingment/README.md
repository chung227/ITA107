# POLY-SHIP DSA Assignment

## 1. Giới thiệu

Project này là bài assignment môn **Cấu trúc dữ liệu và giải thuật**.

Bối cảnh bài toán: hệ thống hậu cần POLY-SHIP cần dùng các thuật toán DSA để:

- Tìm tuyến giao hàng rẻ nhất giữa các kho.
- Thiết kế mạng kho tối thiểu.
- Tra cứu và xử lý dữ liệu đơn hàng bằng hashing.
- Tối ưu combo khuyến mãi bằng dynamic programming.

Project tập trung vào thuật toán, không tập trung vào giao diện đẹp.

---

## 2. Cấu trúc thư mục

```text
POLY_SHIP_Assignment/
├── routing.py
├── hashing_tools.py
├── promo_optimizer.py
├── main_assignment.py
├── README.md
└── tests/
    └── test_basic.py
```

---

## 3. Mô tả từng file

### `routing.py`

Gồm các thuật toán Phần 1:

- `build_graph(edges)`
- `dijkstra(graph, source)`
- `shortest_route(graph, source, target)`
- `DSU`
- `kruskal_mst(vertices, edges)`
- `demo_routing_shortest_path()`
- `demo_mst_network()`

Chạy riêng:

```bash
python routing.py
```

---

### `hashing_tools.py`

Gồm các thuật toán Phần 2:

- `OrderHashTable`
- `group_coupon_anagrams(codes)`
- `longest_consecutive_days(days)`
- `count_revenue_windows(revenues, k)`
- `rolling_hash_search(text, pattern)`

Chạy riêng:

```bash
python hashing_tools.py
```

---

### `promo_optimizer.py`

Gồm các thuật toán Phần 3:

- `fib_tab(n)`
- `climb_stairs(n)`
- `build_combo_dp_table(prices, scores, B)`
- `trace_combo_from_dp(dp, prices, scores, B)`
- `combo_knapsack_1d(prices, scores, B)`

Chạy riêng:

```bash
python promo_optimizer.py
```

---

### `main_assignment.py`

Đây là file menu chính để chạy toàn bộ demo.

Chạy:

```bash
python main_assignment.py
```

Menu gồm:

```text
1. Demo routing - shortest path giữa 2 kho
2. Demo MST - mạng kho tối thiểu
3. Demo hash table đơn hàng
4. Demo hashing: group anagrams, ngày liên tiếp, subarray sum = k
5. Demo rolling hash tìm pattern trong log
6. Demo DP cơ bản: fibonacci, climbing stairs
7. Demo combo khuyến mãi: knapsack 0/1 bản 2D và 1D
8. Thoát
```

---

## 4. Cách chạy project

Bước 1: Mở terminal trong thư mục project.

Bước 2: Chạy file menu chính:

```bash
python main_assignment.py
```

Bước 3: Nhập số từ 1 đến 8 để chọn demo.

---

## 5. Chạy test tùy chọn

Nếu muốn chạy test:

```bash
python tests/test_basic.py
```

File test kiểm tra nhanh một số kết quả cơ bản của Dijkstra, hashing và DP.

---

## 6. Ghi chú

- Project dùng Python 3.
- Không dùng thư viện giải thuật nâng cao như `networkx`, `numpy`.
- Các thuật toán được cài đặt thủ công để đúng yêu cầu assignment.

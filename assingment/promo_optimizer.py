"""
promo_optimizer.py - Phần 3: Dynamic Programming cho gợi ý khuyến mãi POLY-SHIP

Nội dung theo yêu cầu đề bài:
3.1. DP cơ bản:
     - fib_tab(n)
     - climb_stairs(n)
     - demo_dp_basics()

3.2. Khuyến mãi combo - Knapsack 0/1 bản 2D:
     - build_combo_dp_table(prices, scores, B)
     - trace_combo_from_dp(dp, prices, scores, B)
     - demo_combo_knapsack_2d()

3.3. Tối ưu memory - Knapsack 0/1 bản 1D:
     - combo_knapsack_1d(prices, scores, B)
     - demo_combo_knapsack_1d()

Demo tổng hợp:
     - demo_all_promo_optimizer()
"""


# ============================================================
# 3.1. Ôn lại DP nhẹ: Fibonacci và Climbing Stairs
# ============================================================

def fib_tab(n):
    """
    Tính số Fibonacci thứ n bằng dynamic programming dạng bottom-up.

    Quy ước:
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n - 1) + fib(n - 2)
    """
    if n < 0:
        raise ValueError("n phải >= 0")

    if n == 0:
        return 0

    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs(n):
    """
    Tính số cách leo lên n bậc thang.
    Mỗi lần có thể leo 1 bậc hoặc 2 bậc.

    Công thức:
        ways[i] = ways[i - 1] + ways[i - 2]
    """
    if n < 0:
        raise ValueError("n phải >= 0")

    if n == 0:
        return 1

    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def demo_dp_basics():
    """
    Demo yêu cầu 3.1.
    In kết quả Fibonacci và Climbing Stairs với n nhỏ.
    """
    print("\n===== DEMO 3.1: DP CƠ BẢN =====")

    n_fib = 8
    n_stairs = 5

    print(f"fib_tab({n_fib}) =", fib_tab(n_fib))
    print(f"climb_stairs({n_stairs}) =", climb_stairs(n_stairs))

    print("\nTư duy DP:")
    print("- State: dp[i] là kết quả của bài toán nhỏ tại i.")
    print("- Transition: dp[i] được tính từ các trạng thái trước đó.")
    print("- Với Fibonacci/Stairs: dp[i] = dp[i - 1] + dp[i - 2]")


# ============================================================
# 3.2. Khuyến mãi combo - Knapsack 0/1 bản 2D
# ============================================================

def build_combo_dp_table(prices, scores, B):
    """
    Xây bảng DP 2D cho bài toán chọn combo khuyến mãi.

    Input:
        prices: danh sách giá sản phẩm
        scores: danh sách điểm khuyến mãi tương ứng
        B: ngân sách tối đa

    Ý nghĩa bảng:
        dp[i][b] = điểm khuyến mãi lớn nhất khi xét i sản phẩm đầu tiên
                   với ngân sách tối đa là b

    Đây là knapsack 0/1:
        - Mỗi sản phẩm chỉ được chọn hoặc không chọn.
        - Không được chọn lặp lại cùng một sản phẩm.
    """
    n = len(prices)

    dp = [[0 for _ in range(B + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        price = prices[i - 1]
        score = scores[i - 1]

        for b in range(B + 1):
            not_choose = dp[i - 1][b]

            choose = 0

            if price <= b:
                choose = dp[i - 1][b - price] + score

            dp[i][b] = max(not_choose, choose)

    return dp


def trace_combo_from_dp(dp, prices, scores, B):
    """
    Truy vết bảng DP để tìm các sản phẩm được chọn.

    Input:
        dp: bảng DP đã xây bằng build_combo_dp_table()
        prices: danh sách giá sản phẩm
        scores: danh sách điểm khuyến mãi
        B: ngân sách tối đa

    Output:
        selected_items: danh sách index sản phẩm được chọn
    """
    selected_items = []

    i = len(prices)
    b = B

    while i > 0 and b >= 0:
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(i - 1)
            b -= prices[i - 1]

        i -= 1

    selected_items.reverse()

    return selected_items


def print_dp_table(dp):
    """
    In bảng DP 2D ra màn hình.
    Bảng nhỏ thì in toàn bộ để dễ quan sát.
    """
    for row in dp:
        print(row)


def demo_combo_knapsack_2d():
    """
    Demo yêu cầu 3.2.
    Tạo bộ sản phẩm thử, in bảng DP, max score và sản phẩm được chọn.
    """
    print("\n===== DEMO 3.2: COMBO KHUYẾN MÃI - KNAPSACK 0/1 2D =====")

    product_names = ["Áo", "Giày", "Balo", "Tai nghe", "Sách"]
    prices = [3, 4, 5, 2, 1]
    scores = [30, 50, 60, 25, 15]
    B = 8

    dp = build_combo_dp_table(prices, scores, B)

    selected_items = trace_combo_from_dp(dp, prices, scores, B)

    max_score = dp[len(prices)][B]

    total_price = sum(prices[i] for i in selected_items)

    print("Danh sách sản phẩm:")
    for i in range(len(product_names)):
        print(
            f"{i}. {product_names[i]} - price = {prices[i]}, "
            f"bonus_score = {scores[i]}"
        )

    print("\nNgân sách tối đa B =", B)

    print("\nBảng DP 2D:")
    print_dp_table(dp)

    print("\nMax bonus_score:", max_score)

    print("\nCác sản phẩm được chọn:")
    for i in selected_items:
        print(
            f"- {product_names[i]} "
            f"(price = {prices[i]}, bonus_score = {scores[i]})"
        )

    print("Tổng price:", total_price)
    print("Tổng bonus_score:", max_score)

    return max_score, selected_items


# ============================================================
# 3.3. Tối ưu memory - Knapsack 0/1 bản 1D
# ============================================================

def combo_knapsack_1d(prices, scores, B):
    """
    Knapsack 0/1 bản tối ưu bộ nhớ bằng mảng 1D.

    Ý tưởng:
        dp[b] = điểm khuyến mãi lớn nhất với ngân sách b

    Lưu ý quan trọng:
        Phải duyệt b từ B về price.
        Nếu duyệt xuôi, một sản phẩm có thể bị chọn nhiều lần,
        sai với knapsack 0/1.
    """
    dp = [0] * (B + 1)

    n = len(prices)

    for i in range(n):
        price = prices[i]
        score = scores[i]

        for b in range(B, price - 1, -1):
            dp[b] = max(dp[b], dp[b - price] + score)

    return dp[B]


def demo_combo_knapsack_1d():
    """
    Demo yêu cầu 3.3.
    So sánh kết quả max score của bản 1D với bản 2D.
    """
    print("\n===== DEMO 3.3: COMBO KHUYẾN MÃI - KNAPSACK 0/1 1D =====")

    product_names = ["Áo", "Giày", "Balo", "Tai nghe", "Sách"]
    prices = [3, 4, 5, 2, 1]
    scores = [30, 50, 60, 25, 15]
    B = 8

    dp_2d = build_combo_dp_table(prices, scores, B)
    result_2d = dp_2d[len(prices)][B]

    result_1d = combo_knapsack_1d(prices, scores, B)

    print("Danh sách sản phẩm:")
    for i in range(len(product_names)):
        print(
            f"{i}. {product_names[i]} - price = {prices[i]}, "
            f"bonus_score = {scores[i]}"
        )

    print("\nNgân sách tối đa B =", B)
    print("Kết quả max score bản 2D:", result_2d)
    print("Kết quả max score bản 1D:", result_1d)

    if result_1d == result_2d:
        print("Nhận xét: Hai phiên bản cho cùng kết quả.")
    else:
        print("Nhận xét: Có lỗi vì hai phiên bản cho kết quả khác nhau.")

    return result_1d


# ============================================================
# Demo tổng hợp phần 3
# ============================================================

def demo_all_promo_optimizer():
    """
    Chạy toàn bộ demo của Phần 3.
    """
    demo_dp_basics()
    demo_combo_knapsack_2d()
    demo_combo_knapsack_1d()


if __name__ == "__main__":
    demo_all_promo_optimizer()

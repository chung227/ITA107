"""
hashing_tools.py - Phần 2: Hashing cho đơn hàng và dữ liệu POLY-SHIP

Nội dung theo yêu cầu đề bài:
2.1. OrderHashTable dùng separate chaining:
     - insert(order_id, order_data)
     - get(order_id)
     - remove(order_id)

2.2. group_coupon_anagrams(codes)

2.3. longest_consecutive_days(days)

2.4. count_revenue_windows(revenues, k)

2.5. rolling_hash_search(text, pattern) kiểu Rabin-Karp đơn giản

Các hàm demo:
- demo_order_hash_table()
- demo_group_coupon_anagrams()
- demo_longest_consecutive_days()
- demo_count_revenue_windows()
- demo_rolling_coupon_search()
- demo_all_hashing_tools()
"""


# ============================================================
# 2.1. Hash table dùng cho tra cứu đơn hàng
# ============================================================

class OrderHashTable:
    

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def _hash(self, order_id):

        total = 0

        for char in order_id:
            total += ord(char)

        return total % self.capacity

    def insert(self, order_id, order_data):
    
        index = self._hash(order_id)
        bucket = self.table[index]

        for i in range(len(bucket)):
            current_order_id, current_order_data = bucket[i]

            if current_order_id == order_id:
                bucket[i] = (order_id, order_data)
                return

        bucket.append((order_id, order_data))
        self.size += 1

    def get(self, order_id):
       
        index = self._hash(order_id)
        bucket = self.table[index]

        for current_order_id, current_order_data in bucket:
            if current_order_id == order_id:
                return current_order_data

        return None

    def remove(self, order_id):
    
        index = self._hash(order_id)
        bucket = self.table[index]

        for i in range(len(bucket)):
            current_order_id, current_order_data = bucket[i]

            if current_order_id == order_id:
                bucket.pop(i)
                self.size -= 1
                return True

        return False

    def display(self):
        
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index}: {bucket}")


def demo_order_hash_table():
   
    print("\n===== DEMO 2.1: ORDER HASH TABLE =====")

    orders = OrderHashTable(capacity=5)

    orders.insert("ORD001", {"customer": "An", "city": "HCM", "total": 250000})
    orders.insert("ORD002", {"customer": "Binh", "city": "HN", "total": 180000})
    orders.insert("ORD003", {"customer": "Chi", "city": "DN", "total": 320000})
    orders.insert("ORD004", {"customer": "Dung", "city": "CT", "total": 150000})

    print("Hash table sau khi insert:")
    orders.display()

    print("\nTra cứu ORD002:")
    print(orders.get("ORD002"))

    print("\nTra cứu ORD999:")
    print(orders.get("ORD999"))

    print("\nXóa ORD003:")
    removed = orders.remove("ORD003")
    print("Xóa thành công?", removed)

    print("\nHash table sau khi xóa:")
    orders.display()


# ============================================================
# 2.2. Group anagrams - nhóm mã coupon na ná nhau
# ============================================================

def group_coupon_anagrams(codes):
   
    groups = {}

    for code in codes:
        key = "".join(sorted(code))

        if key not in groups:
            groups[key] = []

        groups[key].append(code)

    return list(groups.values())


def demo_group_coupon_anagrams():
  
    print("\n===== DEMO 2.2: GROUP COUPON ANAGRAMS =====")

    codes = ["SAVE10", "AVES10", "FREESHIP", "SHIPFREE", "DISCOUNT", "COUPON"]

    groups = group_coupon_anagrams(codes)

    print("Danh sách mã coupon:", codes)
    print("\nCác nhóm anagram:")

    for group in groups:
        print("-", group)

    print(
        "\nỨng dụng: Có thể phát hiện các mã coupon khác tên "
        "nhưng có cấu trúc ký tự giống nhau."
    )


# ============================================================
# 2.3. Longest consecutive - chuỗi ngày giao liên tiếp
# ============================================================

def longest_consecutive_days(days):
    """
    Tìm độ dài chuỗi ngày liên tiếp dài nhất.

    Input:
        days = [1, 2, 3, 7, 8]

    Output:
        3 vì chuỗi liên tiếp dài nhất là 1, 2, 3
    """
    day_set = set(days)
    longest = 0

    for day in day_set:
        if day - 1 not in day_set:
            current_day = day
            current_length = 1

            while current_day + 1 in day_set:
                current_day += 1
                current_length += 1

            if current_length > longest:
                longest = current_length

    return longest


def demo_longest_consecutive_days():
    """
    Demo yêu cầu 2.3.
    """
    print("\n===== DEMO 2.3: LONGEST CONSECUTIVE DAYS =====")

    days = [10, 11, 12, 20, 21, 30, 31, 32, 33]

    result = longest_consecutive_days(days)

    print("Các ngày có đơn hàng:", days)
    print("Chuỗi ngày liên tiếp dài nhất:", result)
    print("Ứng dụng: Dùng để phát hiện chuỗi ngày cao điểm liên tiếp.")


# ============================================================
# 2.4. Subarray sum = k - kiểm tra doanh thu theo chuỗi ngày
# ============================================================

def count_revenue_windows(revenues, k):
    count = 0
    n = len(revenues)

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += revenues[j]

            if total <= k:
                count += 1

    return count


def count_revenue_windows(revenues, k):
    prefix_sum = 0
    freq = {0: 1}
    count = 0

    for x in revenues:
        prefix_sum += x

        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


# ============================================================
# 2.5. Rolling hash - tìm mã giảm giá trong log
# ============================================================

def rolling_hash_search(text, pattern):
   
    n = len(text)
    m = len(pattern)

    if m == 0:
        return []

    if m > n:
        return []

    base = 256
    mod = 101

    pattern_hash = 0
    window_hash = 0
    highest_power = 1

    for _ in range(m - 1):
        highest_power = (highest_power * base) % mod

    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    positions = []

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                positions.append(i)

        if i < n - m:
            left_char = ord(text[i])
            right_char = ord(text[i + m])

            window_hash = (
                (window_hash - left_char * highest_power) * base + right_char
            ) % mod

            if window_hash < 0:
                window_hash += mod

    return positions


def demo_rolling_coupon_search():
   
    print("\n===== DEMO 2.5: ROLLING HASH - TÌM COUPON TRONG LOG =====")

    log_text = "USER1_USED_SAVE10; USER2_USED_FREESHIP; USER3_USED_SAVE10"
    patterns = ["SAVE10", "FREESHIP", "DISCOUNT"]

    print("Log:", log_text)

    for pattern in patterns:
        positions = rolling_hash_search(log_text, pattern)

        if positions:
            print(f"Pattern '{pattern}' xuất hiện tại vị trí:", positions)
        else:
            print(f"Pattern '{pattern}' không xuất hiện trong log.")


# ============================================================
# Demo tổng hợp phần 2
# ============================================================

def demo_all_hashing_tools():
    """
    Chạy toàn bộ demo của Phần 2.
    """
    demo_order_hash_table()
    demo_group_coupon_anagrams()
    demo_longest_consecutive_days()
    count_revenue_windows([100, 200, 300, 100, 200], 300)
    demo_rolling_coupon_search()


if __name__ == "__main__":
    demo_all_hashing_tools()

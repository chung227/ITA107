# Hàm 1
def sum_to_n(n):
    """
    Base case:
    n = 0 -> 0
    n = 1 -> 1
    Recursive case:
    sum_to_n(n) = n + sum_to_n(n-1)

    Độ phức tạp: O(n)
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return n + sum_to_n(n - 1)
# Hàm 2: Tính n^k
def power(n, k):
    """
    Base case:
    k = 0 -> 1
    n = 0 -> 0

    Recursive case:
    n * power(n, k-1)

    Độ phức tạp: O(k)
    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    return n * power(n, k - 1)
# Hàm 3: Đảo chuỗi
def reverse_string(s):
    """
    Base case:
    len(s) <= 1

    Recursive case:
    reverse_string(s[1:]) + s[0]

    Độ phức tạp: O(n)
    """
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]
# Hàm 4: Kiểm tra palindrome

def is_palindrome(s):
    """
    Base case:
    len(s) <= 1 -> True

    Recursive case:
    kiểm tra phần giữa chuỗi

    Độ phức tạp: O(n)
    """
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


# Test
print(sum_to_n(5))
print(sum_to_n(10))

print(power(2, 5))
print(power(3, 4))
print(power(5, 0))

print(reverse_string("hello"))
print(reverse_string("python"))

print(is_palindrome("racecar"))
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("abba"))
print(is_palindrome("noon"))
print("***********************************************")
print("Bài 2: lab 2")
import time


# Phần A – Fibonacci đệ quy đơn giản
def fibonacci_naive(n):
    """
    Fibonacci đệ quy đơn giản - CHẬM
    F(n) = F(n-1) + F(n-2)
    F(0) = 0, F(1) = 1

    Độ phức tạp: O(2^n)
    """
    if n <= 1:
        return n

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# Test phần A
print("Fibonacci naive:")
print(fibonacci_naive(10))  # 55
print(fibonacci_naive(20))  # 6765

# Phần B – Fibonacci với memoization
def fibonacci_memo(n, memo=None):
    """
    Fibonacci với memoization - NHANH

    Độ phức tạp: O(n)
    """
    # Khởi tạo memo nếu chưa có
    if memo is None:
        memo = {}

    # Kiểm tra n đã có trong memo chưa
    if n in memo:
        return memo[n]

    # Base case
    if n <= 1:
        memo[n] = n
        return memo[n]

    # Recursive case
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


# Phần C – Fibonacci vòng lặp
def fibonacci_iterative(n):
    """
    Fibonacci dùng vòng lặp

    Độ phức tạp thời gian: O(n)
    Độ phức tạp không gian: O(1)
    """
    if n <= 1:
        return n

    prev = 0
    curr = 1

    for i in range(2, n + 1):
        temp = prev + curr
        prev = curr
        curr = temp

    return curr


# Test và so sánh thời gian
print("\n--- So sánh hiệu suất ---")

start = time.time()
result1 = fibonacci_naive(30)
time1 = time.time() - start
print(f"Naive F(30) = {result1}, thời gian: {time1:.4f}s")

start = time.time()
result2 = fibonacci_memo(100)
time2 = time.time() - start
print(f"Memo F(100) = {result2}, thời gian: {time2:.6f}s")


# Test Fibonacci vòng lặp
print("\nFibonacci iterative:")
print(fibonacci_iterative(10))   # 55
print(fibonacci_iterative(20))   # 6765
print(fibonacci_iterative(100))


# Bài 3
import time
import random


def merge_sort(arr):
    """
    Sắp xếp mảng bằng Merge Sort
    Độ phức tạp: O(n log n)
    """

    # Base case: mảng 0 hoặc 1 phần tử
    if len(arr) <= 1:
        return arr

    # Divide - chia đôi mảng
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conquer - đệ quy sắp xếp 2 nửa
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Combine - trộn 2 nửa đã sắp xếp
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Trộn 2 mảng đã sắp xếp thành 1 mảng sắp xếp
    """

    result = []
    i = j = 0

    # So sánh và chọn phần tử nhỏ hơn
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Thêm các phần tử còn lại
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Test
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)

print(f"Mảng sau khi sắp xếp: {sorted_arr}")
# Kết quả: [11, 12, 22, 25, 34, 64, 90]


# Phần nâng cao
arr_small = [random.randint(1, 1000) for _ in range(100)]
arr_large = [random.randint(1, 10000) for _ in range(5000)]

# Đo thời gian với mảng nhỏ
start = time.time()
sorted_small = merge_sort(arr_small.copy())
time_small = time.time() - start

print(f"Thời gian sắp xếp 100 phần tử: {time_small:.6f}s")

# Đo thời gian với mảng lớn
start = time.time()
sorted_large = merge_sort(arr_large.copy())
time_large = time.time() - start

print(f"Thời gian sắp xếp 5000 phần tử: {time_large:.6f}s")

# So sánh với Python built-in sort
start = time.time()
sorted_builtin = sorted(arr_large)
time_builtin = time.time() - start

print(f"Thời gian Python sorted(): {time_builtin:.6f}s")
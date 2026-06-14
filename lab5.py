from collections import deque

# ==========================================
# HÀM 1 - XÂY DỰNG ĐỒ THỊ
# ==========================================

def build_graph(danh_sach_canh, directed=False):
    """
    Xây dựng đồ thị từ danh sách cạnh
    """

    do_thi = {}

    for dinh_u, dinh_v in danh_sach_canh:

        if dinh_u not in do_thi:
            do_thi[dinh_u] = []

        if dinh_v not in do_thi:
            do_thi[dinh_v] = []

        do_thi[dinh_u].append(dinh_v)

        if not directed:
            do_thi[dinh_v].append(dinh_u)

    return do_thi


print("===== TEST BUILD GRAPH =====")

danh_sach_canh_1 = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E')
]

do_thi_1 = build_graph(danh_sach_canh_1)

for dinh, dinh_ke in do_thi_1.items():
    print(dinh, ":", dinh_ke)


# ==========================================
# HÀM 2 - BFS
# ==========================================

def bfs(do_thi, dinh_bat_dau):
    """
    Duyệt đồ thị theo chiều rộng
    """

    da_tham = set()

    hang_doi = deque([dinh_bat_dau])

    da_tham.add(dinh_bat_dau)

    ket_qua = []

    while hang_doi:

        dinh_hien_tai = hang_doi.popleft()

        ket_qua.append(dinh_hien_tai)

        for dinh_ke in do_thi[dinh_hien_tai]:

            if dinh_ke not in da_tham:

                da_tham.add(dinh_ke)

                hang_doi.append(dinh_ke)

    return ket_qua


print("\n===== TEST BFS =====")

do_thi_bfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS từ A:", bfs(do_thi_bfs, 'A'))
print("BFS từ D:", bfs(do_thi_bfs, 'D'))


# ==========================================
# HÀM 3 - DFS ĐỆ QUY
# ==========================================

def dfs_recursive(do_thi,
                  dinh_bat_dau,
                  da_tham=None,
                  ket_qua=None):
    """
    Duyệt đồ thị theo chiều sâu bằng đệ quy
    """

    if da_tham is None:
        da_tham = set()

    if ket_qua is None:
        ket_qua = []

    da_tham.add(dinh_bat_dau)

    ket_qua.append(dinh_bat_dau)

    for dinh_ke in do_thi[dinh_bat_dau]:

        if dinh_ke not in da_tham:

            dfs_recursive(
                do_thi,
                dinh_ke,
                da_tham,
                ket_qua
            )

    return ket_qua


print("\n===== TEST DFS =====")

do_thi_dfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS từ A:", dfs_recursive(do_thi_dfs, 'A'))
print("DFS từ C:", dfs_recursive(do_thi_dfs, 'C'))


# ==========================================
# HÀM 4 - CONNECTED COMPONENTS
# ==========================================

def count_connected_components(do_thi):
    """
    Đếm số thành phần liên thông
    """

    da_tham = set()

    cac_thanh_phan = []

    def bfs_component(dinh_bat_dau):

        hang_doi = deque([dinh_bat_dau])

        da_tham.add(dinh_bat_dau)

        thanh_phan = []

        while hang_doi:

            dinh_hien_tai = hang_doi.popleft()

            thanh_phan.append(dinh_hien_tai)

            for dinh_ke in do_thi[dinh_hien_tai]:

                if dinh_ke not in da_tham:

                    da_tham.add(dinh_ke)

                    hang_doi.append(dinh_ke)

        return thanh_phan

    for dinh in do_thi:

        if dinh not in da_tham:

            thanh_phan = bfs_component(dinh)

            cac_thanh_phan.append(thanh_phan)

    return len(cac_thanh_phan), cac_thanh_phan


print("\n===== TEST CONNECTED COMPONENTS =====")

do_thi_cc = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D', 'E'],
    'D': ['C'],
    'E': ['C'],
    'F': []
}

so_luong, danh_sach_thanh_phan = count_connected_components(do_thi_cc)

print("Số thành phần liên thông:", so_luong)

for i, thanh_phan in enumerate(danh_sach_thanh_phan, 1):
    print(f"Thành phần {i}: {thanh_phan}")
  #Bài 2 
# ==========================================
# BÀI 2 - PHÁT HIỆN CHU TRÌNH
# ==========================================


# ==========================================
# PHẦN A - ĐỒ THỊ VÔ HƯỚNG
# ==========================================

def has_cycle_undirected(do_thi):
    """
    Kiểm tra chu trình trong đồ thị vô hướng
    """

    da_tham = set()

    def dfs(dinh_hien_tai, dinh_cha):

        da_tham.add(dinh_hien_tai)

        for dinh_ke in do_thi[dinh_hien_tai]:

            if dinh_ke not in da_tham:

                if dfs(dinh_ke, dinh_hien_tai):
                    return True

            elif dinh_ke != dinh_cha:
                return True

        return False

    for dinh in do_thi:

        if dinh not in da_tham:

            if dfs(dinh, None):
                return True

    return False


print("===== KIỂM TRA CHU TRÌNH VÔ HƯỚNG =====")

do_thi_1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print(has_cycle_undirected(do_thi_1))

do_thi_2 = {
    0: [1],
    1: [0, 2],
    2: [1]
}

print(has_cycle_undirected(do_thi_2))


# ==========================================
# PHẦN B - ĐỒ THỊ CÓ HƯỚNG
# ==========================================

def has_cycle_directed(do_thi):
    """
    Kiểm tra chu trình trong đồ thị có hướng
    """

    CHUA_THAM = 0
    DANG_XU_LY = 1
    DA_XU_LY = 2

    mau = {dinh: CHUA_THAM for dinh in do_thi}

    def dfs(dinh_hien_tai):

        mau[dinh_hien_tai] = DANG_XU_LY

        for dinh_ke in do_thi[dinh_hien_tai]:

            if mau[dinh_ke] == DANG_XU_LY:
                return True

            if mau[dinh_ke] == CHUA_THAM:

                if dfs(dinh_ke):
                    return True

        mau[dinh_hien_tai] = DA_XU_LY

        return False

    for dinh in do_thi:

        if mau[dinh] == CHUA_THAM:

            if dfs(dinh):
                return True

    return False


print("\n===== KIỂM TRA CHU TRÌNH CÓ HƯỚNG =====")

do_thi_3 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

print(has_cycle_directed(do_thi_3))

do_thi_4 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print(has_cycle_directed(do_thi_4))


# ==========================================
# PHẦN C - SO SÁNH
# ==========================================

def compare_cycle_detection():

    print("\n===== SO SÁNH =====")

    do_thi_vo_huong = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    do_thi_co_huong = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }

    print("Đồ thị vô hướng:",
          has_cycle_undirected(do_thi_vo_huong))

    print("Đồ thị có hướng:",
          has_cycle_directed(do_thi_co_huong))

    print("\nĐồ thị vô hướng dùng:")
    print("- DFS + Parent")

    print("\nĐồ thị có hướng dùng:")
    print("- DFS + WHITE/GRAY/BLACK")


compare_cycle_detection()
#Bài 3
from collections import deque

# ==========================================
# HÀM KIỂM TRA CHU TRÌNH
# ==========================================

def has_cycle_directed(do_thi):

    CHUA_THAM = 0
    DANG_XU_LY = 1
    DA_XU_LY = 2

    mau = {dinh: CHUA_THAM for dinh in do_thi}

    def dfs(dinh_hien_tai):

        mau[dinh_hien_tai] = DANG_XU_LY

        for dinh_ke in do_thi[dinh_hien_tai]:

            if mau[dinh_ke] == DANG_XU_LY:
                return True

            if mau[dinh_ke] == CHUA_THAM:

                if dfs(dinh_ke):
                    return True

        mau[dinh_hien_tai] = DA_XU_LY

        return False

    for dinh in do_thi:

        if mau[dinh] == CHUA_THAM:

            if dfs(dinh):
                return True

    return False


# ==========================================
# TOPOLOGICAL SORT BẰNG DFS
# ==========================================

def topological_sort_dfs(do_thi):

    if has_cycle_directed(do_thi):
        return None

    da_tham = set()

    ngan_xep = []

    def dfs(dinh_hien_tai):

        da_tham.add(dinh_hien_tai)

        for dinh_ke in do_thi[dinh_hien_tai]:

            if dinh_ke not in da_tham:
                dfs(dinh_ke)

        ngan_xep.append(dinh_hien_tai)

    for dinh in do_thi:

        if dinh not in da_tham:
            dfs(dinh)

    return ngan_xep[::-1]


# ==========================================
# TOPOLOGICAL SORT KAHN
# ==========================================

def topological_sort_kahn(do_thi):

    bac_vao = {dinh: 0 for dinh in do_thi}

    for dinh in do_thi:

        for dinh_ke in do_thi[dinh]:
            bac_vao[dinh_ke] += 1

    hang_doi = deque()

    for dinh in do_thi:

        if bac_vao[dinh] == 0:
            hang_doi.append(dinh)

    ket_qua = []

    while hang_doi:

        dinh_hien_tai = hang_doi.popleft()

        ket_qua.append(dinh_hien_tai)

        for dinh_ke in do_thi[dinh_hien_tai]:

            bac_vao[dinh_ke] -= 1

            if bac_vao[dinh_ke] == 0:
                hang_doi.append(dinh_ke)

    if len(ket_qua) != len(do_thi):
        return None

    return ket_qua


# ==========================================
# COURSE SCHEDULE
# ==========================================

def can_finish(so_mon_hoc, dieu_kien_truoc):

    do_thi = {i: [] for i in range(so_mon_hoc)}

    for mon_hoc, mon_hoc_truoc in dieu_kien_truoc:
        do_thi[mon_hoc_truoc].append(mon_hoc)

    return not has_cycle_directed(do_thi)


def find_order(so_mon_hoc, dieu_kien_truoc):

    do_thi = {i: [] for i in range(so_mon_hoc)}

    for mon_hoc, mon_hoc_truoc in dieu_kien_truoc:
        do_thi[mon_hoc_truoc].append(mon_hoc)

    ket_qua = topological_sort_kahn(do_thi)

    if ket_qua is None:
        return []

    return ket_qua


# ==========================================
# TEST TOPOLOGICAL SORT
# ==========================================

print("===== TOPOLOGICAL SORT DFS =====")

do_thi_topo = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

print(topological_sort_dfs(do_thi_topo))

print("\n===== TOPOLOGICAL SORT KAHN =====")
print(topological_sort_kahn(do_thi_topo))


# ==========================================
# TEST COURSE SCHEDULE
# ==========================================

print("\n===== COURSE SCHEDULE =====")

so_mon_hoc_1 = 4

dieu_kien_1 = [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2]
]

print(can_finish(so_mon_hoc_1, dieu_kien_1))
print(find_order(so_mon_hoc_1, dieu_kien_1))


so_mon_hoc_2 = 2

dieu_kien_2 = [
    [1, 0],
    [0, 1]
]

print(can_finish(so_mon_hoc_2, dieu_kien_2))
print(find_order(so_mon_hoc_2, dieu_kien_2))
import heapq

def dijkstra(graph, source):
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    parent = {v: None for v in graph}
    pq = [(0, source)]
    visited = set()

    while pq:
        current_dist, u = heapq.heappop(pq)
        if u in visited: 
            continue
        visited.add(u)

        for v, w in graph[u]:
            new_dist = distances[u] + w
            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    return distances, parent

def reconstruct_path(parent, source, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path if path and path[0] == source else None

if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('D', 1)],
        'B': [('A', 4), ('C', 2), ('E', 3)],
        'C': [('B', 2), ('F', 5)],
        'D': [('A', 1), ('E', 2)],
        'E': [('D', 2), ('B', 3), ('F', 1)],
        'F': [('E', 1), ('C', 5)]
    }
    
    dist, part = dijkstra(graph, 'A')
    print("--- KẾT QUẢ BÀI 1 ---")
    print("Khoảng cách ngắn nhất từ A:", dist)
    print("Đường đi chi tiết từ A đến F:", reconstruct_path(part, 'A', 'F'))

# Bài 2
def make_set(vertices):
    return {v: v for v in vertices}

def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

# DSU PHIÊN BẢN 2: OPTIMIZED
def make_set_optimized(vertices):
    parent = {v: v for v in vertices}
    size = {v: 1 for v in vertices}
    return parent, size

def find_optimized(parent, v):
    if parent[v] != v:
        parent[v] = find_optimized(parent, parent[v])
    return parent[v]

def union_optimized(parent, size, a, b):
    root_a = find_optimized(parent, a)
    root_b = find_optimized(parent, b)
    if root_a != root_b:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]

#bài 3
def make_set(vertices):
    """Khởi tạo ban đầu: mỗi đỉnh tự làm trưởng nhóm của chính mình"""
    return {v: v for v in vertices}

def find(parent, v):
    """Đi tìm ông trùm (root) đại diện cho đỉnh v"""
    while parent[v] != v:
        v = parent[v]
    return v

def union(parent, a, b):
    """Gộp nhóm của a và nhóm của b lại làm một"""
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a  # Cho ông trùm b phục tùng ông trùm a


# =====================================================================
# PHẦN 2: THUẬT TOÁN KRUSKAL (Nội dung chính của Bài 3)
# =====================================================================

def kruskal_mst_basic(vertices, edges):
    # Bước 1: Sắp xếp tất cả các cạnh theo thứ tự trọng số từ nhỏ đến lớn
    edges_sorted = sorted(edges, key=lambda e: e[0])
    
    # Bước 2: Khởi tạo tập hợp DSU cho các đỉnh
    parent = make_set(vertices)
    mst = []                     # Danh sách lưu các cạnh được chọn vào cây khung
    total_weight = 0             # Tổng trọng số của cây khung

    print("Cạnh sau khi sort (trọng số, đỉnh 1, đỉnh 2):")
    for e in edges_sorted:
        print("  ", e)
        
    print("\n--- QUÁ TRÌNH DUYỆT TỪNG CẠNH ĐỂ TÌM MST ---")
    for w, u, v in edges_sorted:
        root_u = find(parent, u)
        root_v = find(parent, v)
        
        print(f"Xét cạnh {u}-{v} (w={w}): root_u = {root_u}, root_v = {root_v}", end="")
        
        # Kiểm tra xem u và v đã thuộc cùng một nhóm hay chưa
        if root_u != root_v:
            print(" → Khác nhóm: CHỌN cạnh này")
            mst.append((u, v, w))    # Thêm cạnh vào cây khung
            total_weight += w         # Cộng trọng số
            union(parent, u, v)       # Gộp 2 nhóm lại
        else:
            print(" → Cùng nhóm: BỎ (Tránh tạo chu trình)")
            
        # Nếu đã chọn đủ (Số đỉnh - 1) cạnh thì dừng giải thuật sớm
        if len(mst) == len(vertices) - 1:
            print("\nĐã chọn đủ số cạnh tối đa (|V| - 1). Kết thúc sớm!")
            break

    return mst, total_weight


# =====================================================================
# PHẦN 3: KHU VỰC CHẠY THỬ NGHIỆM (MAIN)
# =====================================================================
if __name__ == "__main__":
    # Dữ liệu đầu vào mẫu chuẩn hóa từ đề bài
    vertices = ['A', 'B', 'C', 'D', 'E']
    
    # Định dạng các cạnh: (trọng số, đỉnh 1, đỉnh 2)
    edges = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (3, 'B', 'C'),
        (2, 'B', 'D'),
        (5, 'C', 'E'),
        (2, 'D', 'E') 
    ]

    # Gọi hàm xử lý thuật toán
    cay_khung, tong_trong_so = kruskal_mst_basic(vertices, edges)
    
    # In kết quả cuối cùng ra màn hình
    print("\n" + "="*40)
    print("KẾT QUẢ CÂY KHUNG NHỎ NHẤT (MST):")
    for u, v, w in cay_khung:
        print(f"  {u} - {v} (trọng số = {w})")
    print("Tổng trọng số nhỏ nhất tìm được:", tong_trong_so)


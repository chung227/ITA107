import heapq
# ============================================================
# 1.1. Shortest Path - Dijkstra
# ============================================================

def build_graph(edges):
    """
    Tạo đồ thị dạng adjacency list từ danh sách cạnh.

    Input:
        edges = [
            ("WH1", "HCM", 4),
            ("WH1", "DN", 7),
            ...
        ]

    Vì đề bài yêu cầu đồ thị vô hướng nên mỗi cạnh u-v sẽ được thêm 2 chiều:
        u -> v
        v -> u

    Output:
        graph = {
            "WH1": [("HCM", 4), ("DN", 7)],
            "HCM": [("WH1", 4), ...],
            ...
        }
    """
    graph = {}

    for u, v, cost in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append((v, cost))
        graph[v].append((u, cost))

    return graph


def dijkstra(graph, source):
    if source not in graph:
        raise ValueError(f"Source '{source}' không tồn tại trong graph.")

    # Ban đầu, mọi khoảng cách là vô cực
    dist = {vertex: float("inf") for vertex in graph}
    parent = {vertex: None for vertex in graph}

    # Đi từ source đến chính nó có chi phí 0
    dist[source] = 0

    # Heap lưu các phần tử dạng (chi_phi_hien_tai, dinh)
    heap = [(0, source)]

    while heap:
        current_cost, u = heapq.heappop(heap)

        # Nếu đây là bản ghi cũ, bỏ qua
        if current_cost > dist[u]:
            continue

        # Thử đi từ u sang các đỉnh kề v
        for v, edge_cost in graph[u]:
            new_cost = current_cost + edge_cost

            # Nếu tìm được đường rẻ hơn để đến v thì cập nhật
            if new_cost < dist[v]:
                dist[v] = new_cost
                parent[v] = u
                heapq.heappush(heap, (new_cost, v))

    return dist, parent


def shortest_route(graph, source, target):
    if target not in graph:
        raise ValueError(f"Target '{target}' không tồn tại trong graph.")

    dist, parent = dijkstra(graph, source)

    # Nếu target vẫn là vô cực nghĩa là không có đường đi
    if dist[target] == float("inf"):
        return float("inf"), []

    # Truy vết đường đi từ target ngược về source
    route = []
    current = target

    while current is not None:
        route.append(current)
        current = parent[current]

    # Vì truy vết ngược nên cần đảo lại
    route.reverse()

    return dist[target], route


def get_sample_polyship_edges():
    return [
        ("WH1", "HCM", 4),
        ("WH1", "DN", 7),
        ("WH2", "HN", 3),
        ("WH2", "HP", 5),
        ("WH3", "DN", 2),
        ("WH3", "CT", 6),
        ("HCM", "DN", 3),
        ("HCM", "CT", 4),
        ("DN", "HN", 6),
        ("DN", "HP", 5),
        ("HN", "HP", 2),
        ("CT", "DN", 5),
    ]


def demo_routing_shortest_path(source="WH1", target="HN"):
    print("\n===== DEMO 1.1: DIJKSTRA - TUYẾN GIAO HÀNG RẺ NHẤT =====")

    edges = get_sample_polyship_edges()
    graph = build_graph(edges)

    print("Các điểm trong mạng:", ", ".join(graph.keys()))
    print(f"Tìm tuyến rẻ nhất từ {source} đến {target}")

    total_cost, route = shortest_route(graph, source, target)

    if not route:
        print(f"Không tìm thấy đường đi từ {source} đến {target}.")
    else:
        print("Route:", " -> ".join(route))
        print("Tổng chi phí:", total_cost)

    return total_cost, route


# ============================================================
# 1.2. MST - Kruskal + DSU
# ============================================================

class DSU:

    def __init__(self):
        self.parent = {}
        self.size = {}

    def make_set(self, x):
        """Tạo một tập riêng cho x."""
        self.parent[x] = x
        self.size[x] = 1

    def find(self, x):
   
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
     
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        # Union by size: nhóm nhỏ nhập vào nhóm lớn
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return True


def kruskal_mst(vertices, edges):
   
    dsu = DSU()

    # Mỗi đỉnh ban đầu là 1 tập riêng
    for vertex in vertices:
        dsu.make_set(vertex)

    # Sắp xếp cạnh theo chi phí tăng dần
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    mst_edges = []
    total_cost = 0

    for u, v, cost in sorted_edges:
        # Nếu nối u-v không tạo chu trình thì chọn cạnh này
        if dsu.union(u, v):
            mst_edges.append((u, v, cost))
            total_cost += cost

        # MST của n đỉnh chỉ cần n - 1 cạnh
        if len(mst_edges) == len(vertices) - 1:
            break

    # Nếu không đủ n - 1 cạnh nghĩa là graph không liên thông
    if len(mst_edges) != len(vertices) - 1:
        raise ValueError("Không thể tạo MST vì mạng kho không liên thông.")

    return mst_edges, total_cost


def demo_mst_network():

    print("\n===== DEMO 1.2: KRUSKAL - MẠNG KHO TỐI THIỂU =====")

    edges = get_sample_polyship_edges()

    # Lấy danh sách đỉnh từ danh sách cạnh
    vertices = sorted({u for u, v, cost in edges} | {v for u, v, cost in edges})

    mst_edges, total_cost = kruskal_mst(vertices, edges)

    print("Danh sách kho/điểm:", ", ".join(vertices))
    print("\nCác đường truyền được chọn trong MST:")

    for u, v, cost in mst_edges:
        print(f"- {u} -- {v}, chi phí = {cost}")

    print("\nTổng chi phí lắp đặt:", total_cost)
    print(
        "Nhận xét: Đây là bộ khung tối thiểu, "
        "các tuyến giao hàng chi tiết dùng Dijkstra trên mạng này."
    )

    return mst_edges, total_cost
# ============================================================
# Chạy thử riêng file routing.py
# ============================================================
if __name__ == "__main__":
    demo_routing_shortest_path()
    demo_mst_network()

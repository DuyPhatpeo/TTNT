def readmtk(filename):
    with open(filename, "r") as f:
        n = int(f.readline().strip())
        print(n)
        adj = []
        for i in range(n):
            line = list(map(int, f.readline().split()))
            print(line)
            adj.append(line)
    return n, adj

def readh(filename):
    with open(filename, "r") as f:
        n = int(f.readline().strip())
        h = list(map(int, f.readline().split()))
        print(h)
    return h

def BestFS(n, adj, h, start, stop):
    OPEN = [start]
    CLOSE = []
    PARENT = [-1] * n
    while len(OPEN) > 0:
        cur = OPEN.pop(0)
        print(f"cur = {cur}")
        CLOSE.append(cur)
        print(f"CLOSE = {CLOSE}")
        if cur == stop:
            print(f"Tìm thấy đường đi từ {start} -> {stop}")
            path = []
            i = stop
            while i != -1:
                path.append(i)
                i = PARENT[i]
            path.reverse()
            print("Đường đi:", " -> ".join(map(str, path)))
            return
        # tìm các đỉnh kề với cur
        Tn = []
        for i in range(n):
            if adj[cur][i] == 1 and i not in OPEN and i not in CLOSE:
                Tn.append(i)
                PARENT[i] = cur
        print(f"Tn = {Tn}")
        
        
        # thêm Tn vào OPEN
        OPEN += Tn
        # sắp xếp toàn bộ OPEN theo heuristic tăng dần
        OPEN.sort(key=lambda x: h[x])

        
        print(f"OPEN = {OPEN}")
        print(f"PARENT = {PARENT}")
    # hết vòng while
    print(f"Khong tìm thấy đường đi từ {start} đến {stop}")


if __name__ == "__main__":
    n, adj = readmtk("leodoi.mtk")
    h = readh("leodoi.h")
    BestFS(n, adj, h, 0, 8)

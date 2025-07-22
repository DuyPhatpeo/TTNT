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
        h = list(map(int, f.readline().split()))
        print(h)
    return h
    
def AStar(sodinh, adj, h, start, stop):
    OPEN = [start]
    CLOSE = []

    g = [float('inf')] * sodinh
    f = [float('inf')] * sodinh
    CHA = [-1] * sodinh

    g[start] = 0
    f[start] = h[start]

    while OPEN:
        n = OPEN.pop(0)  # lấy đỉnh đầu tiên trong OPEN
        print(f"Xét đỉnh: {chr(n+65)}")

        if n == stop:
            print(f"Tìm thấy đường đi từ {chr(start+65)} đến {chr(stop+65)}:")
            i = stop
            while i != -1:
                print(chr(i + 65), end=" <= ")
                i = CHA[i]
            print()
            return True

        CLOSE.append(n)

        for i in range(sodinh):
            if adj[n][i] > 0:  # có cạnh
                g_new = g[n] + adj[n][i]
                f_new = g_new + h[i]

                if i not in OPEN and i not in CLOSE:
                    g[i] = g_new
                    f[i] = f_new
                    CHA[i] = n
                    OPEN.append(i)

                elif i in OPEN:
                    if f_new < f[i]:
                        g[i] = g_new
                        f[i] = f_new
                        CHA[i] = n

                elif i in CLOSE:
                    if f_new < f[i]:
                        g[i] = g_new
                        f[i] = f_new
                        CHA[i] = n
                        CLOSE.remove(i)
                        OPEN.append(i)

        # Sắp xếp OPEN theo f tăng dần
        OPEN = sorted(OPEN, key=lambda x: f[x])
        print(f"OPEN: {[chr(i+65) for i in OPEN]}")
        print(f"CLOSE: {[chr(i+65) for i in CLOSE]}")
        print(f"g = {g}")
        print(f"f = {f}")
        print(f"CHA = {[chr(c+65) if c != -1 else '-' for c in CHA]}")

    print(f"Không tìm thấy đường đi từ {chr(start+65)} đến {chr(stop+65)}")


if __name__ == "__main__":
    n, adj = readmtk("astar.mtk")
    h = readh("astar.h")
    AStar(n, adj, h, 0, 10)

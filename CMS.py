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
    
def CMS(sodinh, adj, h, start, stop):
  OPEN = [start]
  CLOSE = []
  g = [float('inf')] * sodinh
  g[start] = 0
  print(f"g = {g}")
  CHA = [-1] * sodinh
  print(f"CHA = {CHA}")
  while len(OPEN)>0:
    n = OPEN.pop(0)
    print(f"n = {n}")
    if n == stop:
      print(f"tim thay duong di tu {start} - {stop}")
      i = stop
      while i!= -1:
        print(chr(i+65),end = " <= ")
        i = CHA[i]
      return True
    
    # nguoc lai
    CLOSE.append(n)
    print(f"CLOSE = {CLOSE}")
    # tim cac dinh ke
    Tn = []
    for i in range(sodinh):
      if adj[n][i] == 1:
        if i not in  OPEN and i not in CLOSE:
          g[i] = g[n] + h[i]
          Tn.append(i)
          CHA[i] = n
        elif i in OPEN:
          gnew = g[n] + h[i]
          print(f"gnew[{i}] = {gnew}")
          if gnew < g[i]:
            g[i]=gnew
            CHA[i] = n
    print(f"Tn = {Tn}")
    OPEN = OPEN+Tn
    print(f"OPEN =  {OPEN}")
    # Sap xep OPEN theo g
    OPEN = sorted(OPEN, key = lambda x: g[x])
    print(f"OPEN sort = {OPEN}")
    print(f"g = {g}")
    print(f"CHA = {CHA}")
    
  # Het while
  print(f"Khong tim thay duong di {start} - {stop}")
if __name__ == "__main__":
    n, adj = readmtk("cms.mtk")
    h = readh("cms.h")
    CMS(n, adj, h, 0,7)

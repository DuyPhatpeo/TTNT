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
    
def BranchAndBound(sodinh, adj, h, start, stop):
  OPEN = [start]
  fmin = float('inf')
  flag = False
  g = [float('inf')] * sodinh
  f = [float('inf')] * sodinh
  g[start]=0
  f[start]=h[start]
  print(f"g={g}")
  print(f"f={f}")
  CLOSE = []
  CHA = [-1] * sodinh
  
  while len(OPEN) > 0:
    n=OPEN.pop(0)
    print(f"n = {n}")
    CLOSE.append(n)
    print(f"CLOSE = {CLOSE}")
    if n == stop:
      flag = True
      if f[n]< fmin:
        print(f"Cap nhat fmin = {f[n]}")
        fmin=f[n]
      else:
        print(f"f[{n}] = {f[n]} > fmin = {fmin}")
    else: # n khong phai stop, di tim cac dinh ke
      if f[n] >= fmin:
        print(f"f[{n}] > fmin ({fmin}): xen tia nhanh con")
      else: # f[n] < fmin, tim cac dinh ke
        Tn = [] # reset Tn
        for i in range(sodinh):
          if adj[n][i] > 0:
            # TH1: i NOT thuoc OPEN, NOT thuoc CLOSE
            if i not in OPEN and i not in CLOSE:
              print(f"{i} NOT in OPEN + NOT in CLOSE")
              g[i] = g[n] + adj[n][i]
              f[i] = g[i] + h[i]
              CHA[i]=n         
              Tn.append(i)

            # TH2: i NOT thuoc OPEN, thuoc CLOSE
            if i not in OPEN and i in CLOSE:
              print(f"{i} NOT in OPEN + in CLOSE")
              gnew=g[n]+adj[n][i]
              fnew = gnew + h[i]
              print(f"fnew = {fnew}: update g, f, CHA, chen vao Tn")
              if fnew < f[i]:
                print(f"fnew < f[{i}]")
                f[i] = fnew
                g[i] = gnew
                # Tn.append(i)
                CHA[i] = n

            # TH3: i thuoc OPEN, NOT thuoc CLOSE
            if i in OPEN and i not in CLOSE:
              print(f"{i} in OPEN + NOT in CLOSE")
              gnew=g[n]+adj[n][i]
              fnew = gnew + h[i]
              print(f"fnew = {fnew}")
              if fnew < f[i]:
                print(f"fnew < f[{i}]: update g, f, CHA")
                f[i] = fnew
                g[i] = gnew
                # Tn.append(i)
                CHA[i] = n

            # TH4: i thuoc OPEN, thuoc CLOSE
            if i in OPEN and i in CLOSE:
              print(f"{i} in OPEN + in CLOSE")
              print(f"{i} in OPEN + NOT in CLOSE")
              gnew=g[n]+adj[n][i]
              fnew = gnew + h[i]
              print(f"fnew = {fnew}")
              if fnew < f[i]:
                print(f"fnew < f[{i}]: update g, f, CHA")
                f[i] = fnew
                g[i] = gnew
                # Tn.append(i)
                CHA[i] = n
        # het for : Tn
        print(f"Tn = {Tn}")
        Tn = sorted(Tn, key = lambda x: f[x])
        OPEN = Tn + OPEN
        print(f"OPEN = {OPEN}")
        print(f"g = {g}")
        print(f"f = {f}")

  # OPEN = 0
  if flag:
    print(f"Tim thay duong di tu {start} - {stop}")
    i = stop
    while i!= -1:
      print(i,end = " <= ")
      i =CHA[i]
  else:
    print(f"Khong tim thay duong di tu {start} - {stop}")



if __name__ == "__main__":
    n, adj = readmtk("nhanhcan.mtk")
    h = readh("nhanhcan.h")
    BranchAndBound(n, adj, h, 0, 1)

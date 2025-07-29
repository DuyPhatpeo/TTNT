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

def tinhBac(sodinh, adj):
  bac = [0]*sodinh
  for i in range(sodinh):
    for j in range(sodinh):
      if adj[i][j] == 1:
        bac[i]+=1
  print(f"bac cua do thi: {bac}")
  return bac
  
def toMau(sodinh, adj, bac):
  mau = 0
  dinh = [] # danh sach dinh can to mau
  color = [-1]*sodinh
  for i in range (sodinh):
    dinh.append(i)
  print(f"danh sach dinh: {dinh}")
  #  sap xep danh sach dinh giam dan theo bac
  dinh = sorted(dinh, key=lambda x: bac[x], reverse = True)
  print(f"danh sach dinh giam dan theo bac: {dinh}")
  while len(dinh)>0:
    n = dinh.pop(0)
    print(f"n = {n}")
    color[n] = mau
    #  tim cac dinh ko ke n
    Tn = [] # tap cac dinh can to
    for i in range(sodinh):
      if adj[n][i] == 0 and color[i] == -1:
        Tn.append(i)
    # to mau cac dinh tiem nang
    print(f"Tn = {Tn}")
    #  loai bo ac dinh ke nhau torng Tn
    for i in Tn:
      for j in Tn:
        if i!=j and adj[i][j] == 1:
          Tn.remove(j)
    print(f"Tn sau khi loai no cac dinh ke nhau: {Tn}")
    
    for i in Tn:
      if i in dinh:
        dinh.remove(i)
        color[i] = mau
    print(f"color={color}")
    print(f"dinh con lai chua to: {dinh}")
    mau+=1
    
  

if __name__ == "__main__":
    n, adj = readmtk("tomau.mtk")
    bac = tinhBac(n,adj)
    toMau(n,adj,bac)
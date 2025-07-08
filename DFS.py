'''
giai thuaj BFS, vi du 3
@phattd
8/7/2025
'''
def readfile(filename):
    with open(filename,'r') as f:
        n = int(f.readline().strip())
        print(n)
        
        adj=[]
        for i in range(n): # i=0; i<n; i++
            line = list(map(int,f.readline().split()))
            print(line)
            adj.append(line)
            
    return n, adj

def DFS(n,adj, start, stop):
    OPEN = [start]
    CLOSE = []
    parent= [-1]*n
    print(parent)
    
    while len(OPEN)>0:
        # lay dinh tu dau OPEN
        curr = OPEN.pop(0) # 0:dau, mac dinh la cuoi
        print(f"curr: {curr}")
        
        # dua dinh curr vao CLOSE
        CLOSE.append(curr) # chen cuoi
        print(f"CLOSE: {CLOSE}")
        # kiem tra co phai la dinh stop
        if curr == stop:
            print(f"Tim thay duong di tu {start} den {stop}")
            print(f"parent: {parent}")
            # in ra duong di
            i = stop
            while i != -1:
              print(f"{i}", end = " <= ")
              i = parent[i]
            return True
            
        # neu curr chua la dinh stop, tim cac  dinh ke cua curr
        Tn=[] # reset Tn
        for m in range(n): # duyet het cac dinh
            if adj[curr][m]==1 and m not in (OPEN) and m not in (CLOSE):
                Tn.append(m)
                parent[m] = curr # gan dinh m co cha la curr
        print(f"Tn: {Tn}")
        
        # chen Tn vao sau OPEN
        OPEN = Tn + OPEN
        print(f"OPEN= {OPEN}")
    # het while
    print(f"Khong tim thay duong di tu {start} den {stop}")

if __name__=="__main__":
    n, adj = readfile("input.inp")
    DFS(n,adj, 0, 7)

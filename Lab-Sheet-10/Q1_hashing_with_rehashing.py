class OpenHashing:
    def __init__(self, size=5): self.table=[[] for _ in range(size)]
    def insert(self, key, value):
        bucket=self.table[key % len(self.table)]
        for pair in bucket:
            if pair[0]==key: pair[1]=value; return
        bucket.append([key,value])
    def search(self,key):
        for k,v in self.table[key % len(self.table)]:
            if k==key:return v
        return None
class ClosedHashing:
    def __init__(self,size=5): self.table=[None]*size; self.count=0
    def _place(self,key,value):
        i=key%len(self.table)
        while self.table[i] is not None and self.table[i][0]!=key: i=(i+1)%len(self.table)
        if self.table[i] is None:self.count+=1
        self.table[i]=(key,value)
    def rehash(self):
        old=[x for x in self.table if x is not None]; self.table=[None]*(len(self.table)*2); self.count=0
        for key,value in old:self._place(key,value)
    def insert(self,key,value):
        existing=self.search(key)
        if existing is None and (self.count+1)/len(self.table)>0.7:self.rehash()
        self._place(key,value)
    def search(self,key):
        i=key%len(self.table); start=i
        while self.table[i] is not None:
            if self.table[i][0]==key:return self.table[i][1]
            i=(i+1)%len(self.table)
            if i==start:break
        return None
if __name__ == "__main__":
    op=OpenHashing()
    for k,v in [(1,"A"),(6,"B"),(11,"C"),(2,"D")]:op.insert(k,v)
    print("Open hashing table:",op.table); print("Search 6:",op.search(6))
    ch=ClosedHashing()
    for k,v in [(1,"A"),(6,"B"),(11,"C"),(2,"D"),(7,"E")]:ch.insert(k,v)
    print("Closed hashing table:",ch.table); print("Search 11:",ch.search(11))

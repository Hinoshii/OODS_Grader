class Node:
    def __init__(self, data=None, next: 'Node' = None):
        self.data = data
        self.next = next
        self.ref_count = 0 # มี node กี่ตัวชี้มาที่ตัวเอง

    def __str__(self) -> str:
        out = ''
        while self.next is not None:
            out += str(self.data) + '->'
            self = self.next
        return out + str(self.data)


# 5 1-2,3-4,2-3
n, hooks = input('Enter input: ').split()
# สร้าง node มา n+1 ตัว ใช้เลข index เข้าถึง node โดยตรง
trains = [Node(i) for i in range(int(n) + 1)]
trains[0].ref_count = 1 # ไม่ใช้ node 0
for c in hooks.split(','):
    h, t = map(int, c.split('-'))
    trains[h].next = trains[t]
    trains[t].ref_count += 1
# วนหา node ที่ไม่ถูกชี้
heads = [node for node in trains if node.ref_count == 0]
for i, node in enumerate(heads, 1):
    print(f"{i}: {node}")
print(f"Number of train(s): {len(heads)}")
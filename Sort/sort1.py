def bubbleRecur(arr, n):
    if n <= 1: #base (alr sorted)
        return arr

    def sorting(i):
        if i < n - 1:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
            sorting(i + 1)

    sorting(0)
    bubbleRecur(arr, n - 1)

inp = list(map(int,input("Enter Input : ").split()))
bubbleRecur(inp,len(inp))
print(inp)
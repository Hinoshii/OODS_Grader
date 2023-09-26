def bubbleRecur(arr, n): #got this from my No1
    if n <= 1: #base (alr sorted)
        return arr

    def sorting(i):
        if i < n - 1:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
            sorting(i + 1)

    sorting(0)
    bubbleRecur(arr, n - 1)
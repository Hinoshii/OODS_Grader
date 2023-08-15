def fibo(num):
    if num == 2 or num == 1:
        return 1
    else:
        prev1 = fibo(num-1)
        prev2 = fibo(num-2)
        return prev1 + prev2

inp = input("Enter Number : ")
print(f'fibo({inp}) =',fibo(int(inp)))
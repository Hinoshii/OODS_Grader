def binary(rounds,digits):
    if rounds == 0:
        print(f'{rounds:0{digits}b}')
        return 0
    else:
        binary(rounds-1,digits)
    print(f'{rounds:0{digits}b}')

inp = int(input("Enter Number : "))
if inp < 0:
    print("Only Positive & Zero Number ! ! !")
else:
    binary(pow(2,inp)-1,inp)

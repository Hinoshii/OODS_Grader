def main():
    print("******** Parking Lot ********")
    max,soi,operation,car = input("Enter max of car,car in soi,operation : ").split()
    if soi != '0':
        stack = soi.split(",")
    else:
        stack = []
        
    if operation == 'arrive' :
        if int(max) <= len(stack):
            print(f"car {car} cannot arrive : Soi Full")
        elif car in stack:
            print(f"car {car} already in soi")
        else :
            stack.append(car)
            print(f"car {car} arrive! : Add Car {car}")
    elif operation == 'depart':
        if stack ==[]:
            print(f"car {car} cannot depart : Soi Empty")
        elif car not in stack:
            print(f"car {car} cannot depart : Dont Have Car {car}")
        else :
            stack.remove(car)
            print(f"car {car} depart ! : Car {car} was remove")
    stackanswer = [int(i) for i in stack]
    print(stackanswer)
main()
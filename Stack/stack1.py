def main():
    inp = input("Enter Input : ")
    left_square = inp.count("[")
    right_square = inp.count("]")
    left_brac = inp.count("(")
    right_brac = inp.count(")")

    if left_brac == right_brac and left_square == right_square:
        print("Parentheses : Matched ! ! !")
    else :
        print("Parentheses : Unmatched ! ! !")
main()
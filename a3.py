valid = False

while not valid :
    try:
        n = int(input("enter an even number"))

        while n%2 ==0 :
            print("bye bye")
        valid = True
    except ValueError:
        print("Invalid")

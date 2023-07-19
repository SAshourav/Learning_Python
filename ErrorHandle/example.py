def ask_for_int():
    while True:
        try:
            result = int(input("Please enter an input: "))
        except:
            print("Whoops! That was not a number")
            continue
        else:
            print("Integer Recived !")
            break
        finally:
            print("End of try / execpt / finally")

ask_for_int()
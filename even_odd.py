from even_odd_modul import*
while True:
    attempt=show_menu()

    if attempt==1:
        add_number()
        print("*" * 50)
    elif attempt==2:
        odd()
        print("*"*50)
    elif attempt==3:
        even()
        print("*"*50)
    elif attempt == 4:
        print("Bye!")
        break
    else:
        print("invalid numbers!!!")
def show_menu():
    print("options:\n"
          "1)enter ten numbers:\n"
          "2)the list of odd numbers:\n"
          "3)the list of even numbers:\n"
          "4)exit:")
    choice=int(input("please enter the number:"))
    return choice

list_of_odd=[]
list_of_even=[]

def add_number():
    for i in range(1,11,1):
        numbers=int(input("please enter the numbers:"))
        if numbers % 2 == 0:
            list_of_even.append(numbers)
        else:
            list_of_odd.append(numbers)


def odd():
    print("current list is :", list_of_odd)

def even():
    print("current list is:",list_of_even)

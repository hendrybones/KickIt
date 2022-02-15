# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def cube(num):
    return num * num * num


result = cube(4)
print(result)


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


result2 = max_num(300, 20, 12)

print(result2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # user input strings
    # user = input("Enter your name")
    # age =input("enter your age");
    # print("welocome"+ user+ "your age is:" + age)
    # # numbers
    try:
        num1 = input("enter first number")
        num2 = input("enter second number")
        result = float(num1) + float(num2)
        print(result)
    except:
        print("invalid input")
    #
    # # string formating
    # color = input(" enter your color")
    # plural_noun = input("enter plural noun")
    # celebrity = input("enter celebrity")
    #
    # print("rose are:" + color)
    # print(plural_noun + "are blue")
    # print(" i love " + celebrity)

    # list
    luck_number = [10, 20, 30, 40, 50]
    friends = ["kelvin", "caren", "job"]
    # print([0]) this prints kelvin
    # show a range between caren
    friends[1] = "mike"  # this will change the name
    print(friends[1:])
    friends.append("hendry")  # add item at the end of the list
    friends.insert(1, "kelly")  # add element in between the given range
    friends.remove("job")  # remove in the list
    friends.extend(luck_number)
    print(friends)

    # basic calculater
    fnum = float(input("enter num one: "))
    op = input("enter the operator: ")
    snum = float(input("enter second number: "))

    if op == "+":
        print(fnum + snum)
    elif op == "-":
        print(fnum - snum)
    elif op == "/":
        print(fnum / snum)
    elif op == "*":
        print(fnum * snum)
    else:
        print("invalid operator")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

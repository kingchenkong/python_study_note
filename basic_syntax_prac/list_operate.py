#!/usr/bin/env python3

divider = "-------------------------------------------"

students = ["Mike", "Albert", "Jay", "Vivian"]
students_string = "Mike, Albert, Jay, Vivian"
date_string = "2024/04/09"


def basic_operate():
    print(basic_operate.__name__ +
          ": list basic" + divider)
    print(str(len(students)))
    print(students[1])
    print(students[-3] + ", " + students[-2])
    print(students[1:3])
    print(students[2:])
    print(students[:3])
    print(students[:4])
    print(students[:7])  # is same as [:4]
    print(students[:-2])

    print(basic_operate.__name__ +
          ": string split to list" + divider)
    print(str(len(students_string)))
    print(students_string.split(","))
    print(date_string.split("/"))

    print(basic_operate.__name__ +
          ": list join to string"+divider)
    print("/ ".join(students))


def update_list():
    print(update_list.__name__ + ": ")
    print(students)
    students[2] = "Akon"
    print(students)


def tuple_diff():
    print(tuple_diff.__name__ + ": ")
    students_tuple = ("Mike", "Albert", "Jay", "Vivian")  # is ()
    print(students_tuple)
    # students_tuple[2] = "Akon" # Tuple cannot update, cause tuple is immutable
    # print(students_tuple)


def list_insert():
    print(list_insert.__name__ + ": " + divider)
    students.append("Elon")
    print(students)
    print("append(): " + str(students))
    students.extend(["Albee", "Edward"])
    print("extend(): " + str(students))


def list_delete():
    print(list_delete.__name__ + ": " + divider)
    students.remove("Mike")
    print(students)
    students.pop()  # kill last
    print(students)
    students.pop(2)  # kill the index = 2
    print(students)

    stu_need_removed = "Elon"
    # stu_need_removed = "Ming"

    print("if '" + stu_need_removed + "' in students? " +
          str(stu_need_removed in students))
    if stu_need_removed in students:
        print(stu_need_removed + " is in list")
        students.remove(stu_need_removed)
    else:
        print(stu_need_removed + " isn't in list")

    std_select = "Albert"
    print(students.index(std_select))


price_sys = ["Apple", 25, "Lemon", 44, "Beef", 230, "Pork", 180]


def query_action():
    query_name = input("Plz input the item name you want to query: ")
    if query_name not in price_sys:
        print(query_name + " is not found.")
    else:
        price_index = price_sys.index(query_name)
        print(f"{query_name} is ${price_sys[price_index + 1]}")


def add_action():
    item_data = input(
        "input the item/price (make sure that use '/' split item and price): ")
    split_list = item_data.split("/")
    # price_sys.extend(item_data.split("/")) # you cannot use extend directly, because .split() will return list[str]

    split_0: str = split_list[0]
    split_1: int = int(split_list[1])
    price_sys.append(split_0)
    price_sys.append(split_1)
    print(price_sys)

    print(f"update list. now item count = {int(len(price_sys)/2)}")


def delete_action():
    item_name = input("input the item name you want to delete: ")
    item_index = price_sys.index(item_name)
    price_index = item_index + 1

    # because price_index = item_index + 1
    # version 1: pop price first and pop item
    price_sys.pop(price_index)
    price_sys.pop(item_index)

    # version 2: pop tiwce
    # price_sys.pop(item_index)
    # price_sys.pop(item_index)

    print(price_sys)


def update_action():
    item_name = input("input the item name you want to update price: ")
    price_index = price_sys.index(item_name) + 1
    new_price : int = int(input("input new price: "))
    price_sys[price_index] = new_price
    
    print(price_sys)

def action_catch():
    # print(action_catch.__name__ + ": " + divider)
    # make sure the action is upper case letter.
    action = input(
        "Plz input the action: (Q)uery (A)dd (D)elet (U)pdate: ").upper()

    if action == "Q":
        query_action()
    elif action == "A":
        add_action()
    elif action == "D":
        delete_action()
    elif action == "U":
        update_action()
    else:
        print("action is undifined.")


def price_sys_operate():
    print(price_sys_operate.__name__ + ": " + divider)
    action_catch()


def main():
    print(main.__name__ + ": ")
    # print(type(students))
    # print(type(students_string))
    # print(type(date_string))
    # basic_operate()
    # update_list()
    # tuple_diff()
    # list_insert()
    # list_delete()
    print(price_sys)
    price_sys_operate()


if __name__ == "__main__":
    main()

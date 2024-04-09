#!/usr/bin/env python3

def basic_prac():
    meals = ["egg cake", "sandwich", "hamberg", "rice balls"]
    drinks = ["soybean milk", "black tea", "milk tea"]
    count = 0
    for meal in meals:
        for drink in drinks:
            print(f"'{meal}' with '{drink}'")
            count += 1

    print(f"-------------\nThere are {count} set in total.\n-------------")


max_input_times: int = 5
correct_pwd: str = "0204"


def pwd_input():
    for input_count in range(max_input_times):
        password = input("input pwd: ")
        if password == correct_pwd:
            print("login success!!")
            break
        elif password != correct_pwd and input_count < max_input_times:
            remain: int = (max_input_times-1) - input_count
            print(f"login fail, you remian {remain} teims. plz re-input.")
        else:
            print("you already input too many times..... end.")


def main():
    print(main.__name__ + ": ")
    basic_prac()
    pwd_input()


if __name__ == "__main__":
    main()

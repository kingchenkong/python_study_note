#!/usr/bin/env python3

def range_print(range_list, func_name, param_name):
    for i in range_list:
        print(func_name + ": " + param_name + ": " + str(i))


def sequence_type():
    func_name = sequence_type.__name__ + ": "

    # list
    seq = ["aaa", "bbb", "ccc", "hello world!!"]
    print(func_name + str(seq))
    sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(func_name + str(sum))

    # tuple, immutable
    tuple_1 = [1, 0, 1, 1, 100, 9, 1, 1, 2, 1]
    print(func_name + str(tuple_1))
    print(func_name + "tuple_1 count( 1 ): " + str(tuple_1.count(1)))
    print(func_name + "tuple_1 index( 100 ): " + str(tuple_1.index(100)))
    # print(func_name + "tuple_1 index( aaa ): " + str(tuple_1.index("aaa"))) # NameError: name 'aaa' is not defined

    tuple_2 = ["love", 2, "we"]
    tuple_3 = ["hate", 10, "us"]
    for t in [tuple_2, tuple_3]:
        print(func_name + str(t[0]))
        print(func_name + str(t[2]))

    # range
    range_1 = range(10)  # 0 <= x <9
    range_2 = range(3, 7)  # 3 <= x <7
    range_3 = range(5, -5)  # (X), list cout = 0
    range_print(range_1, sequence_type.__name__, "range_1")
    range_print(range_2, sequence_type.__name__, "range_2")
    range_print(range_3, sequence_type.__name__, "range_3")

    # range(start, stop, step)
    range_4 = range(1, 50, 20)  # 21, 41
    range_print(range_4, sequence_type.__name__, "range_4")


def numeric_type():
    func_name = numeric_type.__name__ + ": "

    # integer
    int_1 = int(5)
    int_2 = int(3.8)
    print(func_name + str(int_1))
    print(func_name + str(int_2))

    # float
    float_1 = float(5)
    float_2 = float(3.1415926)
    print(func_name + str(float_1))
    print(func_name + str(float_2))

    # complex
    complex_1 = 4j
    complex_2 = 1 + 1j
    print(func_name + str(complex_1))
    print(func_name + str(complex_2))
    complex_3 = complex_1*complex_1
    print(func_name + str(complex_3))


def text_type():
    func_name = text_type.__name__ + ": "

    hello_python = "hello python"
    print(func_name + hello_python)

    demo_string = str("demo string")
    print(func_name + demo_string)

    demo_string_int = str(1234)
    print(func_name + demo_string_int)

    demo_string_float = str(3.14159)
    print(func_name + demo_string_float)


def main():
    print("function name: " + main.__name__)
    # text_type()
    # numeric_type()
    sequence_type()


if __name__ == "__main__":
    main()

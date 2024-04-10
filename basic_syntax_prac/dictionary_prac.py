#!/usr/bin/env python3

cellphone_1 = {
    "brand": "Apple",
    "type": "iPhone 14 Pro",
    "capacity": "1 TB",
    "port": "USB Type-C"
}

cellphone_2 = {
    "brand": "Google",
    "type": "Pixel 8",
    "capacity": ["1 TB", "512 GB", "256 GB"],
    "port": "USB Type-C"
}

cellphone_3 = {
    "brand": "Xiaomi",
    "type": ["Xiaomi 14", "POCO F5"],
    "capacity": ["1 TB", "256 GB"],
    "port": "USB Type-C"
}

depository = [cellphone_1, cellphone_2, cellphone_3]


def query_part():
    print("query -----------")
    print(cellphone_1.get("type", "not found"))
    print(cellphone_1.get("color", "not found"))

    search_key = "brand"
    # search_key = "color"

    if search_key in cellphone_1:
        print(
            f"{cellphone_1['brand']} : {cellphone_1['type']} : {cellphone_1['capacity']}")
        # print(f"{cellphone_1['brand']}")
    else:
        print("not found key: brand")


def add_part():
    print("add --------------")
    cellphone_1['color'] = "black"
    print(cellphone_1)

    cellphone_1['capacity'] = ['256 GB', '512 GB', '1 TB']
    print(cellphone_1)


def delete_part():
    print("delete ------------")
    print(cellphone_1)

    cellphone_1.pop('brand')
    print(cellphone_1)

    cellphone_1.popitem()  # delete last item
    print(cellphone_1)

    cellphone_1.clear()
    print(cellphone_1)


def loop_usage():
    print("loop_usage ------------")

    for key, value in cellphone_1.items():
        print(f"{key} : {value}")


def check_inventory():
    print(check_inventory.__name__ + " -------------------")

    query_brand = input("input brand: ")
    if query_brand in str(depository):
        for cellphone in depository:
            if cellphone['brand'] == query_brand:
                print(
                    f"There are {cellphone['type']}, capacity is {cellphone['capacity']}")
    else:
        print(f"There are no {query_brand} cellphone in depository.")


def main():
    print(main.__name__ + ": ")

    # query_part()
    # add_part()
    # delete_part()
    # loop_usage()
    check_inventory()


if __name__ == "__main__":
    main()

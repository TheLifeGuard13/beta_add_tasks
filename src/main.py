from src.utils import count_files_from_path, get_format_string, get_nums_multiple, get_sorted_by_price

dict_ = [
    {"name": "Apple", "price": 2.50, "category": "fruit", "quantity": 100},
    {"name": "Grape", "price": 10.30, "category": "fruit", "quantity": 10},
    {"name": "Banana", "price": 1.20, "category": "fruit", "quantity": 500},
    {"name": "Cucumber", "price": 6.80, "category": "vegetable", "quantity": 30},
    {"name": "Onion", "price": 0.75, "category": "vegetable", "quantity": 75},
]


if __name__ == '__main__':
    # дополнительное задание №1 к ДЗ №0
    print(count_files_from_path())
    print(count_files_from_path(recursive=True))
    print(count_files_from_path("/home/vlad/PycharmProjects/beta_project"))
    print(count_files_from_path("/home/vlad/PycharmProjects/beta_project", recursive=True))

    # дополнительное задание №1
    print(get_sorted_by_price(dict_, "fruit"))
    print(get_sorted_by_price(dict_, "vegetable"))
    print(get_sorted_by_price(dict_))

    # дополнительное задание №1
    print(get_format_string(["hello", "world", "apple", "pear", "banana", "pop"]))
    print(get_format_string(["", "madam", "racecar", "noon", "level", ""]))
    print(get_format_string([]))
    # дополнительное задание №2
    print(get_nums_multiple([2, 3, 5, 7, 11]))
    print(get_nums_multiple([-5, -7, -9, -13]))
    print(get_nums_multiple([1, 2]))
    print(get_nums_multiple([4]))
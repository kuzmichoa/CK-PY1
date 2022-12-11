import random

def get_unique_list_numbers() -> list[int]:
    list_ = list(range(-10, 11))
    list_uniq = random.sample(list_, 15)
    return list_uniq

    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_ind = 0
max_count = 0

for ind, cou in enumerate(list_numbers):
    if max_count <= list_numbers[ind]:
        max_count = list_numbers[ind]
        max_ind = ind

list_numbers[max_ind], list_numbers[-1] = list_numbers[-1], max_count

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

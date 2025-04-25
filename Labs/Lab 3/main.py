# main.py

from functions1.tasks import (
    grams_to_ounces,
    fahrenheit_to_celsius,
    solve_chickens_rabbits,
    filter_primes,
    print_permutations,
    reverse_words,
    has_33,
    spy_game,
    sphere_volume,
    remove_duplicates,
    is_palindrome,
    print_histogram,
    guess_the_number
)

# Пример использования функций:

# Преобразование граммов в унции
grams = 100
print(f"{grams} граммов = {grams_to_ounces(grams)} унций")

# Преобразование Фаренгейта в Цельсий
fahrenheit = 32
print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")

# Решение задачи о курах и кроликах
heads, legs = 35, 94
chickens, rabbits = solve_chickens_rabbits(heads, legs)
print(f"Куры: {chickens}, Кролики: {rabbits}")

# Отбор простых чисел из списка
numbers = [2, 3, 4, 5, 10, 13, 16, 17]
print(f"Простые числа: {filter_primes(numbers)}")

# Печать всех перестановок строки (будет запрашивать ввод)
# print_permutations()

# Переворачивание слов в предложении (будет запрашивать ввод)
# reverse_words()

# Проверка на наличие двух соседних троек
nums = [1, 3, 3]
print(f"Есть ли два соседних 3: {has_33(nums)}")

# Проверка на наличие последовательности 007
nums = [1, 0, 0, 7, 5]
print(f"Есть ли последовательность 007: {spy_game(nums)}")

# Вычисление объема сферы (радиус = 5)
radius = 5
print(f"Объем сферы: {sphere_volume(radius)}")

# Удаление дубликатов из списка
lst = [1, 2, 2, 3, 4, 4, 5]
print(f"Список без дубликатов: {remove_duplicates(lst)}")

# Проверка, является ли слово палиндромом
word = "madam"
print(f"Является ли слово '{word}' палиндромом? {is_palindrome(word)}")

# Печать гистограммы для списка
lst = [4, 9, 7]
print("Гистограмма:")
print_histogram(lst)

# Играть в игру "Угадай число"
# guess_the_number()

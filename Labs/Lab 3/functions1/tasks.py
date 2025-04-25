#1. Convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams
#2. Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
#3. Solve the chicken and rabbit problem
def solve_chickens_rabbits(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if chickens * 2 + rabbits * 4 == legs:
            return chickens, rabbits
    return None
#4. Filter prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]
#5. Print all permutations of a string
import itertools

def print_permutations():
    s = input("Enter a string: ")
    perms = itertools.permutations(s)
    for perm in perms:
        print(''.join(perm))
#6. Reverse words in a sentence
def reverse_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    print(reversed_sentence)
#7. Check for adjacent 3s in a list
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
#8. Check for sequence 007 in a list
def spy_game(nums):
    seq = [0, 0, 7]
    index = 0
    for num in nums:
        if num == seq[index]:
            index += 1
        if index == 3:
            return True
    return False
#9. Calculate the volume of a sphere
import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius**3
#10. Remove duplicates from a list
def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
#11. Check if a word is a palindrome
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
#12. Print a histogram
def print_histogram(lst):
    for num in lst:
        print('*' * num)
#13. Guess the number game
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
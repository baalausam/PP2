import time
import math

number = int(input("Enter a number: "))
delay_ms = int(input("Enter delay in milliseconds: "))

time.sleep(delay_ms / 1000)  # Преобразовать миллисекунды в секунды
sqrt_result = math.sqrt(number)

print(f"Square root of {number} after {delay_ms} milliseconds is {sqrt_result}")





#for example
'''
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858

'''
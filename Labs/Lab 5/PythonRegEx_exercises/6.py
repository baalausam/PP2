import re

# Паттернді анықтау: бос орын, үтір немесе нүкте
pattern = r'[ ,.]'

# Тексерілетін жол
test_string = 'This is a test, with some spaces. And, commas.'

# Бос орындарды, үтірлерді және нүктелерді қосқыш таңбалармен ауыстыру
result = re.sub(pattern, ':', test_string)

print(f"Өзгертілген жол: {result}")

import re

# Паттернді анықтау: кіші әріптен кейін үлкен әріпке дейін бос орын қосу
pattern = r'([a-z])([A-Z])'

# Тексерілетін жол
test_string = 'ThisIsATestString'

# Кіші әріп пен үлкен әріп арасындағы бос орындарды қосу
result = re.sub(pattern, r'\1 \2', test_string)

print(f"Бос орындар қосылған жол: {result}")

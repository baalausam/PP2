import re

# Паттернді анықтау: Үлкен әріптерден бөліну
pattern = r'(?=[A-Z])'

# Тексерілетін жол
test_string = 'ThisIsATestString'

# Жолды үлкен әріптерде бөліп алу
result = re.split(pattern, test_string)

# Алғашқы бос жолды алып тастау
result = [s for s in result if s]

print(f"Бөлінген жол: {result}")

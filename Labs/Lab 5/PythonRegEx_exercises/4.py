import re

# Паттернді анықтау: бір үлкен әріп және одан кейінгі төменгі регистрдегі әріптер
pattern = r'[A-Z][a-z]+'

# Тексерілетін жолдар
test_strings = ['Hello', 'world', 'Python', 'HELLO', 'Python3']

# Паттернге сәйкес келетін жолдарды тексеру
for test in test_strings:
    if re.match(pattern, test):
        print(f"'{test}' паттернге сәйкес келеді.")
    else:
        print(f"'{test}' паттернге сәйкес келмейді.")

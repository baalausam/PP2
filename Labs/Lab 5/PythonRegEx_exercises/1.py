import re

# Паттернді анықтау: 'a' әрпі және одан кейінгі нөл немесе көп 'b' әрпі
pattern = r'a*b*'

# Тексерілетін жолдар
test_strings = ['a', 'ab', 'abb', 'aabb', 'b', 'aaa', 'abbbbb']

# Паттернге сәйкес келетін жолдарды тексеру
for test in test_strings:
    if re.match(pattern, test):
        print(f"'{test}' паттернге сәйкес келеді.")
    else:
        print(f"'{test}' паттернге сәйкес келмейді.")

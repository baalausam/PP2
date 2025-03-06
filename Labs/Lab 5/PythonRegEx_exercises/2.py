import re

# Паттернді анықтау: 'a' әрпі және дәл 2 немесе 3 'b' әрпі
pattern = r'ab{2,3}'

# Тексерілетін жолдар
test_strings = ['ab', 'abb', 'abbb', 'abbbb', 'a', 'b']

# Паттернге сәйкес келетін жолдарды тексеру
for test in test_strings:
    if re.match(pattern, test):
        print(f"'{test}' паттернге сәйкес келеді.")
    else:
        print(f"'{test}' паттернге сәйкес келмейді.")

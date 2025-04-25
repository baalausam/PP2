import re

# Паттернді анықтау: 'a' әрпі және одан кейін не болса да, соңында 'b' әрпі
pattern = r'a.*b'

# Тексерілетін жолдар
test_strings = ['ab', 'acb', 'abb', 'a123b', 'abbb', 'b']

# Паттернге сәйкес келетін жолдарды тексеру
for test in test_strings:
    if re.match(pattern, test):
        print(f"'{test}' паттернге сәйкес келеді.")
    else:
        print(f"'{test}' паттернге сәйкес келмейді.")

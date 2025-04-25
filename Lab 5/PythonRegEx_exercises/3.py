import re

# Паттернді анықтау: төменгі регистрдегі әріптер және оларды асты сызықпен қосу
pattern = r'[a-z]+(_[a-z]+)*'

# Тексерілетін жолдар
test_strings = ['hello_world', 'this_is_a_test', 'HelloWorld', 'hello', 'lower_case']

# Паттернге сәйкес келетін жолдарды тексеру
for test in test_strings:
    if re.match(pattern, test):
        print(f"'{test}' паттернге сәйкес келеді.")
    else:
        print(f"'{test}' паттернге сәйкес келмейді.")

import re

# Camel case-ті snake case-ке ауыстыру функциясы
def camel_to_snake(camel_str):
    # Үлкен әріптер алдында асты сызық қосып, барлық әріптерді кіші әріпке ауыстыру
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()

# Тексерілетін жол
camel_case_string = 'thisIsACamelCaseString'

# Snake case-ке ауыстыру
snake_case_string = camel_to_snake(camel_case_string)

print(f"Snake Case: {snake_case_string}")

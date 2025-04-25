# Snake case-ті Camel case-ке ауыстыру функциясы
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    # Әр компонентті бас әріппен жазу, тек бірінші компоненттен басқа
    return components[0] + ''.join(x.title() for x in components[1:])

# Тексерілетін жол
snake_case_string = 'this_is_a_snake_case_string'

# Camel case-ке ауыстыру
camel_case_string = snake_to_camel(snake_case_string)

print(f"Camel Case: {camel_case_string}")

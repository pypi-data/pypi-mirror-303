def is_number(s: str) -> bool:
    if s.startswith('-'):
        s = s[1:]
    if s.count('.') > 1:
        return False
    if s.replace('.', '', 1).isdigit():
        return True
    return s.isdigit()


print(is_number('-123.45'))
print(is_number('123.45'))
print(is_number('12--3.45'))
print(is_number('123.4.5'))
print(is_number('a123.4.5'))
print(is_number('123.45b'))

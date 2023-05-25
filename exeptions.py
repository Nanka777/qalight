class MyOwnException(Exception):
    pass

def my_func_with_exeption(a: int):
    if not type(a) is int:
        raise MyOwnException(f'має бути число, а не те що сюди передав: {type(a)}')

try:
    my_func_with_exeption('6')
except MyOwnException:
    print('MyOwn')
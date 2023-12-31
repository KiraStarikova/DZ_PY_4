# Напишите функцию, принимающую на вход только ключевые параметры
# и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def myFunc(**args):
    newDict = {}
    for k, value in args.items():
        if value.__hash__ == None:
            value = str(value)
        newDict[value] = k
    return newDict

print(myFunc(x = 20, y = 20.5, z = (20, 30, 40), s = 'street'))

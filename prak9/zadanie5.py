def compose(f, g):
    def h(x):
        return f(g(x))
    return h

f_str = input('lambda x: x')
g_str = input('lambda x: x')

f = eval(f_str)
g = eval(g_str)

composed_function = compose(f, g)

x = float(input("Введите значение x: "))
result = composed_function(x)
print(f"h({x}) =", result)
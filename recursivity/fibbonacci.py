
def fibonacci(loops):
    if loops == 0:
        return 0
    if loops == 1:
        return 1
    else:
        return fibonacci(loops - 1) + fibonacci(loops - 2)

print(fibonacci(10))

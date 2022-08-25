import functools

@functools.lru_cache()
def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for n in range(100):
    print(fib(n), end=' ')

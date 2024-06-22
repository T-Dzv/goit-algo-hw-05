def caching_fibonacci():
    # in dict cache will be stored results of fibonacci calculations
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # if fibonacci for n or lower number was already calculated, it will be returned from cache
        # without new recursive calculations
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

# test case:
# check_fibonacci = caching_fibonacci()
# print(check_fibonacci(0))
# print(check_fibonacci(1))
# print(check_fibonacci(5))
# print(check_fibonacci(3))
def outer(func):
    def inner():
        print('hi how r u??')
    return inner
@outer
def wish():
    print('good morning')
wish()


def change_case(func):
    def inner():
        data=func()
        return data.upper()
    return inner
@change_case
def wish_one():
    return 'good morning'
print(wish_one())
def wish_two():
    return 'good afternoon'
print(wish_two())
def wish_three():
    return 'good night'
print(wish_three())

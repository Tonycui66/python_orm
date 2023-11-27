import schedule
def Timer_1():
    print("trigger Timer job")


class Atest():
    def __init__(self):
        pass

    @property
    def second(self):
        print("second")

    @property
    def minutes(self):
        print("minutes")

def log_name(func,name):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with name {name}")
        return func(*args, **kwargs)
    return wrapper

# @log_name("Alice")
# def greet(name):
#     print(f"Hello, {name}!")

if __name__ == '__main__':
    # schedule.every(2).seconds.do(Timer_1)
    # while True:
    #     schedule.run_pending()
    a =Atest()
    a.second
    # greet("Bob")

def action(f):
    def wrapper():
        print("start")
        f()
        print("end")
        return wrapper

@action
def main():
       print("Hello")

main()
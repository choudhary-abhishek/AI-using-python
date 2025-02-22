def greet_user(name):
    print(f"hello ,{name}!")


def greet_qut(name="Guest"):
    print(f"Hello,{name}!")

def add_number(*args):
    return sum(args)
    
def sum_number(*args):
    return sum(args)

greet_user("Quantum University")
print(sum_number(1,2,3))

result = add_number(5,3)
print(result)

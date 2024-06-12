#return multiples values
def antecessor_and_successor(number: int) -> int:
    antecessor = number -1
    successor = number +1

    return antecessor , successor

var = antecessor_and_successor(5)
print(type(var))
print(var)
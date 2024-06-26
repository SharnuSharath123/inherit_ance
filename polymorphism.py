# Example 1 : overloading polymorphism

class Human:
    def sayhello(self, name = None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hi!!!")

h = Human()
h.sayhello("Scott")
h.sayhello()



# Example 2 : polymorphism overloading

class Calculation:
    def add(self, a = 0, b = 0, c = 0):
        print(a+b+c)

calobj = Calculation()
calobj.add()
calobj.add(10,20)
calobj.add(10,20,30)


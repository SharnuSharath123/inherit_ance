# Example 1 : I want to make A is a parent class of child B class in the bracket specify the class name

class A:
    def m1(self):
        print("This is m1 method from class A")


class B(A):
    def m2(self):
        print("This is m2 method from class B")


bobj = B()
bobj.m1()  # This is m1 method from class A
bobj.m2()  # This is m2 method from class B



# Example 2 : single inheritance

class A:
    x,y = 10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b = 200,100
    def m2(self):
        print(self.a-self.b)

bobj = B()
bobj.m1()  # 30
bobj.m2()  # 100



# Example 3 : Multilevel inheritance

class A:
    x,y = 10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b = 200,100
    def m2(self):
        print(self.a-self.b)

class C(B):
    i,j = 10,20
    def m3(self):
        print(self.i*self.j)

class D(C):
    p,q = 200,100
    def m4(self):
        print(self.p/self.q)

bobj = D()
bobj.m1()
bobj.m2()
bobj.m3()
bobj.m4()



# Example 4 : Heirarchy inheritance

class A:
    x,y = 10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b = 200,100
    def m2(self):
        print(self.a-self.b)

class C(A):
    i,j = 10,20
    def m3(self):
        print(self.i*self.j)

bobj = B()
bobj.m1()
bobj.m2()

bobj = C()
bobj.m1()
bobj.m3()


# Example 5 : multiple inheritance

class A:
    x,y = 10,20
    def m1(self):
        print(self.x+self.y)

class B:
    a,b = 200,100
    def m2(self):
        print(self.a-self.b)

class C(A,B):
    i,j = 10,20
    def m3(self):
        print(self.i*self.j)

cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()



# Example 6 : calling parent class method using child class(super())

class A:
    def m1(self):
        print("This is m1 method from class A")


class B(A):
    def m1(self):
        print("This is m1 method from class B")
        super().m1()


bobj = B()
bobj.m1()  # This is m1 method from class A
           # This is m2 method from class B

# super() :- To invoke the parent class method to invoke the parent class method through the child class method



# Example 7 : In parent class variables we can access in child class

class A:
    a,b = 10,20

class B(A):
    i,j = 100, 200
    def m(self, x, y):
        print(x+y)               # local variables
        print(self.i+self.j)     # class variables
        print(self.a+self.b)     # class variables

bobj = B()
bobj.m(100, 300)



# Example 8 : overriding the variables

class Parent:
    name = "Sumi"

class Child(Parent):
    name = "Sukha"

cobj = Child()
print(cobj.name)


class Parent:
    name = "Sumi"

class Child(Parent):
    name = "Sukha"
    
    def test(self):
        print(super().name)

cobj = Child()
cobj.test()
print(cobj.name)



# Example 9 : overriding the methods can recreate those methods in the child class

class Bank:
    def rateOfInterest(self):
        return 0
    
class XBank:
    def rateOfInterest(self):
        return 10
    
class YBank():
    def rateOfInterest(self):
        return 12
    
objx = XBank()
print(objx.rateOfInterest())  # 10

objy = YBank()
print(objy.rateOfInterest())  # 12
 



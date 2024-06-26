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
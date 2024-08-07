class A:
    def show(self):
        print("Show From Class A")

class B(A):
    def show(self):
        super().show()
        print("Show From Class B")

class C(A):
    def show(self):
        super().show()
        print("Show from Class C")

class D(B,C):
    def show(self):
        super().show()
        print("Show from Class D")

c1=D()
c1.show()

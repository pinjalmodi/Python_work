class A:
    def show(self):
        print("Show From Class A")

class B(A):
    def show(self):
        super().show()
        print("Show From Class B")

class C(B):
    def show(self):
        super().show()
        print("Show from Class C")


c1=C()
c1.show()

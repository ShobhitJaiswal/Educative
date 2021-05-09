class A:
    var1="shobhit"
    def fun1(self):
        print(self.var1)
class B:
    var2="jaiswal"
    def func2(self):
        print(self.var2)
        return self.var2
class C(A,B):
    def func3(self):
        print(self.fun1(),self.func2())

p=C()
print(p.func3())
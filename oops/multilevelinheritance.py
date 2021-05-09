class A:
    var1="shobhit"
    def do_something(self):
        print(self.var1)
class B(A):
    var2="jaiswal"
    def do_something1(self):
        print(self.var1,self.var2)

print(issubclass(B,A))
p=B()
print(p.var1)
class Overload:
    def default(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print("3")
        elif(a!=None and b!= None):
            print("2")
        elif(a!=None):
            print("1")
        else:
            print("0")
        return True


obj=Overload()
print(obj.default("a","b","c"))
print(obj.default("a","b"))
print(obj.default("a"))
print(obj.default())



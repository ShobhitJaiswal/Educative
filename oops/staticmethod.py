class Shape:
    
    def info(msg):
        # show custom message
        print(msg)
        print("This class is used for representing different shapes.")
        

# create info static method
Shape.info = staticmethod(Shape.info)

Shape.info("Welcome to Shape class")


class Shape1:
    @staticmethod
    def info(msg):
        print(msg)

Shape1.info("shobhit jaiswal")
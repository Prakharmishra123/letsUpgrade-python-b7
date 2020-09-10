from math import sqrt
class cone():
    def __init__(self,radius,height,pi):
        self.radius = radius
        self.height = height
        self.pi = pi

    def volume(self):
        vol = self.radius*self.radius*self.pi*self.height/3
        return print("volume is: ",vol)
    def surfacearea(self):
        l = pow(self.radius,2) + pow(self.height,2)
        area = self.radius*self.pi*sqrt(l)
        return print("surface area is: ",area)

cn = cone(5,10,3.14)
cn.volume()
cn.surfacearea()
                                                   

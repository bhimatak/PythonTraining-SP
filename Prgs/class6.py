class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self,*args):
    print("Move! ",d,s)

class Car(Vehicle):

  def move(self, d,s):
      print("Driving",d,s)

class Boat(Vehicle):
    pass
  # def move(self):
  #   print("Sail!")

class Plane(Vehicle):
  def move(self,d,l):
    print("Fly!",d,l)

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


def f1(x,y):
    pass
def f1(x):
    pass
def f1(x,y,z):
    pass

f1(1)
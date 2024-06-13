class House:
  def __init__(self):
    self.numberOfFloors = 0

  def setNewNumberOfFloors(self, floors):
    self.numberOfFloors = floors
    print(self.numberOfFloors)
    

house1 = House () 
house1.setNewNumberOfFloors(7)
               
    
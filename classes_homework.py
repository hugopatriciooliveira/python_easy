# Homework Assignment #9: Classes
"""
Details:
Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year", and "Weight".
The class should also contain a "NeedsMaintenance" boolean that defaults to False, and "TripsSinceMaintenance" Integer that defaults to 0.
Next an inheritance classes from Vehicle called "Cars".
The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  It should have another method called 
"Stop" that sets the value of isDriving to false.
Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100, then 
the NeedsMaintenance boolean should be set to true.
Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.
Create 3 different cars, using your Cars class, and drive them all a different number of times. Then print out their values for Make, Model, 
Year, Weight, NeedsMaintenance, and TripsSinceMaintenance
"""
"""
Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and Landing (similar to Driving 
and Stopping), but different in one respect: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected 
(return false), and an error message should be printed saying that the plane can't fly until it's repaired.
"""
class Vehicle:
    def __init__(self, Make, Model, Year, Weight):
        self.Make = Make
        self.Model = Model
        self.Year = int(Year)
        self.Weight = float(Weight)
        self.TripsSinceMaintenance = int(0)
        self.NeedsMaintenance = False
    def Repair(self):
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
          
class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight):
        super(Cars, self).__init__(Make, Model, Year, Weight)
        self.isDriving = False
    
    def Drive(self):
        self.isDriving = True
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
        else:
            self.NeedsMaintenance = False

    def Stop(self):
        self.isDriving= False

class Planes(Vehicle):
    def __init__(self, Make, Model, Year, Weight):
        super(Planes, self).__init__(Make, Model, Year, Weight)
        self.isFlying = False
    
    def Flying(self):
        self.isFlying = True
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
            print("This plane can't fly until it's repaired!!!" )
        else:
            self.NeedsMaintenance = False
    def Landing(self):
        self.isFlying = False

car1 = Cars("Ford","Mustang",1965, 3.093)
car2 = Cars("Chevrolet","Camaro",1966, 3.353)
car3 = Cars("Gurgel","BR-800",1988, 1.591)
plane1 = Planes("Hawker Aircraft, Ltd.", "Hurricane", 1930, 7.670)
plane2 = Planes("Boeing Company", "B-52", 1948, 23.000)

# car2.Drive()
# car1.Drive()
# car1.Drive()
# car3.Drive()
# car2.Drive()
# car2.Drive()
# car1.Drive()
# car1.Drive()
# car1.Drive()
# car1.Drive()
# car1.Repair()

# print(car1.TripsSinceMaintenance)
# print(car1.NeedsMaintenance)

# plane1.Flying()
# plane1.Flying()
# plane1.Flying()
# plane1.Flying()

# print(plane1.TripsSinceMaintenance)
# print(car1.NeedsMaintenance)


# "Ford","Mustang",1965, 3,093
# "Chevrolet","Camaro",1966, 3,353
# "Gurgel","BR-800",1988, 1,591

# "Hawker Aircraft, Ltd.", "Hurricane", 1930, 7.670
# "Boeing Company", "B-52", 1948, 23.000 


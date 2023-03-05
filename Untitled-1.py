
#super class
class Vehicle():
    def __init__(self, Vehicle_type):
        self.vehicle_type = Vehicle_type
        print("car")

#child class
class Automobile(Vehicle):
    def __init__(self,Vehicle_type, Year, Make, Model, Number_of_doors, Type_of_roof):
        Vehicle.__init__(self, Vehicle_type)
        self.Year = Year
        self.Make = Make
        self.Model = Model
        self.Number_of_doors = Number_of_doors
        self.Type_of_roof = Type_of_roof

#get the year, make, model, doors, and type of roofs from the user
Vehicle_type = input(str("Enter the vehicle type: "))
Year = input(str("Enter the year of the vehicle: "))
Make = input(str("Enter who manufacture of the vehicle: "))
Model = input(str("Enter the model of the vehicle: "))
Number_of_doors = input(str("Enter the number of doors of the vehicle: "))
Type_of_roof = input(str("Enter the type of roof of the vehicle: "))

#output the data
print("Vehicle type: ",Vehicle_type)
print("Year: ",Year)
print("Make: ",Make)
print("Model: ",Model)
print("Number of doors: ",Number_of_doors)
print("Type of roof: ",Type_of_roof)


    
# myList = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# x=0
# while x<3:
#     x+=1
#     for i in myList:
#         print(i)

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
    print(x,y)
print("=========================")
vehicle2=my_vehicle

vehicle2["number_of_tires"]=4
vehicle2.pop("mileage")
for x in vehicle2:
    print(x)
class Car:
    def __init__(self,name,model,year,price):
        self.name=name
        self.model=model
        self.year=year
        self.price=price
    def __str__(self):
        return f"name:{self.name}|model:{self.model}|year:{self.year}|price:{self.price}"
class Rental:
    def __init__(self):

       self.cars={"toyota":{"name":"camry","model":"xle","year":2023,"price":30000},
                 "lexus":{"name":"suv range","model":"xe30","year":2020,"price":50000},
                 "nissan":{"name":"march","model":"k15","year":2023,"price":30000},
                "chevrolet":{"name":"blazer","model":"v40","year":2020,"price":45000}
                }
    def rent_car(self):
        search=input("enter car name:").lower()
        if search in self.cars:
            pay=int(input("make payment:"))
            if pay==self.cars[search]["price"]:
                print(" successfully rent a car.\n")
                del self.cars[search]

            else:
                print("not enough money.\n")


        else:
            print("enter a valid car name.\n")


    def show_cars(self):
        if not self.cars:
            print("\n not available")

        else:
            print("\n available cars.\n")
            for x in self.cars:
                print(x)




def main():
    my_rental=Rental()
    while True:
        print("\n ===God Grace Car Rental===\n")
        print("1.rent car")
        print("2.show cars")
        print("3.exit")


        option=(input("enter option:"))
        if option=="1":
            my_rental.rent_car()

        elif option=="2":
            my_rental.show_cars()

        elif option=="3":
            logging=input("log out (yes or no):").lower()
            if logging=="yes":
                print("exit")
                break
main()

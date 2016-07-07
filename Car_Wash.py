car = str(input("enter your car type: "))
wash = str(input("enter your wash choice: "))
def carprice(car):
        if car== "sport":
            cprice=20
        elif car=="sudan":
            cprice = 30
        elif car == "suv":
            cprice = 40
        return (cprice)
def carwash(wash):
        if wash == "basic":
            wprice = 10
        elif wash == "super":
            wprice = 20
        elif wash == "supreme":
            wprice = 25
        return wprice
def sum(add):
    add= (carprice(car),carwash(wash))
def taxprice(tax):
        tax = float(sum *.085)
print("your type of car is " ,car, "and you chose" ,wash)
print("the tax is" ,taxprice)
print("your total is" ,carprice(car)+carwash(wash)+taxprice)

class Model:
    def __init__(self, car, model, price, year, amount):
        self.car = car
        self.model = model
        self.price = price
        self.year = year
        self.amount = amount

    def __str__(self):
        return f"{self.car} {self.model} | Narxi: {self.price}$ | Miqdori: {self.amount} | Yili: {self.year}"

class Manage:
    def __init__(self):
        self.products = []

    def add(self, product):
        for p in self.products:
            if p.car == product.car and p.model == product.model:
                p.amount += product.amount  
                return
        self.products.append(product)

    def total(self):
        return sum(p.price * p.amount for p in self.products)  

    def display(self): 
        print("Mahsulotlar ro'yxati:")
        for p in self.products:
            print(p) 
        print(f"Jami narx: {self.total()} USD")  

manage = Manage()
manage.add(Model("Toyota", "Camry", 30000, 2022, 10))
manage.add(Model("BMW", "X5", 50000, 2023, 5))
manage.add(Model("Toyota", "Camry", 30000, 2022, 2)) 

manage.display()  

# Task 3
# Product Store

class Product(object):

    def __init__(self, ptype, name, price):
        self.type = ptype
        self.name = name
        self.price = price



class ProductStore():

    def __init__(self):
        self.stock = {}
        self.income = 0

    def update_stock(self, product: Product, amount):
        if product.name in self.stock:
            self.stock[product.name][1] += amount
        else:
            self.stock[product.name] = [product, amount]


    def change_price(self, identifier, percent, identifier_type="name", discount=True):
        if identifier_type == "name":
            if identifier in self.stock:
                if discount:
                    self.stock[identifier][0].price *= 1 - percent/100
                else:
                    self.stock[identifier][0].price *= 1 + percent / 100
                print(f"Price for {identifier} has been updated.")
            else:
                print(f"Product {identifier} not found in stock.")
        elif identifier_type == "type":
            check = False
            for key in self.stock:
                if identifier == self.stock[key][0].type:
                    check = True
                    if discount:
                        self.stock[key][0].price *= 1 - percent / 100
                    else:
                        self.stock[key][0].price *= 1 + percent / 100
            if check is False:
                print("Type of product doesn't exist in stock.")
            else:
                print("Price change has been applied for products.")

    def sell_product(self, product: Product, amount):
        try:
            p = self.stock[product.name]
            if amount > p[1]:
                raise Exception
            elif amount < 1:
                raise ValueError
            self.income += amount * p[0].price
            p[1] -= amount
        except ValueError:
            print("You cannot buy less than 1 product.")
        except KeyError:
            print("Product doesn't exist in stock.")
        except:
            print(f"Sorry, we don't have enough {product.name} in stock. We have only: ", p[1])


    def get_income(self):
        return self.income

    def get_all_products(self):
        for name in self.stock:
            print(self.get_product_info(name))

    def get_product_info(self, name):
        if name in self.stock:
            return f"Name: {name}; Price: {self.stock[name][0].price}; Amount: {self.stock[name][1]} ."
        else:
            return "Product name not found in stock."



def main():
    p1 = Product("Vegetables", "Tomato", 35)
    p2 = Product("Fruits", "Apple", 20)
    p3 = Product("Vegetables", "Onion", 15)
    p4 = Product("Clothes", "T-shirt", 400)
    s1 = ProductStore()
    s1.update_stock(p1, 50)        #calling method update_stock for adding products to the stock (which is dict where key = name of the product)
    s1.update_stock(p2, 15)
    s1.update_stock(p3, 40)
    s1.update_stock(p4, 10)
    identifier = input("Type for which product or product type you want to change price: ")
    percent = int(input("Type percentage of the price change: "))
    s1.change_price(identifier, percent)         #calling method with input values, by default identifier_type="name", discount=True
    s1.change_price(identifier, percent, identifier_type="type", discount=False)  #if we want to apply changes to default parameters
    s1.sell_product(p1, 20)             #calling method to sell 20 tomatoes
    s1.sell_product(p1, 0)              #calling method to sell 0 tomatoes which will raise an error
    s1.sell_product(p2, 30)             #calling method to sell 30 apples which will raise an error
    s1.get_income()
    s1.get_all_products()               #calling method to check all products remained in stock
    name_of_p = input("What product you want to review info for?: ")
    print(s1.get_product_info(name_of_p))      #calling method to review the info of specific product


if __name__ == "__main__":
    main()

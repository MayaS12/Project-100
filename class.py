class icecream:
    def __init__(self, flavor, size, toppings):
       self.flavor = flavor
       self.size = size
       self.toppings = toppings

    def printIcecream(self):
        print('The icecream you have selected is: ')
        print(self.flavor)
        print(self.size)
        print(self.toppings)

bestIcecream = icecream("caramel","extra large", "white chocolate chips, rainbow sprinkles, caramel sauce")
bestIcecream.printIcecream()

secondBestIcecream = icecream("cookies and cream","medium","chocolate chips, chocolate sprinkles, oreo crumbles")
secondBestIcecream.printIcecream()
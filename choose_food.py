import random

class FoodChooser():
    food_list = list()


    def __init__(self, food):
        self.food_list = food.split(" ")
        print("OK, I know. ")


    def draw(self):
        num = random.randint(0, len(self.food_list) - 1)
        print("Random int generated", num)
        print("Your Food is == ", str(self.food_list[num]), "==")
        return self.food_list[num]
        
    def show_menu(self):
        print(self.food_list)
        

if __name__ == '__main__':
    s = input("Input Your Foods, Split each one with 1 white space(' ') \n") 
    choose = FoodChooser(s)
    choose.draw()


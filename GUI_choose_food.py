from choose_food import FoodChooser
import tkinter as tk
import datetime

class GUI:
    title = str()    
    foods = str()
    sel_food = tk.StringVar()

    def __init__(self):
        current_date_time = str(datetime.datetime.now().time())
        current_time = current_date_time[0:current_date_time.find(':')]
        if(current_time < 10)
            self.title = "早上吃啥？"
        elif(current_time >= 10 and current_time <= 14)
            self.title = "中午吃啥？？"
        elif(current_time > 14 and current_time <= 20)
            self.title = "晚上吃啥？？？"
        else
            self.title = "整顿夜宵？"
        
        root = tk.Tk()
        root.title = self.title
        root.geometry('720x520')
        
        self.sel_food.set(self.title)
        status = tk.Label(root, textvariable=self.sel_food, font='Arial', 16))
        status.pack()

        button_input = tk.Button(root, text="录入食物", command = self.input_food)
        button_input.pack()
        button_draw = tk.Button(root, text = "开始选择", command = self.draw_food)
        button_draw.pack()

        root.mainloop()


    def input_food(self):
        temp_window = tk.Tk()
        temp_window.title = "输入食物, 用空格分隔开"
        temp_window.geometry("480x300")
        foods_entry = tk.Entry(temp_window)
        button_submit = tk.Button(temp_window, text="提交食物", command = lambda: (self.foods = foods_entry.get()) or temp_window.destroy())
        temp_window.mainloop()

    def draw_food(self):
        chooser = FoodChooser(self.foods)
        res = chooser.draw()
        self.sel_food.set(res)


if __name__ == '__main__':
    window = GUI()
    

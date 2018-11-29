from choose_food import FoodChooser
import tkinter as tk
import datetime

class GUI(tk.Tk):
    title = str()    
    foods = str()

    def __init__(self):
        current_date_time = str(datetime.datetime.now().time())
        current_time = int(current_date_time[0:current_date_time.find(':')])
        if(current_time < 10):
            self.title = "早上吃啥？"
        elif(current_time >= 10 and current_time <= 14):
            self.title = "中午吃啥？？"
        elif(current_time > 14 and current_time <= 20):
            self.title = "晚上吃啥？？？"
        else:
            self.title = "整顿夜宵？"
        
        root = tk.Tk()
        root.title(self.title)
        root.geometry('720x550')
       
        img = tk.PhotoImage(file="background.png")
        img_label = tk.Label(root, image=img)
        img_label.pack()

        self.sel_food = tk.StringVar()    
        self.sel_food.set(self.title)
        status = tk.Label(root, textvariable=self.sel_food, font=('Microsoft JHenghei', 16))
        status.pack()

        button_input = tk.Button(root, text="录入食物", command = self.input_food, width=50, font=('Microsoft JHenghei', 12))
        button_input.pack()
        button_draw = tk.Button(root, text = "开始选择", command = self.draw_food, width=50, font=('Microsoft JHenghei', 12))
        button_draw.pack()

        copyright = tk.Label(root, text="©HIT-HanBo 2018", font=('Microsoft JHenghei', 8))
        copyright.pack()
        
        root.mainloop()


    def input_food(self):
        temp_window = tk.Tk()
        temp_window.title("录入你的食物们")
        temp_window.title = "输入食物, 用空格分隔开"
        temp_window.geometry("300x200")
        foods_entry = tk.Entry(temp_window, width=160)
        foods_entry.pack()
        button_submit = tk.Button(temp_window, text="提交食物", command = lambda: (self.set_foods(foods_entry.get())) or temp_window.destroy())
        button_submit.pack()
        temp_window.mainloop()


    def draw_food(self):
        if(len(self.foods) == 0):
            self.sel_food.set("还没输入呢~点击输入")
            return 0
        chooser = FoodChooser(self.foods)
        res = chooser.draw()
        self.sel_food.set(res)



    def set_foods(self, s):
        self.foods = s
        self.sel_food.set("点击开始抽签吧~")

if __name__ == '__main__':
    window = GUI()
    

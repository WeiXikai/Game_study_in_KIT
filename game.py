from random import randint
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

mode = "GUI"

events = [
    {"st":"", "hp":0, "cp":0, "eu":0, "p":0},
    {"st":"你被抢劫了，心情-1，资金-100。", "hp":-1, "cp":0, "eu":-100, "p":1},
    {"st":"你生病了，心情-2。", "hp":-2, "cp":0, "eu":0, "p":1},
    {"st":"你家里的东西坏了，心情-3，资金-200。", "hp":-3, "cp":0, "eu":-200, "p":2},
    {"st":"你的手机丢了，心情-3，资金-300。", "hp":-3, "cp":0, "eu":-300, "p":1},
    {"st":"你的卡丢了，心情-1，资金-20。", "hp":-1, "cp":0, "eu":-20, "p":1},
    {"st":"你逛了趟kaufland，心情+1，资金-100。", "hp":+1, "cp":0, "eu":-100, "p":4},
    {"st":"你逛了趟宜家，心情+1，资金-200。", "hp":+1, "cp":0, "eu":-200, "p":2},
    {"st":"你看到朋友圈别人在秀恩爱，而你还是单身，心情-1。", "hp":-1, "cp":0, "eu":0, "p":2},
    {"st":"你看到朋友圈别人毕业了，而你还遥遥无期，心情-1。", "hp":-1, "cp":0, "eu":0, "p":2},
    {"st":"你看到朋友圈别人发论文了，而你还遥遥无期，心情-1。", "hp":-1, "cp":0, "eu":0, "p":2},
    {"st":"过节了，每逢佳节倍思亲，心情-1。", "hp":-1, "cp":0, "eu":0, "p":2},
    {"st":"你在餐馆吃了顿大餐，心情+1，资金-50。", "hp":+1, "cp":0, "eu":-50, "p":2},
    {"st":"你的签证过期了，但是还没有约到延签的termin，被要求缴纳滞纳金。资金-100。", "hp":-3, "cp":0, "eu":-100, "p":1},
    {"st":"你遭到了种族歧视，心情-1。", "hp":-1, "cp":0, "eu":0, "p":2},
    {"st":"你的Seminar很成功，心情+1。", "hp":+1, "cp":0, "eu":0, "p":1},
    {"st":"你同学过生日，送礼物，资金-50。", "hp":0, "cp":0, "eu":-50, "p":2},
    {"st":"你父母给了你一些零花钱，资金+100。", "hp":0, "cp":0, "eu":100, "p":2},
    {"st":"你的作业遇到了很多问题，心情-1。", "hp":-1, "cp":0, "eu":0, "p":3},
    {"st":"你的课没听懂，心情-1。", "hp":-1, "cp":0, "eu":0, "p":5},
    {"st":"你的作业没过，心情-1。", "hp":-1, "cp":0, "eu":0, "p":3},
    {"st":"你和心爱的对象表白了，但惨遭拒绝，心情-5。", "hp":-5, "cp":0, "eu":0, "p":1},
    {"st":"你的和舍友吵架，心情-1。", "hp":-1, "cp":0, "eu":0, "p":2},
    {"st":"德国政府发了补贴，资金+100。", "hp":-1, "cp":0, "eu":100, "p":1},
    {"st":"你的老同学从外地来看你，心情+2，资金-150。", "hp":+2, "cp":0, "eu":-150, "p":1},
    {"st":"你被朋友喊去吃饭，心情+1，资金-50。", "hp":+1, "cp":0, "eu":-50, "p":2},
    {"st":"你被朋友喊去旅游，心情+3，资金-200。", "hp":+3, "cp":0, "eu":-200, "p":1},
    {"st":"无事发生。", "hp":0, "cp":0, "eu":0, "p":1},
]

choices = [
    {"st":"自己学习", "result":"学到了一些知识，但也觉得很疲惫。", "hp":-1, "cp":2, "eu":0},
    {"st":"和同学一起学习", "result":"学到了很多知识，但是聚餐也花费了一点点费用。", "hp":-1, "cp":3, "eu":-50},
    {"st":"自己出去玩", "result":"心情好一些了，但也花费了一点点费用。", "hp":1, "cp":0, "eu":-50},
    {"st":"和同学一起旅游", "result":"花了很多钱，但是心情好多了。", "hp":+5, "cp":0, "eu":-200},
    {"st":"打工", "result":"挣了点小钱，但是身心俱疲。", "hp":-5, "cp":0, "eu":+150},
    {"st":"摆烂", "result":"无事发生。", "hp":0, "cp":0, "eu":0},
]

be_st = "你从楼上一跃而下，在随风而落的瞬间，你第一次感受到了释然，从入学KIT以来第一次感受到了自由。"

def get_event():
    total_rand = sum(map(lambda e:e["p"], events))
    rand_num = randint(1,total_rand)
    for e in events:
        if e["p"] >= rand_num:
            return e
        else:
            rand_num -= e["p"]


class Player:
    def __init__(self):
        self.eu = 0
        self.hp = 0
        self.cp = 0


class CLI:
    def output(self,st):
        print(st)
        print()
    
    def make_choice(self, st, choices):
        print(st)
        for i in range(len(choices)):
            print(f"{i}: {choices[i]['st']}")
        print("请输入你的决策：")
        n = int(input())
        return choices[n]

    def __init__(self):
        pass


class GUI:
    def show_custom_messagebox(self, st):
        # 创建自定义消息框窗口
        messagebox = Toplevel(self.root)
        messagebox.title("消息框")
        messagebox.geometry("300x200+50+100")  # 设置位置为屏幕坐标 (500, 300)
        
        # 禁用消息框的最大化和最小化按钮
        messagebox.resizable(False, False)
        
        # 创建消息文本标签
        text_label = tk.Label(messagebox, text=st, justify=tk.LEFT, wraplength=250)
        text_label.pack(fill=tk.BOTH, expand=True)
        
        # 定义关闭消息框的函数
        def close_messagebox():
            messagebox.destroy()
        
        # 创建一个确认按钮
        ok_button = tk.Button(messagebox, text="确定", command=close_messagebox)
        ok_button.pack(pady=5)

        messagebox.wait_window()


    def output(self,st):
        self.show_custom_messagebox(st)
        self.text_box.insert(tk.END, f"{st}\n\n")
        # 自动滚动到最新内容
        self.text_box.see(tk.END)
        self.root.update_idletasks()  # 刷新窗口以显示新添加的内容
    

    def make_choice(self, st, choices):
        self.result = None
        popup = Toplevel(self.root)
        popup.title("选项框")
        popup.geometry(f"300x{120+30*len(choices)}+50+100")
        popup.resizable(False, False)
        
        
        # 创建标签
        label = tk.Label(popup, text=st)
        label.pack(pady=10)
        

        # 创建一个函数处理按钮点击事件
        def button_action(choice):
            self.result = choice
            popup.destroy()

        # 创建按钮
        for choice in choices:
            button = tk.Button(popup, text=choice["st"], command=lambda param=choice: button_action(param))
            button.pack(pady=5)
        popup.wait_window()

        return self.result
        

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("模拟KIT留学")
        self.root.geometry("800x600+400+100")

        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(expand=True, fill=tk.BOTH)

        self.text_box = tk.Text(self.text_frame, wrap='word', height=15)
        self.text_box.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.text_frame, orient=tk.VERTICAL, command=self.text_box.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 将文本框绑定到滚动条
        self.text_box['yscrollcommand'] = self.scrollbar.set



class Game:
    def __init__(self):
        self.player = Player()
        self.week = 0
        self.max_week = 20
        self.max_hp = 35
        self.semester = 0
        self.cp = 0
        if mode == "CLI":
            self.ui = CLI()
        elif mode == "GUI":
            self.ui = GUI()
        self.basic_cost = 80
        self.win_label = False

    def end(self, st, label="be"):
        if label == "be":
            st = st + be_st
        self.ui.output(st)
        sys.exit()

    def do_choice(self, month_label="normal"):
        choice = self.ui.make_choice("到周末了，你决定：", choices)
        self.player.eu += choice["eu"]
        if month_label == "last":
            if choice["hp"] < 0:
                self.player.hp += choice["hp"] * 2
            else:
                self.player.hp += choice["hp"] * 2
            self.cp += (choice["cp"] + 1)
        else:
            self.player.hp += choice["hp"]
            self.cp += choice["cp"]
        self.ui.output(f"本周你选择了{choice['st']}，你{choice['result']}")
        self.player.hp = min(self.player.hp, self.max_hp)


    def do_event(self):
        event = get_event()
        self.ui.output("本周，"+event["st"])
        self.player.hp = min(self.player.hp + event["hp"], self.max_hp)
        self.player.eu += event["eu"]

    def check(self):
        if self.player.eu < 0:
            self.end("你破产了。资金的压力让你无法继续生活，学业更是无从谈起。","be")
        if self.player.hp < 0:
            self.end("你崩溃了。你已经完全丧失了活下去的动力，认为人生已经毫无希望了。","be")
        
    def next(self): 
        self.week += 1
        if self.week == 0:
            self.ui.output("新学期开始了。父母帮你交了学费，希望你好好学习。")
            self.cp = 0

        month_label = "normal"
        self.ui.output(f"第{self.semester}学期的第{self.week}周开始了。")
        if self.week > self.max_week - 4:
            self.ui.output("这已经是考试月了，你感到压力很大，也感觉需要认真学习。")
            month_label = "last"
        if self.week % 4 == 1:
            self.player.eu += 400
            self.ui.output(f"新的一个月，你从保证金账户获得了1000欧元的生活费。你支付了430欧的房租，50欧的电车票和120欧的医保，净入账400欧元。")
        
        self.do_event()
        self.ui.output(f"你现在还有{self.player.eu}欧元的存款，以及{self.player.hp}的心情。")
        self.check()
        self.do_choice(month_label)
        self.player.eu -= self.basic_cost
        self.ui.output(f"本周的基础开销是{self.basic_cost}欧。你现在还有{self.player.eu}欧元的存款，以及{self.player.hp}的心情。")
        self.check()
        if self.week > 4 and self.cp / self.week <= 1:
            self.ui.output("你觉得这个学期你学业上画的时间太少了，应该要好好学习。")
        if self.week > 4 and self.player.hp / (self.max_week - self.week + 0.01) < 0.9:
            self.ui.output("你觉得最近心情实在是太差了，需要放松。")

        if self.week == self.max_week:
            self.player.cp += self.cp
            self.ui.output(f"这学期结束了。本学期你一共获得了{self.cp}学分。至此你一共获得了{self.player.cp}学分。")

            if self.player.cp >= 180:
                self.end(f"经历了{self.semester+1}个学期的磨难，你终于毕业了。然而，你因为学校QS排名太低，没有能够找到工作。你感到留学KIT从一开始就是个错误——但是人生已经没有回头药了。")

            if self.cp < 10:
                self.ui.output("你这个学期的学习情况太糟糕了，要加强学习鸭。")
                if self.semester >= 3 and (self.player.cp / self.semester < 15):
                    self.end("你因为挂科被退学了。你觉得无法向自己交代，也无法向父母交代。", "be")

            if self.semester >= 5:
                self.ui.output("你因为延毕被家长催着要赶快毕业。")
                self.player.hp -= 2

            if self.semester % 2 == 0:
                self.ui.output("你回了趟国，心情恢复了。")
                self.player.hp = self.max_hp
                if self.semester >= 6:
                    self.player.hp -= 2
            else:
                self.ui.output("假期里你好好休息了一下，心情恢复了很多。")
                self.player.hp = min(self.max_hp, self.player.hp+10)
                if self.semester >= 6:
                    self.player.hp -= 2

            if self.semester == 1:
                choice = self.ui.make_choice("有同学问你是不是想转学TUM，你决定：",[{"st":"申请转学"},{"st":"不申请转学"}])
                if choice["st"] == "申请转学":
                    self.win_label = True
                    self.ui.output("你申请了转学TUM。")

            if self.semester == 2:
                if self.player.cp >= 45:
                    choice = self.ui.make_choice("你获得了TUM的转学offer，你决定：",[{"st":"转学"},{"st":"不转学"}])
                if choice["st"] == "转学":
                    self.end("你转学了。在从卡鲁到慕尼黑的火车上，你满是快乐——你知道，黑暗已经过去，幸福就在前方。美好的人生，即将展开。","he")

            self.semester += 1

            if self.semester == 14:
                self.end("你因为超过最长修业年限被退学了。你觉得无法向自己交代，也无法向父母交代。", "be")

            self.week = 0

        self.next()
    
    def start(self):
        self.ui.output("你录取了KIT。")
        self.ui.output("你立刻申请了签证，开开心心地乘着飞机飞向了德国——然而此时你并不知道等待你的是一场噩梦。")
        self.player.hp = self.max_hp
        self.ui.output("KIT一共要180学分才能从本科毕业，你需要认真学习，才能顺利完成学业。")
        self.player.cp = 0
        self.ui.output("父母给了2000欧元的启动资金，但你的房租押金就支出了1000。你现在还有1000欧元。欧洲的物价很贵，即便再节省，每周的固定开销也要80欧。每个月初会有一笔保证金解冻，减去房租车票医保大约还剩400欧。注意不要破产哦。")
        self.player.eu = 1000
        self.semester = 1
        self.next()

game = Game()
game.start()
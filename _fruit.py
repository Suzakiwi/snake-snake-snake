import random

class Fruit:


    def __init__(self):

        self.pos = 21

    def teleport(self, snake):
        interdit = []
        # 水果不能去的地点的集合，包括蛇四周和边框
        for i in snake.bodys:
            interdit.append(i.pos)
            interdit.append(i.pos-9)
            interdit.append(i.pos-1)
            interdit.append(i.pos+1)
            interdit.append(i.pos+9)
            #表示蛇四周
            interdit = list(set(interdit))
            #列表整理
        possible = list(set(list(range(81)))-set(interdit)-set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 27, 36, 45, 54, 63, 72, 73, 74, 75, 76, 77, 78, 79, 80, 17, 26, 35, 44, 53, 62, 71]))
        if possible.__len__()==0:
            raise NameError("You win!")
        self.pos = possible[random.randint(0,possible.__len__()-1)]
        
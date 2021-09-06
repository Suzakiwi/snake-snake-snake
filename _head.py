class Head():

    belongs_to = 'snake'

    space = map

    def __init__(self):
        self.pos = 40
        self.lst_pos = 49
        self.critique = 31

    def judge(self, diao):

        if diao[0] not in [1, 2, 3, 4]:
        #尝试注释之
            if self.pos - self.lst_pos == 1:
                self.critique = self.pos + 1
            if self.pos - self.lst_pos == -1:
                self.critique = self.pos - 1
            if self.pos - self.lst_pos == 9:
                self.critique = self.pos + 9
            if self.pos - self.lst_pos == -9:
                self.critique = self.pos - 9
        if diao[0] == 1:
            self.critique = self.pos - 9
        if diao[0] == 2:
            self.critique = self.pos - 1
        if diao[0] == 3:
            self.critique = self.pos + 9
        if diao[0] == 4:
            self.critique = self.pos + 1

    def hit(self,snake):
        solid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 27, 36, 45, 54, 63, 72, 73, 74, 75, 76, 77, 78, 79, 80, 17, 26, 35, 44, 53, 62, 71]
        for i in snake.bodys:
            solid.append(i.pos)
        if self.critique in solid:
            print('Game over!')
            raise NameError('Game over!')

    def eat(self, fruit, snake):
        # fruit 是果子的坐标
        if self.critique == fruit.pos:
            # 框图中判断之下的内容
            fruit.teleport(snake)

#            for number, body in reversed(enumerate(snake.bodys)):
#                body.move()
#                # i.move 需要蛇身类的 move 和蛇头类的 move 方法的支持

            for i in range(snake.bodys.__len__()):
                snake.bodys[-i -1].move(i, snake)

            snake.grow(snake)

        else:

            for i in range(snake.bodys.__len__()):
                snake.bodys[-i - 1].move(i, snake)



    def move(self, i, snake):
        
        lst = self.lst_pos
        self.lst_pos = self.pos

        self.pos = self.critique



#        if Diao[0] not in [1, 2, 3, 4]:
#        #尝试注释掉这些not in
#            if self.pos - lst == 1:
#                self.pos += 1
#            if self.pos - lst == -1:
#                self.pos -= 1
#            if self.pos - lst == 9:
#                self.pos += 9
#            if self.pos - lst == -9:
#                self.pos -= 9
#        if Diao[0] == 4:
#            self.pos += 1
#        if Diao[0] == 2:
#            self.pos -= 1
#        if Diao[0] == 3:
#            self.pos += 9
#        if Diao[0] == 1:
#            self.pos -= 9

        



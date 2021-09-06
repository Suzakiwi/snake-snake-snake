class Body:
    
    

    def __init__(self, snake):
        self.pos = snake.bodys[-1].lst_pos
        
        if snake.bodys[-1].pos - snake.bodys[-1].lst_pos == 1:
            self.lst_pos = self.pos -1
        if snake.bodys[-1].pos - snake.bodys[-1].lst_pos == -1:
            self.lst_pos = self.pos +1
        if snake.bodys[-1].pos - snake.bodys[-1].lst_pos == 9:
            self.lst_pos = self.pos -9
        if snake.bodys[-1].pos - snake.bodys[-1].lst_pos == -9:
            self.lst_pos = self.pos +9


        #### Snake.grow 直接调用，要写！！
        

    def move(self, i, snake):

        # num 传入目前这个蛇身是第几段

        # 蛇：   O O O O O O
        # 蛇编号  1 2 3 4 5 6
        # i序号   5 4 3 2 1 0
        # 迭代顺序 6 5 4 3 2 1

        self.lst_pos = self.pos

        self.pos = snake.bodys[snake.bodys.__len__() -2 - i].pos
        


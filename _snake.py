import _body, _head


class Snake:


    def __init__(self):


        self.bodys = []
        
        self.bodys.append(_head.Head())


    def grow(self, snake):

        self.bodys.append(_body.Body(snake))


        



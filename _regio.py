class Regio:

    
    def __init__(self):
        self.data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3,
            3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def collect(self, snake, fruit):
        self.data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3,
                     3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in snake.bodys:
            self.data[i.pos] = 1

        self.data[fruit.pos] = 2

    def draw(self):
        content = []

        for i in self.data:
            if i == 0:
                content.append('#')
            if i == 1:
                content.append('0')
            if i == 2:
                content.append('*')
            if i == 3:
                content.append(' ')

        print(f'{" ".join(str(i) for i in content[0:9])}\n{" ".join(str(i) for i in content[9:18])}\n{" ".join(str(i) for i in content[18:27])}\n{" ".join(str(i) for i in content[27:36])}\n{" ".join(str(i) for i in content[36:45])}\n{" ".join(str(i) for i in content[45:54])}\n{" ".join(str(i) for i in content[54:63])}\n{" ".join(str(i) for i in content[63:72])}\n{" ".join(str(i) for i in content[72:81])}')




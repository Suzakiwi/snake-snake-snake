import time

import keyboard
import random
import os

from _body import Body

from _fruit import Fruit

from _head import Head

from _regio import Regio

from _snake import Snake



##


fuck_you = [1]



def shang(_):
    fuck_you.pop()

    fuck_you.append(1)



def xia(_):
    fuck_you.pop()

    fuck_you.append(3)



def zuo(_):
    fuck_you.pop()

    fuck_you.append(2)



def you(_):
    fuck_you.pop()

    fuck_you.append(4)



keyboard.on_press_key("up", shang)


keyboard.on_press_key("left", zuo)


keyboard.on_press_key("down", xia)


keyboard.on_press_key("right", you)



##



regio = Regio()



snake = Snake()



fruit = Fruit()



regio.collect(snake, fruit)



os.system('cls')



regio.draw()



# 生成完第一张图片



time.sleep(1)



##



while True:


    diao = []


    diao.append(fuck_you[0])


    snake.bodys[0].judge(diao)


    snake.bodys[0].hit(snake)


    snake.bodys[0].eat(fruit, snake)


    os.system('cls')


    regio.collect(snake, fruit)


    regio.draw()


    time.sleep(1)


    diao = ''


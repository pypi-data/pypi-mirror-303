import pyautogui  as pg
import time
import random
import pygetwindow as gw


def random_float(start, end):
    return round(random.uniform(start, end), 1)

def wait(a,b):
    time.sleep(random_float(a, b))

def three_positive_random_numbers():
    # 生成两个随机数
    num1 = random.random()
    num2 = random.random() * (1 - num1)  # 第二个随机数的范围受第一个随机数影响
    
    # 计算第三个随机数，使得三个数的和为1
    num3 = 1 - num1 - num2
    
    return [num1, num2, num3] 


def random_numbers_list(n):
    numbers = [random.random() for _ in range(n)]
    total = sum(numbers)
    normalized_numbers = [num/total for num in numbers]
    return normalized_numbers


def get_active_window_title():
    active_window = gw.getActiveWindow()
    if active_window is not None:
        return active_window.title
    else:
        return "没有"


def SaoMouseMoveTo(a, b, delay=0.5):
    cishu = 12
    wait(1, 2.5)

    p = pg.position()
    print(p)
    start_x = p.x
    start_y = p.y
    len_x = a - start_x
    len_y = b - start_y
    nodex = [i * len_x for i in random_numbers_list(cishu)]
    nodey = [i * len_y for i in random_numbers_list(cishu)]

    for j in range(cishu):

        pg.moveRel(nodex[j], nodey[j], duration=0.2)
        wait(0.1, 0.2)


def SaoAltTab():
    pg.hotkey('alt', 'tab')
    wait(1,1.5)

def switch_to_window(title):
    i = 1
    while True:
        active_window_title = get_active_window_title()
        print(active_window_title)
        if title in active_window_title:
            break
        j = i
        pg.keyDown('alt')
        for k in range(j):
            pg.press('tab')            
            time.sleep(0.5)
        pg.keyUp('alt')    
        i = i + 1 
        if i == 10:
            break 

def SaoMouseDrag(a=0,b=0,c=100,d=100):
    SaoMouseMoveTo(a,b)
    pg.mouseDown()
    wait(0.1,0.2)
    SaoMouseMoveTo(c,d)
    wait(0.1,0.2)
    pg.mouseUp()        

if __name__ == '__main__':


    switch_to_window("Chrome")

    SaoMouseDrag(802,477,931,476)


# SaoMouseDrag(843,637,993,635,delay=2,duration=4,atctive=True)

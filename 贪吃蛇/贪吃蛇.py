import pygame as pg
import sys
import snake_setting
import time
import numpy as np
import atexit

pg.init()  # 初始化
background = pg.display.set_mode((840, 780))
pg.display.set_caption("Curry's snake game")
background_rect = background.get_rect()

t11 = time.gmtime()  # 获取开始时间
tt1 = time.time()
c1 = time.ctime()
day1 = c1.split(" ")[3]
hour1 = c1.split(" ")[4].split(":")[0]
try:
    int(day1)
except ValueError:
    day1 = c1.split(" ")[2]
    hour1 = c1.split(" ")[3].split(":")[0]
t_1 = time.strftime(f"时间:%Y-%m-{day1} %a {hour1}:%M:%S", t11)

fs_most = 0  # 最高分

op = 1  # 定义玩了几次

historical_group = pg.sprite.Group()  # 定义历史记录群组
historical_background_group = pg.sprite.Group()

while True:  # 设置玩了几次
    try:
        with open(f"贪吃蛇\\贪吃蛇({op}).txt") as f:
            op += 1
    except FileNotFoundError:
        break

kbt_img = pg.image.load("topline.png")  # 设置历史记录顶
kbt = kbt_img.get_rect()
kbt.midtop = background_rect.midtop

kbb = pg.Rect(0, 0, 750, 50)  # 设置历史记录下
kbb.midbottom = background_rect.midbottom

historical_background_img = pg.image.load("topline.png")  # 设置第一个历史记录背景
historical_background_rect = historical_background_img.get_rect()
historical_background_rect.midtop = background_rect.midtop
historical_background_sprite = pg.sprite.Sprite()
historical_background_sprite.rect = historical_background_rect
historical_background_sprite.image = historical_background_img
historical_background_group.add(historical_background_sprite)

kbz_font = pg.font.SysFont("SimHei", 30)  # 设置顶上的字
kbz_img = kbz_font.render("序号             时间             单次最高分", snake_setting.historical_background_color,
                          snake_setting.parkour_icon_color)
kbz_rect = kbz_img.get_rect()
kbz_rect.midleft = kbt.midleft

hh_1 = ["目前历史最高分:0分"]  # 获取历史最高分

while True:  # 获取历史最高分和历史记录
    try:
        with open(f"贪吃蛇\\贪吃蛇({op}).txt") as asd:
            pass
    except FileNotFoundError:
        break
    op += 1
if op != 1:
    for i in range(2, op + 1):
        with open(f"贪吃蛇\\贪吃蛇({i - 1}).txt") as asd:
            hh_1.append(asd.read())
fs_most = int(hh_1[-1].split("目前历史最高分:")[1].split("分")[0])

for hh in range(len(hh_1)):  # 写入历史记录群组
    if hh != 0:
        historical_background_img = pg.image.load("allline.png")
        historical_background_rect = historical_background_img.get_rect()
        historical_background_rect.topleft = historical_background_group.sprites()[-1].rect.bottomleft
        historical_background_sprite = pg.sprite.Sprite()
        historical_background_sprite.rect = historical_background_rect
        historical_background_sprite.image = historical_background_img
        historical_background_group.add(historical_background_sprite)
        historical_font = pg.font.SysFont("SimHei", 30)
        historical_img = historical_font.render(
            f" {hh}      {hh_1[hh].split(' 到')[0].split('时间:')[1]}        {hh_1[hh].split('本次最高分是:')[1].split('分')[0]}",
            snake_setting.historical_background_color,
            snake_setting.parkour_icon_color
        )
        historical_rect = historical_img.get_rect()
        historical_rect.midleft = historical_background_rect.midleft
        historical_sprite = pg.sprite.Sprite()
        historical_sprite.rect = historical_rect
        historical_sprite.image = historical_img
        historical_group.add(historical_sprite)

parkour_icon = pg.font.SysFont("楷体", 100)  # 图标
parkour_icon_image = parkour_icon.render("snake game!!!", True, snake_setting.parkour_icon_color,
                                         snake_setting.parkour_icon_background_color)
parkour_icon_rect = parkour_icon_image.get_rect()
parkour_icon_rect.center = background_rect.center
parkour_icon_rect.y -= 200

cu = pg.font.SysFont("SimHei", 50)  # 解释如何查看历史记录
cu_img = cu.render("历史记录", True, snake_setting.parkour_icon_color,
                   snake_setting.parkour_icon_background_color)
cu_rect = cu_img.get_rect()
cu_rect.center = background_rect.center
cu_rect.top = parkour_icon_rect.bottom + 150

explain = pg.font.SysFont('SimHei', 50)  # 解释怎么退出
explain_img = explain.render("按Esc或点叉退出", True, snake_setting.parkour_icon_color,
                             snake_setting.parkour_icon_background_color)
explain_rect = explain_img.get_rect()
explain_rect.center = parkour_icon_rect.center
explain_rect.top = parkour_icon_rect.bottom

play_icon = pg.font.SysFont("SimHei", 50)  # 主页上的开始按钮
play_icon_image = play_icon.render("开始游戏", True, snake_setting.parkour_icon_color,
                                   snake_setting.parkour_icon_background_color)
play_icon_rect = play_icon_image.get_rect()
play_icon_rect.center = background_rect.center
play_icon_rect.left = parkour_icon_rect.left
play_icon_rect.y += 100

parkour_explain = pg.font.SysFont('SimHei', 50)  # 主页里的解释游戏按钮
parkour_explain_img = parkour_explain.render("游戏说明", True, snake_setting.parkour_icon_color,
                                             snake_setting.parkour_icon_background_color)
parkour_explain_rect = parkour_explain_img.get_rect()
parkour_explain_rect.center = background_rect.center
parkour_explain_rect.left = parkour_icon_rect.left
parkour_explain_rect.y += 100
parkour_explain_rect.right = parkour_icon_rect.right

play_icon2 = pg.font.SysFont("SimHei", 25)  # 解释里的开始按钮
play_icon2_image = play_icon2.render("开始游戏", True, snake_setting.parkour_icon_color,
                                     snake_setting.parkour_icon_background_color)
play_icon2_rect = play_icon2_image.get_rect()
play_icon2_rect.right = background_rect.right

go_home = pg.font.SysFont('SimHei', 25)  # 解释里的回到主页按钮
go_home_img = go_home.render("回到主页", True, snake_setting.parkour_icon_color,
                             snake_setting.parkour_icon_background_color)
go_home_rect = go_home_img.get_rect()

historical_explain_font = pg.font.SysFont('SimHei', 25)  # 解释到历史记录
historical_explain_img = historical_explain_font.render("历史记录", True, snake_setting.parkour_icon_color,
                                                        snake_setting.parkour_icon_background_color)
historical_explain_rect = historical_explain_img.get_rect()
historical_explain_rect.midright = play_icon2_rect.midleft
historical_explain_rect.x -= 15

play_again_icon = pg.font.SysFont("SimHei", 75)  # 游戏里的重新开始按钮
play_again_icon_image = play_again_icon.render("重新开始", True, snake_setting.parkour_icon_color,
                                               snake_setting.parkour_icon_background_color)
play_again_icon_rect = play_again_icon_image.get_rect()
play_again_icon_rect.center = background_rect.center
play_again_icon_rect.y += 100

parkour_explain2 = pg.font.SysFont('SimHei', 75)  # 游戏里的解释游戏按钮
parkour_explain2_img = parkour_explain2.render("游戏说明", True, snake_setting.parkour_icon_color,
                                               snake_setting.parkour_icon_background_color)
parkour_explain2_rect = parkour_explain2_img.get_rect()
parkour_explain2_rect.center = background_rect.center
parkour_explain2_rect.y -= 125
parkour_explain2_rect.x -= 225

historical_font = pg.font.SysFont("SimHei", 75)  # 游戏失败页面到历史记录
historical_img = historical_font.render("历史记录", True, snake_setting.parkour_icon_color,
                                        snake_setting.parkour_icon_background_color)
historical_rect = historical_img.get_rect()
historical_rect.midtop = play_again_icon_rect.midbottom
historical_rect.y += 75

go_historical_font = pg.font.SysFont("SimHei", 40)  # 历史记录里面到历史记录
go_historical_img = go_historical_font.render("回到历史记录", True, snake_setting.parkour_icon_color,
                                              snake_setting.parkour_icon_background_color)
go_historical_rect = go_historical_img.get_rect()

go_home2 = pg.font.SysFont('SimHei', 75)  # 游戏里的回到主页按钮
go_home2_img = go_home2.render("回到主页", True, snake_setting.parkour_icon_color,
                               snake_setting.parkour_icon_background_color)
go_home2_rect = go_home_img.get_rect()
go_home2_rect.center = background_rect.center
go_home2_rect.top = parkour_explain2_rect.top
go_home2_rect.x += 125

go_home_22 = pg.Rect(0, 0, 300, 75)  # 因为游戏里的回到主页按钮右bug所以加了一个背景
go_home_22.center = go_home2_rect.center
go_home_22.x += 100
go_home_22.y += 25

home_historical_font = pg.font.SysFont("SimHei", 50)  # 历史记录到主页
home_historical_img = home_historical_font.render("回到主页", True, snake_setting.parkour_icon_color,
                                                  snake_setting.parkour_icon_background_color)
home_historical_rect = home_historical_img.get_rect()
home_historical_rect.midleft = kbb.midleft

explain_historical_font = pg.font.SysFont("SimHei", 50)  # 历史记录到解释
explain_historical_img = explain_historical_font.render("游戏说明", True, snake_setting.parkour_icon_color,
                                                        snake_setting.parkour_icon_background_color)
explain_historical_rect = explain_historical_img.get_rect()
explain_historical_rect.midleft = home_historical_rect.midright
explain_historical_rect.x += 50

play_historical_font = pg.font.SysFont("SimHei", 50)  # 历史记录到游戏
play_historical_img = play_historical_font.render("开始游戏", True, snake_setting.parkour_icon_color,
                                                  snake_setting.parkour_icon_background_color)
play_historical_rect = play_historical_img.get_rect()
play_historical_rect.midleft = explain_historical_rect.midright
play_historical_rect.x += 50

historical_number_background_rect = pg.Rect(0, 0,  # 历史记录里面的背景
                                            background_rect.width -
                                            2 * snake_setting.historical_number_beside_background + 10, 605)
historical_number_background_rect.center = background_rect.center

kbb_number_rect = pg.Rect(0, 0,  # 历史记录里面的底
                          background_rect.width -
                          2 * snake_setting.historical_number_beside_background + 10,
                          (background_rect.height - historical_number_background_rect.height) / 2)
kbb_number_rect.midtop = historical_number_background_rect.midbottom

hdt_background_rect = pg.Rect(0, 0, 30, 660)  # 历史记录滑动条背景
hdt_background_rect.topright = historical_background_group.sprites()[0].rect.bottomright

hdt_number_background_rect = pg.Rect(0, 0, 30, historical_number_background_rect.height)  # 历史记录里面的滑动条背景
hdt_number_background_rect.bottomright = historical_number_background_rect.bottomright

if len(historical_background_group.sprites()) > 14:  # 历史记录滑动条长度控制和定义
    hdt_number_height = 660 * 660 / ((len(historical_background_group.sprites()) - 1) *
                                     historical_background_group.sprites()[1].rect.height)
else:
    hdt_number_height = 660
hdt_rect = pg.Rect(0, 0, 30, hdt_number_height)
hdt_rect.topright = hdt_background_rect.topright

hdt_number_rect = pg.Rect(0, 0, 30, 0)  # 历史记录里面的滑动条定义
hdt_number_rect.topright = historical_number_background_rect.topright

kbt_number_rect = pg.Rect(0, 0, historical_number_background_rect.width,
                          historical_number_background_rect.y)  # 历史记录里面底定义
kbt_number_rect.midbottom = historical_number_background_rect.midtop

go_play = False  # 变量
go_home = True
go_explain = False
go_historical = False
go_historical_number = False
snake_destiny = snake_setting.snake_destiny
snake_destiny_all = snake_setting.snake_destiny
explain_word_list = snake_setting.explain_word.split("\n")
left = False
right = False
up = True
down = False
cc = False
kk = False
t1 = 1
j1 = False
fs = 0
tt = False
hdt_go = False
hdt_number_go = False
hdt_number_j = 0
new_hdt_go = True
new_hdt = {}
last_mouse_pos = 1
mouse_pos = (0, 0)
plus2 = ""
most_fs = 0
become_long_img = 1
historical_number = 0
score = []
score_all = []

pig_head_img = pg.image.load("猪头.png")  # 蛇头
pig_head_rect = pig_head_img.get_rect()
pig_head_rect.center = background_rect.center
pig_head_rect.y -= 45
pig_head_rect.x += 15
snake_head_sprite = pg.sprite.Sprite()
snake_head_sprite.rect = pig_head_rect
snake_head_sprite.image = pig_head_img
snake_group = pg.sprite.Group()
snake_group.add(snake_head_sprite)

body_group = pg.sprite.Group()  # 身体精灵盒子

for i in range(0, snake_setting.snake_first_length - 1):  # 蛇身
    pig_body_img = pg.image.load("圆形.png")
    pig_body_rect = pig_body_img.get_rect()
    pig_body_rect.center = background_rect.center
    pig_body_rect.y -= 15 - i * 30
    pig_body_rect.x += 15
    snake_body_sprite = pg.sprite.Sprite()
    snake_body_sprite.rect = pig_body_rect
    snake_body_sprite.image = pig_body_img
    snake_group.add(snake_body_sprite)
    body_group.add(snake_body_sprite)

become_long_Group = pg.sprite.Group()  # 第一个能量果

zt_img = pg.image.load("猪头.png")  # 猪头数量的猪头标识
zt_rect = zt_img.get_rect()
zt_rect.x, zt_rect.y = 13.5, 13.5

x_img = pg.image.load("线.png")  # 顶端线
x_rect = x_img.get_rect()
x_rect.y = 57

zt_number = pg.font.SysFont("SimHei", 30)  # 猪头数量

fs_font = pg.font.SysFont("SimHei", 30)  # 分数

most_fs_font = pg.font.SysFont("SimHei", 30)  # 最高分数

fs_most_font = pg.font.SysFont("SimHei", 30)  # 历史最高分数

xg_font = pg.font.SysFont("SimHei", 30)  # 属性

historical_number_title_font = pg.font.SysFont("SimHei", 55)  # 顶上的数字

historical_number_font = pg.font.SysFont("SimHei", 45)


def explain(exp, top):  # 解释函数
    explain_word_font = pg.font.SysFont('SimHei', 40)  # 解释游戏
    explain_word_img = explain_word_font.render(exp, True, snake_setting.parkour_icon_color,
                                                snake_setting.explain_background_color)
    explain_word_rect = explain_word_img.get_rect()
    if top == 0:
        explain_word_rect.center = background_rect.center
        explain_word_rect.top = background_rect.top
    else:
        explain_word_rect.top = background_rect.top + top
    background.blit(explain_word_img, explain_word_rect)


def historical_function(word, jian):  # 历史记录里面的每行画图
    if jian == 0:
        historical_number_img = historical_number_title_font.render(word, True,
                                                                    snake_setting.parkour_icon_background_color,
                                                                    snake_setting.historical_number_background_color)
        historical_number_rect = historical_number_img.get_rect()
        historical_number_rect.midtop = background_rect.midtop
    else:
        historical_number_img = historical_number_font.render(word, True,
                                                              snake_setting.parkour_icon_background_color,
                                                              snake_setting.parkour_icon_color)
        historical_number_rect = historical_number_img.get_rect()
        historical_number_rect.x = 30
        historical_number_rect.y += jian
    background.blit(historical_number_img, historical_number_rect)
    if new_hdt_go:
        new_hdt[historical_number] += 1


def suspended():  # 暂停函数
    go_break = False
    while True:
        for event_more in pg.event.get():
            if event_more.type == pg.QUIT:
                sys.exit()
            elif event_more.type == pg.KEYDOWN:
                if event_more.key == pg.K_ESCAPE:
                    sys.exit()
                if event_more.key == pg.K_q:
                    go_break = True
                    break
        if go_break:
            break


def write_score():
    ttt = time.gmtime()
    c2 = time.ctime()
    day2 = c2.split(" ")[3]
    hour2 = c2.split(" ")[4].split(":")[0]
    try:
        int(day2)
    except ValueError:
        day2 = c1.split(" ")[2]
        hour2 = c1.split(" ")[3].split(":")[0]
    tttt = time.strftime(f" 到 %Y-%m-{day2} %a {hour2}:%M:%S。\n", ttt)
    timetime = "玩了{:.2f}秒。\n".format(time.time() - tt1)
    score_all.insert(0, t_1 + tttt + timetime)
    score_all.append("本次最高分是:{:,}分。\n".format(most_fs))
    score_all.append("目前历史最高分:{:,}分。".format(fs_most))
    with open(f"贪吃蛇\\贪吃蛇({op}).txt", mode="w") as hhh:
        hhh.writelines(score_all)


atexit.register(write_score)  # 使用atexit库让退出时自动执行write_score


def become():  # 生成能量果的函数
    global become_long_Group
    global t1
    global j1
    become_long_Group.empty()
    global kk
    global become_long_img
    if np.random.randint(1, snake_setting.c2_gl) == 1 and time.time() >= t1 + snake_setting.c2_time:
        become_long_img = pg.image.load("乘2.png")
        kk = True
    elif np.random.randint(1, snake_setting.j1_gl) == 1:
        become_long_img = pg.image.load("加1.png")
        j1 = True
    else:
        become_long_img = pg.image.load("能量果.png")
    become_long_rect = become_long_img.get_rect()
    while True:
        become_long_Group.empty()
        become_long_rect.x = 30 * np.random.randint(3, 23)
        become_long_rect.y = 30 * np.random.randint(3, 21)
        become_long_sprite = pg.sprite.Sprite()
        become_long_sprite.image = become_long_img
        become_long_sprite.rect = become_long_rect
        become_long_Group.add(become_long_sprite)
        if not pg.sprite.spritecollideany(become_long_Group.sprites()[-1], snake_group):
            break


def suspended_time(time_time):  # 暂停时间函数
    time1 = time.time()
    while time.time() - time1 <= time_time:
        for event2 in pg.event.get():  # 扑捉操作
            if event2.type == pg.QUIT:
                sys.exit()
            elif event2.type == pg.KEYDOWN:
                if event2.key == pg.K_ESCAPE:
                    sys.exit()
                if event2.key == pg.K_q:
                    suspended()
                global right
                global left
                global up
                global down
                if event2.key == pg.K_LEFT:
                    if not right:
                        left = True
                        right = False
                        up = False
                        down = False
                if event2.key == pg.K_RIGHT:
                    if not left:
                        left = False
                        right = True
                        up = False
                        down = False
                if event2.key == pg.K_UP:
                    if not down:
                        left = False
                        right = False
                        up = True
                        down = False
                if event2.key == pg.K_DOWN:
                    if not up:
                        left = False
                        right = False
                        up = False
                        down = True


def zx():  # 身体移动函数
    for snake_number in range(1, len(snake_group.sprites())):
        if snake_group.sprites()[-snake_number].rect.top == \
                snake_group.sprites()[-snake_number - 1].rect.bottom:
            snake_group.sprites()[-snake_number].rect.y -= 30
        if snake_group.sprites()[-snake_number].rect.bottom == \
                snake_group.sprites()[-snake_number - 1].rect.top:
            snake_group.sprites()[-snake_number].rect.y += 30
        if snake_group.sprites()[-snake_number].rect.right == \
                snake_group.sprites()[-snake_number - 1].rect.left:
            snake_group.sprites()[-snake_number].rect.x += 30
        if snake_group.sprites()[-snake_number].rect.left == \
                snake_group.sprites()[-snake_number - 1].rect.right:
            snake_group.sprites()[-snake_number].rect.x -= 30


def pd():  # 失败时使用的函数
    global score
    global snake_destiny
    global left
    global right
    global up
    global down
    global score_all
    global snake_group
    global snake_destiny_all

    score.append(fs)

    snake_group.sprites()[0].rect.center = background_rect.center

    for snake_bd in range(len(snake_group.sprites())):  # 蛇身
        snake_group.sprites()[snake_bd].rect.center = background_rect.center
        snake_group.sprites()[snake_bd].rect.y += snake_bd * 30 + 15
        snake_group.sprites()[snake_bd].rect.x += 15

    if snake_destiny == 1:
        score_all.append(f"第{len(score_all) + 1}次(命数:{snake_destiny_all},分数:{score})\n")

        score = []

        suspended_time(2)
    else:
        suspended_time(1)

    snake_destiny -= 1

    left = False
    right = False
    up = True
    down = False


become()  # 生成第一个能量果

pg.display.flip()  # 刷新页面
while True:
    for event in pg.event.get():  # 获取鼠标和键盘操作
        mouse_pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            key = pg.key.get_pressed()
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key == pg.K_q:
                suspended()
            if event.key == pg.K_LALT and not (go_play and snake_destiny != 0):
                go_home = False
                go_explain = True
                go_play = False
                go_historical = False
                go_historical_number = False
            if event.key == pg.K_RALT and not (go_play and snake_destiny != 0):
                go_home = True
                go_explain = False
                go_play = False
                go_historical = False
                go_historical_number = False
            if key[pg.K_RCTRL] or key[pg.K_LCTRL] and key[pg.K_g] and \
                    not (go_play and snake_destiny != 0):
                hdt_go = False

                go_home = False
                go_explain = False
                go_play = False
                go_historical = True
                go_historical_number = False

            if event.key == pg.K_SPACE and not (go_play and snake_destiny != 0):  # 点击游戏里的重新开始按钮后
                go_play = True
                go_explain = False
                go_home = False
                go_historical = False
                go_historical_number = False

                snake_destiny = snake_setting.snake_destiny

                left = False
                right = False
                up = True
                down = False

                pig_head_img = pg.image.load("猪头.png")  # 蛇头
                snake_group.empty()
                body_group.empty()
                pig_head_rect = pig_head_img.get_rect()
                pig_head_rect.center = background_rect.center
                pig_head_rect.y -= 45
                pig_head_rect.x += 15
                snake_head_sprite = pg.sprite.Sprite()
                snake_head_sprite.rect = pig_head_rect
                snake_head_sprite.image = pig_head_img
                snake_group.add(snake_head_sprite)

                for i in range(0, snake_setting.snake_first_length - 1):  # 蛇身
                    pig_body_img = pg.image.load("圆形.png")
                    pig_body_rect = pig_body_img.get_rect()
                    pig_body_rect.center = background_rect.center
                    pig_body_rect.y += i * 30 - 15
                    pig_body_rect.x += 15
                    snake_body_sprite = pg.sprite.Sprite()
                    snake_body_sprite.rect = pig_body_rect
                    snake_body_sprite.image = pig_body_img
                    snake_group.add(snake_body_sprite)
                    body_group.add(snake_body_sprite)
                become()

                snake_destiny_all = snake_setting.snake_destiny

            if event.key == pg.K_LEFT:
                if not right:
                    left = True
                    right = False
                    up = False
                    down = False
            if event.key == pg.K_RIGHT:
                if not left:
                    left = False
                    right = True
                    up = False
                    down = False
            if event.key == pg.K_UP:
                if not down:
                    left = False
                    right = False
                    up = True
                    down = False
            if event.key == pg.K_DOWN:
                if not up:
                    left = False
                    right = False
                    up = False
                    down = True
        elif event.type == pg.MOUSEBUTTONUP:
            if hdt_go and go_historical:
                hdt_go = False
            if hdt_number_go and go_historical_number:
                hdt_number_go = False
            if cu_rect.collidepoint(mouse_pos) and go_home:
                go_play = False
                go_home = False
                go_explain = False
                go_historical = True
                go_historical_number = False
            if historical_rect.collidepoint(mouse_pos) and go_play and not (go_play and snake_destiny != 0):
                go_play = False
                go_home = False
                go_explain = False
                go_historical = True
                go_historical_number = False
            if explain_historical_rect.collidepoint(mouse_pos) and go_historical:
                go_play = False
                go_home = False
                go_explain = True
                go_historical = False
                go_historical_number = False
            if historical_explain_rect.collidepoint(mouse_pos) and go_explain:
                go_play = False
                go_home = False
                go_explain = False
                go_historical = True
                go_historical_number = False
        elif event.type == pg.MOUSEBUTTONDOWN:  # 点击后
            if home_historical_rect.collidepoint(mouse_pos) and go_historical:
                go_play = False
                go_home = True
                go_explain = False
                go_historical = False
                go_historical_number = False
            if play_historical_rect.collidepoint(mouse_pos) and go_historical:
                go_play = True
                go_home = False
                go_explain = False
                go_historical = False
                go_historical_number = False
            if play_icon_rect.collidepoint(mouse_pos) and go_home:  # 点击主页上的开始按钮后
                go_play = True
                go_home = False
                go_explain = False
                go_historical = False
                go_historical_number = False
            if parkour_explain_rect.collidepoint(mouse_pos) and go_home:  # 点击主页上的开始按钮后
                go_play = False
                go_home = False
                go_explain = True
                go_historical = False
                go_historical_number = False
            if go_home_rect.collidepoint(mouse_pos) and go_explain:  # 点击解释里的回到主页按钮后
                go_home = True
                go_explain = False
                go_play = False
                go_historical = False
                go_historical_number = False
            if play_icon2_rect.collidepoint(mouse_pos) and go_explain:  # 点击解释里的开始游戏按钮后
                go_home = False
                go_explain = False
                go_play = True
                go_historical = False
                go_historical_number = False
            if parkour_explain2_rect.collidepoint(mouse_pos) and go_play:  # 点击游戏里的解释游戏按钮后
                go_home = False
                go_explain = True
                go_play = False
                go_historical = False
                go_historical_number = False
            if go_home_22.collidepoint(mouse_pos) and go_play:  # 点击游戏里的回到主页按钮后
                go_home = True
                go_explain = False
                go_play = False
                go_historical = False
                go_historical_number = False
            if go_historical_rect.collidepoint(mouse_pos) and go_historical_number and not go_historical:
                hdt_go = False
                go_home = False
                go_explain = False
                go_play = False
                go_historical = True
                go_historical_number = False
            if hdt_background_rect.collidepoint(mouse_pos) and go_historical:
                hdt_go = True
            if hdt_number_background_rect.collidepoint(mouse_pos) and go_historical_number:
                hdt_number_go = True
            if play_again_icon_rect.collidepoint(mouse_pos) and go_play and snake_destiny == 0:  # 点击游戏里的重新开始按钮后
                go_play = True
                go_explain = False
                go_home = False
                go_historical = False
                go_historical_number = False

                snake_destiny = snake_setting.snake_destiny

                left = False
                right = False
                up = True
                down = False

                pig_head_img = pg.image.load("猪头.png")  # 蛇头
                snake_group.empty()
                body_group.empty()
                pig_head_rect = pig_head_img.get_rect()
                pig_head_rect.center = background_rect.center
                pig_head_rect.y -= 45
                pig_head_rect.x += 15
                snake_head_sprite = pg.sprite.Sprite()
                snake_head_sprite.rect = pig_head_rect
                snake_head_sprite.image = pig_head_img
                snake_group.add(snake_head_sprite)

                for i in range(0, snake_setting.snake_first_length - 1):  # 蛇身
                    pig_body_img = pg.image.load("圆形.png")
                    pig_body_rect = pig_body_img.get_rect()
                    pig_body_rect.center = background_rect.center
                    pig_body_rect.y += i * 30 - 15
                    pig_body_rect.x += 15
                    snake_body_sprite = pg.sprite.Sprite()
                    snake_body_sprite.rect = pig_body_rect
                    snake_body_sprite.image = pig_body_img
                    snake_group.add(snake_body_sprite)
                    body_group.add(snake_body_sprite)
                become()
            if go_historical and not kbb.collidepoint(mouse_pos) and not kbt.collidepoint(mouse_pos) and len(
                    historical_background_group.sprites()) >= 2:
                for historical in range(1, len(historical_background_group.sprites())):
                    if historical_background_group.sprites()[historical].rect.collidepoint(mouse_pos):
                        new_hdt_go = True
                        historical_number = historical
                        hdt_go = False
                        go_historical_number = True
                        go_play = False
                        go_explain = False
                        go_home = False
                        go_historical = False
                        break

    if go_play and not go_home and not go_explain and snake_destiny > 0 and not go_historical and \
            not go_historical_number:  # 游戏界面

        if fs > most_fs:  # 设置最高分数
            most_fs = fs

        if fs_most < most_fs:  # 设置最高分数
            fs_most = most_fs

        background.fill(snake_setting.play_background_color)  # 覆盖之前的东西

        if snake_head_sprite.rect.x == 0 or \
                snake_head_sprite.rect.x == 810 or \
                snake_head_sprite.rect.y == 60 or \
                snake_head_sprite.rect.y == 750:  # 如果碰到墙壁
            pd()

        background.blit(x_img, x_rect)  # 画顶端线

        zt_number_img = zt_number.render("×{:,}".format(snake_destiny), snake_setting.parkour_icon_color,
                                         snake_setting.parkour_icon_background_color)  # 设置猪头数量
        zt_number_rect = zt_number_img.get_rect()
        zt_number_rect.left = zt_rect.right
        zt_number_rect.y = 13.5

        fs_img = fs_font.render("分数:{:,}".format(fs), snake_setting.parkour_icon_color,
                                snake_setting.parkour_icon_background_color)  # 设置分数
        fs_rect = fs_img.get_rect()
        fs_rect.left = zt_number_rect.right + snake_setting.xg_distance_apart
        fs_rect.y = 13.5

        most_fs_img = most_fs_font.render("本次最高分数:{:,}".format(most_fs), snake_setting.parkour_icon_color,
                                          snake_setting.parkour_icon_background_color)  # 设置本次最高分数
        most_fs_rect = most_fs_img.get_rect()
        most_fs_rect.left = fs_rect.right + snake_setting.xg_distance_apart
        most_fs_rect.y = 13.5

        fs_most_img = fs_most_font.render("历史最高分数:{:,}".format(fs_most), snake_setting.parkour_icon_color,
                                          snake_setting.parkour_icon_background_color)  # 设置历史最高分数
        fs_most_rect = fs_most_img.get_rect()
        fs_most_rect.left = most_fs_rect.right + snake_setting.xg_distance_apart
        fs_most_rect.y = 13.5

        if kk or time.time() >= snake_setting.c2_time + t1:  # 设置×2时间
            plus2 = ""
        else:
            plus2 = "×2:{:.2f}秒".format(snake_setting.c2_time - time.time() + t1)

        xg_img = xg_font.render("{}".format(plus2), snake_setting.parkour_icon_color,
                                snake_setting.parkour_icon_background_color)  # 设置属性标识
        xg_rect = xg_img.get_rect()
        xg_rect.right = background_rect.right - 13.5
        xg_rect.y = 13.5

        background.blit(xg_img, xg_rect)  # 画属性标识

        background.blit(zt_number_img, zt_number_rect)  # 画猪头数量

        background.blit(fs_img, fs_rect)  # 画分数

        background.blit(most_fs_img, most_fs_rect)  # 画本次最高分数

        background.blit(fs_most_img, fs_most_rect)  # 画历史最高分数

        background.blit(zt_img, zt_rect)  # 画猪头数量的猪头标识

        zx()  # 贪吃蛇身体的走动

        if left:  # 贪吃蛇尾部的走动
            snake_head_img_left = pg.image.load("猪头(左).png")
            snake_head_sprite.image = snake_head_img_left
            snake_head_sprite.rect.x -= 30
            suspended_time(snake_setting.snake_sd)
        elif right:
            snake_head_img_left = pg.image.load("猪头(右).png")
            snake_head_sprite.image = snake_head_img_left
            snake_head_sprite.rect.x += 30
            suspended_time(snake_setting.snake_sd)
        elif up:
            snake_head_img_left = pg.image.load("猪头.png")
            snake_head_sprite.image = snake_head_img_left
            snake_head_sprite.rect.y -= 30
            suspended_time(snake_setting.snake_sd)
        elif down:
            snake_head_img_left = pg.image.load("猪头(下).png")
            snake_head_sprite.image = snake_head_img_left
            snake_head_sprite.rect.y += 30
            suspended_time(snake_setting.snake_sd)

        if pg.sprite.spritecollideany(snake_head_sprite, become_long_Group):  # 如果贪吃蛇碰到能量果
            if j1:
                j1 = False
                snake_destiny += 1
                snake_destiny_all += 1
            if kk:
                cc = True
                kk = False
                t1 = time.time()
            if time.time() >= t1 + snake_setting.c2_time:
                cc = False
                kk = False
            for _ in range(2):
                fs += 1
                pig_body_img = pg.image.load("圆形.png")
                pig_body_rect = pig_body_img.get_rect()
                if snake_group.sprites()[-1].rect.top == snake_group.sprites()[-2].rect.bottom:
                    pig_body_rect.x = snake_group.sprites()[-1].rect.x
                    pig_body_rect.top = snake_group.sprites()[-1].rect.bottom
                if snake_group.sprites()[-1].rect.right == snake_group.sprites()[-2].rect.left:
                    pig_body_rect.y = snake_group.sprites()[-1].rect.y
                    pig_body_rect.right = snake_group.sprites()[-1].rect.left
                if snake_group.sprites()[-1].rect.left == snake_group.sprites()[-2].rect.right:
                    pig_body_rect.y = snake_group.sprites()[-1].rect.y
                    pig_body_rect.left = snake_group.sprites()[-1].rect.right
                if snake_group.sprites()[-1].rect.bottom == snake_group.sprites()[-2].rect.top:
                    pig_body_rect.x = snake_group.sprites()[-1].rect.x
                    pig_body_rect.bottom = snake_group.sprites()[-1].rect.top
                snake_body_sprite = pg.sprite.Sprite()
                snake_body_sprite.rect = pig_body_rect
                snake_body_sprite.image = pig_body_img
                snake_group.add(snake_body_sprite)
                body_group.add(snake_body_sprite)
                if not cc:
                    break
            become_long_Group.empty()
            become()

        become_long_Group.draw(background)  # 画能量果

        snake_group.draw(background)  # 画蛇

        if pg.sprite.spritecollideany(snake_head_sprite, body_group):  # 如果碰到自己

            pd()

    elif go_play and not go_home and not go_explain and snake_destiny == 0 and not go_historical and \
            not go_historical_number:  # 失败页面

        t1 -= snake_setting.c2_time + 1  # 设置变量
        kk = False
        cc = False
        fs = 0

        background.fill(snake_setting.play_again_background_color)  # 覆盖之前的东西

        background.blit(play_again_icon_image, play_again_icon_rect)  # 画重新开始按钮

        background.blit(parkour_explain2_img, parkour_explain2_rect)  # 画解释游戏按钮

        pg.draw.rect(background, snake_setting.parkour_icon_background_color, go_home_22)  # 画回到主页按钮背景

        background.blit(go_home2_img, go_home2_rect)  # 画回到主页按钮

        background.blit(historical_img, historical_rect)  # 画回到主页按钮

    elif go_home and not go_play and not go_explain and not go_historical and not go_historical_number:  # 主页
        background.fill(snake_setting.home_background_color)  # 覆盖之前的东西

        background.blit(parkour_icon_image, parkour_icon_rect)  # 画标志

        background.blit(explain_img, explain_rect)  # 画解释如何退出

        background.blit(play_icon_image, play_icon_rect)  # 画开始游戏按钮

        background.blit(parkour_explain_img, parkour_explain_rect)  # 画解释游戏按钮

        background.blit(cu_img, cu_rect)  # 画

    elif not go_home and not go_play and not go_explain and go_historical and not go_historical_number:  # 历史记录
        background.fill(snake_setting.historical_background_color)  # 覆盖之前的东西

        # 滑动条控制
        if hdt_go and 780 - kbb.height - hdt_rect.height >= hdt_rect.y >= \
                historical_background_group.sprites()[0].rect.height and len(
            historical_background_group.sprites()) >= 2:
            if hdt_background_rect.collidepoint(mouse_pos) and not hdt_rect.collidepoint(mouse_pos):
                hdt_rect.y = mouse_pos[1] - hdt_rect.height / 2
            else:
                hdt_rect.y += mouse_pos[1] - last_mouse_pos[1]

            if 780 - kbb.height - hdt_rect.height < hdt_rect.y:
                hdt_rect.y = 780 - kbb.height - hdt_rect.height
            if hdt_rect.y < historical_background_group.sprites()[0].rect.height:
                hdt_rect.y = historical_background_group.sprites()[0].rect.height

            high = (hdt_rect.y - historical_background_group.sprites()[0].rect.height) * (
                    (len(historical_background_group.sprites()) - 1) * historical_background_group.sprites()[
                1].rect.height) / 660

            historical_background_group.sprites()[1].rect.y = historical_background_group.sprites()[
                                                                  0].rect.height - high

            for i in range(2, len(historical_background_group.sprites())):
                historical_background_group.sprites()[i].rect.top = historical_background_group.sprites()[
                    i - 1].rect.bottom
            for i in range(len(historical_group.sprites())):
                historical_group.sprites()[i].rect.midleft = historical_background_group.sprites()[i + 1].rect.midleft

        historical_background_group.draw(background)  # 画出历史记录背后的条

        historical_group.draw(background)  # 画出历史记录字

        pg.draw.rect(background, snake_setting.historical_background_color, kbb)  # 画出历史记录底

        background.blit(kbt_img, kbt)  # 画出历史记录头

        background.blit(kbz_img, kbz_rect)  # 画出历史记录背后

        pg.draw.rect(background, snake_setting.hdt_background_color, hdt_background_rect)  # 画出历史记录滑动条背景

        pg.draw.rect(background, snake_setting.hdt_color, hdt_rect)  # 画出历史记录滑动条

        background.blit(play_historical_img, play_historical_rect)  # 画出进入游戏

        background.blit(explain_historical_img, explain_historical_rect)  # 画出进入解释

        background.blit(home_historical_img, home_historical_rect)  # 画出进入主页

    elif go_historical_number and not go_play and not go_home and not go_historical and not go_explain:  # 进入历史记录里面
        background.fill(snake_setting.historical_number_background_color)  # 覆盖之前的东西

        pg.draw.rect(background, snake_setting.parkour_icon_color, historical_number_background_rect)  # 画出历史记录背景

        pg.draw.rect(background, snake_setting.hdt_number_background_color, hdt_number_background_rect)  # 画出滑动条背景

        wb = 0  # 定义wb

        if new_hdt_go:  # 设置长度
            new_hdt[historical_number] = 0

        for i in range(len(hh_1[historical_number].split("\n"))):  # 设置真的历史记录
            historical_str = hh_1[historical_number].split("\n")[i]
            while len(historical_str) >= snake_setting.historical_most_font:
                historical_function(str(historical_str)[:snake_setting.historical_most_font],
                                    i * 45 + wb * 45 + 90 - hdt_number_j)
                wb += 1
                historical_str = historical_str[snake_setting.historical_most_font:]
            historical_function(str(historical_str), i * 45 + wb * 45 + 90 - hdt_number_j)

        if new_hdt_go:  # 设置滑动条长度
            if new_hdt[historical_number] <= hdt_number_background_rect.height / 55:
                hdt_number_high = hdt_number_background_rect.height
            else:
                hdt_number_high = 660 * 660 / (new_hdt[historical_number] * 55)
            hdt_number_rect = pg.Rect(0, 0, 30, hdt_number_high)
            hdt_number_rect.midtop = hdt_number_background_rect.midtop

        # 设置滑动条滚动
        if hdt_number_go and hdt_number_background_rect.height - hdt_number_rect.height + kbt_number_rect.height >= hdt_number_rect.y >= \
                kbt_number_rect.height:
            if hdt_number_background_rect.collidepoint(mouse_pos) and not hdt_number_rect.collidepoint(mouse_pos):
                hdt_number_rect.y = mouse_pos[1] - hdt_number_rect.height / 2
            else:
                hdt_number_rect.y += mouse_pos[1] - last_mouse_pos[1]

            if hdt_number_background_rect.height - hdt_number_rect.height + kbt_number_rect.height < hdt_number_rect.y:
                hdt_number_rect.y = hdt_number_background_rect.height - hdt_number_rect.height + kbt_number_rect.height
            if hdt_number_rect.y < kbt_number_rect.height:
                hdt_number_rect.y = kbt_number_rect.height

            hdt_number_j = (
                                   hdt_number_rect.y - kbt_number_rect.height) * hdt_number_background_rect.height / hdt_number_rect.height

        pg.draw.rect(background, snake_setting.historical_number_background_color, kbt_number_rect)  # 画出顶

        pg.draw.rect(background, snake_setting.historical_background_color, kbb_number_rect)  # 画出底

        historical_function(str(historical_number), 0)  # 画出数字

        new_hdt_go = False  # 设置不要新建东西

        pg.draw.rect(background, snake_setting.hdt_number_color, hdt_number_rect)  # 画出滚动条

        background.blit(go_historical_img, go_historical_rect)  # 画出回到历史记录

    elif go_explain and not go_play and not go_home and not go_historical and not go_historical_number:  # 解释页面

        background.fill(snake_setting.explain_background_color)  # 覆盖之前的东西

        for explain_word in range(len(explain_word_list)):  # 画解释文字
            explain(explain_word_list[explain_word], (explain_word-1) * 50)

        background.blit(go_home_img, go_home_rect)  # 画回到主页按钮
        background.blit(play_icon2_image, play_icon2_rect)  # 画开始游戏按钮
        background.blit(historical_explain_img, historical_explain_rect)
    pg.display.flip()  # 刷新页面

    last_mouse_pos = mouse_pos
# 一共1051行代码

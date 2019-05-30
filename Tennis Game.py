import pygame as pg
from pygame.locals import *    #将pygame所有常量导入，如后面的QUIT
from time import sleep
import sys
import os
import time

pg.init()                          #初始化，如果没有的话字体会报错等等
scr=pg.display.set_mode((600,550))   #设置屏幕大小
pg.display.set_caption(("Tennis Game"))   #设置屏幕标题
pp=255,140,0                     #red是一个元组，表示乒乓球的RGB颜色
green=0,255,0
white=255,255,255
cs=225,121,21               #橙色

x=120
y=120
vx=8
vy=8
a=100


zt1=pg.font.SysFont('arial',30)
zt2=pg.font.SysFont('arial',30)

def printtext(font,text,x,y,color):
   img=font.render(text,True,color)
   scr.blit(img,(x,y))

c=10   #c是加速器，如果接了10次，那么加速
fs=0   #fs是分数，接到一次乒乓球就加分
k=1  #基础加分量


# Background
background=pg.image.load('./pic/tennis_court.jpg')  #图片位置

rocket = pg.image.load('./pic/tennis_rocket.png')

ball = pg.image.load('./pic/tennis_ball.png')

while True:
    # scr.fill((199,21,133))

    scr.blit(background,(0,0))  #对齐的坐标
    time.sleep(0.01)   #延迟时间

    for eve in pg.event.get():
        if eve.type == QUIT:    #点击左上角的×
            sys.exit()         #如果无效，可以试试exit()函数
    mx,my=pg.mouse.get_pos()     #获得鼠标的x，y坐标
    a=mx   #鼠标x坐标就是乒乓板的坐标，因此移动鼠标乒乓板也移动
    #pg.draw.circle(scr,pp,(x,y),40,0)
    scr.blit(ball,(x,y))
    # pg.draw.rect(scr,green,(a,530,100,20),0)
    scr.blit(rocket, (a, 400))
    x=x+vx
    y=y+vy
    if x>550 or x<40:
        vx=-vx
    if  y<40:
        vy=-vy
    if y>510 and abs(a-x+50)<200:
        if vy>0:
            vy=-vy
        else:pass
        c=c+1     #每接到3次后乒乓球加速
        fs=fs+k    #加分
        if c>=3:
            c=0
            k=k+k  #乒乓球加速后记分量双倍
            if vx>0:  #加速
                vx=vx+1
            else:
                vx=vx-1
        else:pass
    elif y>510 and abs(a-x+50)>200:
        break
    sleep(0.005)  #休眠一定时间，不然乒乓球速度依然很快
    printtext(zt1,"Move the mouse to hit the ball",20,30,white)
    printtext(zt2,"Score",500,12,cs)
    printtext(zt2,str(fs),510,32,cs)
    pg.display.update()

scr.blit(background,(0,0))   #游戏结束后全屏改变颜色
zt3=pg.font.SysFont('stkaiti',120)
zt4=pg.font.SysFont('stkaiti',60)
printtext(zt3,"Game Over!",60,120,white)
printtext(zt4,'Score: '+str(fs),120,400,white)
pg.display.update()



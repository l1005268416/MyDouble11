#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from PIL import Image
import cv2
import numpy as np


def getlocal(img="screen.png",tp="tp.png"):
    arr=[]
    img = cv2.imread(img, 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(tp, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    locs = np.where(res >= 0.965)
    for loc in zip(*locs[::-1]):
        arr.append(loc[0]+w/2)
        arr.append(loc[1] + h / 2)
    print(len(arr))
    return arr


def screencap(name="screen.png"):
    os.system('adb shell screencap -p /storage/emulated/0/book/{}'.format(name))
    os.system('adb pull /storage/emulated/0/book/{}'.format(name))


def unlock(mima):
	os.system('adb shell input keyevent 26')
	time.sleep(1)
	os.system('adb shell input swipe 900 1800 900 800')
	img="lock.png"
	screencap(img)
	time.sleep(1)
	for item in mima:
		arr=getlocal(img,"{}.png".format(item))
		os.system('adb shell input tap {} {}'.format(arr[0],arr[1])) 


def qu_guang_dian():
    print('====== 进入领喵币中心,去逛店 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 900 1670')  # 点击下方领喵币
    for i in range(1, 30):
        os.system('adb shell input swipe 900 500 900 800')  # 点击
        time.sleep(2)
        print('第{}次去逛店...'.format(i))
        screencap()
        time.sleep(1)
        arr=getlocal()
        if len(arr)<2:
            print("数值不对{}".format(len(arr)))
            break

        os.system('adb shell input tap {} {}'.format(arr[0],arr[1]))  # 点击去逛店，然后等15s
        # os.system('adb shell input tap 900 1847')  # 点击去逛店，然后等15s
        time.sleep(3)
        os.system('adb shell input swipe 900 500 900 200') # 滑动
        print('进入店铺,浏览页面中，请等待15s...')
        time.sleep(16)
        os.system('adb shell input keyevent KEYCODE_BACK')
    print('已完成去逛店领取喵币任务')
    os.system('adb shell input tap 977 400')  # 返回


def kan_zhi_bo():
    print('====== 进入领喵币中心，看直播 ======')
    for i in range(1, 4):
        os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
        os.system('adb shell input tap 900 1670')  # 点击下方领喵币
        screencap()
        img = Image.open('screen.png')
        # print(img.getpixel((111, 1824)))
        if img.getpixel((111, 1824)) == (248, 239, 237, 255):
            print('第{}次去看直播...'.format(i))
            time.sleep(1)
            os.system('adb shell input tap 900 1800')  # 点击去看直播，然后等12s
            print('观看直播中，请等待20s...')
            time.sleep(20)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
        else:
            print('3次看直播任务已完成')
            break
    print('已完成去看直播领取喵币任务')
    os.system('adb shell input tap 996 136')  # 点击右上角关闭


def liu_lan_hui_chang2(x,y):
    print('====== 进入领喵币中心，浏览会场 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 900 1670')  # 点击下方领喵币
    for i in range(1, 4):
        os.system('adb shell input tap {} {}'.format(x,y))  # 点击去会场
        time.sleep(3)
        print('浏览会场中，请等待15s...')
        os.system('adb shell input swipe 900 500 900 200')  # 滑动
        time.sleep(16)
        os.system('adb shell input keyevent KEYCODE_BACK')  # 返回

    print('已完成浏览会场领取喵币任务')
    os.system('adb shell input tap 977 400')  # 返回


if __name__ == "__main__":
	#是否锁屏状态
	result=os.popen("adb shell dumpsys window policy")
	res = result.read()
	print(res)
	if 'interactiveState=INTERACTIVE_STATE_SLEEP' in res:
		unlock("1314")
	time.sleep(2)
	#回到home页
	os.system('adb shell input keyevent 3')
	# 打开淘宝
	os.system('adb shell am start -n "com.taobao.taobao/com.taobao.tao.TBMainActivity"')
	# 等待淘宝打开
	time.sleep(2)
	os.system('adb shell input tap 780 1680')
	time.sleep(5)
	qu_guang_dian()
    # liu_lan_hui_chang2(881, 1286)
    # liu_lan_hui_chang2(881, 1462)
    # liu_lan_hui_chang2(881, 1656)

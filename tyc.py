import pyautogui,time
time.sleep(5)
sb_nums=[
'12919473','13062357','13076487','13184135','13340718',
'13452695','13530163','13691700','14037353','14037353A','14037833',
'14037833','14038151','14057562','14057562A','14394047','14394320',
'14394720'
]
for num in sb_nums:
    x=pyautogui.locateOnScreen('trade/注册号.png')
    x,y=pyautogui.center(x)
    pyautogui.click(x+200,y,duration=0.2)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.typewrite(num)
    search=pyautogui.locateOnScreen('trade/查询.png')
    pyautogui.click(pyautogui.center(search))
    while True:
        print('查找搜索结果')
        not_find=pyautogui.locateOnScreen('trade/没有检索到.png')
        apply_num=pyautogui.locateOnScreen('trade/序号.png')
        if not_find or apply_num:
            break
        else:
            print('未找到搜索结果')
            time.sleep(2)
    if not_find:
        sb_tag=pyautogui.locateOnScreen('trade/商标综合检索.png')
        pyautogui.click(pyautogui.center(sb_tag),duration=0.2)
        time.sleep(1)
    elif apply_num:
        print('找到序号')
        x,y=pyautogui.center(apply_num)
        pyautogui.click(x+35,y,duration=0.2)
        time.sleep(2)
        while True:
            sb_detail=pyautogui.locateOnScreen('trade/商标详情.png')
            if sb_detail:
                break
            else:
                print('未找到商标详情')
                time.sleep(2)
        x,y=pyautogui.center(sb_detail)
        pyautogui.rightClick(x+20,y+300,duration=0.2)
        time.sleep(1)
        pyautogui.click(x+51,y+351,duration=0.2)
        time.sleep(1)
        save_sb=pyautogui.locateOnScreen('trade/商标详细内容.png')
        while not save_sb:
            pyautogui.rightClick(x+20,y+300,duration=0.2)
            time.sleep(1)
            pyautogui.click(x+51,y+351,duration=0.2)
            time.sleep(1)
            save_sb=pyautogui.locateOnScreen('trade/商标详细内容.png')
        pyautogui.click(pyautogui.center(save_sb),duration=0.2)
        pyautogui.hotkey('ctrl','a')
        time.sleep(1)
        pyautogui.typewrite(num+'_detail.html')
        time.sleep(1)
        save_btn=pyautogui.locateOnScreen('trade/保存.png')
        pyautogui.click(pyautogui.center(save_btn),duration=0.2)
        time.sleep(1)
        pyautogui.click(pyautogui.center(save_btn),duration=0.2)
        time.sleep(1)
        tihuan=pyautogui.locateOnScreen('trade/替换.png')
        if  tihuan:
            print('替换详情')
            time.sleep(1)
            x,y=pyautogui.center(tihuan)
            pyautogui.click(x+150,y,duration=0.2)
            time.sleep(1)
        elif not tihuan:
            print('不用替换')
        sb_milepost=pyautogui.locateOnScreen('trade/商标流程.png')
        pyautogui.click(pyautogui.center(sb_milepost),duration=0.2)
        time.sleep(2)

        x,y=pyautogui.center(sb_milepost)
        pyautogui.rightClick(x+20,y+300,duration=0.2)
        time.sleep(1)
        pyautogui.click(x+51,y+351,duration=0.2)
        time.sleep(1)
        save_sb=pyautogui.locateOnScreen('trade/商标详细内容.png')
        while not save_sb:
            pyautogui.rightClick(x+20,y+300,duration=0.2)
            time.sleep(1)
            pyautogui.click(x+51,y+351,duration=0.2)
            time.sleep(1)
            save_sb=pyautogui.locateOnScreen('trade/商标详细内容.png')
        pyautogui.click(pyautogui.center(save_sb),duration=0.2)
        pyautogui.hotkey('ctrl','a')
        time.sleep(1)
        pyautogui.typewrite(num+'_milepost.html')
        time.sleep(1)
        save_btn=pyautogui.locateOnScreen('trade/保存.png')
        pyautogui.click(pyautogui.center(save_btn),duration=0.2)
        time.sleep(1)
        pyautogui.click(pyautogui.center(save_btn),duration=0.2)
        time.sleep(1)
        tihuan1=pyautogui.locateOnScreen('trade/替换.png')
        if tihuan1:
            print('替换流程')
            x,y=pyautogui.center(tihuan1)
            pyautogui.click(x+150,y,duration=0.2)
            time.sleep(1)
        sb_tag=pyautogui.locateOnScreen('trade/商标综合检索.png')
        pyautogui.click(pyautogui.center(sb_tag),duration=0.2)
        time.sleep(1)
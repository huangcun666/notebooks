from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Firefox()
# options.add_argument('User-Agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"')
# driver=webdriver.Chrome('/opt/google/chrome/chromedriver')
driver.get('http://wsjs.saic.gov.cn')
sb_nums=[
'12919336','12919473','13062357','13076487','13184135','13340718',
'13452695','13530163','13691700','14037353','14037353A','14037833',
'14037833','14038151','14057562','14057562A','14394047','14394320','14394720',
'14671439','14707861','14813886','14772697','14685216','15634197','15117606',
'15117863','15118107','15140742','15140795','15165120','15212435','15248842',
'15249026','15268495','15332848','15333012','15357232','15364163','15364739','15365374',
'15365481','15369211','15489946','15634197','15634245','15663282','15689070','15815651',
'16010130','16010224','16010339','16295255','16471607','16471509','16660172','16930332',
'16930598','17008856',]
while True:
    try:
        
        element=driver.find_element_by_xpath("//img[@src='/tmrp/images/icon2.png']")
        break
    except:
        print('未找到商标综合查询')
        driver.implicitly_wait(10)

element.click()
for sb_num in sb_nums:
    while True:
        try:
            try:
                element=driver.find_element_by_xpath("//img[@src='/tmrp/images/icon2.png']")
                element.click()
            except:
                print('未找到商标综合查询2')
            apply_num=driver.find_element_by_xpath("//input[@name='request:sn']")
            break
        except:
            print('未找到'+sb_num+'申请/注册号输入框')
            driver.implicitly_wait(10)
    apply_num.clear()
    apply_num.send_keys(sb_num)

    while True:
        try:
            searchButton=driver.find_element_by_xpath("//input[@id='_searchButton']")
            break
        except:
            print('未找到'+sb_num+'查询按钮')
            driver.implicitly_wait(10)


    searchButton.click()
    while True:
        try:
            try:
                searchButton=driver.find_element_by_xpath("//input[@id='_searchButton']")
                apply_num.clear()
                apply_num.send_keys(sb_num)
                searchButton.click()
            except:
                print('未找到'+sb_num+'查询按钮2')
            allHandlers=driver.window_handles
            driver.switch_to_window(allHandlers[-1])
            print(driver.title)
            try:
                not_sub=driver.find_element_by_xpath("//*[text()='没有检索到结果！']")
                if not_sub:
                    driver.switch_to_window(allHandlers[0])
                    break
            except:
                pass
            binding=driver.find_elements_by_xpath("//a[@class='ng-binding']")[0]
            print(binding.text)
            break
        except:

            print('未找到'+sb_num+'商标详细内容入口')
            driver.implicitly_wait(10)
    binding.click()
    if driver.title!='商标综合检索':
        while True:
            try:
                allHandlers=driver.window_handles
                driver.switch_to_window(allHandlers[-1])
                if driver.title=='商标检索结果':
                    binding.click()
                xqbox=driver.find_elements_by_class_name('xqbox')
                if xqbox:
                    source=driver.find_element_by_xpath("//*")
                    source_code=source.get_attribute('outerHTML')
                    print(driver.title)
                    with open('trade/'+sb_num+'商标详情.html','wb') as f:
                        f.write(source_code.encode('utf-8'))
                    print('写入'+sb_num+'商标详情完成')
                    
                    break
            except:
                print('未找到'+sb_num+'商标详情')
                driver.implicitly_wait(10)
        while True:
            try:

                txnDetail2=driver.find_element_by_id('txnDetail2')
                txnDetail2.click()
                break
            except:
                print('未找到'+sb_num+'商标流程入口')
                driver.implicitly_wait(10)
        while True:
            try:
                try:
                    txnDetail2=driver.find_element_by_id('txnDetail2')
                    txnDetail2.click()
                except:
                    print('未找到'+sb_num+'商标流程入口2')
                xqboxx=driver.find_element_by_class_name('xqboxx')
                if xqboxx:
                    source=driver.find_element_by_xpath("//*")
                    source_code=source.get_attribute('outerHTML')
                    with open('trade/'+sb_num+'商标流程.html','wb') as f:
                        f.write(source_code.encode('utf-8'))
                    print('写入'+sb_num+'商标流程完成')
                    driver.close()
                    allHandlers=driver.window_handles
                    driver.switch_to_window(allHandlers[-1])
                    if driver.title=='商标检索结果':
                        driver.switch_to_window(allHandlers[0]) 
                    break       
            except:
                print('未找到'+sb_num+'商标流程')
                driver.implicitly_wait(10)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Firefox()
# options.add_argument('User-Agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"')
# driver=webdriver.Chrome('/opt/google/chrome/chromedriver')
driver.get('http://wsjs.saic.gov.cn')
while True:
    try:
        
        element=driver.find_element_by_xpath("//img[@src='/tmrp/images/icon2.png']")
        break
    except:
        print('未找到')
        driver.implicitly_wait(10)

element.click()
while True:
    try:
        try:
            element=driver.find_element_by_xpath("//img[@src='/tmrp/images/icon2.png']")
            element.click()
        except:
            pass 
        apply_num=driver.find_element_by_xpath("//input[@name='request:sn']")
        break
    except:
        print('未找到2')
        driver.implicitly_wait(10)

apply_num.send_keys('21468056')

while True:
    try:
        searchButton=driver.find_element_by_xpath("//input[@id='_searchButton']")
        break
    except:
        print('未找到3')
        driver.implicitly_wait(10)


searchButton.click()
while True:
    try:

        allHandlers=driver.window_handles
        driver.switch_to_window(allHandlers[-1])
        print(driver.title)
        binding=driver.find_elements_by_xpath("//a[@class='ng-binding']")[0]
        print(binding.text)
        break
    except:

        print('未找到4')
        driver.implicitly_wait(10)
binding.click()
while True:
    try:
        allHandlers=driver.window_handles
        driver.switch_to_window(allHandlers[-1])
        if driver.title=='商标检索结果':
            binding.click()
        info=driver.find_elements_by_class_name('info')
        s=driver.find_element_by_xpath("//*")
        source_code=s.get_attribute("outerHTML")
        print(driver.title)
        with open('21468056.html','w') as f:
            f.write(source_code)
        break
    except:
        print('未找到4')
        driver.implicitly_wait(10)



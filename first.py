import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.barco.com/eu-en/support/clickshare-extended-warranty/warranty")
driver.maximize_window()
#time.sleep(1)
driver.find_element_by_id("serial").send_keys("1863552437")
#time.sleep(1)
driver.find_element_by_xpath('//*[@id="warranty"]/div/div[2]/div/div/form/button').click()
driver.implicitly_wait(10)
link=driver.find_element_by_id("onetrust-accept-btn-handler")
link.click()
try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"onetrust-accept-btn-handler")))
    element.click()
    dl_elements=driver.find_element_by_xpath('//*[@id="warranty"]/div/div[2]/div/div/dl')
    infor_list=[]
    for dl_element in dl_elements:
        dic={}
        description=dl_element.find_element_by_xpath('//*[@id="warranty"]/div/div[2]/div/div/dl/dt[1]').text
        part_number=dl_element.find_element_by_xpath('//*[@id="warranty"]/div/div[2]/div/div/dl/dt[2]').text
        installation_date=dl_element.find_element_by_xpath('//*[@id="warranty"]/div/div[2]/div/div/dl/dt[3]').text
        warranty_end_date=dl_element.find_element_by_xpath('//*[@id="warranty"]/div/div[2]/div/div/dl/dt[4]').text
        dic['description']=description
        dic['part_number']=part_number
        dic['installation_date']=installation_date
        dic['warranty_end_date']=warranty_end_date
        print(dic)
        infor_list.append(dic)
        head=['description','part_number','installation_date','warranty_end_date']
        with open('list.csv',w,encoding='utf-8',newline='') as f:
            writer=csv.DicWriter(f,head)
            writer.writeheader()
            writer.writeroews(infor_list)
except:
    driver.quit()


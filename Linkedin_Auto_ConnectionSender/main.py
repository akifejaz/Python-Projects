from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(2)
page = 1
name = []

#********** LOG IN *************
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('example@gmail.com')       #Enter YOur Email / Username Here
password.send_keys('@Pasword')                #Enter YOur Pasword Here !!
time.sleep(2)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(20)

#**********1st 2nd and 3rd Connection **********
#driver.get("https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH")
driver.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102105699%22%2C%22105117694%22%2C%22103121230%22%2C%22102890883%22%2C%22100642566%22%2C%22101174742%22%2C%22104305776%22%2C%22101165590%22%2C%22106057199%22%2C%22101022442%22%2C%22103644278%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=" + str(page))
time.sleep(5)




while page < 100 :

    driver.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102105699%22%2C%22105117694%22%2C%22103121230%22%2C%22102890883%22%2C%22100642566%22%2C%22101174742%22%2C%22104305776%22%2C%22101165590%22%2C%22106057199%22%2C%22101022442%22%2C%22103644278%22%5D&network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=" + str(page))
    time.sleep(5)

    try:
        all_buttons = driver.find_elements_by_tag_name("button")
        time.sleep(2)
        connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
        name = [btn for btn in all_buttons if btn.text == "Connect" ]
        time.sleep(1)
        page += 1

        for btn in connect_buttons:
            try:
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(5)
                send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
                driver.execute_script("window.scrollTo(0, 200)")
                driver.execute_script("arguments[0].click();", send)
                close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
                driver.execute_script("arguments[0].click();", close)
                time.sleep(5)
                name += 1
            except:
                pass
    
    except:
        pass



print("Total Connection Reequest sent : ", len(name))
print("Closed !")



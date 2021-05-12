from selenium import webdriver
from selenium.webdriver.common import keys
import xlrd
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime
start_time = datetime.now()



PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
contacts = []

#For thoes who get msg
all_get_msg = []
#For thoes who not get msg
all_not_get_msg = []

def extract_contacts():

    # Give the location of the file
    loc = ("NamesOnly.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    n = 1
    while (n < 321): 
# n = no of contacts in your excel file
#In my case i have 321 contacts for whatsapp

        contacts.append(sheet.cell_value(n, 0))  # adding the element
        n += 1


def open_whatsap():


    driver.get("https://web.whatsapp.com/")
    time.sleep(20)


def search_contact(contact):
    time.sleep(2)
    search_field = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    time.sleep(1)
    search_field.click()

    #clear previous input
    search_field.clear()

    #send name
    search_field.send_keys(contact)
    search_field.send_keys(Keys.ENTER)
    time.sleep(1)

def check_if_available_on_whatsap(contact):

    time.sleep(2)
    header_name = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')

    #convert html element to text (string)
    header_name_txt = header_name.text
    time.sleep(3)

    # extra check (if not used msg may sent more than one time to previous person)
    if contact == header_name_txt:
        time.sleep(1)
        return True

    else:

        return  False


def send_msg(msg):

    send_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    send_msg.click()
    time.sleep(1)

    # msg that will be send
    send_msg.send_keys(msg)
    time.sleep(1)
    enter_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    enter_button.click()
    time.sleep(1)


#Enter the msg here, that you want to send
#Make sure the format for multiple lines use
# """ Messege """ format 

msg = "!"


extract_contacts()
open_whatsap()
x=0
y=0

for contact in contacts:

    search_contact(contact)
    if (check_if_available_on_whatsap(contact)):
        send_msg(msg)
        print("Msg Sent to : " + contact)

        x=+1
        f = open("all_get_msg.txt", "a")
        f.write(contact)
        f.write("\n")
        f.close()

    else :
        print("Msg Not Sent to : " + contact)
        y = y+1

        f = open("all_not_get_msg.txt", "a")
        f.write(contact)
        f.write("\n")
        f.close()




time.sleep(1)
print ("Total Msg sent : ", x)
print ("Total Not Msg sent : ", y)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
driver.close()

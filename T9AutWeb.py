# Python selenium automation to login, get the title, url and contents of the web page
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
# using firefox for launching my website
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class SwagLabs:
    #Login Data for logging into web page
    userName_Value = "standard_user"
    passWord_Value = "secret_sauce"
    #Locator for each element
    username = "user-name"
    password = "password"
    button_id = "login-button"
    body_xpath = "/html/body"

    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #method for logging into web page
    def pageLogin(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            self.driver.find_element(by=By.ID,value=self.username).send_keys(self.userName_Value)
            sleep(2)
            self.driver.find_element(by=By.ID,value=self.password).send_keys(self.passWord_Value)
            sleep(2)
            self.driver.find_element(by=By.ID,value=self.button_id).click()
            return True
        except:
            return False
            print("Error")
    #method for getting web page details
    def urlDetails(self):
        title = self.driver.title
        curl = self.driver.current_url
        return title,curl

    #method for gettiing web page contents
    def getWebPage(self):
        webData = self.driver.find_element(By.XPATH,self.body_xpath).text
        file = open('Webpage_task_11.txt','w')
        file.write(webData)
        file.close()
        return True

    def shutdown(self):
        self.driver.quit()
        return None

if __name__ == "__main__":
    sl = SwagLabs("https://www.saucedemo.com/")
    sl.pageLogin()
    print(sl.urlDetails())
    sl.getWebPage()
    sl.shutdown()
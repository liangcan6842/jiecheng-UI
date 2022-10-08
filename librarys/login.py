from selenium.webdriver.common.by import By
class Login:
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element(By.XPATH,'//input[@placeholder="请输入您的用户名"]').send_keys(username)
        self.driver.find_element(By.XPATH,'//input[@placeholder="请输入您的密码"]').send_keys(password)
        self.driver.find_element(By.XPATH,'//span[text()="登录"]').click()

import pytest
from librarys.login import Login
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://jiecheng.admin.sauou.com/#/home")
login = Login(driver)
login.login("admin","123456")
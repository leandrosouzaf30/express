from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from time import sleep

def before_feature(context):
    driver = webdriver.Chrome(executable_path=r'../webdriver/chromedriver')

def after_feature(context):
    context.driver.quit()
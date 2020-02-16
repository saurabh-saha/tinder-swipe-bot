from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(10)
        
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        try:
            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
            popup_1.click()
            print('pop1done')

            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_2.click()
            print('pop2done')

            popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_3.click()
            print('pop3done')
        except Exception:
            pass

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                self.close_popup()
                # try:
                #     self.close_popup()
                # except Exception:
                #     self.close_match()

    def close_popup(self):
        try:
            waittime_div = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/span/div/div/div[1]/div')
            waitime = waittime_div.get_attribute('innerHTML')
            waitime = [int(i) for i in waitime.split(':')]
            mult = [3600, 60, 1]
            waitime = sum([i*j for i,j in zip(waitime, mult)])
            sleep(waitime)
            print('Plus clicked')
        except Exception:
            try:
                
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()



bot = TinderBot()
print('final page')
bot.login()

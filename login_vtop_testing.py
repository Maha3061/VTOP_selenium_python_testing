import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import tkinter as tk


class Vtoptest(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver for Firefox (you can use Chrome if preferred)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_home_page_title(self):
        driver = self.driver
        driver.get("https://vtop.vit.ac.in/vtop/open/page")
        self.assertIn("VTOP", driver.title)


    def test_home_page_elements(self):
        driver = self.driver
        driver.get("https://vtop.vit.ac.in/vtop/login")
        driver.fullscreen_window()
        try:
            # Use explicit wait to ensure the element is present
            logins = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]'))
            )
            self.assertTrue(logins)

            student_login = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, 'button'))
            )
            self.assertTrue(student_login.is_displayed())

            employee_login = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.TAG_NAME, 'button'))
            )
            self.assertTrue(employee_login.is_displayed())

            parent_login = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.TAG_NAME, 'button'))
            )
            self.assertTrue(parent_login.is_displayed())

            alumini_login = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.TAG_NAME, 'button'))
            )
            self.assertTrue(alumini_login.is_displayed())

        except Exception as e:
            page_source = driver.page_source
            print("Page Source:", page_source)  # Output page source for debugging
            self.fail("Home page elements not found within 10 seconds")

    def test_Student_LoginPage(self):
        driver = self.driver
        driver.get("https://vtop.vit.ac.in/vtop/login")
        self.assertIn("VTOP", driver.title)

        student=driver.find_element(By.XPATH,'//*[@id="stdForm"]/a/div/div[2]/button')
        student.click()

        elem_un = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        un = input('Enter username:')
        elem_un.send_keys(un)

        elem_pswd= WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        pwd = input('Enter Password:')
        elem_pswd.send_keys(pwd)

        cap = driver.find_element(By.ID, 'captchaStr')

        # cap.click()
        if cap.is_displayed():
            captcha = input('Enter captcha:')
            cap.send_keys(captcha)

        sub=driver.find_element(By.ID,'submitBtn')
        sub.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )
        self.assertNotIn("No results found.", driver.page_source)

    def test_Employee_LoginPage(self):
        driver = self.driver
        driver.get("https://vtop.vit.ac.in/vtop/login")

        self.assertIn("VTOP", driver.title)

        employee=driver.find_element(By.XPATH,'//*[@id="empForm"]/a/div/div[2]/button')
        employee.click()

        elem_un = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        un = getpass('Enter username:')
        elem_un.send_keys(un)

        elem_pswd= WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        pwd = getpass('Enter Password:')
        elem_pswd.send_keys(pwd)

        sub=driver.find_element(By.ID,'submitBtn')
        sub.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )
        self.assertNotIn("No results found.", driver.page_source)

    def test_Parent_LoginPage(self):
        driver = self.driver
        driver.get("https://vtop.vit.ac.in/vtop/login")
        self.assertIn("VTOP", driver.title)

        parent = driver.find_element(By.XPATH, '//*[@id="parentForm"]/a/div/div[2]/button')
        parent.click()

        elem_un = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        un = getpass('Enter username:')
        elem_un.send_keys(un)

        elem_pswd = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        pwd = getpass('Enter DOB:')
        elem_pswd.send_keys(pwd)

        elem_phno = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "otpFieldId"))
        )
        # elem_phno.click()
        pwd = getpass('Enter mobile number:')
        elem_phno.send_keys(pwd)

        cap=WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID,'captchaStr'))
        )
        # cap.click()
        captcha = getpass('Enter captcha:')
        cap.send_keys(captcha)

        sub = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bodyContent"]/form/div[6]/button'))
        )
        sub.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
VTOP Test Automation

This repository contains a set of automated tests for the VTOP website using Selenium and Python's unittest framework. These tests cover various login scenarios for different user types including students, employees, and parents.

Table of Contents

•	Installation

•	Usage

•	Test Cases:

  >	Home Page Title

  >	Home Page Elements

  >	Student Login Page

  >	Employee Login Page

  >	Parent Login Page

•	Installation


1)	Clone the repository:
   
  sh

  git clone https://github.com/yourusername/vtop-test-automation.git

3)	Navigate to the project directory:
   
  sh
  
  cd vtop-test-automation
  
5)	Install the required packages:
   
  sh
  
  pip install -r requirements.txt
  
7)	Usage
   
  To run the tests, execute the following command:
  
  sh
  
  python -m unittest vtop_test.py
  
  Ensure that you have the appropriate WebDriver installed and available in your system's PATH. The script uses the Chrome WebDriver by default. You can download it from here.


Test Cases


->	Home Page Title

  >	Purpose: Verify that the home page title contains "VTOP".
  
  >	Test Method: test_home_page_title
  
  >	Steps:

    •	Navigate to the VTOP home page.
    •	Check if the title contains "VTOP".


->	Home Page Elements

  >	Purpose: Verify the presence of login buttons for different user types on the home page.
  
  >	Test Method: test_home_page_elements
  
  >	Steps:
  
    •	Navigate to the VTOP login page.
    •	Verify the presence of login buttons for student, employee, parent, and alumni.


->	Student Login Page

  >	Purpose: Test the login functionality for students.
  
  >	Test Method: test_Student_LoginPage
  
  >	Steps:
  
    •	Navigate to the VTOP login page.
    •	Click on the student login button.
    •	Enter username, password, and captcha.
    •	Verify successful login by checking for specific content on the landing page.


->	Employee Login Page

  >	Purpose: Test the login functionality for employees.
  
  >	Test Method: test_Employee_LoginPage
  
  >	Steps:
  
    •	Navigate to the VTOP login page.
    •	Click on the employee login button.
    •	Enter username, password, and captcha.
    •	Verify successful login by checking for specific content on the landing page.


->	Parent Login Page

  >	Purpose: Test the login functionality for parents.
  
  >	Test Method: test_Parent_LoginPage
  
  >	Steps:
  
    •	Navigate to the VTOP login page.
    •	Click on the parent login button.
    •	Enter username, date of birth, mobile number, and captcha.
    •	Verify successful login by checking for specific content on the landing page.

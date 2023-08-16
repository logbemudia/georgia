#amazon search file

 create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\lilia\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert actual_text == expected_text, F'Expected{expected_text} but you got a{actual_text}'

#verify legal text
driver.find_element(By.ID, 'ap_email')

#verify legal text.
expected_text ="Conditions of Use and Privacy Notice"
actual_text = driver.find_element(By.ID, 'legalTextRow').text

#to verify actual result if diffferent from expected result
assert actual_text

assert actual_text == expected_text, f'Expected{expected_text} but you got a{actual_text}'

driver.quit()

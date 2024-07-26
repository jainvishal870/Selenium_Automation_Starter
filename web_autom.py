from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options= chrome_options)
browser.get("https://techstepacademy.com/trial-of-the-stones")

#first quiz
riddle_input_one_path = "input[id='r1Input']"
Input1element = browser.find_element(By.CSS_SELECTOR, riddle_input_one_path)
Input1element.send_keys("ROCK")
answer_button_one = "button[id='r1Btn']"
submit_answer_first = browser.find_element(By.CSS_SELECTOR, answer_button_one).click()

#riddle_one_answer_element = browser.find_element(By.CSS_SELECTOR, "#passwordBanner h4")
riddle_one_answer_element = browser.find_element(By.XPATH, "//div[@id='passwordBanner']/h4")
riddle_one_answer = riddle_one_answer_element.text


#Second quiz
riddle_input_two_path = "input[id='r2Input']"
Input2element = browser.find_element(By.CSS_SELECTOR, riddle_input_two_path)
Input2element.send_keys(riddle_one_answer)
answer_button_two = "button[id='r2Butn']"
submit_answer_second = browser.find_element(By.CSS_SELECTOR, answer_button_two).click()

riddle_two_answer_element = browser.find_element(By.XPATH, "//div[@id='successBanner1']/h4")
riddle_two_answer = riddle_two_answer_element.text

assert riddle_two_answer == "Success!"

#Merchants data

richest_merchant_name = browser.find_element(By.XPATH,"//p[text()='3000']/../span")
richest_merchant_input = browser.find_element(By.CSS_SELECTOR, "input[id='r3Input']")
richest_merchant_input.send_keys(richest_merchant_name.text)
answer_button_three = "button[id='r3Butn']"
submit_answer_three = browser.find_element(By.CSS_SELECTOR, answer_button_three).click()

#Check Answers

check_answers_btn =  browser.find_element(By.CSS_SELECTOR, "button[id='checkButn']" ).click()
final_answer_element = browser.find_element(By.CSS_SELECTOR, "div[id='trialCompleteBanner']>h4")

final_answer_text = final_answer_element.text

assert final_answer_text == "Trial Complete"







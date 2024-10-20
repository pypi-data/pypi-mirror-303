from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
import pytz
import requests

#Chegg_Management_Bot
troubleshooting_bot_token = '7972332699:AAHs1ZGYQFXRtVELFou8zZ08IrWAE__cDRc'
troubleshooting_chatID =  '6966110728'


def telegram_bot_sendtext(bot_message, bot_token, bot_chatID):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + str(bot_message).replace('.', '\\.')  # Escape the dot character
    response = requests.get(send_text)
    return response.json()

def login_to_chegg(username, password,driver):
    try:


        # Open the Chegg website and log in
        driver.get("https://expert.chegg.com/auth")
        time.sleep(3)

        #print(driver.find_element(By.XPATH, "/html/body").text)

        # Username
        element = driver.find_element(By.XPATH, "/html/body/div/main/section/div/div/div/form/div[1]/div/div[1]/div/input")  # Replace with the correct XPath
        element.send_keys(username)
        #element.send_keys(Keys.ENTER)
        time.sleep(3)

        # Password
        passw = driver.find_element(By.XPATH, "/html/body/div/main/section/div/div/div/form/div[1]/div/div[2]/div/input")  # Replace with the correct XPath
        passw.send_keys(password)
        passw.send_keys(Keys.ENTER)
        time.sleep(3)
        # if login is succesfull, it sets flag to false and exits loop, thus exiting the function 
        return False
    except Exception as e:
        # if login is unsuccesfull, it sets flag to True and comtinues loop, and send notification thus exiting the function
        telegram_bot_sendtext("Login Failed \\- error in page",troubleshooting_bot_token,troubleshooting_chatID)
        return True



def refresh_chegg(driver,accept_option,start_time,end_time,user_bot_token,user_bot_chatID,account_name):
    limit_texts = f"Limit hit on {account_name}"
    question_texts = f"Question found on {account_name}"



    # Navigate to the authoring page
    driver.get("https://expert.chegg.com/qna/authoring/answer")
    time.sleep(3)
    while True:

        driver.get("https://expert.chegg.com/qna/authoring/answer")
        time.sleep(3)
        limit = driver.current_url
        limit_text = f"{limit}"

        if limit_text != "https://expert.chegg.com/qna/authoring/answer":
            time.sleep(3)
            driver.get("https://expert.chegg.com/qna/authoring/answer")
            time.sleep(3)
            limit = driver.current_url
            limit_text = f"{limit}"
            if limit_text != "https://expert.chegg.com/qna/authoring/answer":
                time.sleep(3)
                driver.get("https://expert.chegg.com/qna/authoring/answer")
                time.sleep(3)
                limit = driver.current_url
                limit_text = f"{limit}"
                if limit_text != "https://expert.chegg.com/qna/authoring/answer":
                    time.sleep(3)
                    driver.get("https://expert.chegg.com/qna/authoring/answer")
                    time.sleep(3)
                    limit = driver.current_url
                    limit_text = f"{limit}"

                    # Define the time zone (UTC+5:30)
                    tz = pytz.timezone('Asia/Kolkata')
                    # Get the current time in UTC+5:30
                    now = datetime.now(tz)
                    # Define the target time (12:30 PM)
                    target_time = now.replace(hour=12, minute=30, second=0, microsecond=0)
                    # If the current time is already past 12:30 PM, set the target time to the next day
                    if now > target_time:
                        target_time += timedelta(days=1)
                    # Calculate the difference in seconds
                    n = (target_time - now).total_seconds()
                    telegram_bot_sendtext(limit_texts)
                    time.sleep(n)

        driver.get("https://expert.chegg.com/qna/authoring/answer")
        time.sleep(5)
        message = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[2]/div[1]")
        text_to_copy = message.text

        if text_to_copy == "Thank you for your efforts on Chegg Q&A! Unfortunately, no Qs are available in your queue at the moment.":
            driver.refresh()
            
        else:
            #Teleram of User
            telegram_bot_sendtext(question_texts,user_bot_token,user_bot_chatID)
            if(accept_option):
                try:
                    # Check if the submit button is present
                    submit_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/footer/div/div[1]/div[2]/button/span/span[1]"))
                    )

                    # Get the text of the button
                    button_text = submit_button.text
                    #print(button_text)

                    # Proceed only if the button text is "Start Solving"
                    if button_text == "Start Solving":
                        try:
                            # Try clicking the button
                            submit_button.click()
                            #print(f"Accepted")
                        except ElementClickInterceptedException:
                            #print("Element is not clickable due to an overlay, using JavaScript click")
                            # Fallback: click using JavaScript
                            driver.execute_script("arguments[0].click();", submit_button)
                            #print("Clicked using JavaScript")

                    else:
                        #print(f"Button text is not 'SUBMIT'. It's '{button_text}'.")
                        driver.refresh()

                except (NoSuchElementException, TimeoutException):
                    #print("Button not found, refreshing.")
                    driver.refresh()
                except Exception as e:
                    time.sleep(1)
                    driver.refresh()
                    time.sleep(1)
            time.sleep(720)
            driver.refresh()


        # Define the time zone (UTC+5:30)
        tz = pytz.timezone('Asia/Kolkata')
        # Get the current time in UTC+5:30
        now = datetime.now(tz)
        current_hour = now.hour        
        if not (start_time <= current_hour < end_time):
            #print("OT")
            break
    # Quit the WebDriver
    driver.quit()

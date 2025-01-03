from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    
    text_to_type = (
        "Patient complains of neuropathic pain in the legs. He has a history of plantar fasciitis. "
        "The right foot and leg are worse. He can't walk more than 10 feet before onset of pain and weakness. "
        "He's also experiencing some dizziness as well with the tingling in the extremities. "
        "He has not seen a neurologist. Patient has history of hepatic encephalopathy. "
        "Patient is also following up after seeing the gastroenterologist. Dr. Gastro performed an endoscopy on him "
        "which was normal. Symptoms of nausea and vomiting have resolved. "
        "Patient is undergoing dialysis for end stage renal disease. "
        "Counseled patient on when to take his medications."
    )

    
    delay_per_word = 60 / 102  
    
    try:
        driver.get("https://school.keyhero.com/typing/")
        
        # Log in with username and password
        username_field = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
        password_field = driver.find_element(By.ID, "id_password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys("") #input username
        password_field.send_keys("") #input password
        login_button.click()

        
        print("Please navigate to the typing test page and place the cursor in the typing area...")
        time.sleep(8)

        
        print("Typing text...")
        for word in text_to_type.split():
            webdriver.ActionChains(driver).send_keys(word).send_keys(Keys.SPACE).perform()
            time.sleep(delay_per_word) 

        print("Typing completed.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        time.sleep(5)  
        driver.quit()

if __name__ == "__main__":
    main()

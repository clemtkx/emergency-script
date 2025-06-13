from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, ElementClickInterceptedException
import time

# Step 1: Open browser and go to NHS 111 triage start page
def step_1():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://111.nhs.uk/Location/TriageStart")
    
    # Minimize the window after initial page load
    try:
        driver.minimize_window()
    except Exception:
        pass  # Some platforms may not support minimization
    
    print("Step 1 completed: Browser opened and navigated to triage start page.")
    return driver

# Step 2: Fill in postcode and click Next
def step_2(driver):
    wait = WebDriverWait(driver, 10)
    
    # Fill postcode with retry logic
    for attempt in range(3):
        try:
            postcode_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='postcode-input']")))
            postcode_input.clear()
            postcode_input.send_keys('PL53PY')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 2 completed: Postcode entered and Next button clicked.")

# Step 3: Fill in age and click Next
def step_3(driver):
    wait = WebDriverWait(driver, 10)
    
    # Fill age with retry logic
    for attempt in range(3):
        try:
            age_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='age-input']")))
            age_input.clear()
            age_input.send_keys('34')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 3 completed: Age entered and Next button clicked.")

# Step 4: Select Female and click Next
def step_4(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click Female label with retry logic
    for attempt in range(3):
        try:
            female_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='Female-label']")))
            female_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 4 completed: Selected 'Female' and clicked Next.")

# Step 5: Click 'Head, face and neck' link
def step_5(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click category link with retry logic
    for attempt in range(3):
        try:
            category_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-title='Head, face and neck']")))
            category_link.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 5 completed: Clicked 'Head, face and neck' category link.")

# Step 6: Click 'Fluid or wax coming from the ear with no loss of hearing' link
def step_6(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click pathway link with retry logic
    for attempt in range(3):
        try:
            pathway_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-title='Fluid or wax coming from the ear with no loss of hearing']")))
            pathway_link.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 6 completed: Clicked 'Fluid or wax coming from the ear with no loss of hearing' link.")

# Step 7: Click 'I understand' button
def step_7(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click I understand button with retry logic
    for attempt in range(3):
        try:
            understand_button = wait.until(EC.element_to_be_clickable((By.ID, "nextScreen")))
            understand_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 7 completed: Clicked 'I understand' button.")

# Step 8: Click 'No' (answer 1) label and Next button
def step_8(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-1']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    time.sleep(1)  # Brief pause as in original
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 8 completed: Clicked 'No' (answer 1) label and Next button.")

# Step 9: Click 'No' (answer 2) label and Next button
def step_9(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-2']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 9 completed: Clicked 'No' (answer 2) label and Next button.")

# Step 10: Click 'I'm not sure' (answer 1) label and Next button
def step_10(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-1']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 10 completed: Clicked 'I'm not sure' (answer 1) label and Next button.")

# Step 11: Click 'No - I feel well enough to do most of my usual daily activities' (answer 2) label and Next button
def step_11(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-2']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 11 completed: Clicked 'No - I feel well enough to do most of my usual daily activities' (answer 2) label and Next button.")

# Step 12: Click 'No' (answer 2) label and Next button
def step_12(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-2']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 12 completed: Clicked 'No' (answer 2) label and Next button.")

# Step 13: Click 'No' (answer 2) label and Next button
def step_13(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-2']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 13 completed: Clicked 'No' (answer 2) label and Next button.")

def step_14(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-2']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 14 completed: Clicked 'No' (answer 2) label and Next button.")

def step_15(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-3']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 15 completed: Clicked 'No' (answer 3) label and Next button.")

def step_16(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-2']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 16 completed: Clicked 'No' (answer 2) label and Next button.")

def step_17(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click answer label with retry logic
    for attempt in range(3):
        try:
            answer_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='answer-2']")))
            answer_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 17 completed: Clicked 'No' (answer 2) label and Next button.")

# Step 18: Click 'Refer me to a pharmacist' link
def step_18(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click pharmacist referral link with retry logic
    for attempt in range(3):
        try:
            referral_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-test-id='action-link-text']")))
            referral_link.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 18 completed: Clicked 'Refer me to a pharmacist' link.")

# Step 19: Click 'Honicknowle Pharmacy' button
def step_19(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click pharmacy button with retry logic
    for attempt in range(3):
        try:
            pharmacy_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='start-referral']")))
            pharmacy_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 19 completed: Clicked 'Honicknowle Pharmacy' button.")

def step_20(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click informant type label with retry logic
    for attempt in range(3):
        try:
            informant_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='informant-type-self-label']")))
            informant_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 20 completed: Clicked 'Me' label and Next button.")

def step_21(driver):
    wait = WebDriverWait(driver, 10)
    
    # Fill forename with retry logic
    for attempt in range(3):
        try:
            forename_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='patient-forename-input']")))
            forename_input.clear()
            forename_input.send_keys('clement')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Fill surname with retry logic
    for attempt in range(3):
        try:
            surname_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='patient-surname-input']")))
            surname_input.clear()
            surname_input.send_keys('tan')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 21 completed: Entered forename and surname, then clicked Next button.")

def step_22(driver):
    wait = WebDriverWait(driver, 10)
    
    # Fill day with retry logic
    for attempt in range(3):
        try:
            day_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='dob-day-input']")))
            day_input.clear()
            day_input.send_keys('14')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Fill month with retry logic
    for attempt in range(3):
        try:
            month_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='dob-month-input']")))
            month_input.clear()
            month_input.send_keys('5')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Fill year with retry logic
    for attempt in range(3):
        try:
            year_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='dob-year-input']")))
            year_input.clear()
            year_input.send_keys('1991')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 22 completed: Entered DOB and clicked Next button.")

def step_23(driver):
    wait = WebDriverWait(driver, 10)
    
    # Fill telephone with retry logic
    for attempt in range(3):
        try:
            phone_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='telephonenumber-input']")))
            phone_input.clear()
            phone_input.send_keys('01752773335')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 23 completed: Entered telephone number and clicked Next button.")

def step_24(driver):
    wait = WebDriverWait(driver, 10)
    
    # Scroll down slightly before clicking address button
    driver.execute_script("window.scrollBy(0, 200);")
    
    # Click address button with retry logic
    for attempt in range(3):
        try:
            address_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='address-option-button']")))
            address_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 24 completed: Clicked address option for Honicknowle Pharmacy.")

def step_25(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click home address label with retry logic
    for attempt in range(3):
        try:
            home_address_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='home-address-no-label']")))
            home_address_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 25 completed: Clicked 'No' for home address and Next button.")

def step_26(driver):
    wait = WebDriverWait(driver, 10)
    
    # Fill home postcode with retry logic
    for attempt in range(3):
        try:
            postcode_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test-id='home-postcode-input']")))
            postcode_input.clear()
            postcode_input.send_keys('ex20ad')
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 26 completed: Entered home postcode and clicked Next button.")

def step_27(driver):
    wait = WebDriverWait(driver, 10)
    
    # Click none label with retry logic
    for attempt in range(3):
        try:
            none_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[data-test-id='none-label']")))
            none_label.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    # Click Next button with retry logic
    for attempt in range(3):
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test-id='next-button']")))
            next_button.click()
            break
        except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
            if attempt == 2:
                raise
            time.sleep(0.5)
    
    print("Step 27 completed: Clicked 'None of these, I'll make a note myself' and Next button.")

def step_28(driver):
    # Maximize the window before final step for user review
    try:
        driver.maximize_window()
    except Exception:
        pass
    
    print("Step 28 completed: Browser maximized for user review. Script finished, browser remains open.")
    input("Press Enter to exit and close the browser...")
    driver.quit()

if __name__ == "__main__":
    driver = step_1()
    step_2(driver)
    step_3(driver)
    step_4(driver)
    step_5(driver)
    step_6(driver)
    step_7(driver)
    step_8(driver)
    step_9(driver)
    step_10(driver)
    step_11(driver)
    step_12(driver)
    step_13(driver)
    step_14(driver)
    step_15(driver)
    step_16(driver)
    step_17(driver)
    step_18(driver)
    step_19(driver)
    step_20(driver)
    step_21(driver)
    step_22(driver)
    step_23(driver)
    step_24(driver)
    step_25(driver)
    step_26(driver)
    step_27(driver)
    step_28(driver)

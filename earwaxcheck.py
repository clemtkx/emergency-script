from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# Step 1: Open browser and go to NHS 111 triage start page
def step_1():
    chrome_options = Options()
    # Do not minimize for debugging; keep browser visible
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://111.nhs.uk/Location/TriageStart")
    print("Step 1 completed: Browser opened and navigated to triage start page.")
    return driver

# Utility for robust click/send_keys with staleness retry
def robust_action(driver, by, selector, action, value=None):
    for attempt in range(3):
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((by, selector))
            )
            if action == 'click':
                elem.click()
            elif action == 'send_keys' and value is not None:
                elem.clear()
                elem.send_keys(value)
            return
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

def wait_between_steps():
    pass  # No wait needed now

# Step 2: Fill in postcode and click Next
def step_2(driver):
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='postcode-input']", 'send_keys', 'PL53PY')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 2 completed: Postcode entered and Next button clicked.")
    wait_between_steps()

# Step 3: Fill in age and click Next
def step_3(driver):
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='age-input']", 'send_keys', '34')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 3 completed: Age entered and Next button clicked.")
    wait_between_steps()

# Step 4: Select Female and click Next
def step_4(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='Female-label']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 4 completed: Selected 'Female' and clicked Next.")
    wait_between_steps()

# Step 5: Click 'Head, face and neck' link
def step_5(driver):
    robust_action(driver, By.CSS_SELECTOR, "a[data-title='Head, face and neck']", 'click')
    print("Step 5 completed: Clicked 'Head, face and neck' category link.")
    wait_between_steps()

# Step 6: Click 'Fluid or wax coming from the ear with no loss of hearing' link
def step_6(driver):
    robust_action(driver, By.CSS_SELECTOR, "a[data-title='Fluid or wax coming from the ear with no loss of hearing']", 'click')
    print("Step 6 completed: Clicked 'Fluid or wax coming from the ear with no loss of hearing' link.")
    wait_between_steps()

# Step 7: Click 'I understand' button
def step_7(driver):
    robust_action(driver, By.ID, "nextScreen", 'click')
    print("Step 7 completed: Clicked 'I understand' button.")
    wait_between_steps()

# Step 8: Click 'No' (answer 1) label and Next button
def step_8(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-1']", 'click')
    time.sleep(1)
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 8 completed: Clicked 'No' (answer 1) label and Next button.")
    wait_between_steps()

# Step 9: Click 'No' (answer 2) label and Next button
def step_9(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-2']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 9 completed: Clicked 'No' (answer 2) label and Next button.")
    wait_between_steps()

# Step 10: Click 'I'm not sure' (answer 1) label and Next button
def step_10(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-1']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 10 completed: Clicked 'I'm not sure' (answer 1) label and Next button.")
    wait_between_steps()

# Step 11: Click 'No - I feel well enough to do most of my usual daily activities' (answer 2) label and Next button
def step_11(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-2']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 11 completed: Clicked 'No - I feel well enough to do most of my usual daily activities' (answer 2) label and Next button.")
    wait_between_steps()

# Step 12: Click 'No' (answer 2) label and Next button
def step_12(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-2']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 12 completed: Clicked 'No' (answer 2) label and Next button.")
    wait_between_steps()

# Step 13: Click 'No' (answer 2) label and Next button
def step_13(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-2']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 13 completed: Clicked 'No' (answer 2) label and Next button. Browser left open for user review.")
    wait_between_steps()

def step_14(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-2']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 14 completed: Clicked 'No' (answer 2) label and Next button.")
    wait_between_steps()

def step_15(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-3']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 15 completed: Clicked 'No' (answer 3) label and Next button.")
    wait_between_steps()

def step_16(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-2']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 16 completed: Clicked 'No' (answer 2) label and Next button.")
    wait_between_steps()

def step_17(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='answer-2']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 17 completed: Clicked 'No' (answer 2) label and Next button.")
    wait_between_steps()

# Step 18: Click 'Refer me to a pharmacist' link
def step_18(driver):
    robust_action(driver, By.CSS_SELECTOR, "span[data-test-id='action-link-text']", 'click')
    print("Step 18 completed: Clicked 'Refer me to a pharmacist' link.")
    wait_between_steps()

# Step 19: Click 'Honicknowle Pharmacy' button
def step_19(driver):
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='start-referral']", 'click')
    print("Step 19 completed: Clicked 'Honicknowle Pharmacy' button. Automation finished, browser left open for review.")
    wait_between_steps()

def step_20(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='informant-type-self-label']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 20 completed: Clicked 'Me' label and Next button.")
    wait_between_steps()

def step_21(driver):
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='patient-forename-input']", 'send_keys', 'clement')
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='patient-surname-input']", 'send_keys', 'tan')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 21 completed: Entered forename and surname, then clicked Next button.")
    wait_between_steps()

def step_22(driver):
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='dob-day-input']", 'send_keys', '14')
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='dob-month-input']", 'send_keys', '5')
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='dob-year-input']", 'send_keys', '1991')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 22 completed: Entered DOB and clicked Next button.")
    wait_between_steps()

def step_23(driver):
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='telephonenumber-input']", 'send_keys', '01752773335')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 23 completed: Entered telephone number and clicked Next button.")
    wait_between_steps()

def step_24(driver):
    # Scroll down slightly before clicking address button
    driver.execute_script("window.scrollBy(0, 200);")
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='address-option-button']", 'click')
    print("Step 24 completed: Clicked address option for Honicknowle Pharmacy.")
    wait_between_steps()

def step_25(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='home-address-no-label']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 25 completed: Clicked 'No' for home address and Next button.")
    wait_between_steps()

def step_26(driver):
    robust_action(driver, By.CSS_SELECTOR, "input[data-test-id='home-postcode-input']", 'send_keys', 'ex20ad')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 26 completed: Entered home postcode and clicked Next button.")
    wait_between_steps()

def step_27(driver):
    robust_action(driver, By.CSS_SELECTOR, "label[data-test-id='none-label']", 'click')
    robust_action(driver, By.CSS_SELECTOR, "button[data-test-id='next-button']", 'click')
    print("Step 27 completed: Clicked 'None of these, I'll make a note myself' and Next button.")
    wait_between_steps()

def step_28(driver):
    driver.maximize_window()
    print("Step 28 completed: Browser maximized for user review. Script finished, browser remains open.")
    input("Press Enter to exit and close the browser...")

# Debugging utility to print all radio button labels and their attributes
def print_radio_button_labels(driver):
    labels = driver.find_elements(By.CSS_SELECTOR, "label.nhsuk-label.nhsuk-radios__label")
    for lbl in labels:
        print(
            f"Label: for={lbl.get_attribute('for')}, "
            f"data-test-id={lbl.get_attribute('data-test-id')}, "
            f"text='{lbl.text.strip()}'"
        )

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
    print("Automation completed. Browser is open for user review.")
    input("Press Enter to exit and close the browser...")
    driver.quit()

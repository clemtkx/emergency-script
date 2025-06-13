from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Step 1: Fill postcode and click Next

def step_1(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="postcode-input"]'))).clear()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="postcode-input"]'))).send_keys("PL53PY")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="age-input"]')))
            print("Step 1 completed: Postcode entered and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 2: Fill age and click Next

def step_2(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="age-input"]'))).clear()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="age-input"]'))).send_keys("34")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[data-test-id="Female-label"]')))
            print("Step 2 completed: Age entered and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 3: Select Female and click Next

def step_3(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="Female-label"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-test-id="category-title"][data-title="Blood pressure problems"]')))
            print("Step 3 completed: Female selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 4: Click 'Blood pressure problems' category link

def step_4(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test-id="category-title"][data-title="Blood pressure problems"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.nhsuk-u-font-weight-bold[data-title="Blood pressure problems"]')))
            print("Step 4 completed: Blood pressure problems category clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 5: Click 'Blood pressure problems' triage pathway link

def step_5(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nhsuk-u-font-weight-bold[data-title="Blood pressure problems"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer"][data-test-id="answer-0"]')))
            print("Step 5 completed: Blood pressure problems pathway clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 6: Click 'High' label and Next button

def step_6(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer"][data-test-id="answer-0"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer"][data-test-id="answer-0"]')))
            print("Step 6 completed: High selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 7: Click 'Yes' label and Next button

def step_7(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer"][data-test-id="answer-0"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.nhsuk-button[role="button"][data-module="nhsuk-button"]')))
            print("Step 7 completed: Yes selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 8: Click 'Next' button (as a link)

def step_8(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nhsuk-button[role="button"][data-module="nhsuk-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.nhsuk-u-font-weight-bold[data-title="Headache or migraine"]')))
            print("Step 8 completed: Next link clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 9: Click 'Headache or migraine' pathway link

def step_9(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nhsuk-u-font-weight-bold[data-title="Headache or migraine"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button#nextScreen.button--next')))
            print("Step 9 completed: Headache or migraine pathway clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 10: Click 'I understand' button

def step_10(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#nextScreen.button--next'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_1"][data-test-id="answer-1"]')))
            print("Step 10 completed: I understand button clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 11: Click 'No' (SelectedAnswer_1) label and Next button

def step_11(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_1"][data-test-id="answer-1"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 11 completed: No (1) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 12: Click 'No' (SelectedAnswer_2) label and Next button

def step_12(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 12 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 13: Click 'No' (SelectedAnswer_2) label and Next button

def step_13(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_3"][data-test-id="answer-3"]')))
            print("Step 13 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 14: Click 'No' (SelectedAnswer_3) label and Next button

def step_14(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_3"][data-test-id="answer-3"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 14 completed: No (3) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 15: Click 'No' (SelectedAnswer_2) label and Next button

def step_15(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 15 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 16: Click 'No - I feel well enough to do most of my usual daily activities' label and Next button

def step_16(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_4"][data-test-id="answer-4"]')))
            print("Step 16 completed: No (2, feel well) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 17: Click 'No' (SelectedAnswer_4) label and Next button

def step_17(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_4"][data-test-id="answer-4"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 17 completed: No (4) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 18: Click 'No' (SelectedAnswer_2) label and Next button

def step_18(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 18 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 19: Click 'No' (SelectedAnswer_2) label and Next button

def step_19(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 19 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 20: Click 'I'm not sure' label and Next button (amended as per user)

def step_20(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_3"][data-test-id="answer-3"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label.nhsuk-label.nhsuk-radios__label')))
            print("Step 20 completed: I'm not sure selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 21: Click 'No' (SelectedAnswer_2) label and Next button

def step_21(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 21 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 22: Click 'No' (SelectedAnswer_2) label and Next button

def step_22(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 22 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 23: Click 'No' (SelectedAnswer_2) label and Next button

def step_23(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 23 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 24: Click 'No' (SelectedAnswer_2) label and Next button

def step_24(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 24 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 25: Click 'No' (SelectedAnswer_2) label and Next button

def step_25(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 25 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 26: Click 'No' (SelectedAnswer_2) label and Next button

def step_26(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="SelectedAnswer_2"][data-test-id="answer-2"]')))
            print("Step 26 completed: No (2) selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 27: Click 'No' (SelectedAnswer_2) label and Next button (corrected as per user)

def step_27(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer"][data-test-id="answer-0"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            print("Step 27 completed: 'I've been diagnosed with high blood pressure' selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 28: Click 'Refer me to a pharmacist' link

def step_28(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-test-id="action-link-text"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="start-referral"]')))
            print("Step 28 completed: Refer me to a pharmacist clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 29: Click 'Honicknowle Pharmacy' button

def step_29(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="start-referral"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="informant-type-self-label"]')))
            print("Step 29 completed: Honicknowle Pharmacy button clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 30: Select 'Me' and click Next

def step_30(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="informant-type-self-label"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="patient-forename-input"]')))
            print("Step 30 completed: Me selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 31: Fill in patient details and click Next

def step_31(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="patient-forename-input"]'))).send_keys("clement")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="patient-surname-input"]'))).send_keys("tan")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="dob-day-input"]')))
            print("Step 31 completed: Forename and surname entered and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 32: Fill in DOB and click Next

def step_32(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="dob-day-input"]'))).send_keys("14")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="dob-month-input"]'))).send_keys("5")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="dob-year-input"]'))).send_keys("1991")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="telephonenumber-input"]')))
            print("Step 32 completed: DOB entered and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 33: Fill in telephone number and click Next

def step_33(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="telephonenumber-input"]'))).send_keys("01752773335")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="address-option-button"]')))
            print("Step 33 completed: Telephone number entered and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 34: Click address option button

def step_34(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="address-option-button"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="home-address-no-label"]')))
            print("Step 34 completed: Address option button clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 35: Select home address 'No' and click Next

def step_35(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="home-address-no-label"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="home-postcode-input"]')))
            print("Step 35 completed: Home address 'No' selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 36: Enter home postcode and click Next

def step_36(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test-id="home-postcode-input"]'))).send_keys("ex20ad")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"][name="changeHomeAddressPostcode"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="none-label"]')))
            print("Step 36 completed: Home postcode entered and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

# Step 37: Click 'None of these' label and Next button

def step_37(driver):
    wait = WebDriverWait(driver, 10)
    for attempt in range(3):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="none-label"]'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))).click()
            print("Step 37 completed: None of these selected and Next clicked.")
            break
        except StaleElementReferenceException:
            if attempt == 2:
                raise
            continue

def main():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    driver.get("https://111.nhs.uk/Location/TriageStart")
    step_1(driver)
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
    step_29(driver)
    step_30(driver)
    step_31(driver)
    step_32(driver)
    step_33(driver)
    step_34(driver)
    step_35(driver)
    step_36(driver)
    step_37(driver)
    driver.maximize_window()
    print("All steps completed. Browser remains open.")
    while True:
        pass

if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import datetime
import time  # if not already imported

def run_emergency_script(gender, forename, surname, dob_day, dob_month, dob_year, home_postcode, progress_callback=None):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # Hide automation indicators
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    # Add random delay to seem more human
    import random
    time.sleep(random.uniform(1, 3))
    
    driver.get("https://111.nhs.uk/guided-entry/medicines-help")
    
    wait = WebDriverWait(driver, 15)
    
    # Immediately minimize the window to hide steps 3-21 from view.
    driver.minimize_window()
    
    # --- Step 3: Example: Select Emergency Prescription radio ---
    try:
        emergency_label = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedValue-1"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", emergency_label)
        emergency_label.click()
        if progress_callback:
            progress_callback(3)
        print("Step 3 completed: Emergency Prescription selected.")
    except Exception as e:
        print("Could not select Emergency Prescription radio:", e)
        print(driver.page_source)
        return

    # --- Step 4: Click Next button ---
    try:
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(4)
        print("Step 4 completed: Next button clicked.")
    except Exception as e:
        print("Could not click Next button:", e)
        return

    # --- Step 5: Click the 'Start now' button ---
    try:
        start_now = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test-id="start-triage-link"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", start_now)
        start_now.click()
        if progress_callback:
            progress_callback(5)
        print("Step 5 completed: Start now clicked.")
    except Exception as e:
        print("Could not click Start now:", e)
        return

    # --- Step 6: Click 'I have none of these' ---
    try:
        none_of_these = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test-id="i-have-none-of-these-link"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", none_of_these)
        none_of_these.click()
        if progress_callback:
            progress_callback(6)
        print("Step 6 completed: 'I have none of these' clicked.")
    except Exception as e:
        print("Could not click 'I have none of these':", e)
        return

    # --- Step 7: Select 'Me' and click Next ---
    try:
        me_label = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="InformantType"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", me_label)
        me_label.click()
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(7)
        print("Step 7 completed: 'Me' selected and Next clicked.")
    except Exception as e:
        print("Could not select 'Me' or click Next:", e)
        print(driver.page_source)
        return

    # --- Step 8: Fill postcode and click Next ---
    try:
        postcode_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="postcode-input"][id="CurrentPostcode"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", postcode_input)
        postcode_input.clear()
        postcode_input.send_keys("PL5 3PY")
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(8)
        print("Step 8 completed: Postcode filled and Next clicked.")
    except Exception as e:
        print("Could not fill postcode or click Next:", e)
        print(driver.page_source)
        return

    # --- Step 9: Fill age and click Next ---
    try:
        # Calculate age from DOB inputs
        dob = datetime.date(int(dob_year), int(dob_month), int(dob_day))
        today = datetime.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        age_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="age-input"][id="UserInfo_Age_Age"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", age_input)
        age_input.clear()
        age_input.send_keys(str(age))  # Use the calculated age
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(9)
        print("Step 9 completed: Age (" + str(age) + ") filled and Next clicked.")
    except Exception as e:
        print("Could not fill age or click Next:", e)
        print(driver.page_source)
        return

    # --- Step 10: Select gender and click Next ---
    try:
        if gender.lower() == "male":
            gender_selector = 'label[for="UserInfo_Gender-1"]'
        else:
            gender_selector = 'label[for="UserInfo_Gender"]'
        gender_label = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, gender_selector))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", gender_label)
        gender_label.click()
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(10)
        print("Step 10 completed: Gender selected and Next clicked.")
    except Exception as e:
        print("Could not select gender or click Next:", e)
        print(driver.page_source)
        return

    # --- Step 11: Select 'Yes' and click Next ---
    try:
        yes_label = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="SelectedAnswer"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", yes_label)
        yes_label.click()
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(11)
        print("Step 11 completed: 'Yes' selected and Next clicked.")
    except Exception as e:
        print("Could not select 'Yes' or click Next:", e)
        print(driver.page_source)
        return

    # --- Step 12: Select 'Not approved yet by GP' with retry and click Next ---
    attempt = 0
    max_attempts = 3
    while attempt < max_attempts:
        try:
            not_approved_label = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[data-test-id="answer-0"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", not_approved_label)
            # Optionally wait a brief moment if needed:
            time.sleep(0.5)
            not_approved_label.click()
            break
        except StaleElementReferenceException as e:
            attempt += 1
            print("Stale element encountered in Step 12 - retrying (attempt {}/{})".format(attempt, max_attempts))
            time.sleep(0.5)  # wait a moment before retrying
            if attempt == max_attempts:
                print("Failed to locate not approved label after several attempts:", e)
                print(driver.page_source)
                return
        except Exception as e:
            print("Other error encountered in Step 12:", e)
            print(driver.page_source)
            return

    try:
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(12)
        print("Step 12 completed: 'Not approved yet by GP' selected and Next clicked.")
    except Exception as e:
        print("Could not click Next after Step 12:", e)
        print(driver.page_source)
        return

    # --- Step 13: Select 'In 6 to 12 hours' with bulletproof verification ---
    attempt = 0
    max_attempts = 5
    radio_selected = False

    while attempt < max_attempts and not radio_selected:
        try:
            print(f"Step 13 attempt {attempt + 1}/{max_attempts}")
            
            # Wait for page to be fully loaded
            time.sleep(1)
            
            # Find the radio button input (not the label)
            radio_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="SelectedAnswer_1"]'))
            )
            
            # Scroll to make sure it's visible
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", radio_input)
            time.sleep(0.5)
            
            # Try multiple clicking methods
            try:
                # Method 1: Click the label
                label = driver.find_element(By.CSS_SELECTOR, 'label[for="SelectedAnswer_1"]')
                driver.execute_script("arguments[0].click();", label)
                time.sleep(0.3)
            except:
                pass
                
            try:
                # Method 2: Click the radio input directly
                driver.execute_script("arguments[0].click();", radio_input)
                time.sleep(0.3)
            except:
                pass
                
            try:
                # Method 3: Set checked property directly
                driver.execute_script("arguments[0].checked = true;", radio_input)
                driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", radio_input)
                time.sleep(0.3)
            except:
                pass
            
            # CRITICAL: Verify the radio button is actually selected
            if radio_input.is_selected():
                radio_selected = True
                print(f"✅ Radio button successfully selected on attempt {attempt + 1}")
                break
            else:
                print(f"❌ Radio button not selected on attempt {attempt + 1}")
                attempt += 1
                time.sleep(1)
                
        except Exception as e:
            print(f"❌ Exception on attempt {attempt + 1}: {e}")
            attempt += 1
            time.sleep(1)

    if not radio_selected:
        print("❌ FAILED: Could not select radio button after all attempts")
        print("Current page source:")
        print(driver.page_source[:2000])  # First 2000 chars
        return

    # Only proceed with Next button if radio is definitely selected
    try:
        print("🔄 Clicking Next button...")
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(0.5)
        
        # Click Next button
        driver.execute_script("arguments[0].click();", next_button)
        
        # Wait a moment and check if we moved to next page
        time.sleep(3)
        
        # Check if we're still on the same page (indicates failure)
        try:
            # Use XPath instead of CSS selector
            still_on_page = driver.find_element(By.XPATH, "//h1[contains(text(), 'When are you next due to take your medicine?')]")
            print("❌ FAILED: Still on medicine timing page after clicking Next")
            print(driver.page_source[:2000])
            return
        except:
            # Good! We moved away from the medicine timing page
            if progress_callback:
                progress_callback(13)
            print("✅ Step 13 completed: 'In 6 to 12 hours' selected and Next clicked.")
            
    except Exception as e:
        print(f"❌ Could not click Next after Step 13: {e}")
        print(driver.page_source[:2000])
        return

    # --- Step 14: Click "Start my request" span ---
    try:
        start_request_span = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-test-id="action-link-text"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", start_request_span)
        start_request_span.click()
        if progress_callback:
            progress_callback(14)
        print('Step 14 completed: "Start my request" span clicked.')
    except Exception as e:
        print('Could not click "Start my request" span:', e)
        print(driver.page_source)
        return

    # --- Step 15: Click "Honicknowle Pharmacy" button ---
    try:
        pharmacy_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="start-referral"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", pharmacy_button)
        pharmacy_button.click()
        if progress_callback:
            progress_callback(15)
        print('Step 15 completed: "Honicknowle Pharmacy" button clicked.')
    except Exception as e:
        print('Could not click pharmacy button:', e)
        print(driver.page_source)
        return

    # --- Step 16: Fill forename and surname ---
    try:
        forename_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="patient-forename-input"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", forename_input)
        forename_input.clear()
        forename_input.send_keys(forename)
        
        surname_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="patient-surname-input"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", surname_input)
        surname_input.clear()
        surname_input.send_keys(surname)
        
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(16)  # Should be 16, not 17
        print("Step 16 completed: Forename and surname entered and Next clicked.")
    except Exception as e:
        print("Could not fill forename/surname or click Next button:", e)
        print(driver.page_source)
        return

    # Step 17: Fill Day, Month, Year inputs for Date of Birth and click Next button
    try:
        day_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="dob-day-input"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", day_input)
        day_input.clear()
        day_input.send_keys(dob_day)

        month_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="dob-month-input"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", month_input)
        month_input.clear()
        month_input.send_keys(dob_month)

        year_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="dob-year-input"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", year_input)
        year_input.clear()
        year_input.send_keys(dob_year)

        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(17)
        print("Step 17 completed: Date of Birth entered and Next clicked.")
    except Exception as e:
        print("Could not fill Date of Birth inputs or click Next button:", e)
        print(driver.page_source)
        return

    # Step 18: Fill Telephone Number input and click Next button
    try:
        tel_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="telephonenumber-input"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", tel_input)
        tel_input.clear()
        tel_input.send_keys("01234567890")
        
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(18)
        print("Step 18 completed: Telephone Number entered and Next clicked.")
    except Exception as e:
        print("Could not fill Telephone Number input or click Next button:", e)
        print(driver.page_source)
        return

    # Step 19: Click on the address option button
    try:
        address_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="address-option-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", address_button)
        address_button.click()
        if progress_callback:
            progress_callback(19)
        print("Step 19 completed: Address option button clicked.")
    except Exception as e:
        print("Could not click on the address option button:", e)
        print(driver.page_source)
        return

    # Step 20: Click the "No" radio option by clicking its label, then click Next
    try:
        no_label = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="AddressInformation_HomeAddressSameAsCurrent_1"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", no_label)
        no_label.click()
        
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(20)
        print("Step 20 completed: 'No' option selected and Next clicked.")
    except Exception as e:
        print("Could not click home address 'No' option or Next button:", e)
        print(driver.page_source)
        return

    # Step 21: Fill the home postcode input with provided value and click Next button
    try:
        home_postcode_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="home-postcode-input"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", home_postcode_input)
        home_postcode_input.clear()
        home_postcode_input.send_keys(home_postcode)
        
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="changeHomeAddressPostcode"][data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(21)
        print("Step 21 completed: Home postcode entered and Next clicked.")
    except Exception as e:
        print("Could not fill home postcode or click Next button:", e)
        print(driver.page_source)
        return

    # Before step 22, maximize the window so the final step is shown visually.
    driver.maximize_window()
    
    # --- Step 22: Select 'communication type none' and click Next ---
    try:
        comm_label = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="ConfirmationCommunicationTypeNone"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", comm_label)
        comm_label.click()
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="next-button"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        if progress_callback:
            progress_callback(22)
        print("Step 22 completed: Communication type none selected and Next clicked.")
    except Exception as e:
        print("Could not complete Step 22:", e)
        print(driver.page_source)
        return

    print("All steps completed successfully. Browser remains open for visual confirmation.")
    return

if __name__ == "__main__":
    # For testing directly, provide default values and a dummy progress callback to print progress.
    def dummy_progress(step):
        print("Progress updated to step:", step)
    run_emergency_script("male", "Ronak", "Plant", "20", "3", "1956", "po123rd", progress_callback=dummy_progress)
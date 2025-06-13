# Copilot Instructions for NHS 111 Condition Referral Automation

## Overview
This project automates the NHS 111 online condition referral pathway using Selenium with Python. The goal is to streamline referral generation into pharmacies by automating browser interactions for a specified condition.

## Coding Guidelines

1. **Prompting Style**  
   The script is developed through **step-by-step prompts**, one step at a time. Do not assume a fixed number of steps — the pathway length may vary depending on the condition.

2. **Function Structure**  
   Each browser interaction must be implemented as a named function:  
   `step_1(driver)`, `step_2(driver)`, ..., continuing sequentially. Each function should handle **only one logical step** of the journey.

3. **Minimal and Readable Code**  
   - Keep code easy to read, clear, and linear.  
   - Avoid over-engineering or creating abstraction layers.  
   - Use descriptive but simple naming conventions.

4. **Use Explicit Waits and Safe Element Handling (REQUIRED)**  
   Every interaction must use **Selenium's `WebDriverWait` with `expected_conditions`** to:
   - Wait for elements to be **present**, **visible**, or **clickable**  
   - Avoid using `time.sleep()` unless strictly necessary  
   - Ensure fast and reliable transitions between steps

   ❗ **Important: Never store web elements across page transitions**  
   Web elements may become stale after page changes or reloads. To avoid errors:
   - Always locate the element **immediately before** interacting with it  
   - Do **not store a reference to an element** for later use across steps  
   - Use `WebDriverWait(...).until(...)` right before `click()` or `send_keys()`  
   - Avoid using `EC.staleness_of(...)` — wait for a **unique element on the next page** instead

   **Example:**  
   ```python
   # ✅ GOOD: Wait and click directly
   button = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.ID, "continue-button"))
   )
   button.click()

   # ❌ BAD: Reusing a previously stored element after navigation
   # button.click()  # may throw StaleElementReferenceException
   ```   ❗ **MANDATORY: Implement Comprehensive Retry Logic for All Element Interactions**  
   **EVERY SINGLE element interaction in ALL step functions MUST include retry loops** to handle `StaleElementReferenceException` and other WebDriver exceptions. This is especially critical when the browser is minimized during automation.
   
   **Required Implementation Rules:**
   - **NO EXCEPTIONS**: Every `click()`, `send_keys()`, and element interaction needs retry logic
   - Wrap **ALL element interactions** in a 3-attempt retry loop
   - Re-locate the element on each retry attempt using `WebDriverWait`
   - Include `time.sleep(0.5)` between retry attempts for stability
   - Only raise the exception after all 3 attempts fail
   - This applies to **EVERY step function** without exception
   - **Use comprehensive exception handling** to catch multiple WebDriver exception types

   **Mandatory retry pattern for EVERY element interaction:**  
   ```python
   from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, ElementClickInterceptedException
   import time

   def step_X(driver):
       wait = WebDriverWait(driver, 10)
       
       # For clicking elements
       for attempt in range(3):
           try:
               element = wait.until(
                   EC.element_to_be_clickable((By.CSS_SELECTOR, 'your-selector'))
               )
               element.click()
               break
           except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
               if attempt == 2:
                   raise
               time.sleep(0.5)
       
       # For input elements
       for attempt in range(3):
           try:
               input_element = wait.until(
                   EC.element_to_be_clickable((By.CSS_SELECTOR, 'input-selector'))
               )
               input_element.clear()
               input_element.send_keys("value")
               break
           except (StaleElementReferenceException, WebDriverException, ElementClickInterceptedException):
               if attempt == 2:
                   raise
               time.sleep(0.5)
       
       print("Step X completed: Action description.")
   ```   **⚠️ CRITICAL:** 
   - Scripts without comprehensive retry logic on ALL interactions will fail when browser is minimized
   - Single-attempt element interactions (e.g., `wait.until(...).click()`) are NOT allowed
   - ALL steps must follow the retry pattern consistently
   - Use comprehensive exception handling to catch `StaleElementReferenceException`, `WebDriverException`, and `ElementClickInterceptedException`
   - This ensures maximum robustness across different WebDriver conditions and browser states

5. **No Hallucination**  
   Only implement elements and logic that are explicitly described.  
   **Do not guess** field names, button labels, or page flow.

6. **No Boilerplate or Extra Code**  
   Do not add:
   - Utility classes or unnecessary helper functions  
   - Logging frameworks  
   - Error-handling blocks unless specifically requested

7. **Approved Libraries Only**  
   Use only:
   - `selenium`
   - `time` (required for retry logic stability)
   - Python standard libraries (no external dependencies)

8. **Conditional Logic Handling**  
   Add logic where the pathway diverges, such as patient sex.  
   For example: if the patient is female, include steps that only appear for females; skip otherwise.

9. **Browser Visibility Behavior**  
   The script must implement dynamic browser visibility control:
   - **Start browser normally** (do not use `--start-minimized` Chrome option as it causes element staleness)
   - **Minimize immediately after initial page load** using `driver.minimize_window()`
   - **Keep browser minimized throughout all automation steps**
   - **Maximize browser before final step** using `driver.maximize_window()` for user review
   - **Leave the browser open** after completion for user review
   - **Do not call `driver.quit()`** unless user confirms completion

   **Implementation pattern:**
   ```python
   # At start of automation
   driver = webdriver.Chrome()
   driver.get("initial-url")
   try:
       driver.minimize_window()
   except Exception:
       pass  # Some platforms may not support minimization
   
   # ... all automation steps with browser minimized ...
   
   # Before final step
   try:
       driver.maximize_window()
   except Exception:
       pass
   
   print("Automation completed. Browser maximized for user review.")
   input("Press Enter to exit and close the browser...")
   driver.quit()
   ```

10. **When Uncertain**  
    If a step lacks clear instruction or details, insert this comment:  
    `# TODO: Clarify this step with user`

11. **Commenting Style**  
    - Use brief comments to explain *actions only* (e.g., clicks, waits, inputs).  
    - Avoid verbose explanations or redundant comments.

12. **GUI Integration Note**  
    This script will later be triggered via a GUI (e.g. tkinter).  
    **Do not include any GUI logic** in this automation script.

## Console Logging for Debugging

- After each automation step (such as clicking a label, filling an input, or clicking a button), print a clear console log message describing the action taken.
- The log should include the step number and a brief description (e.g., `Step 4 completed: Clicked 'Head, face and neck' category link.`).
- This helps with debugging and tracking progress, especially if an error occurs.

**Example:**
```python
print("Step 4 completed: Clicked 'Head, face and neck' category link.")
```

## Required Imports
All scripts must include these imports at the top:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, ElementClickInterceptedException
import time
```

---

## Implementation Enhancements and Best Practices

### Comprehensive Exception Handling
The scripts implement robust exception handling that goes beyond just `StaleElementReferenceException`:

- **`StaleElementReferenceException`**: Elements become stale after DOM changes or page transitions
- **`WebDriverException`**: General WebDriver communication issues or unexpected browser states  
- **`ElementClickInterceptedException`**: Elements are obscured or not clickable due to page layout changes

This comprehensive approach ensures maximum reliability across different automation scenarios, browser states, and platform variations.

### Browser Minimization Strategy
The browser minimization/maximization pattern serves multiple purposes:

- **User Experience**: Hides automation steps from users while showing final results
- **Performance**: Minimized browsers can run faster and use fewer system resources
- **Testing Robustness**: Forces the automation to handle the most challenging element interaction conditions
- **Real-world Reliability**: Ensures scripts work when users minimize browsers or switch applications

### Modular Step Function Design
Each condition pathway is broken into individual step functions because:

- **Debugging**: Easy to identify which specific step fails during development or production use
- **Maintenance**: Individual steps can be updated without affecting the entire workflow
- **Reusability**: Common steps (like postcode entry) can be shared across different condition pathways
- **Progress Tracking**: Clear console logging shows exactly where the automation is in the process

### Element Interaction Patterns
The scripts follow specific patterns that have proven reliable:

1. **Element Lookup Inside Retry Loop**: Always re-locate elements on each retry attempt
2. **Immediate Action After Lookup**: Perform the action immediately after finding the element
3. **Consistent Wait Conditions**: Use `element_to_be_clickable` for interactive elements
4. **Timing Controls**: Include `time.sleep(0.5)` between retries for stability

These patterns prevent the most common automation failures and ensure consistent performance across different system loads and browser conditions.

---

The script must be **modular**, **lightweight**, **robust against element staleness**, and **ready for pharmacy-facing use**. Build it sequentially with a focus on accuracy, simplicity, comprehensive retry logic, and proper browser visibility control using robust waiting mechanisms.

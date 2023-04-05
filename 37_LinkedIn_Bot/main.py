from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from decouple import config
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to the Edge driver executable
EDGE_DRIVER_PATH = "C:\Edge_Webdriver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)
page = 1

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3455101269&distance=25&f_AL=true&f_E=1%2C2&f_WT=2&geoId=92000000&keywords=software%20developer")
time.sleep(1)

sign_in_button = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_in_button.click()

email_field = driver.find_element_by_id("username")
email_field.send_keys(config("USER"))

pass_field = driver.find_element_by_id("password")
pass_field.send_keys(config("PASS"))

sign_in_2 = driver.find_element_by_css_selector(".btn__primary--large")
sign_in_2.click()


def inputs_fill():
    try:
        inputs = driver.find_elements_by_css_selector(".artdeco-text-input--container .artdeco-text-input--input")

        # Loop through each input element
        for input in inputs:
            # Check if the input element is empty
            if input.get_attribute("value") == "":
                # Set the value to "0"
                input.send_keys("0")
                time.sleep(1)
    except Exception as ex:
        print(ex)


def next_button_loop():
    try:
        resume_button = driver.find_element_by_css_selector(".jobs-resume-picker__resume-btn-container .artdeco-button")
    except Exception as ex:
        print(ex)
    else:
        resume_button.click()
        time.sleep(1)

    inputs_fill()

    try:
        next_button = driver.find_element_by_css_selector(".justify-flex-end .artdeco-button--primary")
        if "Continue to next step" == next_button.get_attribute("aria-label"):
            next_button.click()
            time.sleep(2)
            inputs_fill()
    except Exception as ex:
        print(ex)
    else:
        time.sleep(2)
        # Find the button element
        try:
            button_element = driver.find_element_by_css_selector(".justify-flex-end .artdeco-button--primary")
            # print(button_element.get_attribute("aria-label"))
            # Check if the aria-label attribute contains "Review your application"
            if "Review your application" == button_element.get_attribute("aria-label"):
                button_element.click()
                time.sleep(2)
                return True
            else:
                time.sleep(2)
                if next_button_loop():
                    return True
        except Exception as ex:
            print(ex)
        else:
            pass

    return False


def job_apply_per_page(page_num):
    time.sleep(2)
    global page

    jobs_containers = driver.find_elements_by_css_selector(".job-card-container")
    for job in jobs_containers:
        job.click()
        time.sleep(2)
        try:
            apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card .jobs-apply-button")
        except Exception as ex:
            print(ex)
        else:
            apply_button.click()
            time.sleep(2)

            try:
                submit_element = driver.find_element_by_css_selector(".artdeco-button--primary")
                if "Submit application" == submit_element.get_attribute("aria-label"):
                    is_submit = True
                    resume_button = driver.find_element_by_css_selector(
                        ".jobs-resume-picker__resume-btn-container .artdeco-button")
                    resume_button.click()
                else:
                    raise Exception
            except Exception as ex:
                print(ex)
                is_submit = next_button_loop()

            print(is_submit)
            if is_submit:
                try:
                    checkbox = driver.find_element_by_id("follow-company-checkbox")

                    # scroll to the checkbox element
                    driver.execute_script("arguments[0].scrollIntoView();", checkbox)

                    # use ActionChains to move mouse cursor to checkbox and click it
                    action = ActionChains(driver)
                    action.move_to_element(checkbox).click().perform()

                    time.sleep(2)
                    button_element = driver.find_element_by_css_selector(".artdeco-button--primary")
                    # print(button_element)
                    # Check if the aria-label attribute contains "Review your application"
                    if "Submit application" == button_element.get_attribute("aria-label"):
                        button_element.click()
                        time.sleep(2)
                        button_2 = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
                        # Check if the aria-label attribute contains "Review your application"
                        if "Dismiss" == button_2.get_attribute("aria-label"):
                            button_2.click()
                            time.sleep(5)
                except Exception as ex:
                    print(ex)
                else:
                    pass
            else:
                pass
    # print("Here before pag")
    try:
        pagination_button = driver.find_element_by_css_selector(f"[data-test-pagination-page-btn='{page_num}']")
    except Exception as ex:
        print(ex)
    else:
        pagination_button.find_element_by_css_selector("button").click()
        page += 1
        job_apply_per_page(page)

    driver.quit()


job_apply_per_page(page)

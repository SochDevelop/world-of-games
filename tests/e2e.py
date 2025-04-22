from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import time


def test_scores_service(url):
    """
    Tests the score service by navigating to the URL, extracting the score,
    and checking if it is a number between 1 and 1000.

    Args:
        url (str): The URL of the score service.

    Returns:
        bool: True if score is valid, False otherwise.
    """
    try:
        # Optional: run browser in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # Launch browser
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        # Wait a moment for the page to fully load
        time.sleep(2)

        # Find score element
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text.strip()

        driver.quit()

        # Validate score
        if score_text.isdigit():
            score = int(score_text)
            return 1 <= score <= 1000
        else:
            return False

    except Exception as e:
        print(f"Error in test_scores_service: {e}")
        return False


def main_function():
    """
    Calls test_scores_service. Exits with code 0 if passed, -1 if failed.
    """
    url = "http://localhost:5000"  # server url

    if test_scores_service(url):
        print("Test passed.")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)


if __name__ == "__main__":
    main_function()

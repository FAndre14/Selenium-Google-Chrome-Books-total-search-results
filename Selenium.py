from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

try:
    start_year = int(input("Input the starting year: "))
    initial_year = start_year
    end_year = int(input("Input the ending year: "))
    if end_year < start_year:
        print("The ending year needs to be bigger than the starting year.")
        sys.exit(0)
    number_of_titles = int(input("Tell us the number of words you want to search: "))
    if number_of_titles < 1 :
        print("You need to enter at least 1 title.")
        sys.exit(0)
    search_titles = []
    for i in range(number_of_titles):
        n = input("Number {} word: ".format(i+1))
        search_titles.append(n)
    show_results = False
    Path = "C:\Program Files (x86)/chromedriver.exe"
    driver = webdriver.Chrome(Path)

    driver.get("https://books.google.com/")
    for title in search_titles:
        #Locating the search bar, inserting the title and simulating the enter command
        que=driver.find_element_by_xpath("//input[@name='q']")
        que.clear()
        que.send_keys(title)
        que.send_keys(Keys.RETURN)
        print("Searching for the word: " + title)
        while start_year <= end_year:
            start_date = "1/1/" + str(start_year)
            end_date = "12/31/" + str(start_year)
            main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.hdtbU:nth-child(12)")))
            date_button = driver.find_element_by_xpath("//*[@id='hdtbMenus']/div/div[5]")
            driver.execute_script("arguments[0].click();", date_button)
            #Pressing the custom-range button
            main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[3]/div/div/div[2]/div/ul[4]")))
            custom_range_button = driver.find_element_by_xpath("//*[@id='cdr_opt']/div")
            custom_range_button.click()
            #Adding the data//*[@id='T3kYXe']
            main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='T3kYXe']")))
            starting_year_textbox = driver.find_element_by_xpath("//*[@id='OouJcb']")
            starting_year_textbox.clear()
            starting_year_textbox.send_keys(start_date)
            ending_year_textbox = driver.find_element_by_xpath("//*[@id='rzG2be']")
            ending_year_textbox.clear()
            ending_year_textbox.send_keys(end_date)
            custom_range_confirm_button = driver.find_element_by_xpath("//*[@id='T3kYXe']/g-button")
            driver.execute_script("arguments[0].click();", custom_range_confirm_button)


            #Here you get the numbers of results per page
            tool_button = driver.find_element_by_xpath("//*[@id='hdtb-tls']")
            tool_button.click()
            print("Year: "+ str(start_year) + " results: " + driver.find_element_by_xpath("//*[@id='result-stats']").get_attribute('textContent'))
            start_year += 1
            tool_button.click()
        start_year = initial_year #Resetting for the next title
    print("Done collecting data from " + str(initial_year) + " until " + str(end_year))
    driver.quit()
except:
    print("Sorry, you entered invalid data.")
    sys.exit(0)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
 
# What you enter here will be searched for
query = input("Enter search query: ")
 
# Creating a webdriver instance
driver = webdriver.Chrome('./chromedriver_win32_new/chromedriver.exe')
 
# Maximize the screen
driver.maximize_window()
 
# Open Google Images in the browser
driver.get('https://images.google.com/')
 
# Finding the search box
driver.maximize_window() 
#driver.implicitly_wait(20)
box = driver.find_element("xpath",'//*[@id="APjFqb"]')
 
# Type the search query in the search box
box.send_keys(query)
 
# Pressing enter
box.send_keys(Keys.ENTER)

# Function to take the screenshots of all the images loaded
def screenshot_images():
    print("Now capturing screenshots...\n" + "--------------------\n")
    # This will capture (give or take) the max amount of Google image results for a given query (~728)
    for i in range(1, 728):
        # This logic is used to determine the XPath construction for Google images 
        # (It is not as straightforward as previously envisioned)
        image_path = ''
        if i < 51:
            image_path = '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img'
        elif i >= 51 and i < 104:
            image_path = '//*[@id="islrg"]/div[1]/div[51]/div['+str(i - 50)+']/a[1]/div[1]/img'
        elif i >= 104 and i < 208:
            image_path = '//*[@id="islrg"]/div[1]/div[52]/div['+str(i - 103)+']/a[1]/div[1]/img'
        elif i >= 208 and i < 312:
            image_path = '//*[@id="islrg"]/div[1]/div[53]/div['+str(i - 207)+']/a[1]/div[1]/img'
        elif i >= 312 and i < 416:
            image_path = '//*[@id="islrg"]/div[1]/div[54]/div['+str(i - 311)+']/a[1]/div[1]/img'
        elif i >= 416 and i < 520:
            image_path = '//*[@id="islrg"]/div[1]/div[55]/div['+str(i - 415)+']/a[1]/div[1]/img'
        elif i >= 520 and i < 624:
            image_path = '//*[@id="islrg"]/div[1]/div[56]/div['+str(i - 519)+']/a[1]/div[1]/img'
        elif i >= 624 and i < 728:
            image_path = '//*[@id="islrg"]/div[1]/div[57]/div['+str(i - 623)+']/a[1]/div[1]/img'

        try:
            # XPath of each image
            img = driver.find_element("xpath", image_path)
            driver.execute_script("window.scrollTo(0,0)") 
            img_loc = img.location

            # Scroll up then down to get the google top bar to disappear
            driver.execute_script("window.scrollTo(" + str(img_loc['x']) + "," + str((img_loc['y'])-50)+")") 

            # Give plenty of time for the browser to render correctly after scrolling
            time.sleep(0.2) 

            # Take the screenshot
            img.screenshot(query.replace(" ", "_") + str(i) + '.png')
            
            # Just to avoid unwanted errors
            time.sleep(0.2)
 
        except:
            # if we can't find the XPath of an image,
            # we skip to the next image
            print("Error reading XPath for: " + image_path)
            continue
    print("Finished!\n" + "--------------------\n")

# Function to scroll to the bottom of the Google results and pre-load all results
def scroll_to_bottom():
    print("Pre-loading images...\n" + "--------------------\n")

    last_height = driver.execute_script('\
    return document.body.scrollHeight')
 
    while True:
        driver.execute_script('\
        window.scrollTo(0,document.body.scrollHeight)')
 
        # waiting for the results to load
        # Sleep for 4 seconds because my internet is garbage, you can probably get away with 2-3
        time.sleep(4)
 
        new_height = driver.execute_script('\
        return document.body.scrollHeight')


        # click on "Show more results" (if exists)
        try:

            driver.find_element("xpath", '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click()
 
            # waiting for the results to load
            # Sleep for 4 seconds because my internet is garbage, you can probably get away with 2-3
            time.sleep(4)
 
        except:
            pass

        # checking if we have reached the bottom of the page
        if new_height == last_height:
            break
 
        last_height = new_height
 
 
# Function calls
st = time.time()
scroll_to_bottom()
screenshot_images()
et = time.time()
total_time = et - st
print('Total time of execution:', total_time, 'seconds')

# Finally, we close the driver
driver.close()
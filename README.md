# ImageScraperTool

Selenium based image scraping script to gather all image results for a given query <br />

## About the tool 

This is a super simple script which is able to scrape images for a given query and automatically save them. <br />
It was originally developed as a method to generate datasets for a machine learning project. <br />
It was created due to current solutions failing to scrape all ~700 results for the newest chrome driver. <br />

## How it works

You must have ChromeDriver installed. You may create and place the driver executable in a folder in your current directory called "chromedriver_win32_new" which is the default. Else, you can edit the script where is says "Create webdriver instance" (line ~9) to specify a custom path to your driver executable. Other than that, you can specify your query where it says "Specify query" (line ~6). Then, simply execute the python script. 

## Future

I like the idea of a very simple and editable script, but eventually there may be a few convenience features added such as: <br />
- User inputted queries
- Result folder specifications <br />

The latter will probably be done first.



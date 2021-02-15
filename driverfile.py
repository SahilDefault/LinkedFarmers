from selenium import webdriver


driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 " \
             "Safari/537.36 "

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()

driver = webdriver.Chrome() # פותח חלון דפדפן חדש
driver.get("http://www.wgalil.ac.il") # פותח את הדף הרלוונטי


driver = webdriver.Chrome() # פותח חלון דפדפן חדש
driver.get("http://www.wgalil.ac.il") # פותח את הדף הרלוונטי

button = driver.find_element_by_id("menu-item-2679") # מציאת הכפתור לפי ה-ID שלו
button.click() # לחיצה על הכפתור


driver = webdriver.Chrome() # פותח חלון דפדפן חדש
driver.get("http://www.wgalil.ac.il") # פותח את הדף הרלוונטי

input_box = driver.find_element_by_name("s") # מציאת תיבת הטקסט לפי השם שלה
input_box.send_keys("חוג לקרימונולוגיה") # הזנת הטקסט לתיבה


driver = webdriver.Chrome() # פותח חלון דפדפן חדש
driver.get("http://www.wgalil.ac.il") # פותח את הדף הרלוונטי

element = driver.find_element_by_id("menu-item-2679") # מציאת

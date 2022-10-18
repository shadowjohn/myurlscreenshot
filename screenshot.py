import getopt, sys
from selenium import webdriver
from PIL import Image
import time
import os
PWD = os.path.dirname(os.path.realpath(sys.argv[0]));

argumentList = sys.argv[1:]
# Options
options = "hu:d:o:"
 
# Long options
long_options = ["Help", "Url=", "Delay=", "Output="]

message_usage = '''
  URL ScreenShot
  
  Author: 
    Feather Mountain (https://3wa.tw)
    
  Usage:  
    screenshot.exe -u <URL> -d <Delay[ms]> -o <outputfile>
  
  Example:    
    screenshot.exe -u "https://3wa.tw" -d 3000 -o "output_3wa.png"    

'''

ARGV_URL = "https://3wa.tw"
ARGV_DELAY = 1500 # default 1500ms
ARGV_OUTPUT = "output.png"

if len(sys.argv) == 1:
  print (message_usage)
  sys.exit();  
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print (message_usage)
            sys.exit();                     
        elif currentArgument in ("-u", "--Url"):            
            ARGV_URL = currentValue
        elif currentArgument in ("-d", "--Delay"):
            ARGV_DELAY = int(currentValue)                         
        elif currentArgument in ("-o", "--Output"):
            #print (("Enabling special output mode (% s)") % (currentValue))
            ARGV_OUTPUT = currentValue             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

print("ARGV_URL: %s\n" % (ARGV_URL))
print("ARGV_DELAY: %s\n" % (ARGV_DELAY))
print("ARGV_OUTPUT: %s\n" % (ARGV_OUTPUT))
    

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1280x768')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(executable_path = PWD + "\\chromedriver.exe", chrome_options=options)

driver.get(ARGV_URL)

time.sleep((ARGV_DELAY/1000.0))

driver.save_screenshot(ARGV_OUTPUT)


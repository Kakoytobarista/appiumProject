# appiumProject
The appiumProject is a framework with configurations designed 
for flexible execution of automated tests. It includes predefined 
capabilities for various test execution methods. Additionally, you 
can find prototypes of test packages with pytest, Allure, 
Page Object Model (POM), and Page Element Object (PEO).

1. Install appium lib

2. Install xcode

3. Install client for python 

4. install allure



____
### REPORTS:
```allure serve ./allure-results```
____
DEBUG MODE:
Run:
1. Appium server
```appium --log-level debug```
2. Simulator of ios device
```inside of xCODE```



--- instruction for setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

-- build app on simulator
select device
build on xcode
find your device's UUID
 xcrun simctl list 'devices' 'booted'

-- run test
capabilities.py -> update UUID
pytest -s -v --alluredir=./allure-results tests


-- find button identifier
open accessibility inspector (help->search for it)
select the device we want to monitor on top left (Simulator -> all processes)
click on the circle button on the top right
select on device, note down either the labvel or identifier. Apparently both works. 

-- modify the code to add the new custom action
-- in main_page_object.py, modify the code to see your custom action


TestingBot:
store app into storage:
```
curl -X POST "https://api.testingbot.com/v1/storage" \
-u 76a48a70109b8cc5740ebe8815871256:50a1abfc8f00f15d47091fdc07442ae4 -F "file=@/Users/aslan/PetProjects/appiumProject/helloWorld/helloWorld.ipa"
```

You should create file .env in root dir and set these:
KEY=76a48a70109b8cc5740ebe8815871256
SECRET=50a1abfc8f00f15d47091fdc07442ae4

# Verification and Validation

**Group 10:** _Clash of Clans Auto Player_\
**Date:** April 16th, 2021\
**Group members:** Teng Ao, Miles Brown, Ran Li, Devin O'Neal, Ulugbgek Abdullayev, and Junjian Yin

## 1. Description

Clash of Clans Autoplayer allows players to save time and minimize frustration. Our Autoplayer automates all of the boring parts of Clash of Clans so that you can free up your time to do other things. The system can build/upgrade structures and collect your resources. Clash of Clans Autoplayer saves you time and helps you enjoy playing the game even more.

This release of the system has the ability to harvest resources and build buildings from a queue. A simple UI runs alongside the Clash of Clans emulator to allow the user to change these things while playing. For Clash of Clans players who don’t enjoy the repetitive gameplay loops, or want to succeed in the game, the Clash of Clans Autoplayer helps you get through all the boring repetitive gameplay. Our product does not overwhelm your device with inappropriate ads and has a user friendly interface.

## 2. Verification

### 2.1 Unit Test
####   2.1.1 We have used pytest framework to develop our tests<br> 
  The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries\
  **Link**: https://docs.pytest.org/en/6.2.x/
####   2.1.2 Link to our GitHub folder where automated unit tests are located: <br> https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/tree/main/pythonCode/Unit-Tests
####   2.1.3 A test case that makes use of mock object:
  Since we have used pyautogui, most of our classes consist of return types that are completely different in every run time. In order to tackle that problem, we have decided to create our own mock object within every function return so that pytest can detect them using ***assert*** <br>
  **Link to the test:** https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/pythonCode/Unit-Tests/PlayerClassTest.py <br>
  **Link to the class being tested:** https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/pythonCode/PlayerClass.py
####   2.1.4 Print Screen showing the results of the unit test
![Our Sequence Diagram](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/mscScreenShots/Capture.PNG)

### 2.2 Integration Test<br> 
  We continue use pytest to test overall usability of our code\
  **Link**: https://docs.pytest.org/en/6.2.x/
####   2.2.2 Link to our GitHub folder where automated unit tests are located: <br>
https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/pythonCode/IntegrationTest.py

####   2.2.3 A test case that makes use of mock object:
  We import all functions into the main, to test the overall usage we will test the core function that be constructed in the main.
  **Link to the test:** https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/pythonCode/IntegrationTest.py <br>
  **Link to the class being tested:** https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/pythonCode/ClashOfClansAutoplayer2.py <br>
  
####   2.2.4 Print Screen showing the results of the unit test


### 2.3 Acceptance Test

We were unable to find an adequate framework for writing acceptance tests for Python code, however our Validation and our own experiences show that the user interface for our system is intuitive and works well for both new and veteran players of Clash of Clans.

## 3. Validation
**Script:**\
Clash of Clans autoplayer is designed to help you automate certain repetitive tasks so that you can improve your base constantly. By using our product, you are not going to ace this game guaranteed since autoplayer is a supplementary product for the game itself.
In order to initiate the autoplayer, there are few tools you need to install to your system.
NOX - android emulator (to install Clash of Clans game)
PyCharm - in order to run the product

Once you have installed the software given above which is available for free, you can run the autoplayer by typing in ClashOfClansAutoPlayer.py. The autoplayer will take over the cursor and the keyboard so it is recommended that you do not open external windows in your computer. 

- Now you have tested out our product, what is your opinion on our choice of user interface?
- How do you think our product will improve your gaming experience in Clash of Clans?
- On a scale of 1 to 10, 1 being completely useless and 10 being above and beyond the expectations, how satisfied are you with our product?
- Do you think there are any areas we could improve our product for future release?

**Results**:<br>
***User - 1:***
This user just started playing clash of clans and used our product to see if there is any substantial improvement he can get. This user did not have any issues running the autoplayer and was overall satisfied with the features that were implemented. He was very satisfied with the user interface and the simplicity of the GUI. On a scale of 1 - 10, he said he would give 8 for the autoplayer. His suggestions were to improve the dynamic of building upgrading queue since there were limited options for that feature.<br>
***User - 2:***
This user has been playing Clash of Clans for a few years now and is very experienced in the game. She said that she really liked the user interface but said that it could be improved by adding the icons of the tasks users can choose. “Since my base is very highly upgraded and advanced, the app didn’t have much impact on the overall gameplay” she said. However, she mentioned that resource collection is a nifty feature to have in order to get more resources while not playing the game. On a scale of 1 - 10, she gave our autoplayer 7.<br>
***User - 3:***
This user has never played clash of clans and has little to no experience in the game. He tested out our autoplayer and was very enthusiastically excited for the fact that our product can do things without user input. He said he would give 10 on a scale of 1 - 10 for our product and thinks that we should think of making other products similar to our automation.

**Reflections:**<br>
After the interviews we have done on users who have tested our product, we have seen few areas where we could improve our product. Most users mentioned that the product is hardware performance dependent and might lag behind when the user’s machine is slow. We have also noticed that our UI doesn’t give the users an option of exiting out of the autoplayer in runtime so we are thinking to implement an actual python GUI to improve our user interface.<br>

Resource collection feature of our autoplayer was one of the most appreciated features and all three test users were satisfied with it. Since the resource collection was the minimum value proposition, we have satisfied MVP in the eyes of all test users.<br>
Overall, we have learned valuable lessons throughout the development of our product and it was a great experience.

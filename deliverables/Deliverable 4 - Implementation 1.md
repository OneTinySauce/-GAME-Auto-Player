# Analysis

**Group 10:** _Clash of Clans Auto Player_\
**Date:** March 18th, 2021\
**Group members:** Teng Ao, Miles Brown, Ran Li, Devin O'Neal, Ulugbgek Abdullayev, and Junjian Yin

## 1. Introduction

Clash of Clans Auto Player will allow players to save time and minimize frustration while playing or by running in the background. The full system will have the ability to harvest resources, train troops, and build buildings from a queue, all automatically and customizable in the settings for each action. A simple UI will run alongside the Clash of Clans emulator to allow the user to change these things while playing. The version being released here has basic start up functions, a functional and prototype UI, and the automated resource collection system.

Github: https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player \
Trello: https://trello.com/b/y1373xdI/project-board

## 2. Implemented Requirements
We implemented the use case involved with resource collection.

Use Case: Enable Resource Collection
Actor: Player
Description: The player wants to enable resource collection
Preconditions: The player has the game installed and starts the system
Post-conditions: The system set to automatically collect resources
Main Flow:
1. The player starts the program
2. The system asks the player if they are ready to to begin
3. The player confirms
4. The system asks the player what resources they wish to collect
5. The player selects all types.\

Alternative Flows:\
3a. The player cancels\
3b. The system closes\
4a. The player selects coins only\
4b. The system is set to collect coins only\
4.1a. The player selects elixir only\
4.1b. The system is set to collect elixir only

Features:
UI Experimentation / Prototyping - Ulugbek, Junjian
Image Recognition / Image Gathering - Ulugbek, Ran, Teng, Junjian
Program Startup - Ulugbek, Junjian
Resource Collection System - Ulugbek, Junjian, Miles, Ran, Teng

## 3. Adopted Technologies 

We have adopted many different technologies for this project. We are using Python for our code and writing it using the Pycharm IDE, and writing the code to be used by the 
PyAutoGUI program, that interprets our code for automating certain systems. We are testing our code using the mobile game Clash Of Clans, which we are runing on several different Android emulators to ensure that we write code that can run on as many systems as possible. We are using GitHub and Trello for collaboration purposes, as well as Docker and Amazon AWS to deploy our code.

## 4. Learning/Training

We have learned the technology not only how to coding to solve the problem in real-world but how to work as a software engineering team. We connect and sharing ideas with each other on Discord and we using Trello and GitHub to keep track of our project. We learned to use those tools to help us improve efficiency as a team. Focus on the view as a team is the main strategy to learn those team-work tools. For the coding part, we using pyautogui library. We aim to reach the MVP and thinking to improve the user experience while coding. Generally, our strategy is to set the goal and think the base of the goal.

## 5. Deployment 

We are in the process of deploying our system using Docker and Amazon AWS. We are attempting to create a Docker image for our program in order to deploy it, and we are following the tutorials to do this. We hope to have this process complete by our next release.

## 6. Licensing 

We have adopted the MIT license because it is a short and simple license that includes permissions for Distribution and Modification as well as Commercial and Private use.

## 7. ReadMe File

We have created a comprehensive ReadMe file that explains the purpose of our project and links to our guide to contributing as well as our code of conduct.

## 8. Look and Feel

Our UI is a simple alert box system from pyAutoGUI. It allows the user to navigate a series of windows that allow them to select one of several options. This allows users to turn on and off certain functions of the system, exit, or set building queues, resources to collect, etc. When an option is selected, a new window appears, with the change implemented and, if necessary, moves to a new window.

![App Launch UI](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/screenshots/UI_intro.PNG?raw=true)
![App Main Menu UI](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/screenshots/UI_ActonMenu.PNG?raw=true)

## 9. Lessons Learned

During MVP implementation, we have faced few challenges. First, a platform to run our code which is the Android emulator was challanging to find since most emulaters had third-part ads and pyautogui has image recognition problems when those ads present themselves. We have settle on Nox app player which has minimal ads and suser friendly interface. For the future release, we will try to work more on our GUI unser interface to make it more functional on player's perspective. We will also try to work on implementing some clan management tools like worker queues and trash removing in the base.

## 10. Demo 

Demo Video Link: https://youtu.be/BGOPTqpIFx0

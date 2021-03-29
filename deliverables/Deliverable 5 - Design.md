# Design

**Group 10:** _Clash of Clans Auto Player_\
**Date:** March 24th, 2021\
**Group members:** Teng Ao, Miles Brown, Ran Li, Devin O'Neal, Ulugbgek Abdullayev, and Junjian Yin

## 1. Description

Clash of Clans Autoplayer will allow players to save time and minimize frustration. Our Autoplayer automates all of the boring parts of Clash of Clans so that you can free up your time to do other things. The system can train your troops, build/upgrade structures, collect your resources, and even take care of destroying rocks and trees for you. Clash of Clans Autoplayer saves you time and helps you enjoy playing the game even more.

The full system will have the ability to harvest resources, train troops, destroy rocks/trees and build buildings from a queue, all automatically and customizable in the settings for each action. A simple UI will run alongside the Clash of Clans emulator to allow the user to change these things while playing. For Clash of Clans players who don’t enjoy the repetitive gameplay loops, or want to succeed in the game, the Clash of Clans Autoplayer helps you get through all the boring repetitive gameplay and succeed in the game. Our product does not overwhelm your device with inappropriate ads and has a user friendly interface.

## 2. Architecture

![Our UML Package Diagram](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/screenshots/Autoplayer%20Package%20Diagram.png?raw=true)

Above is the UML Package Diagram for our system, which I designed close to the examples given because I was not sure how to create a package diagram for our system. I believe to make a more accurate package diagram, we will need to split our system into classes with some restructuring.

## 3. Class Diagram

![Our Class Diagram](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/D5%20Class%20Diagram.PNG)

## 4. Sequence Diagram
**Use Case:** Collect Resource
**Actor:** Player
**Description:** The user wants to turn on the resource collection to collect resources automatically
**Pre-Conditions:** 
**Post-Conditions:** 
**Main Flow & Alternative Flows** (shown with #.# format):

**Use Case:** Collect Resource
**Actor:** Player
**Description:** The user wants to turn on the resource collection to collect resources automatically
**Pre-Conditions:** The user opened the auto-player correctly
**Post-Conditions:** The program collect resources till the user hit exit
**Main Flow & Alternative Flows** (shown with #.# format): 
1.User opened the auto-player and see the GUI
2.User clicked on collect resources
 2.1.Resource founded and collected
 2.2.Can't found the resources
 2.3.Resource founded but storge is full
3.The program will run continusely till the user hit 'esc' on keyboard

## 5. Design Patterns

**Desing Pattern 1**: (Structural) *Singleton* - method to add building to queues and to retrieve the queue

![](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/buildingQueue.PNG)

Figure 5.1 - UML Diagram of the implementation of the Singleton patter in the BuildQueue class

**Desing Pattern 2**: (Behavioral) *Template Method* - overrides the setTroopQueue in the Troop class and displayes the set troop preset

![](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/behavioral.PNG)

Figure 5.2 - UML diagram of the implementation of the template pattern in the Clash Of Clans Autoplayer

## 6. Design Principles

***Single Responsibility Principle***: Troop class only quantifies the troop types in the game

***Open/Closed Principle***: Our code follows this principle since the resource collection is automated and well intergrated with UI that the user will not need to re enitiate each state. Also, it is closed because no action is required once the collection action is set.

***Liskov Substitution Principle***: Our code follows this principle because our program can be run in multiple emulators so that users can chose any platform they would like to play the game in.

***Interface Segregation Principle***: We decided to create multiple requests for the UI so that it can be modified and there won't be a spagetti code.

***Dependency Inversion Principle***: Our code follows this principle since all actions are automated and user do not need to accomodate any pre conditions. Only action that is required by the user is to initiate the code through pycharm and opt for prefered outcome from the code.

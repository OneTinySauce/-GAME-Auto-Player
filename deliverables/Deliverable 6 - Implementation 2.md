# Implementation 2

**Group 10:** _Clash of Clans Auto Player_\
**Date:** April 1st, 2021\
**Group members:** Teng Ao, Miles Brown, Ran Li, Devin O'Neal, Ulugbgek Abdullayev, and Junjian Yin

## 1. Introduction
In our previous release, we have implemented the resource collection feature which was requested as per the MVP. Since Clash of Clans is a highly object related game, we have had to implement a building upgrade queue for our new release. Now, as a clash of clans player, you can automate your building upgrade queue and our program will assign available workers to the  buildings in order of your queue.
  
We have also updated a new version of user interface that is bug-free and includes building automation choice at the start of the program. Once the user opts for the building upgrade automation, our product will launch the emulator and the Clash of Clans game as well. There are new features like Town Hall upgrade and Gold Storage upgrade and our product will choose which building to upgrade depending on the availability of resources and workers.
  
Trello Board: https://trello.com/b/y1373xdI/project-board
  
GitHub: https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player
## 2. Implemented Requirements
Since we have implemented the MVP for this release we are focusing on the upgrade buildings automatically in the game.
![](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/screenshots/building_UI.png?raw=true)
  
As this image shows, the upgrade buildings is our new implementation, this function will upgrade the Town Hall and Gold Storage in the game, the user will able to develop their town with simple click.
  
Use Case: Upgrade buildings
  
Actor: Player
  
Description: The player wants to upgrade their buildings
  
Preconditions: The player has the game installed and starts the system 
  
Post-conditions: The system set to automatically collect resources. 
  
Main Flow:
  
1.Player opened the software\
2.Player clicked on the upgrade buildings\
3.The program start to check the any building is upgradeable\
4.If so, upgrade now, if not, will check later

Alternative Flows:
  
1.The player closed the program\
2.The resources are not enough to upgrade the buildings\
3.The buildings already in upgrade progress

Features:
  
UI / Building’s upgrade - Ulugbek, Miles, Devin

Testing - Junjian Yin, Ran, Teng

Document Writing - Ulugbek, Miles, Devin, Junjian Yin, Ran, Teng

Demo Video: Ulugbek

## 3. Demo
**Link to demo video:** https://youtu.be/E6WXAoOFr0M

## 4. Code Quality
In order to ensure high quality, we implemented several techniques on this release. Firstly, we separated our code from a single controller file to break it into several reusable code classes that allowed for far more modular code. Splitting code into separate files in this way can sometimes have issues in python, and we ran into some of these while separating our code into smaller chunks, but through some modification we were able to make our changes functional.

We changed our naming conventions of classes and functions to more accurately reflect the effects and actions they had, with some being changed when we split into classes and some being less accurately labeled in the initial release.

We also ran tests on several different devices between our group to find issues with compatibility, which found an issue with recognizing images between different computers.

Lastly we ran code oversight and clear up from other members of the group who were able to clear up and clarify code after the fact and add comments and spacing changes to document.

## 5. Lessons Learned
During the development of this release, we learned how important it is to have modular code. A major part of this release was the refactoring of our existing code into seperate classes so that we could better manage our code and any bug fixes. This release saw our system really come together, because now we have multiple features that work in tandem with each other. The only thing that we would change is making this change earlier in development.

If you would continue developing the project, we will definitely optimize the code of each method more and reduce the number of identical parts between each method. Our project is more accurately a game script, so if we would develop the project, we must consider whether it will affect the overall balance of the game, and the satisfaction of the players after using it. We will optimize or modify each method based on the player's feedback to make the player's experience better. We will also make each function more complete, and make each step of the operation of each function smoother and more complete.

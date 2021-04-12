# Analysis

**Group 10:** _Clash of Clans Auto Player_\
**Date:** April 1st, 2021\
**Group members:** Teng Ao, Miles Brown, Ran Li, Devin O'Neal, Ulugbgek Abdullayev, and Junjian Yin

## 1. Introduction
  In our previous release, we have implemented resource collection feature which was requested as per MVP. Since Clash of Clans is highly object related game, we have had to implement building upgrade queue for our new realse. Now, as a clash of clans player, you can automate building upgrade queue and our program will assign available workers to the essencail buildings that need upgrading.
  
  We have also upgdated a new version of user interface that is bug-free and includes building automation choice at the start of the program. Once the user opts for the building upgrade automation, our product will lounch the emulator and the clash of clans game as well. There are new features like Town Hall upgrade and Gold Storage upgrade and our product will choose which building to upgrade depending on the availability of resources and workers.
  
  Trello Board: https://trello.com/b/y1373xdI/project-board
  
  GitHub: https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player
## 2. Implemented Requirements
  

## 3. Demo
**Link to demo video:** https://youtu.be/E6WXAoOFr0M

## 4. Code Quality
	In order to ensure high quality, we implemented several techniques on this release. Firstly, we separated our code from a single controller file to break it into several reusable code classes that allowed for far more modular code. Splitting code into separate files in this way can sometimes have issues in python, and we ran into some of these while separating our code into smaller chunks, but through some modification we were able to make our changes functional.
	We changed our naming conventions of classes and functions to more accurately reflect the effects and actions they had, with some being changed when we split into classes and some being less accurately labeled in the initial release.
	We also ran tests on several different devices between our group to find issues with compatibility, which found an issue with recognizing images between different computers.
	Lastly we ran code oversight and clear up from other members of the group who were able to clear up and clarify code after the fact and add comments and spacing changes to document.

## 5. Lessons Learned
During the development of this release, we learned how important it is to have modular code. A major part of this release was the refactoring of our existing code into seperate classes so that we could better manage our code and any bug fixes. This release saw our system really come together, because now we have multiple features that work in tandem with each other. The only thing that we would change is making this change earlier in development.

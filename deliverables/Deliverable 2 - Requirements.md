# Deliverable 2: Requirements

**Group 10** - Clash of Clans Autoplayer \
**Group members:** Devin O’Neal, Miles Brown, Junjian Yin, Ulugbek, Ran Li, Teng Ao \
**Date:** 2/20/21

## 1. Positioning
  ### 1.1 Problem Statement: 
  The problem of inefficient and repetitive gameplay loops affects Clash of Clans players; the impact of which is wasting time and checking the phone fretfully .

The problem of
inefficient and repetitive gameplay loops
affects
Clash of Clans players
The impact of which is
wasted time and check phone very fretfully 


Product Position Statement:For Clash of Clans players who don’t enjoy the repetitive gameplay loops and want to succeed in the game, the Clash of Clans Autoplayer is a software that helps you automate all the boring repetitive gameplays and succeed in the game. Unlike MyBot.run, does not overwhelm your device with inappropriate ads and has a user friendly interface

For
Clash of Clans players
Who
Don’t enjoy the repetitive gameplay loops, or wants to succeed in the game
The 
The Clash of Clans Autoplayer
That
Help you play all the boring repetitive gameplays and succeed in the game
Unlike
MyBot.run (competitor)
Our product
Does not overwhelm your device with inappropriate ads and has a user friendly interface

Value Proposition and Consumer Segment:
Value proposition: Save time by automating repetitive tasks in the game and succeed in the game with little to no effort.
Consumer segment: Clash of Clans Player who wants to get their village from zero to hero with better time management.
Stakeholders
Clash of Clans players: is the user directly to our product, wants to have an easier auto play tool to use, hopefully, no ads.
Group 10: we have a manager, quality assurance, developer and product manager in our team, we are providing a powerful and user-friendly auto player.
Clash of Clans: The game that will be auto played by our software, the game company wants the real players to play the game, they may find a way to block the auto player.
Other auto player software: The competitors are providing the similar product as we do.
  Functional Requirements
User-friendly interface
Collect resources in timely manner 
Troop training
Building queues
Simple installation and setup
Autonomous actions after setup
Assign workers depending their availability
Non-Functional Requirements
Automatically and quickly connect between the game and application
Response time between the application and the game should be near-instant
Gameplay actions the autoplayer performs should be done faster than otherwise possible by the player.
 MVP
User-friendly interface,  resource collection, and building queue will be our MVP. resource collection and building queue will use time tracking tools and are very handy for players, but we need a simple GUI so players know how to use it.
 Use cases
Use case diagram

Use Case Descriptions and Interface Sketch
Devin’s Use Case Description:
Use Case: Delete from building queue
Actor: Player
Description: Player wants to delete an action from the building queue
Pre-conditions: The building queue contains an action
Post-Conditions: The building queue contains less or no actions
Main Flow: 
The player sees an action in the building queue that they no longer want there
The player selects the icon in the building queue to remove the action
		Alternative Flow:
The player sees that there is no action in the building queue
No action is taken
		
Miles’ Use Case Description:
Use Case: Turn on resource Collection
Actor: Player
Description: Player wants to enable automatic resource collection
Pre-conditions: Resource Collection is currently off
Post-Conditions: Resource Collection is on
Main Flow:
Player opens UI
Player flips the resource collection switch from ‘off’ to ‘on’

	Ulugbek’s Case Description
Select Urgent Items to auto-upgrade: (Two Worker scenario) Select which item in the village you would like to auto-upgrade and autoplayer will make sure items are queued depending the urgency and availability of the worker. Whether it’s midnight or daytime, auto-upgrade queue will assure that workers are always assigned to certain tasks. 
Flow: 
1. Checks which item takes the shortest period to upgrade 
2. Moves the selected item to the top of the queue 
3. When second worker = free, seeks the second longest item to upgrade and assigns the worker 
4. Third longest time-consuming item is detected and the first worker is assigned
	Junjian’s Case Description
	Use Case: One-click auto play mode
	Actor: Player
	Description: The one-click mode is a model that helps player complete daily tasks in the
game such as resource collection, complete building.
	Pre-conditions: Player wants to use one-click auto play mode
	Post-Conditions: The auto player is not processing any task
	Main Flow:
User open the auto player
Click on one-click mode to turn on
Software will complete daily tasks for the person
Alternative Flow:
Auto player is on other tasks currently

	

Teng Ao’s Case Description
	Use Case: Building construction
Actor: Player
Description: Player wants to take action for buildings
Pre-conditions: The building is in process
Post-Conditions: Have the all precondition to take next action
Main Flow: 
l  The player wants to select the building’s type.
2  The player wants to level up the building automatically.
3 The player wants to set a timer to remind the player to set the next building.
Alternative Flow:
 
The player sees that there is no action in the building queue
There is limited building to set up and no more precondition to take the next move.
It will need more material to level up

Ran Li’s use description
Use Case: Set a timer
Actor: Player
Description: Player wants to be reminded
Pre-conditions: The building is in process
Post-Conditions: The building is under construction
Main Flow: 
1 The player wants to seize the time when the construction is done.
2 The construction is in process
3 The player wants to set a timer to remind the player to set the next building.
Alternative Flow:
The player sees that there is no action in the building
There is limited building to set up and no more precondition to take the next move.

 User stories
As a clash of clans player, I want to achieve higher levels with little effort so I can manage my day better.
As a Clash of Clans player, I want this program to run quickly so I don’t waste time waiting for the software.
As a Clash of Clans player, I want this program to register my inputs reliably for that, I don’t need to input it again.
As a Clash of Clans player, I want to have automatic resource collection without my active input for that, I don’t need to pay any attention to the game.
As a Clash of Clans player, I want to be able to set a building queue for Clash of Clans, for that I don’t have to do it by myself.
As a Clash of Clans player, I want to have no boring gameplay loops during my experience so that I can enjoy another part of the game.
As a Clash of Clans player, I want to collect every resource and finish upgrading buildings on time so that I am successful in the game.
As a Clash of Clans player, I want this program to run with no bugs.
As a Clash of Clans player, I want my buildings to level up continuously so I don’t need to waste time .
As a Clash of Clans player, I want to receive feedback in time so I can think about what I should do for the next steps.
As a Clash of Clans player, I want this program to run quickly.
As a Clash of Clans player, I want to have automatic resource collection without my active input.
 Issue Tracker
Trello Link: https://trello.com/b/y1373xdI/project-board
Screenshot: 



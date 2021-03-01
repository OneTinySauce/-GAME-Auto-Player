# Analysis

**Group 10:** _Clash of Clans Auto Player_\
**Date:** February 28th, 2021\
**Group members:** Teng Ao, Miles Brown, Ran Li, Devin O'Neal, Ulugbgek Abdullayev, and Junjian Yin

## System Description

Clash of Clans Autoplayer will allow players to save time and minimize frustration. Our Autoplayer automates all of the boring parts of Clash of Clans so that you can free up your time to do other things. The system can train your troops, build/upgrade structures, collect your resources, and even take care of destroying rocks and trees for you. Clash of Clans Autoplayer saves you time and helps you enjoy playing the game even more.\

This system will have an opening main page that shows _current statuses of resource collection_, **_troop settings_**, and **_building queues_**. From the status page, a **main switchboard** will be able to be accessed by users, allowing them to turn on and off systems altogether, but not allow for changing of settings within those systems.\

**Elixir collection** settings can be selected, and the _collection loop timer_ can be set and edited, as well as turning on or off **elixir collection**. Max storage will be found, and will test on delay if at _elixir max storage_.\

**Gold collection** settings is a mirror to **elixir collection** settings, but with different areas of the game being tested to find the _gold max storage_.\

From the **main switchboard, troop settings** can also be accessed. The _current on or off status_ will be shown, and from here the user will be able to turn on or off the troop training and access the troop training presets. The troops training presets will be a list of _troops in preset_, which can be edited by the user.\

Also from the **main switchboard**, the **building queue** settings can be accessed. In the **building queue**, the user can add or remove buildings from the **building queue**, as well as view the current _buildings in queue_ and current _on/off status of the queue_.\

The **obstacle destruction settings** can be accessed as a sub menu of the **building queue**, and from them the user can turn on or off the obstacle destruction, and set the _type of obstacles to destroy_.\

Each **building** added to the queue will contain a _name_, and each **obstacle** will include a _name_ and _resource type_.\

The user **account** will contain data on the **account**, including _player name, player level_, and _max elixir_ and _gold storage_ values.\

## Model
![Our UML Class Diagram](https://github.com/OneTinySauce/Clash-Of-Clans-Auto-Player/blob/main/UMLDiagram.jpg?raw=true)

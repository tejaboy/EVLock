# EVLock
Unlocking safe (ev3-powered) via smile detection and/or Discord commands.

A simple Internet of Things (IoT) application that uses the MQTT network to allow communication to takes place between an EV3 Brick and personal computer.

## Getting Started

### Prerequisites

* Visual Studio Code with [ev3dev-browser plugin installed](https://marketplace.visualstudio.com/items?itemName=dlech.ev3dev-browser)
* EV3 Brick with [ev3dev installed](https://www.ev3dev.org/)
* EV3 Robot Built - (LDD file will be provided later)

[Optional]
* Discord Bot's Tokean - if one wishes to send commands via Discord.

### Installing

1. Clone/Download the Repo.

## Running the tests

1. Open up Visual Studio Code.
2. Open Folder (File -> Open Folder -> EVLock/Client)
3. Open another Visual Studio Instance
4. Open Folder (File -> Open Folder -> EVLock/Server)

The Client directory is for the EV3 Brick. The server is for the PC.

On the client, to download the script to the ev3 robot, press F5.
On the server, to start the server, press F5.
(The run settings has already been set in the .vscode folder).

## Built with

* Python
* OpenCV
* ev3dev
* ev3dev-browser
* discord.py

## License

This project is licensed under the ...

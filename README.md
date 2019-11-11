# GeneticAsteroids

A small side project to use a genetic learning algorithm and neural networks to train a computer to play the retro arcade game Asteroids

-------

## Setup:
1. **Install Dependencies**

	````bash
	pip install .
	````

2. **Run Project**

	````bash
	python main.py
	````

-------

## Building:
To package the project into an executable pyinstaller is required:

````bash
pip install pyinstaller
````

You can then pacakge the program by running:

````bash
pyinstaller --onefile main.py 
````

This will create an executable in the dist/ directory

-------

## Project Architecture:

To allow for easy instancing, this project is structured to be object oriented. The classes are organized as follows:

````
├── Game
│       ├── Ship
│       │       ├── NeuralNet
│       │       └── Bullet
│       └── Asteroid
````
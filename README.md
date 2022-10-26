# Experimental Maze with Python and PyOpenGL

Simple 3D maze I built to learn OpenGL. Textures ripped from [Doom II](https://en.wikipedia.org/wiki/Doom_II).

![pyopengl-maze-01](https://user-images.githubusercontent.com/87952/198073750-1d8ee9f1-6a70-48c9-a0e7-2d030c904f9e.png)

![pyopengl-maze-02](https://user-images.githubusercontent.com/87952/198073809-8c461e0b-01a3-486e-8404-7a754af02735.png)

## Requirements

* Python
* [PyOpenGL](http://pyopengl.sourceforge.net/)

Only tested with Python 3.7.2 on [Pop_OS 20.04](https://pop.system76.com/) (basically Ubuntu).

## Running

In the root path, enter: `python3 maze.py`

## Adding textures

Textures must be 8-bit BMP images (max 256 colors)

## Controls

`Esc` = Exit

`W` = Move forward

`S` = Move back

`A` = Turn left

`D` = Turn right

## Things to do

* ~~Collision detection~~
* ~~Free movement~~
* Sprites
* Decals
* Doors
* Animated textures
* Loadable maps

## Things to fix

* Collision detection makes walls sticky
* ~~Cannot move and turn at the same time~~

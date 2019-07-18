# shittycurses README

A small python 3 module that makes it easier to treat a two-dimensional array as a coordinate plane of characters. 
I made this because I wanted to make something like the curses or ncurses library, but cross-platform.
The module was made for my own purposes but if you want to use it, have fun.

It is very easy to use another color module (such as colorama or termcolor) or Unicode codes with this module.

The way I intend for this module to be used is like this: 
A loop keeps clearing and re-drawing the main "grid" (what the module refers to its arrays as).

There should probably be some sort of pause (like a sleep() call from the time module).

The length of the pause can vary depending on how fast you want the program to be. 

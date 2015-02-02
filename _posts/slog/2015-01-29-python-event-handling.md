---
title: Event Handing in Python
author: JC
layout: post
category: slog
---

[Python](https://www.python.org/) can be considered a sequential programming language in the sense that each line of code leads to the next, with very few possibilities to create event based code natively. However, some pseudo-non-sequential code can be implemented in a way that makes sense and provides an additional abstraction level that helps organize a piece of code.

In the course *CSC148* at the University of Toronto, our first assignment was implementing a two-player game system that could utilize a strategy in order to generate valid moves by the PC, and an interface to let the user interact with the game. To me and my partner, it made sense to have some sort of event-driven functions in each part of the code, such that certain functions would be executed when certain conditions were met. In other words, we wanted to have functions that would be executed when certain events where *emitted*.

For example, our abstract *Interface* class looked something like this:

    class Interface:       
        def on_load(self):
            pass # Optional event handler
        
        def on_start(self):   
            pass # Optional event handler
        
        def on_move(self, move, player):
            pass # Optional event handler
    
        def on_end(self):
            pass # Optional event handler

In general, each of these functions is an event hander that *can* be implemented by a subclass that inherits *Interface*. The actual game system takes care of calling the event handlers once certain conditions have been met, such as when the game has been initialized (*on_load*), or when a game has ended (*on_end*). This way of organizing the code in event handlers makes sense mainly because a game is heavily *event-based*. Things do not necessarily happen in a particular order, given that events take place depending on the actions of the user. Therefore, it becomes extremely useful to think of particular user actions as events that trigger the execution of certain functions.

Keep event handling,  
Juan Camilo Osorio
---
title: "Real Life Abstract Data Types"
author: JC
layout: post
category: slog
---

When you are a computer scientist, you begin to see abstract data types everywhere. From the queues to get food at a cafeteria, to stacks of paper in your desk, and even complex objects such as people, which have different properties and methods. You see, this is the very reason why having abstract data types makes sense in the first place: they can be used to model or describe real-world environments or situations. Strings, numbers, and boolean values are seldom useful if you are trying to describe virtually what a person is, or how a line queue operates. Thus, having a type where you can `.enqueue()` and `.dequeue()` people is convenient.

For example, in class, we were asked to implement a *minimax* algorithm in order to play an arbitrary two-person game (such as tic-tac-toe or subtract square). There, we could have used strings to store each state of the game, and would have had to create a crazy function to parse them and apply the moves, generating new states in order to assess what the best move was. But that's insane and counter intuitive. That's why we used recursion and an abstract data type that we created for game states, which allowed us to easily compute new states by applying moves to them, and thus made recursion *100x* easier. What would life be without some good ol' [object oriented programming](http://blog.jcoc611.com/slog/oop-for-dummies) and abstract data types?
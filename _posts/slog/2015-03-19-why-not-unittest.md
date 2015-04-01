---
title: "Why Unit Testing Might Seem Like a Waste of Time"
author: JC
layout: post
category: slog
---

Most of us in first year don't have much (or any) practice in production environments, and we usually work with small code bases and relatively simple software. To me, and many others, unit testing is a complete waste of time, given that we could just check things manually in less time, and our code seldom breaks randomly. If you are one of us who doesn't see much benefit in testing, don't worry, I've been there. 

For example, for the second assignment for CSC148 at the University of Toronto, I spent a good two hours trying to figure out why my doctest wasn't passing, and the reason turned out to have nothing to do with the actual code I had written. I had basically understood doctests wrong for the longest time. The problem was that I was trying to do two things that don't go well together: check for newline characters as part of the result of a function call, and split the lines as to meet the "lines must contain 80 characters or less" style guidelines for the course. You can witness part of my struggle, and how I solved it, in [this StackOverflow question](http://stackoverflow.com/q/28805567/532978).

However, consider a project that has thousands of lines of code and a few thousand methods or functions. Now check each one manually. Not fun, right? My point is that, although unit testing might seem pointless in the early days, it will be more than worth it once you join a company or start your own large code base. Writing documentation and making sure your code works with doctests or unit tests is something that we learn out of context. I think that a great idea that beginner courses such as CSC148 could do is have a class-wide project as part of the course, where unit testing and documenting code suddenly becomes crucial to the success of the project.

One of the things I have done to practice writing good test cases and documentation is go through dozens of API documentations, such as [Facebook's](https://developers.facebook.com/), [Pinterest's](https://developers.pinterest.com/), or [Spotify's](https://developer.spotify.com/web-api/). Although these are mostly web-based, they can help get a general understanding of production-level documentation and testing.

Keep unit testing,  
Juan Camilo Osorio
---
title: "Object Oriented Programming [For Dummies]"
author: JC
layout: post
category: slog
---

As a **Friday the 13th** special, here is my guide to *[spooky]* object-oriented programming for dummies. Regardless of whether or not you are a *dummy* in this subject, I hope this post explains why it makes sense to code in an object-oriented fashion. I will talk about the main concepts in OOP using simple analogies to fictional characters. I won't be including any code, mainly because this is meant to be an intuitive explanation, and should work with pretty much any OOP language.

## Instances

![Jason Vorhees](/images/posts/2015-02-13/json.png) This character is [Jason Voorhees](http://en.wikipedia.org/wiki/Jason_Voorhees), from the franchise [Friday the 13th](http://en.wikipedia.org/wiki/Friday_the_13th_(franchise)). He is an example of a *fictional character*. Of course, there are many similar characters, such as [Freddy Krueger](http://en.wikipedia.org/wiki/Freddy_Krueger) and [Michael Myers](http://en.wikipedia.org/wiki/Michael_Myers_(Halloween)). In programming, we usually call each specific *character* an **instance**, or an **object**; you can think of them as concrete *examples* of a certain *type* of character. Each one of these characters has specific *attributes*, and we programmers specify them like this:

## Properties

<img src="/images/posts/2015-02-13/properties.png" alt="Jason Voorhees Example Properties" style="margin-bottom:20px">

Properties are the various things that make each character, or instance, different from others. In the case of the characters we have already mentioned, each has several characteristics that make them different to each other, such as their *name*, *origin*, and *immortality*. 

A good thing to keep in mind while understanding object-oriented programming is that programmers are *lazy*. We will usually avoid having to write similar code twice; therefore, although each one of these characters is slightly different from the others, it is possible to write code that describes all of them by simply storing their differences as variables, which we call **properties**. Similarly, all of the characters mentioned can **do** very similar things. Programmers handle actions like this:

## Methods

<img src="/images/posts/2015-02-13/dancing.gif" alt="Dance of Death" style="width: 250px;">
Horror movie characters can, among other things, *dance*, *jump-scare*, and *murder*. In programming, each instance has certain actions that you can have them execute. We call these **methods**. Additionally, we call the process of having an instance execute one of its methods a **method call**. For instance (see what I did there?), if `ghoul` referred to the character at your left, an example of a **method call** that got it to dance is `ghoul.dance()`. The great thing about this is that `jason.dance()`, `freddy.dance()`, and similar for other characters *should* work seamlessly too. In order to accomplish this, programmers group all these different characters like this:

## Classes

<div class="pimgcenter">
<img src="/images/posts/2015-02-13/class.jpg" alt="Horror Movie Characters"/>
</div>

You guessed it, each one of these characters is also an **instance**, and has both **properties** and **methods**. However, when we talk about characters being instances, it is important to specify *what* they are instances *of*. In this case, all of these characters are instances, or examples, of *horror movie characters*. Each has different, unique, properties, as we mentioned earlier; however, in general, all of them murder people and scare us in films. Given these similarities, it is often useful to group them into **classes**. Then, it becomes possible to define generic **methods** and **properties** for an entire **class** instead of having to do this for each specific character.

## (Super)classes and (Sub)classes

<div class="pimgcenter">
<img src="/images/posts/2015-02-13/superclass.jpg" alt="Superclass of Characters"/>
</div>

Sometimes, programmers need to group several different **classes**. For example, we might want to have a general class that includes *horror movie characters*, along with any other fictional character. It is easy to imagine that this general class is going to be larger than any of the classes it contains. Therefore, programmers call these big, general classes **super-classes**, and the smaller, more specific classes inside them are analogously called **sub-classes**.

## Why?

Imagine you had to create a program that could run several different two-player games, such as *Chess* and *Tic-tac-toe*. If the number of games was small (such as *one* specific game), it could make sense to write very specific code without the need for an object-oriented structure. However, imagine you had to do pretty much the same thing for *two*, *ten*, or even *hundreds* of games! It would definitely be tedious. It would be great if you could write code for things each game had in common only *once*. If only you had a **super-class** that was general enough to describe *any* two-player game, and then **sub-classes** that represented each specific game; if only each had the needed **properties** such as the rules, and **methods** such as a way to check if a player has won; and if only you could create **instances** of each sub-class each time a specific game was played, right? Well, now you can. There are a *lot* of [OOP tutorials](https://www.google.com/?gws_rd=ssl#q=object+oriented+programming+tutorial+%5Binsert+language+here%5D) for each specific language out there.

Keep coding,   
JC
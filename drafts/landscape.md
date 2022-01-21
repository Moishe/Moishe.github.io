---
layout: post
title: A Landscape Generator
description: A Landscape Generator
permalink: /2022/01/20/Landscape-Generator/
---
One of my favorite things at Recurse so far has been the weekly "Creative Coding" meetup. Every week a group of about half a dozen of us get together and spend about 90 minutes writing code to respond to two randomly selected prompts. For instance, last week one of the prompts was "tech support" so I wrote a thing that creates a Markov chain from the longest Outlook FAQ I could find, and used that chain to build nonsense tech advice. Other people made very clever animations and even interactive games; it's really amazing what can be done in 90 minutes!

Some people choose to pair and others work independently; I've been working independently because working on this kind of problem solo brings me a great deal of joy, but in the spirit of sharing what I've learned I want to start writing up some of my code. Be forewarned, this is simple and silly code, but I *have* learned something new at each of these meetups.

This week the prompts were "hard rain" and "lush green" which to me and others called to mind the Pacific Northwest. I immediately thought of one of my favorite Twitter bots, [Soft Landscapes](https://twitter.com/softlandscapes), and wondered if I could make a grey and green version of it.

In the waiting-for-folks-to-arrive pre-meeting time today, we were talking about Turtle graphics, and how you could create fractals with them. So fractals were on my mind.

Many many years ago I remember trying to write some code that would split up a line recursively, offseting the middle of the line a bit, perpendicular to the existing line. Then with the two new lines, doing the same thing again, etc. This is in some ways the ur-fractal. Anyway way back when I tried to do this I gave up on the math of figuring out the perpendicular line to a line for the offset (in my defense I think I was in 7th or 8th grade, and I've always been bad at math). Here's a picture of what I wanted to do:

![line-break](/images/line-break.jpg)

it was that 3rd step that stuck me all those years ago.
---
layout: post
title: Phsyarum Background
description: Physarum
---

Physarum -- aka slime mold -- is an one-cell organism that displays surprising and beautiful emergent behavior. This [New York Times Article](https://www.nytimes.com/2020/06/16/magazine/the-unexpected-beauty-of-dog-vomit-and-other-slime.html) has some pictures and discussion about the wonders of this organism.

My interest -- and what I'll be discussing here -- isn't so much in the biology of living slime molds, but that they're a perfect example of emergent behavior. I love simple rules that produce unexpectedly beautiful and complicated results when applied at large scale; indeed I think this behavior is my favorite thing about computers. I've been fascinated by this since the very first time I implemented [Conway's Life](thttps://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#:~:text=The%20Game%20of%20Life%2C%20also,state%2C%20requiring%20no%20further%20input.) (and variants of it) on my TRS-80 in the mid-1980s. I even did a science fair project about it during my sophomore year of high school.

I was lucky enough to find (Sage Jenson's excellent writeup of physarum algorithms)[https://cargocollective.com/sagejenson/physarum] and used it to write my first simulation in javascript. I still return to this page regularly for insight and inspiration.

So let's talk about the simple rules of physarum. For purposes of simulation, we can treat physarum as a large number of "actors" which operate independently and communicate with each other by modifying their environment.

Each actor does essentially three things:
* sense
* move
* deposit


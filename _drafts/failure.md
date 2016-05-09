---
layout: post
title: On Failure
cover: trees.jpg
---

(_this is adopted from part of my Last Lecture at Etsy_)

I want to take about failure.

I hate even typing that sentence. Stories of failure, particularly in the tech industry, tend toward the saccarine and banal. We talk about "failing forward," and "embracing failure" but truly failing at something *sucks*. 

There's a word for failing then succeeding at the very thing you failed at in the first place: success. 

Failure is not invariably a thing that drives us towards something positive. I worry that by making every story about failure a veiled story of success, we rob failure of its power and we mask the things that make us human.

But I'm still writing about failure. I want to talk about 3 kinds of failure I've been part of over the past 3 years. They were all painful, in different ways, and 2 of them were just steps toward success.

Maybe I can start by telling a couple of stories.

Sometimes an engineer at Etsy will crash, or nearly crash, the web site. This is _scary as hell_ but because of the nature of Etsy's infrastructure, it's almost always possible to get things back on track very easily. Etsy's designed a system that is incredibly resilient. However, before you live through this experience, it's hard to actually _believe_ that everything's gonna be okay.

When I'd been at Etsy a little while, I needed to run some code that modified a huge number of listings. In engineer-speak, this is called a backfill: you write some code that reads a bunch of entries, makes a change to each entry, and writes the new entry back to the database. Code that does this needs to be designed in such a way that it doesn't run too fast -- writing an entry into a database can, depending on the kind of data you're writing, cause other things to happen, and you need to make sure that the rate of your changes don't overwhelm the system.

So I wrote this backfill code, did what I thought was a good job thinking through the effects of changing the data.

====

(true failure requires a correction on a different plane; )
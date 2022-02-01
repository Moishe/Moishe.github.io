---
layout: post
title: An Actor Class for P5
description: An Actor Class for P5
permalink: /2022/02/01/Actors-for-P5/
---

Yesterday, I wrote a [tiny class](https://github.com/Moishe/p5-director) to make
it easier to create actor-based programs in p5. I've written some variant of this
code about half a dozen times in the past few weeks and I realized it was a little
silly to keep re-writing it.

The main thing this class does is some very very basic memory management. It just
preallocates a fixed-size array, then maintains a free list within that array so
that slots can be re-used. This saves javascript trying to resize arrays as items
are sliced out and pushed to the end, which can cause really obnoxious slowdowns
or even browser crashes.

The code's not super fast and could probably be improved dramatically by someone
with a little bit more knowledge about javascript than me, but it felt good to
write and to get into a state where it's (hopefully) easy to use, even if the only
person to ever use it is me.

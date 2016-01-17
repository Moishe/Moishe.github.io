---
layout: post
title: Ask in Questions
cover: mountain.jpg
---

Despite being a nerd, I was never all that into reading science fiction and fantasy when I was growing up. I tried _so hard_ to like Asimov and Tolkien -- I considered liking them kind of a ticket to entry into the world of people who liked other things I like -- but I don't think I ever finished a single book by either of them.

Then, when I was about 20, I read _The Left Hand of Darkness_ by Ursula K. LeGuin. It not only changed what I thought science fiction books could be but what I thought _books_ could be.

In the [introduction to that book](http://theliterarylink.com/leguinintro.html), LeGuin says something that I've never forgotten:

>The artist deals with what cannot be said in words. 
>
>The artist whose medium is fiction does this in words. The novelist says in words what cannot be said in words.

I found that idea revelatory. It's an elegant expression of, maybe, what literary criticism and to some degree history and every other liberal art _is_ -- the art of uncovering things that can't be spoken of directly; the oblique approach when the direct one fails not despite but because of its directness.

After being actively involved in interviewing for a few years, I realized that deriving answers to unasked questions is at the heart of what great interviewers do. I also realized that questions that are anything _other_ than surface-level starting places -- lights to cast shadows on the cave wall, if you will -- are classic examples of bad interview questions.

Imagine you are conducting an interview where every question you ask would be answered with perfect fidelity. What kind of questions would you ask? Are the answers you'd want even answers to ask-able questions? I assert that what you want is qualitatively un-askable _and_ unanswerable. Unanswerable in words, at any rate.

For instance, something I look for in co-workers is, well, whether they _know how a computer works_. So in our imaginary full-fidelity, absolute-honesty world, maybe I could ask a candidate "hey candidate, do you know how a computer works?" hoping for a magical shortcut. But what would the answer be? If "yes," what does that mean? Does it mean the candidate could give a formal proof of Turing-completeness for an arbitrary set of rules? Does it mean they could explain how a modern processor works in perfect detail? Does it mean they could debug an intermittent failure in minified Javascript? Any of those things might be examples of "knowing how a computer works" but any one of them doesn't imply the others.

Again in this magical full-fidelity and perfectly honest world, imagine you ask a candidate "could you debug an intermittent failure in minified Javascript?" Maybe in this world, they say "yes" and maybe they even point you at an instance when they did exactly that.

I assert that even then the information you've received is useless.

Let's think about what you know, with your perfect fidelity and absolute honesty: you know one particular thing that candidate can do. You don't know why they can do that, or how they do it, or whether they can teach someone else to do it. You don't if they can apply what they know from that particular thing to anything else.

In the spirit of high fidelity and honesty leading to absence of knowledge, I want to briefly talk about _bad_ interview questions. There is a broad class of terrible interview questions I call "vocab" questions, and they basically are all instances of 'tell me the definition of _x_'. These come in lots of different forms, but some common ones are "what is an immutable class?" or "what is a critical section?"

These might be things that the person you're looking to hire should know, if you aren't in a position to mentor and invest in them, but the problem is that the answer only gives you one piece of data. If the candidate answers the question perfectly, what do you know? You know they know the answer to that question, and that's all. If they don't know the answer, what do you know? You know they don't know the answer, and that's all.

So maybe part 1 to being a good interviewer is "avoid vocab questions."

It's deeper than that. I believe that much of the reason for hatred of technical interviews, and the reason they so frequently fail, is because so many interviewers reduce even interesting technical questions to vocab questions.

Let's take one of my favorite questions, [solve a boggle board](http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver). Here's a terrible way to evaluate a candidate's performance in that question:

"$CANDIDATE wrote code to use breadth-first search to find all the strings in the board, and looked up each string in the dictionary to find matches. $CANDIDATE's code for breadth-first search was cleanly written and worked after a couple of minor changes. $CANDIDATE was unable to make further optimizations."

Like the "what's a critical section" question, you have only determined whether the candidate could recognize and code a breadth-first search. You've identified nothing beyond that; you have mapped an infinitesimally small piece of the candidate's [potato-space](/2015/12/16/lowering-the-bar/).

Presumably something else happened in the interview beyond you, the interviewer, presenting the problem and the candidate writing code to solve it. Your job as an interviewer isn't only to ask a question and see if the candidate can answer it correctly -- indeed, that isn't your job _at all_.


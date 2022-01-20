---
layout: post
title: A Story of a Wordle Solver
description: A Story of a Wordle Solver
permalink: /2022/01/20/Wordle-Solver/
---
### A Narrative Journey
Like the rest of the Internet I've been enjoying playing [Wordle](https://www.powerlanguage.co.uk/wordle/) for the past few weeks. While playing it I started thinking about good ways to approach the game, which of course led writing a computer program.

I woke up this past Saturday morning around 4am thinking, "could you enumerate every Wordle game?" That is, could you write a program that cataloged every starting guess and every possible subsequent guess for every solution, then use the data from that catalog to describe a good strategy for guessing? Naïvely, the answer is probably "no" because there are about 12,000 guess words in Wordle and about 2,000 solution words; in the worst case, a program might need to walk roughly 2,000 * 12,000^5 solutions, a staggeringly large space. However, of course, that space is significantly restricted by the game itself, because each guess narrows the search space for the next guess.

So I started writing some Python to see if I could get a handle on the size of the number of legal moves in the game, and maybe see some patterns about what kinds of words to chose when.

I started with [Peter Norvig's corpus of the 1/3rd million most frequent words](https://norvig.com/ngrams/), and wrote a script to grab only 5-letter words from that dictionary. I knew that Wordle's dictionary didn't exactly map to Norvig's dictionary, but I thought that the shape of the words might be enough to see the data I wanted, without spoiling the game for me by seeing the game's actual corpus.

I then wrote some Python code to implement the rules of the game, and then play the game, and score words that led to wins in two ways: ones that matched the most letters, and ones that restricted the search space the most.

When I ran this it was, to put it mildly, discouraging. My script ran okay if I restricted solution words to 200 or so, and guess words to about 300. But it became untenable with larger data sets, slowing down, geometrically, to the point that it would've taken weeks to run. With the smaller corpus it made some interesting predictions. For instance, on one of the runs, it thought that "chuck" might be the best starting guess. That's a terrible starting guess.

I had had fun implementing this but thought it would be useful to walk away from it for a while, because something seemed off. I kept confusing myself about what the simulation was _doing_, which felt like a warning sign. So I put the simulation aside until Sunday morning.

Once again, on Sunday, I woke up early thinking about Wordle solvers. I thought that it might be most efficient to only explore _starting_ words, and the ways they constrained the guesses for the second turn. I could assign a weight to each guess based on the amount of information it conveyed when guessed against each solution. This would eliminate a *ton* of complexity. So my new algorithm would be something like:

```
for each solution:
  for each guess:
    evaluate guess against solution
    store the quality of that guess in an array
```

Then to test the effectiveness of this:

```
sort the array of guesses and quality
for each solution:
  repeat up to 5 times
    pop the first element off the array
    guess that element
    if that guess is correct
      finish
    else 
      restrict the array by results from guess
      continue repeating
```

I coded this up and ran it and the results were disappointing. I implemented a random solver (which used no algorithm at all other than 'pick an available word at random') and, to my dismay, it did *better* than my so-called "optimized" algorithm. Woe is me!

Coincidentally, around this time, a friend posted a link to a [Donald Knuth paper on Mastermind](http://www.cs.uni.edu/~wallingf/teaching/cs3530/resources/knuth-mastermind.pdf), which is a problem that is shaped a lot like Wordle. While reading it, I realized I'd made a really silly mistake: while I was filtering out words based on the matches (letters at locations, letters that existed), I wasn't filtering out words based on the letters that didn't match. This is one of the most powerful filters in the game! Maybe implementing that filter would help my word-ranking.

Also around this time I got my hands on the "real" corpus of words used by Wordle. I asked my source to rot-13 encode them to try to keep them hidden from myself (and, I guess, anyone who looks at my repo on github) and used those words for my guesses and solutions.

So, I added the above logic and re-ran my code, with the official corpus. This time, it outperformed my random guessing (thank god!) but not, really, by a whole lot.

Here's the output, with my two algorithms' results at the top, and then the random solver's results:

```
Running solver
Scanning 2315 solutions
match
  mean:   4.394816
  median: 4
  mode:   4
1 (1   ):
2 (61  ): #####
3 (421 ): #########################################
4 (814 ): ################################################################################
5 (576 ): ########################################################
X (442 ): ###########################################

winnow
  mean:   4.324406
  median: 4
  mode:   4
1 (1   ):
2 (67  ): ######
3 (470 ): ##############################################
4 (806 ): ################################################################################
5 (584 ): #########################################################
X (387 ): ######################################

random
  mean:   4.706695
  median: 5
  mode:   6
1 (0   ):
2 (49  ): #####
3 (281 ): #################################
4 (644 ): ############################################################################
5 (667 ): ###############################################################################
X (674 ): ################################################################################
```

What this means is that my two algorithms *usually* arrived at a solution within 4 or fewer guesses, but also failed to find a solution a little less than 20% of the time. That's much worse than my failure rate since I started playing Wordle.

The random chooser, on the other hand, failed about 30% of the time.

There was something else missing from my implementation, of course. The algorithm above assumes that the "power" of words to find the word is constant even as the set of guesses shrinks, which (of course) isn't true. I modified the algorithm so that, for the first *n* of the ranked words, it would re-rank them based on how well they constrained the remaining guesses.

I thought this worked extremely well and had a delightful few hours of thinking I had done something amazing. These really are great results!

```
smart-match
  mean:   2.215551
  median: 2
  mode:   2
1 (17  ):
2 (1782): ################################################################################
3 (516 ): #######################
smart-winnow
  mean:   2.223758
  median: 2
  mode:   2
1 (13  ):
2 (1771): ################################################################################
3 (531 ): #######################
```

In other words, most of the time this algorithm would find the word in 2 guesses, and never took more than 3.

But that feeling of delight turned into a feeling of dread. It felt too good to be true. Unfortunately, it was. The code that I was using to rank the guesses required knowledge of the solution. Obviously no real solver would allow this! In that sense, my implementation was _terrible_ -- if you know the solution, every guess should be correct on the first try. So, back to the drawing board.

My first attempt at this was looking at letter frequencies and then trying to use that to choose words, eg if you had a lot of words with the letter 'a', but hadn't yet eliminated 'a' from your possibilities, maybe try one of those words. That worked better than before:

```
smart-match
  mean:   4.192225
  median: 4
  mode:   4
1 (1   ):
2 (61  ): #####
3 (508 ): ###########################################
4 (931 ): ################################################################################
5 (550 ): ###############################################
X (264 ): ######################
smart-winnow
  mean:   4.258315
  median: 4
  mode:   4
1 (1   ):
2 (67  ): ######
3 (482 ): #############################################
4 (856 ): ################################################################################
5 (601 ): ########################################################
X (308 ): ############################
```

but still not great, just an incremental improvement.

Wait, though, realized I wasn't omitting a whole set of words: words that had a letter, but in a location we know is invalid. After that change:

```
smart-match
  mean:   4.177106
  median: 4
  mode:   4
1 (1   ): 
2 (99  ): #########
3 (509 ): ##############################################
4 (869 ): ################################################################################
5 (554 ): ###################################################
X (283 ): ##########################
smart-winnow
  mean:   4.166739
  median: 4
  mode:   4
1 (1   ): 
2 (87  ): ########
3 (556 ): #####################################################
4 (839 ): ################################################################################
5 (545 ): ###################################################
X (287 ): ###########################
```

That improved my first two methods even more! But it still felt ... off.

At this point I'd been heads-down on the problem for a few days, and my code was getting ugly. I found some bugs that weren't leading to incorrect results, per se (every win was a real win) but which were making the code behave not as well as it should. I also had lots of weird code paths to accomodate my various methods of searching.

So, on Wednesday (day 5 of this project) I decided to refactor it. This was a delight, and in some ways the best part of the whole project. At this point I had a pretty good grasp of the _shape_ of the problem, and I was able to organize my code in a way that accommodated multiple strategies, but also kept a (still overrideable) core method. The refactor also meant I could incorporate memoization into the foundation of the implementation.

The core algorithm I used for my refactor looks like this:

```
for each remaining guess A:
  for each remaining guess B that isn't A:
    pretend that A is the solution and B is the guess
    calculate a score for how well A would reveal B

use the best score to determine current guess, and repeat
```

This allows me to substitute the "calculate a score" and "best score" parts of that algorithm, as well as giving me a good hook for memoization around the entire algorithm. For that, I make a cache which is keyed on a hash of the list of guesses and stores the best guess from that list.

Running my code after the refactor (and plenty of debugging) led to very satisfying results:

```
random
  mean:   4.186609
  median: 4
  mode:   4
1 (1   ):
2 (86  ): #######
3 (525 ): ###############################################
4 (880 ): ################################################################################
5 (514 ): ##############################################
X (309 ): ############################

matches
  mean:   3.715767
  median: 4
  mode:   4
1 (1   ):
2 (132 ): ###########
3 (890 ): ############################################################################
4 (935 ): ################################################################################
5 (215 ): ##################
X (142 ): ############

winnowing
  mean:   3.638877
  median: 4
  mode:   3
1 (1   ):
2 (131 ): ###########
3 (943 ): ################################################################################
4 (937 ): ###############################################################################
5 (234 ): ###################
X (69  ): #####
```

The `matches` scoring algorithm is "calculate how many letters match the theoretical solution" (if you've played Wordle, how many yellow and green squares you'd get if you guessed B against A) and "whichever guess has the highest number of matches against all the other guesses wins."

The `winnowing` scoring algorithm is "calculate how many guesses would be left after making guess B against A, whichever guess has the lowest average number of remaining guesses wins"

Random is what you'd think, but note that it constrains guesses to words that _could_ match on every turn (if you've played Wordle, it's random, but in hard mode).

I decided to add one last scoring mechanism: I was curious if counting letter frequencies could give good results. I talked to a very smart friend about this late on Wednesday, and that was the mechanism he was using. The letter frequency method has one huge advantage -- its complexity is O(n) where _n_ is the number of guesses, unlike my two methods which are O(n^2), which is what led me to using memoization. I was _sort of_ doing this earlier, but in a not very good way, and redoing it correctly felt right.

The frequency algorithm is similar to the `matches` algorithm described above, but is I think a more elegant implementation of it. Basically, at each of the 5 guess "levels", count up how many times each letter occurs in each guess, and at each location in each word, and store that.

When I was looking at the scores for this, I realized something startling (that astute readers and players of Wordle have probably already realized): Wordle allows _6_ guesses, not the 5 I'd been capping it at! So the above charts treat "more than 5 guesses" as a failure.

Here's the final chart of the various methods, allowing 6 guesses:

```
random
  mean:   4.209071
  median: 4
  mode:   4
1 (0   ):
2 (85  ): #######
3 (489 ): ###########################################
4 (907 ): ################################################################################
5 (589 ): ###################################################
6 (181 ): ###############
X (64  ): #####

matches
  mean:   3.685961
  median: 4
  mode:   4
1 (1   ):
2 (132 ): ###########
3 (898 ): ##########################################################################
4 (960 ): ################################################################################
5 (239 ): ###################
6 (56  ): ####
X (29  ): ##

winnowing
  mean:   3.644060
  median: 4
  mode:   3
1 (1   ):
2 (131 ): ###########
3 (943 ): ################################################################################
4 (937 ): ###############################################################################
5 (238 ): ####################
6 (49  ): ####
X (16  ): #

frequency
  mean:   3.761555
  median: 4
  mode:   4
1 (1   ):
2 (146 ): ############
3 (788 ): #################################################################
4 (965 ): ################################################################################
5 (320 ): ##########################
6 (74  ): ######
X (21  ): #
```

The `frequency` algorithm performed very well, especially given that it runs profoundly faster.

### Conclusions/Thoughts

I never answered my original question ("could you build a map of every possible Wordle game?") because figuring out "what's a good method for solving Wordle" became more fun. I think this is okay! I also have written a framework which would allow me to answer the first question, if (when) I inevitably return to it.

In terms of the other questions I explored, it appears that the `winnowing` method is most effective, but not emphatically so.

I think there are refinements to be made to these algorithms. In particular I'd be curious about adding recursive scoring to explore paths that result from each candidate choice. The most common failure pattern I see is getting into a trap where a lot of words match and no one word narrows the search space more than any other, such as this sequence of guesses:

```
Solution:eater 
guess 1: raise (remaining possibilities: 28)
guess 2: taper (remaining possibilities: 5)
guess 3: later (remaining possibilities: 4)
guess 4: water (remaining possibilities: 3)
guess 5: hater (remaining possibilities: 2)
guess 6: cater (remaining possibilities: 1)
```

(I should note here that this solver was written for "hard mode" where you must use any matching letters; when the guesses aren't constrained by previous guesses the shape of the problem becomes very different)

By guess 2 above, it seems like maybe we should've taken a different path, because the value of any guess relative to another guess is zero. Could we have chosen a different word? Future research is probably warranted!

If you'd like to explore the code or extend it, [here is the repo](https://github.com/Moishe/wordle-exploration).

### Thoughts and Feelings

I intentionally approached this problem naïvely, because I wanted to explore the nature of the problem, rather than implement someone else's work. I am extremely lucky to have time and mental space to do this -- I'm currently doing a 12-week batch at [Recurse Center](https://www.recurse.com/), so my life is more or less completely organized in a way to let me explore problems that catch my eye for the sake of exploring them.

But this got me thinking a lot about how I learn, and I almost always grasp a problem by playing with it. Computers are, it turns out, amazing tools for playing with problems. They help me make lots of mistakes very quickly (as Adam Osborne noted decades ago), and each mistake contributes to my understanding in a way that's qualitatively better (for me) than I could reach from reading about a solution someone else has already found.

Note that I don't think I found the best implementation of a Wordle solver; in fact, I'm quite sure I didn't. But: I think I could have a pretty informed discussion with a lot of people with varying degrees of expertise in this *kind* of problem, now, and that would not have been the case without bumbling around and playing and screwing things up for 5 days.

This sort of exploration via play, as a tool for understanding, seems incredibly valuable to me, and not just in the context of something like Recurse Center. I've had times at jobs when I've been able to explore in this way, and when I've had that space, I've invariably done better work. It's not congruent with the ways many projects are managed these days, and I think that is detriment both to how we work and what we make.

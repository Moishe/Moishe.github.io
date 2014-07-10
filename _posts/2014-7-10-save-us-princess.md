---
layout: post
title: Save us, Princess!

---
On my second day at Etsy, I pushed code to production. I'm below average; almost all engineers push on their first day. When I pushed, I saw this:

_screenshot of old "save the princess with tests" button_

as did every engineer at Etsy, every time they deployed code via Deployinator, which we collectively do about 30 times per day. 

That button is used to push our most recent code to a server that accesses live production data. We use it to test before pushing to production servers. That intermediate server is called 'princess' rather than something more conventional like 'staging' to avoid confusion: 'staging' has many concrete but different meanings; the engineers who named 'princess' wanted a name that was unique (server name-wise, anyway) so that it could have just one concrete meaning. This way, we would avoid the failure mode of, for example, somebody testing code on a "staging" server and thinking that "staging" mean "new code accessing test data" when in fact it was accessing live production data.

I didn't think anything of the phrasing of that button. It seemed like a harmless joke. I am too old to have grown up playing Mario Bros., but I thought it might've been an oblique reference to that game. I never thought about it in any more depth than that.

This may seem unrelated, but indulge me: I have an 8 year old daughter, Amelia, whom I love and who is quirky and weird and awesome and, it turns out, abhors most princesses. Once, someone gave her a tote bag with Disney Princesses on it for her birthday and after everyone left she took the bag up to her room with a Sharpie marker and gave all the princesses mustaches and beards. It took me months to convince her to watch The Princess Bride because of its title. (an aside: her favorite character was the Rodent of Unusual Size, and she cried when Westley killed it) However, she doesn't hate all princesses: her newest favorite book series is Patricia Wrede's Enchanted Forest Chronicles, whose protagonist is a strong, powerful princess named Cimorene.

A few weeks ago, an engineer here at Etsy asked if anyone else was concerned that a primary piece of UI in one of our key pieces of infrastructure could be construed as sexist and/or perpetuating a sexist trope. We had some discussion about it, some ideas were tossed around, but there was a reasonable fear that renaming the 'princess' server would be very difficult and risky. After a few more rounds of discussion another engineer asked, "Perhaps we could just make it say that the princess is saving us?"

Aha.

_screenshot_

It turns out this language not only gets us away from the sexist overtones in the original button and provides a neat counter-narrative to the tired trope, but also actually makes sense:

https://twitter.com/zmagg/status/476871440365805569

I wanted to tell the story of simply renaming the button. But it wasn't until I started writing it that I started thinking about my own daughter, and how I had never drawn the connection between her fierce independence and her dislike of a standard trope -- princesses that need saving -- and the language of something I do almost every day. On reflection, I am very lucky to be surrounded by people who notice things I don't, and bring them up, and fix them -- and how lucky I am to work in a place where it’s easy to do all of those things. Amelia's not deploying code to production yet, but when she does I hope there's a princess there to help her.


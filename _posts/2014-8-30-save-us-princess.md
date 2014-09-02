---
layout: post
title: Save us, Princess!
cover: princess.jpg

---
On my second day at Etsy, I pushed code to production. I'm below average; almost all engineers push on their first day. When I pushed, I pressed a button that said, *"Save the Princess, with Tests,"* as did every engineer at Etsy, every time they deployed code via Deployinator, which we collectively do at least 50 times per day.

That button is used to push our most recent code to a server that accesses live production data. We use it to test before pushing to production servers. That intermediate server is called 'princess' rather than something more conventional like 'staging' to avoid confusion: 'staging' has many concrete but different meanings; the engineers who named 'princess' wanted a name that was unique (server name-wise, anyway) so that it could have just one concrete meaning. This way, we would avoid the failure mode of, for example, somebody testing code on a 'staging' server and thinking that 'staging' mean 'new code accessing test data' when in fact it was accessing live production data. Opinions vary on the exact etymology of the princess server's peculiar name, but the intent was clear: it was deliberately named to be something with no assocations or idioms related to moving code from one place to another and what data that code accesses.

If I thought about the phrasing of that button at all, I probably thought it was a harmless joke. I am too old to have grown up playing Mario Bros., but I thought it might've been an oblique reference to that game. I never thought about it in any more depth than that.

A few weeks ago, an engineer here at Etsy asked if anyone else was concerned that a primary piece of UI in one of our key pieces of infrastructure -- that button, in Deployinator -- could be perpetuating a sexist trope. This was partly prompted by Arthur Chu's excellent [Your Princess is in Another Castle](http://www.thedailybeast.com/articles/2014/05/27/your-princess-is-in-another-castle-misogyny-entitlement-and-nerds.html) article. We had some discussion about it, some ideas were tossed around, but there was a reasonable fear that renaming the 'princess' server would be tricky. After a few more rounds of discussion another engineer asked, "Perhaps we could just make it say that the princess is saving us?"

Aha.

<img src="/images/getsaved.png" width="310">

As is the way of things at Etsy, this idea bounced around a tiny bit more until someone decided to just *do it* -- and they did it, and, as is the way of things at Etsy, pushed it to production within about 15 minutes.

It turns out this language not only provides a neat counter-narrative to a tired trope, but also actually makes sense:

<a href="https://twitter.com/zmagg/status/476871440365805569">
<img src="/images/saved.png" width="585">
</a>

I told this story, pretty much as I wrote it above, when I spoke at The Evergreen State college a little while ago, and it was met with an amount of appreciation that, honestly, surprised me. So I started writing the story down, but as I did, I started thinking about my own daughter, Amelia. Amelia is quirky and weird and (in my totally unbiased opinion) awesome and, it turns out, she abhors most princesses. Once, someone gave her a tote bag with Disney Princesses on it for her birthday and after everyone left she took the bag up to her room with a Sharpie marker and gave all the princesses mustaches and beards. It took me months to convince her to watch The Princess Bride because of its title. (an aside: her favorite character was the Rodent of Unusual Size, and she cried when Westley killed it) However, she doesn't hate all princesses: her newest favorite book series (thanks to [@ansate](https://twitter.com/ansate)!) is Patricia Wrede's [*Enchanted Forest Chronicles*](http://pcwrede.com/books/enchanted-forest/), whose princess-protagonist runs away from home to live with a dragon and -- between discouraging overanxious knights bent on "saving" her -- becomes the dragon's librarian, chef, and an accomplished adventurer and spell-caster. Amelia certainly didn't start dressing up like a princess after reading those books, but she started to realize, I think, that people can be strong and adventurous and smart even if they are dressed like princesses.

As I wrote this, though, I realized I'd never drawn the connection between Amelia's fierce independence and her dislike of a standard trope -- princesses that need saving -- and the language of something I do almost every day. I somehow got inured to it and despite thinking of myself as a feminist, and *despite just reading Arthur Chu's article!* -- it never occurred to me that this UI I was using every single day probably would've infuriated my daughter, with very good reason.

I'm very lucky to be surrounded by people more perceptive than me, and to work in a place where thinking about those things is encouraged, where fixing the text on a button is as easy as it should be. I'm stoked there's a princess there to save me when my code needs it, and to have co-workers who are more observant than me and who see things and fix things I don't see. Changing the text on this button is obviously a tiny little thing and it ain't gonna fix tech's diversity problems by itself and it's not gonna make it less likely that my daughter's love of science gets diminished as she gets older and sees the bullshit gender biases that so many people have, but it's *something* and I hope if we make it easy and right and encouraged to do little somethings one at a time, a whole lot of tiny little somethings will add up.

*Huge thanks to my Etsy co-workers, @zmaggs in particular, for help editing this article*

*Edit 2014-9-2: verified that Arthur Chu's article was a strong prompt for initial email about this problem*

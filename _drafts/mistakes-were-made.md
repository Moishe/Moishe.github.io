---
title: Mistakes Were Made
cover: trees.jpg
---

This is a transcript from a talk I gave at a recent "engineering leadership" offsite at Etsy.

_(this slide intentionally left blank)_
--

Hi there, I’m Moishe. I’m an engineer on the Performance team; before that I was the manager of the Community Engineering team and before that I was a member of the Seller Economics team.

I’m going to talk about talking to users, and sellers in particular. I’m going to talk about this through the lens of my personal experience: this talk is not meant to be a rigorous “how to” guide. There are lots of people at Etsy, many of them in this room, who know far more about talking to our sellers than I do, and who have talked to far more of them than I have. If you’re one of them: this talk isn’t for you. Sorry! You get a consolation prize which I’ll discuss in a second.

My goal in this talk is to convince those of you who haven’t talked to our sellers often, or those of you who lead teams whose members haven’t, to go meet some of our sellers and talk to them in person. It’s mostly fun, I promise, and sometimes it’s not fun, and that’s okay too.

For those of you who already know all the things I’m saying and/or anyone who finds this boring for other reasons, all the slides except 2 of them are still lifes from the 17th and 18th centuries. If you find yourself nodding off, you could look at these paintings and think about the impermanence of all things including, but not limited to, this talk.

![Avi & Amelia](/images/mistakes/avi-amelia.png)
---
So, I want to start by talking about my childhood, if you'll indulge me.

Many of my childhood memories are of my mom sitting at our dining room table, making things. She made quilts, she painted, she made pysanky eggs, she made incredible cards and birth announcements and paper cuts.

On the left is a picture of my daughter and my brother at my childhood home. Things haven’t changed much: my brother’s painting more than my mom now, but you can see the art on the walls and art supplies everywhere and some clutter and mess and maybe you get the sense that that is okay as long as something is being made. 

And you see a kid watching an adult making things, and learning.

On the right is my daughter, applying some of that learning, just straight up painting on the walls, under the watchful eye of some of my brother's art.

![Painting on Walls](/images/mistakes/wall-paint.png)
---
When I walked into Etsy for my interview, it felt like I was coming home. There was weird art, a palpable sense of creativity, a bunch of weird people, and it was all a bit of a mess. There was nobody painting on the walls right then but it sure seemed like someone might, at any minute.

I'd never felt more at home at a place I might work.

After interviewing, I thought a lot about Etsy and its mission. I thought about how different my childhood might've been if Etsy had existed when I was a kid: while my mom's creativity never faltered, we struggled financially, and my mom was never able to generate an income from her art.

I took the job at Etsy with one seller in mind: my mom.

![Table with Lobster, Silver Jug, Fruit Bowl, Violin and Books | Pieter Claesz, 1641](/images/mistakes/claesz.png)
---

For about a year, I learned lots more about engineering at Etsy, but I didn’t meet any sellers. I knew a little bit more about them, but mostly through hearsay or by reading forums. Other than admin who were sellers, the only actual Etsy seller I knew was my mom, who had set up her own shop on Etsy shortly after I started working here.

That changed, serendipitously, in 2014.

As part of the 2014 planning process, I submitted a proposal to improve Etsy Teams. If you haven’t heard of them, Teams are basically a way for sellers on Etsy to self-organize. Teams organize around common interests or geographic location, and some of them are quite big and well-known. These Teams are generally run by one person, called a Captain, and sometimes a few helpers, called Leaders. These Captains and Leaders fill all sorts of roles, from recruiting members to organizing Craft Fairs to kicking obnoxious people off their team and everything in between. These Teams are organized in what are essentially sub-forums on Etsy itself.

Because I was planning to work on improving features related to Teams in 2014, I was invited to give a presentation at the Captain’s Summit in Berlin. If you don’t know about Captain’s Summits (I didn’t before I was invited!) let me give a little bit of background. These summits are organized by Etsy as a place for Captains and some non-Captain Leaders to get together and socialize and tell each other about their teams and what works and what doesn’t and so on. Many Etsy admin put a ton of work into making these things successful: inviting particularly great captains to talk, giving their own talks, making sure everything runs smoothly, etc.

I have, honestly, never had a more transformative work-related experience than I did at that Summit. I thought I knew some things about our sellers: I assumed (correctly) that many of them were very, very good at making things. What I didn't know is that many of them are also incredible business-people, incredible leaders of people, and incredibly good at doing a vast array of very hard things far outside the scope of making what they sell.

I left Berlin after spending time with this amazing group of people -- hearing them present, helping them brainstorm, eating delicious food with them, seeing them literally cry about each other’s successes and failures -- as inspired as I’ve ever been about a job. 

DO NOT TELL MY MOM BUT THESE SELLERS ALMOST TRUMPED MY MOM.

Among other great talks, I heard about organizing a team on a shoestring budget and solely volunteer work to become a social-media powerhouse. I heard about organizing an extraordinarily successful pop-up shop with no money and no time. I heard, amazingly, about the entire Lithuanian team defeating a draconian postage-rate increase by the Lithuanian government.

![Still Life with Asparagus | Adriaen Coorte, 1697](/images/mistakes/coorte.png)
---
So: I came back from Berlin incredibly excited. I had just taken over as manager of what was then the Seller Economics team, which was soon to become the Community Engineering team.

I wanted to give my teammates the chance to share in my excitement and inspiration and positive feelings about our sellers. I wanted them to have the same kinds of experiences that I did, and have a way to think about some of the individual humans who would use the software we were writing. I encouraged everyone on my team to attend Captain’s Summits and Craft Fairs; two members talked at Captain’s Summits (one in Paris and one in London); all of us talked to sellers on Forums and Teams.

One of the people on my team went to a Home for the Holidays event and met a seller who showed him a picture of the house she’d bought with money she made from Etsy. 

Another member of our team described the joy of telling a bunch of Sellers -- in France, through a translator -- about the work she was doing and watching the room react with delight.

![Still Life with Oysters, Lemons and Grapes | Cornelis de Heem, 1660s](/images/mistakes/deHeem.png)
---
While we were building software, and while we were talking to sellers, we started thinking about the idea that we, as Etsy Admin, fill a very similar role for our sellers as our sellers do for their buyers.

Etsy is built on the idea that we can build a more fulfilling and lasting world by increasing the sense of connection between people who make things and people who use those things.

We all, in this room, in Engineering, and everyone who works at Etsy, are actively involved in building a thing. Our users … well, they use that thing by definition, right? So there’s a beautiful parallel between what we -- all of Etsy Admin -- do for our users and what our sellers do for our buyers.

This is happy and positive and full of good feelings, isn’t it?

![Still Life with Oysters, Lemons and Grapes | Cornelis de Heem, 1660s](/images/mistakes/hulsdonck.png)
---
It is happy and positive and so on, but: as we talked to more sellers in person, some things happened.

When I attended the Captain’s Summit in Toronto, I had a very difficult conversation with a Captain who’d built a treasury team. As you may know, Treasury teams are a special kind of team whose members create collections of items, called Treasuries. For a long time, there was a chance that one of these collections would be featured on the Etsy homepage, and there was obviously a huge amount of pride -- not to mention the potential for sales! -- that came with having your Team’s Treasury featured on the homepage. People did a lot of work to try to get featured.

When we launched the Activity Feed on the homepage, we removed Treasuries, and suddenly these Teams had no real purpose any more. There were very good reasons for this (getting featured was a little capricious, we could do a better job personalizing the homepage without treasuries, conversion rates increased). But still: these Teams were full of people who loved making Treasuries, and now there was no purpose to doing that.

So, in Toronto, I spoke to a woman who was devastated by this: she’d been running a Treasury Team for years and cared so much about it and the people on it. I told her the good reasons that we changed the homepage, but her sense of loss was palpable: though she was obviously trying not to, she cried when she told me about the effect our change had on her life. It was awkward, and difficult, and I felt powerless.

One of my teammates met a seller who had been very successful but whose shop just stopped getting traffic. He couldn’t find a great explanation, and the seller was understandably upset. It was awkward, and difficult, and he felt powerless.

It wasn’t like there was some sea change in seller happiness, it was just that we were talking to sellers in person frequently enough that our sample size grew enough to include sellers who were willing to tell us the hard parts, in person.

Then, Etsy re-prioritized its projects, and our team got shifted around, and the things we thought we were doing were no longer the things we were doing. That was awkward, and difficult, and we felt powerless.

![Still Life with Bread | Giacomo Ceruti, ca 1750](/images/mistakes/ceruti.png)
---
Now, we knew our users. We’d been working on projects with an eye towards long-term investment. We could easily think about individual human beings using the stuff we’d been working on, because we’d met them in person. But all of a sudden we weren’t doing those things for those people any more.

I will admit that, for longer than I’d like to admit, I thought that I’d made a terrible mistake. I thought that, in a system where we could suddenly not be doing the things we thought we were doing, that investing the time in building human relationships with our users was for naught. These people were my Facebook friends for god’s sake; they’d hear about this and then they’d write on my wall about how terrible I was and MY MOM would see it!

I thought about the seller I’d talked to in Toronto, and the seller my teammate had talked to in Minnesota, and how disappointed they were at changes we’d made. I thought about all the Captains we’d met in Berlin, and Paris, and London, and how disappointed they’d be.

I thought I made a mistake by getting to know all these sellers and telling them about the work our team was doing. Worse still, I thought I’d made a mistake by encouraging the people on my team to meet sellers and tell them about what we were doing.

I thought, for a while, that I’d made things worse for lots of people -- me, my teammates, some sellers -- by talking to sellers and encouraging my teammates to do the same.

I’ve made lots and lots of mistakes, plenty of them here at Etsy, but I don’t think knowing all these amazing people was one of them.

![Still Life with a Gilt Cup | Willem Claesz. Heda, 1635](/images/mistakes/claesz-2.png)
---
Before I tell you why I don’t think it was a mistake, I want to talk about these still-lifes I’ve been showing you. Still lifes, because they capture a moment in time and attempt to freeze it -- those perfect translucent lemons, those glistening oysters, that perfect bundle of asparagus -- because they attempt to freeze time, they ultimately can do nothing but remind us of its transience. Those lemons have rotted, those oysters are gone, shells and all, that asparagus has turned back to dirt. The artists who painted those beautiful things died long ago. The paint itself is cracking and fading.

Nothing is permanent and very little is predictable, least of all people and the connections people build.

We are building a business based on the connections between people. These connections are beautiful and good. Meeting other human beings is a thing that brings us human beings joy. Watching other people use the things we’ve built is incredibly fulfilling.

But that fulfillment and that joy cannot exist without pain and disappointment and sorrow. Those hard things are an inextractible, essential part of every human connection. Those hard things are immanent in building things that other people use. We, as engineers, are not special in that regard. I promise that for every hardship we endure -- every broken build, every hold in the push queue, every organizational frustration -- each one of our sellers can match it and more: dried-up paint, cracked clay, bad suppliers, derelict buyers, bills that pile up faster than orders.

The fun and joyful things bring us joy; the hard and painful things bring us empathy.

The fulfillment we feel in building Etsy, in reimagining commerce, comes not only from the fun and inspiring times, but also from the things that are hard. I’m asking you to do something -- talk to sellers, in person, face to face -- that is mostly fun and inspiring but inevitably difficult.

Please, go talk to our sellers. They’re a lot like us.

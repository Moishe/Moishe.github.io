---
layout: post
title: Software and craftsmanship

---
A few months ago I bought a Laguiole knife for myself. It took about 3 months to arrive, and when I unwrapped it from its packaging it smelled like wood and smoke and oil. It's not perfect -- the engraving on the back of the blade isn't exactly symmetric, and the wood of the handle has a tiny gap against the butt of the blade. Functionally it's like many other knives, and I could use something which cost about 1/10th what this knife did to the same end. But it's handmade and it's beautiful. The blade is forged and the handle carved and the whole thing assembled in the same town, and when you use it you can think about the fact that the blade was made by one guy, and he's probably been doing it his whole life, and he spends enough time on just that blade to sort of get to know it. There is a particular pattern in the handle, made of brass rivets, which is impossible \(or at least prohibitively hard\) to duplicate by machine, and the guy who carved the handle placed those rivets; again, he had time to think about this particular handle as he was doing it.  
  
I also own a bicycle frame which took about nine months to arrive. One guy designed the geometry and mitred and joined the tubes and sprayed the paint. He had time to think about _me_ while doing this, because he had built another bike for me many years ago, which I rode into the ground and broke, and he saw how the old frame broke and where. When I ride this bike, when I don't completely forget it exists beneath me \(because the cliché is true, it really does disappear\), I can think about the time and pride that goes into building something like this.  
  
What does this have to do with software?  
  
The software you use every day is in a very real sense hand-crafted. It is simply impossible to mass-produce code because the software is the direct result of the person or people who built it; there is no factory, no assembly line, no repetition of creation. Software is labored over in an analogous way to the brazing on my bicycle or the blade on my knife; the person doing it has done similar things many times but none exactly the same; each problem solved in code is unique, as each piece of steel is unique.  
  
Writing code is and should be an exercise in pride and craftsmanship. It is no exaggeration to say that the best software is written with love. Some of my favorite examples are detailed on Andy Hertzfeld's [folklore.org](http://www.folklore.org/) site; for example see the description of [the original Mac's sound driver](http://www.folklore.org/StoryView.py?project=Macintosh&story=Sound_By_Monday.txt&sortOrder=Sort%20by%20Date&detail=medium).  
  


>   
As usual, Burrell's new design was very clever. The Macintosh was already continuously fetching data from memory to drive the video display, interleaving memory bandwidth between the display and processor in a similar fashion to the Apple II. But every 44 microseconds, there was a "horizontal blanking interval" where no video data was needed, so Burrell used that time to fetch data for the sound. That gave us a sample rate of 22kHz, which would allow us to do frequencies up to 11kHz, which isn't too bad.  


  
  
Read that again. What he's saying is that the computer is busy grabbing data from memory to display on the screen most of the time. But if you think about how a CRT is designed, there's an electron gun which scans across the display, then moves down and back to the other side. There's a tiny little gap after every line is drawn when the computer doesn't need to do anything related to drawing stuff on the screen -- so the programmers used that little slice to deal with the sound. Ideas like that come from people who are artists, who obsess over their craft, and who truly love doing so.  
  
Of course not every problem you get to solve as a programmer is so magical; most are mundane. But the mundane problems add up, and if you solve each mundane problem with an eye towards the end, you will transcend the mundane. Incredible software -- my personal list includes but is not limited to the original Mac OS, NeXTstep, Excel, and the new Google Reader -- is the result of thousands of mundane tasks done with pride in addition to the few huge magical leaps and bold strokes of genius.

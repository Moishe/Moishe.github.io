---
layout: post
title: The Windows Shutdown crapfest

---
I worked at Microsoft for about 7 years total, from 1994 to 1998, and from 2002 to 2006.  
  
The most frustrating year of those seven was the year I spent working on Windows Vista, which was called Longhorn at the time. I spent a full year working on a feature which should've been designed, implemented and tested in a week. To my happy surprise \(where "happy" is the _freude_ in _schadenfreude_\), Joel Spolsky wrote an [article](http://www.joelonsoftware.com/items/2006/11/24.html) about my feature.  
  
I would like to try to explain how this happened.  
  
I worked on the "Windows Mobile PC User Experience" team. This team was part of Longhorn from a feature standpoint but was organizationally part of the Tablet PC group. To find a common manager to other people I needed to work with required walking 6 or 7 steps up the org chart from me.  
  
My team's raison d'etre was: improve the experience for users on laptops, notebooks and ultra-mobile PCs. Noble enough. Of course the Windows Shell team, whose code I needed to muck about in to accomplish my tiny piece of this, had a charter of their own which may or may not have intersected ours.  
  
My team had a very talented UI designer and my particular feature had a good, headstrong program manager with strong ideas about user experience. We had a Mac \[owned personally by a team member\] that we looked to as a paragon of clean UI. Of course the Shell team also had some great UI designers and numerous good, headstrong PMs who valued \(I can only assume\) simplicity and so on. Perhaps they had a Mac too.  
  
In addition to our excellent UI designer and good headstrong program manager, we had a user-assistance expert, a team of testers, a few layers of management, and me, writing code.  
  
So just on my team, these are the people who came to every single planning meeting about this feature:  
  


> 1 program manager  
1 developer  
1 developer lead  
2 testers  
1 test lead  
1 UI designer  
1 user experience expert  
\--  
8 people total

These planning meetings happened every week, for the entire year I worked on Windows.  
  
In addition to the above, we had dependencies on the shell team \(the guys who wrote, designed and tested the rest of the Start menu\), and on the kernel team \(who promised to deliver functionality to make our shutdown UI as clean and simple as we wanted it\). The relevant part of the shell team was about the same size as our team, as was the relevant part of kernel team.  
  
So that nets us an estimate -- to pull a number out of the air -- of 24 people involved in this feature. Also each team was separated by 6 layers of management from the leads, so let's add them in too, giving us 24 + \(6 \* 3\) + 1 \(the shared manager\) **43** total people with a voice in this feature. Twenty-four of them were connected sorta closely to the code, and of those twenty four there were exactly zero with final say in how the feature worked. Somewhere in those other 19 was somebody who did have final say but who that was I have no idea since when I left the team -- after a year -- there was still no decision about exactly how this feature would work.  
  
By the way "feature" is much too strong a word; a better description would be "menu". Really. By the time I left the team the total code that I'd written for this "feature" was a couple hundred lines, tops. \[edit: note that that are _tons_ of other more complicated features that support this menu, like the control panel, the additional kernel work, etc., whose code was huge compared to mine. Note also that these features weren't, by a long shot, the only thing all these people were working on\]  
  
But here's how the design process worked: approximately every 4 weeks, at our weekly meeting, our PM would say, "the shell team disagrees with how this looks/feels/works" and/or "the kernel team has decided to include/not include some functionality which lets us/prevents us from doing this particular thing". And then in our weekly meeting we'd spent approximately 90 minutes discussing how our feature -- er, menu -- should look based on this "new" information. Then at our next weekly meeting we'd spend another 90 minutes arguing about the design, then at the next weekly meeting we'd do the same, and at the _next_ weekly meeting we'd agree on something... just in time to get some other missing piece of information from the shell or kernel team, and start the whole process again.  
  
I'd also like to sketch out how actual coding works on the Windows team.  
  
In small programming projects, there's a central repository of code. Builds are produced, generally daily, from this central repository. Programmers add their changes to this central repository as they go, so the daily build is a pretty good snapshot of the current state of the product.  
  
In Windows, this model breaks down simply because there are far too many developers to access one central repository. So Windows has a tree of repositories: developers check in to the nodes, and periodically the changes in the nodes are integrated up one level in the hierarchy. At a different periodicity, changes are integrated down the tree from the root to the nodes. In Windows, the node I was working on was 4 levels removed from the root. The periodicity of integration decayed exponentially and unpredictably as you approached the root so it ended up that it took between 1 and 3 months for my code to get to the root node, and some multiple of that for it to reach the other nodes. It should be noted too that the only common ancestor that my team, the shell team, and the kernel team shared was the root.  
  
So in addition to the above problems with decision-making, each team had no idea what the other team was _actually_ doing until it had been done for weeks.  
  
The end result of all this is what finally shipped: the lowest common denominator, the simplest and least controversial option.  
  
I have no idea how much of the rest of Vista ended up like this. I think \(indeed hope\) my team was a pathological case; unfortunately it's a visible one.  
  
_edits: fixed link, removed some strong language, fixed math_

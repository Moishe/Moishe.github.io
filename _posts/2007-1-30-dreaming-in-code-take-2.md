---
layout: post
title: dreaming-in-code-take-2

---
True story: when I was 18 years old, a series of unhappy accidents left me the only programmer on a massive software project. This project was an upgrade to the cash cow for the company I worked for; if it didn't ship, the company stood to lose lots of money and indeed might've gone out of business. I worked 80-100 hour weeks for months to try to make the thing work right, and every time I fixed a bug it felt like I introduced 2 others.  
  
One night, in the midst of this, I had a vivid nightmare. In this nightmare, I felt sick and feverish; my limbs didn't work correctly and my brain was fuzzy. As I stumbled about, I realized that I _was_ the project I was working on: I wasn't dreaming about working on it, I was dreaming about becoming it. I was a huge collection of code, I was ill and nothing worked right and I had no idea how to fix myself.  
  
When I saw the title of Scott Rosenberg's book, I thought: yes, that's right, that is not nearly so idyllic as it might sound.  
  
And, as it turns out, the subject of the book is not a transcendent glimmering example of software genius. [Chandler](http://chandler.osafoundation.org/newinalpha4.php) is, rather, one of those projects that, I suspect, inspires the sort of dreams one might be glad to wake from.  
  
Another reminiscence, if you will indulge me: when I was 22 years old, I got a job at Microsoft. No bullshit or exaggeration: my dream job. I worked on Outlook, with about 20 other developers and maybe half as many program managers. Most of us were recent college grads or at least \(in my case\) the correct _age_ to have just graduated from college. Our product manager, Brian, had a huge vision for Outlook, and I think we all shared it, and we worked our butts off to make it happen, to the extent that it could. Brian's vision was that Outlook should be an über-PIM, the place to which all your data flow, and the place from which you can see everything. Sound familiar?  
  
Anyone who knows Outlook well must've shared the déjà-vu I felt when I read about Chandler. For instance, its "revolutionary" idea of applying arbitrary views to data was implemented by Outlook in 1994. All the views in Outlook are data-type agnostic; you can apply a calendar view to your files, if you'd like, or a timeline view to your email.  
  
Of course, this sort of abstraction leads to endless feature creep. For instance: did you know that, until Outlook 11, you could browse your files in Outlook, as if it were the Windows shell? It was possible, through some tweaking, to browse the web with Outlook and might still be, for all I know. Did this fit into Outlook's Grand Vision? Absolutely. Did it add unnecessary complexity and make it much, much harder to ship? Hell yes. Chandler is clearly facing similar scoping problems.  
  
Beyond the functional overlap between Chandler and Outlook, there's something else that's interesting. When I first booted Chandler, it took about 45 seconds to start. If you ever used Outlook 97, you may remember a similar experience.  
  
I was on the team responsible for improving performance for Outlook 98. Right after Outlook 97 shipped, my lead printed out **every single function call** made when Outlook started up. It was a stack of paper about a foot high. He spent about a week going through this printout with a highlighter, looking for "stupid shit", as he called it. Turned out, there was plenty of it. It further turned out that most of this "stupid shit" wasn't a result of any one programmer making a dumb decision; most of it was a result of an architecture and a mindset which tried to prevent developers from shooting themselves in the foot by gratuitously abstracting away "dangerous" things like memory management. Again: needless abstraction will bite you in the ass if you're not careful. My lead and I spent months going through the Outlook code exorcising "stupid shit" -- removing code which hid what it was actually doing, getting the code cleaner and closer to the machine, making everything more explicit, tighter, and less generic. I suspect Chandler is going to need someone to go through its code with a fine-tooth comb in the same way before it's viable.  
  
As a programmer, I find abstraction a beautiful idea. In practice, abstraction is useful only when its benefits are concrete. Here is today's Advice To Young Programmers: Create a class you can instantiate _first_; then, only if you need to create a similar class should you create an abstract base. Create an application which solves one problem really, really well; then, if you see that the problem you solved is similar to some others, you'll have a nice framework to expand on.

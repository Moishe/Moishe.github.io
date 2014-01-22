---
layout: post
title: Programming interviews sort of exposed but not really

---
Today while my car was getting an oil change I wandered into Barnes & Noble and browsed through the computer section. I almost bought a book called "Death March" but decided I had other options...

  
I also flipped through a book called [Programming Interviews Exposed](http://www.amazon.com/gp/product/0471383562/qid=1134609245/sr=8-1/ref=pd_bbs_1/002-0056116-6754414?n=507846&s=books&v=glance). I've never actually read one of these books which purports to tell how to answer interview questions at tech companies. If you're thinking about buying this book to help you land a job at a place like Microsoft or Google, don't.

  
The first thing I checked was to see if the book contained the very first interview question I was ever asked, and my favorite. The question is this:

  
**Write a program to draw a circle.**

  
This question is delightful in its depth. It's easy to write a functional solution, and very hard indeed to write a fast and elegant solution. It's such a great interview question because there are a bunch of iterative optimizations to be made; getting to the best solution is like peeling an onion and once you get it, it's beautiful.

  
The book did contain this question, sort of. I'll get to that after I describe what I went through to solve this question.

  
My first solution was something like:  
  

    
    
      
    void DrawCircle(int r, int xCenter, int yCenter)  
    {  
        for (float f=0; f < pi * 2; f += 0.1)  
            {  
                SetPixel(xCenter + cos(f) * r, yCenter + sin(f) * r);  
        }  
    }  
    

  
  
.

  
That works and it was indeed something I'd been playing around with in various permutations for a long time \(in 8th & 9th grade I became obsessed with spirograph-style computer graphics, and started animating them -- the above loop was an instrinsic part of that\).

  
So of course my interviewer said: speed it up.

  
The first thing that jumps out is that there's a lot of symmetry -- you can do simple transformations around the center of the circle to speed this up by a factor of 8. Like so:  


> 
>       
>     void DrawCircle(int r, int xCenter, int yCenter)  
>     {  
>         for (float f=0; f < pi / 4; f += 0.1)  
>             {  
>                 float x = cos(f) * r;  
>                 float y = sin(f) * r;  
>                 SetPixel(xCenter + x, yCenter + y);  
>                 SetPixel(xCenter + x, yCenter - y);  
>                 SetPixel(xCenter - x, yCenter + y);  
>                 SetPixel(xCenter - x, yCenter - y);  
>                 SetPixel(xCenter + y, yCenter + x);  
>                 SetPixel(xCenter + y, yCenter - x);  
>                 SetPixel(xCenter - y, yCenter + x);  
>                 SetPixel(xCenter - y, yCenter - x);  
>         }  
>     }  
>     

  
.

  
Cool, but you're still gonna make pi / 4 \* 10 \(rougly 160\) calls to sin\(\) and cos\(\) -- very, very expensive calls. And if the circle's small, you'll be drawing the same pixel over and over again. My interviewer's next question cut to the heart of both these problems: no more trig functions -- derive sin\(\) and cos\(\) yourself.

  
OK, easy enough, the formula for a circle is _x_2 \+ _y_2 = _r_2. We know _r_, and we can iterate through _x_ values computing for _y_. The only catch is knowing when to stop, and it turns out that's fairly easy: it's when _x_ > _y_ \(since at that point you've crossed a line of symmetry\).  


> 
>       
>     void DrawCircle(int r, int xCenter, int yCenter)  
>     {  
>         float r2 = r * r;  
>         float x = 0;  
>         float y = r;  
>         while (y >= x)  
>         {  
>             y = sqrt(r2 - (x * x)) + 0.5; // round up  
>             x++;  
>       
>             SetPixel(xCenter + x, yCenter + y);  
>             SetPixel(xCenter + x, yCenter - y);  
>             SetPixel(xCenter - x, yCenter + y);  
>             SetPixel(xCenter - x, yCenter - y);  
>             SetPixel(xCenter + y, yCenter + x);  
>             SetPixel(xCenter + y, yCenter - x);  
>             SetPixel(xCenter - y, yCenter + x);  
>             SetPixel(xCenter - y, yCenter - x);  
>         }  
>     }  
>     

  
.

  
OK, cool\! No trig functions, we just use multiplication, addition and... ugh, yeah, sqrt\(\). It's certainly much, much faster than the method above, but it sure looks like it could be better.

  
At this point \(remember, this is my first real programming interview ever -- it was 1994, I was 22, at Microsoft, and scared shitless\) my interviewer said, "great\! Let's make it faster. Now you don't have a math library -- you can only add, subtract and compare integers."

  
Whoa.

  
So now one starts thinking, "I know what pixel I just drew \(it's easy enough to seed this with x=0,y=r\) -- I wonder if there's a way to compute the next pixel based on the last one." Now, you know something about where that next pixel is going to fall -- it's either going to be directly to the right of the current pixel, or it's going to be diagonally down from the current pixel. We know this because the slope from the starting to ending position is -1 -- _x_ has to equal _y_ at some point, and _x_ starts at zero and _y_ starts at some positive integer. So we're going to increment _x_ no matter what, and we may or may not decrement _y_.

  
How do we know whether to decrement y? Aha, there's the rub. Let's think about it this way: is there a way we can tell if we _shouldn't_? Or is there a way to tell that we'll deviate too far from where we should be?

  
Remember the equation for the circle is this:  


>   
_x_2 \+ _y_2 \- _r_2 = 0  


  
So if the above evaluates to something other than 0, we're off from where we should be \(call that the error, e\):  


>   
_x_2 \+ _y_2 \- _r_2 = _e_  


  
If the current _e_ is less than or equal to 0, that means we're "inside" the circle and should merely move to the right. If the current _e_ is greater than 0, we're "outside" the circle and should move diagonally down to stay inside the circle.

  
  
After setting the pixel and modifying _x_ and \(perhaps\) _y_, we recompute _e_ based on our new position. This is where the magic is: we hijack our previous position to compute our new _e_, which means we don't need to calculate any squares or square roots or anything. It just comes down to addition:  
  
We can solve for _e_ given a previous _e_ and a new _x_ \(indicating moving to the right\):  


>   
_e_R = \(_x_ \+ 1\)2 \+ _y_2 \+ _r_2
> 
>   
_e_R = _x_2 \+ 2_x_ \+ 1 + _y_2 \- r2
> 
>   
_e_R = e + 2_x_ \+ 1
> 
>   


  
And a new _x_ and a new _y_ \(indicating moving diagonally\):  


>   
_e_D = \(_x_ \+ 1\)2 \+ \(_y_ \- 1\)2 \+ _r_2
> 
>   
_e_D = _e_ \+ \(2_x_ \+ 1\) - \(2_y_ \- 1\)
> 
>   
_e_D = _e_R \- \(2_y_ \- 1\)  


  
Thus the actual program is this \(note that I moved all those SetPixels\(\) into a \_SetPixelReflected\(\) function for clarity\)  


> 
>       
>     void DrawCircle(int r, int xCenter, int yCenter)  
>     {  
>         int y = r;  
>         int x = 0;  
>         int e = 0;  
>       
>         while (y >= x)  
>         {  
>             if (e > 0)  
>             {  
>                 e -= (y + y - 1);  
>                 y--;  
>             }  
>       
>             e += (x + x + 1);  
>             x++;  
>       
>             _SetPixelReflected(x, y, xCenter, yCenter);  
>         }  
>     }  
>     

  
.

  
When I got that, my interviewer said, "Congratulations. You've pretty much written the circle routine used by Windows." I had about 2 minutes to get to my next interview, followed by 6 more that day, of varying difficulty \(I had harder questions that day, but none as interesting\).

  


## What the book said

  
_Programming Interviews Exposed_ presented this problem as, "draw an eighth of a circle". Already the question has lost some of its charm -- part of the goodness of the question is seeing the simple matrix transform to make 1 calculation equal 8 because of the symmetry.

  
The book presents a solution using sqrt\(\), and claims that since it's an O\(_n_\) solution, it has "the best possible running time". An algorithm's big-O is certainly important, but \(as in this case\) sometimes there are huge differences between different solutions with the same big-O.

  
The final sentence of this problem's solution is, "There are faster circle-drawing algorithms that don't make repeated calls to slow functions like _sqrt\(\)_ or have repeated multiplications, but you wouldn't be expected to implement them in an interview." That's the sentence that really bothered me; the algorithm above isn't necessarily obvious but it's _certainly_ within the realm of what a candidate at Microsoft or Google would be asked to figure out in the course of the interview. If I interviewed a candidate nailed the sqrt\(\) solution, I would press really hard to get to a solution that doesn't involve any function calls. Even if I didn't necessarily expect the candidate to get the exact solution, I'd like to see the thought process that goes into it.

  
The process of solving the question -- not the solution -- is what every technical interview question aims to expose. Good, meaty questions do this very well; there are lots of routes a candidate can go down to get the solution \(and indeed there are other solutions that I didn't go into here\).

  
Anyway, writing this up has inspired me to document more of my favorite interview questions. Look for them in coming blog entries.

  
Note, too, that if you're an interview candidate and get a question you already know the answer to, tell your interviewer. It will be obvious you know the solution and if you try to fake it, you'll just look like an asshole. Chances are good that if you 'fess up, your interviewer will ask you to outline the solution anyway \(a good chance for you to look smart\) and then move on to another question. As in all things interview-related, transparency and honesty are vital.  
  
_\(update: fixed bug in code; y was being incremented if e was too big; should've been decremented -- thanks, Jonas\)_

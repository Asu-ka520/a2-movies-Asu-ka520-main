[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/e0OQHIms)
# CP1404 Assignment 2 - Must-See Movies 2.0 by Hu Zedong

A Python project with GUI and Console programs that (re)use classes to manage a list of movies.

# Project Reflection

## 1. How long did the entire project (assignment 2) take you in working hours?

### Estimate:

I thought it would take about 6-7 hours since I already had assignment 1 working and just needed to convert it to use classes and add a GUI.

### Actual:

It actually took me around 12-14 hours total. I spent way more time on debugging than I expected, especially with the Kivy GUI and getting the JSON file handling working properly

## 2. What are you most satisfied with?

I'm most satisfied with how the Movie and MovieCollection classes turned out. They're clean and reusable - I can use the exact same classes for both the console program and the GUI without any changes. The console program works exactly like my assignment 1 but with better code structure. 
I also like that the GUI actually looks decent and has proper error handling for user input.

## 3. What are you least satisfied with?

I'm least satisfied with the GUI design - it's quite basic and could look much better. The colors are okay but not great, and the layout could be more polished. I also think my error handling could be more robust, especially for file operations. 
Some of my functions are getting a bit long and could probably be broken down further.

## 4. What worked well in your development process?

Writing the classes first and testing them before building the applications worked really well. It meant I could be confident that the core functionality was solid before I started on the UI parts. The step-by-step approach from the assignment helped a lot - doing Movie class, then MovieCollection, then tests, then console, then GUI. 
I also found it helpful to keep my assignment 1 code nearby for reference.

## 5. What about your process could be improved the next time you do a project like this?

I should have spent more time planning the GUI layout before jumping into the code. I ended up changing the layout several times which wasted time. I also should have read more Kivy documentation before starting - I spent too much time figuring out basic things that were probably explained in the docs. 
Better time estimation would help too - I kept thinking "this will just take 30 minutes" and then spending 2 hours on it.

## 6. Describe what learning resources you used and how you used them.

I used the lecture notes and course materials for understanding OOP concepts and class design. The Kivy documentation was essential for learning about GUI components, though it took me a while to find the right examples. I used the Python documentation for JSON handling and some built-in functions. Stack Overflow helped when I got stuck on specific bugs, especially with the file loading issues. 
I also looked at some Kivy tutorials on YouTube to understand how the .kv files work

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

The biggest challenge was getting the Kivy GUI to update properly when movies were marked as watched/unwatched. The buttons wouldn't change color at first, and it took me ages to figure out I needed to call create_movie_buttons() again to refresh them. 
Converting from CSV to JSON format was trickier than expected - I had to completely rewrite the file handling code. 
I also struggled with the .kv file syntax at first and had some path issues with loading the file. I overcame these by lots of trial and error, reading documentation more carefully, and breaking problems down into smaller parts to debug step by step

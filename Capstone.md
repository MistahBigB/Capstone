
# Capstone Proposal

The Capstone is a web application that touches on every major technology we covered: Python, HTML, CSS, JavaScript, and Django. Below are the criteria for your proposal. It's difficult to be certain how long each feature will take to develop. Therefore you should plan out multiple 'milestones' for your project. That way, if you reach milestone 2 but not 3, you still have something worthwhile to present and be proud of. It also gives you the opportunity to plan out what you'd like to work on after the class is finished. I can help you sculpt out an idea, and I'll tell you very plainly whether a goal is attainable given our time constraints. I highly recommend doing some sketches of pages. This document is for you as much as it is for me. By planning thoroughly and precisely, the implementation will be much easier. Please do not change your idea after we start working on our capstones, it wastes your time and your end result won't be as good. Your proposal is due by the time we start our capstones (3-4 weeks before the end of the course).

- Your proposal must set specific and attainable goals
- Your proposal must cover all major topics we've covered
- Your proposal must include the sections below
- Your proposal must be in a markdown `.md` file [more info](https://help.github.com/articles/basic-writing-and-formatting-syntax/)

## Name
WITNESS: the Fitness App

## Project Overview
I want to create a fitness tracking app that helps users set goals, build custom workouts or have the program provide one, record and track progress (recalculating as necessary), and finally, achieve those goals. 

## Features
As a person concerned with their health, I want an app that can help me set, track, and achieve fitness goals with minimal input.
As a coach helping others with their goals, I want an app that can help me set, track, and achieve fitness goals for multiple people with great detail.

Tasks =>
Provide login security
Allow users to see other people's posts with privacy controls

Provide inputs to set starting ability/weight
Provide input for before photo
Provide input for desired outcome
Provide input for what length of time planned to achieve goals

Provide a screen to build a plan
Provide a list of workouts to choose from
Provide the ability to load/save/edit different workouts
Provide computer generated plans

Provide a calendar to pin workouts to days

*Stretch: algorithm to determine the realism of user goals
*Stretch: injuries etc., which would disqualify certain exercises
*Stretch: user being able to build multiple plans, e.g. as a coach with clients
*Stretch: individual pages for exercises, including Youtube links, still photos, written instructions, etc.
*Stretch: provide encouragement in the form of achievements/trophies/etc when goals are reached, new high performances, etc.
*Stretch: graph the progress of the user as they progress
*Stretch: provide a stopwatch for rests, cardio, planks, etc

#### Questions to ask yourself about functionalities
What will the user see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?

Login page

Inputs page: Name, photo, gender, height, weight, age, strength
Ask: what are the users goals: 
Input: goals, timeline
goals allows a quantity to be added to act as a multiplier, i.e. a person wants to lose X amount of weight, push Y amount more

Exercise Page: list (no limit to number of exercises on list, repeats allowed):
10x exercises each for arm, leg, back, core
10x warmup exercises
4 buttons to randomly select an exercise randomly based on arm, leg, back, core
Button to save, name/id required for list

List of exercises on a page? Or straight to the calendar? (Nice to have a page of exercise notes?)
Button to randomly generate a complete workout based on arm, leg, back, core
Button to see all saved workouts
Button to edit saved workouts
Button to make a new workout

Calendar looks like Google Calendar, except instead of setting an appointment, user pins a workout
Options to add a workout directly to the calendar? Build/save a new workout to the calendar, edit one previously

## Data Model
Username tied to user info: name, photo, gender, height, weight, age, strength
height/weight/gender/age/strength tied to expectations

Exercises have: muscles used, weights/body_weight/cardio

Muscles belong to a class of arm, leg, back, core

Exercise in calendar needs to have weight/reps (Does this need to be a part of the original set of attributes) YES
List of exercises in calendar needs to have checklist (exercise list becomes a todo app)

What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'. These are *schemas* for your data models (database tables).

## Schedule
Week 1: Build API Exercise list, todo app for exercises
Week 2: Build Calendar, attach lists
Week 3: Login, algorithm
Week 4: Feasibility of users goals
Week 5: Graph of goals

Here you'll want to come up with some (very rough) estimates of the timeframe for each section, as well as milestones. State specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.

### Agiles/Scrum Methodology and Workflow
We're going to be following a modified [Agile/Scrum](https://linchpinseo.com/the-agile-method/) workflow. Most software development teams follow Agile/Scrum methodology, so we're going to as well. The difference is that rather than working on a team, you'll be working as a team of one with me as your *Scrum Master*. 

#### Iterative Development
Agile development is **iterative development**. The goal is to set short sprints (1-4 week intervals), where at the end of each sprint you have a **minimal viable product**, or **MVP**. This means you have a functioning, *end-to-end* application at the end of each iteration.

So, rather than spend a huge amount of time building up the infrastructure for your application (i.e. setting up the wheels and frame for a car) and not have a complete, shippable product until the very end of the process, you build MVPs each sprint (i.e. start off with a scooter, then bike, then motorcycle, until eventually you have a car). 

![MVP diagram](./Making-sense-of-MVP-.jpg)

This way, you can fall back to a shippable, completed product at any phase. Also, if your requirements change (as they often do) midway through development, your product can much more easily adapt to changing needs since you haven't locked yourself in with an extensive infrastructure.

#### Setting up MVP
E: Login page
E: Input page

E: Workout list with attributes
R: Workout list with sorting by attributes
N: Workout list with sorting and descriptions

N: Drag and drop workout to workout list CRUDL

E: Calendar page
E: Pin workout to calendar day
R: Track progress
N: Set milestones
N: Home page with tracking and milestones 

You want each of your milestones to result in a minimal viable product. For each milestone, take a few features off of your **product backlog** (the set of user stories you have defined). 

Generally, you want to rank your product backlog in terms of:

- Essential features
- Really-great-to-haves
- Nice-to-haves

Each MVP must be a completed *end-to-end product*. What this means is you need a functioning back-end connected to a functioning front-end. Get all your models, views/templates, and controller/views connected.

Daily:

Week1:
1/16: Data structure synthesized, API built, database relationships set up. We can make exercises and assign them to workouts
1/17: Write basic html, JS inputs with Vue components
1/20: Have axios/Vue call the database thru the API, have the buttons display data
    Search function required heavy Serializer modification
1/21: Have the buttons display data, get dropdown working
1/22: save data to workout/superset (chasing bugs)
1/23: save data to workout/superset, display 2 containers, make selector for workout list and currently active workout, style buttons 
1/24: Solve this 400 bad request error when attempting to post, make selector for workout list and currently active workout, have only the items in active workout display, display all data in active workout MILESTONE!!!!

Week2:
1/27: Users!
1/28: Ensuring user CRUDL, display workout names/links on user page, signup page, permissions to post/retrieve workouts
1/29: Adding workouts of any kind gives a 403. Delete individual exercises in a workout button. CODE FREEZE, MAKE A FORK
1/30: Calendar using the Calandly links!


    Blocks/bugs:
            Would like to have new list be default on rerender
            rep and weight inputs are still all linked --> hide rep/weight until ex is selected, reveal fields for one ex
            List of workouts displayed on user's home page
            
    Blocks/bugs solved: 
            Add exercise needs to refresh the current workout to show the recent addition -> check rerendering of state for VUE
            Add exercise is displaying an extra blank container when the button is pressed
            Delete button takes up 25% of screen
            Can't add to the first workout in the list --> id=0 is not the same as pk=0
            

Presentation: Login page --> Sign up --> make user --> log in as user

Check my calendar, showing no entries
mention a link to put in place user registration, hardcoded today

Create a workout button 
Create two workouts --> Crazy, Cool
Select workout from dropdown that appears

Give me something to do right now! enter W/R, add, clear exercise
Search for bench press --> enter W/R, add
Browse by muscle group --> Back, show whole list, enter W/R from top entry, clear
Browse by muscle group --> Core, show whole list, show that PUSHUPS is on both lists, enter W/R from top entry, clear 

Schedule this workout! 

That workout actually looks pretty terrifying, I think we're just going to delete it. 

Delete workout, select the other from the dropdown, show that the other one is no longer accessible.

Stretch goals: tracking, adjusting based on data, different calendar to track data, users having multiple clients that they're training, full list of pre-built workouts based on what HHS thinks a human can do, adjusting those numbers to meet user goals

favorite part: When the API call successfully returned a random exercise to the screen, based on a button click

hardest part: rebuilding this main page to include author in all relevant fields once users had been added



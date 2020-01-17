
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

You want each of your milestones to result in a minimal viable product. For each milestone, take a few features off of your **product backlog** (the set of user stories you have defined). 

Generally, you want to rank your product backlog in terms of:

- Essential features
- Really-great-to-haves
- Nice-to-haves

Each MVP must be a completed *end-to-end product*. What this means is you need a functioning back-end connected to a functioning front-end. Get all your models, views/templates, and controller/views connected.

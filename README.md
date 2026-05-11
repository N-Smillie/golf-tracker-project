# UX
## Project Goals
The goal of Golf Tracker is to provide users with an intuitive and responsive web application for recording and reviewing golf rounds. The application allows users to record their full 18 hole scores as well as front or back 9 hole scores, compare their performance against par, and see their improvement over time through a clean and user-friendly dashboard.

The project was designed with a focus on:
* Creating an intuitive and responsive user experience across all device sizes
* Allowing users to record and review golf scores during or after a round
* Providing meaningful statistics and historical data to help users track performance
* Implementing CRUD functionality using Django models, views and templates
* Building a visually polished and consistent application using Bootstrap and CSS styling

## User Stories
As a user, I want:
1. To create an account, so that I can save and track my golf scores over time

    **Acceptance Criteria**
    * User can access a registration page
    * User must enter username and password
    
    ![Signup Page](docs/images/signup-ss.png)

2. To log in to my account, so that I can access my previous rounds and personal statistics

    **Acceptance Criteria**
    * User can access login page
    * Valid credentials log user in successfully
    * Invalid credentials display an error message

    ![Login Page](docs/images/login-ss.png)

3. To choose a golf course before starting a round, so that the correct holes and par values are loaded

    **Acceptance Criteria**
    * User can view list of courses from database
    * User can select a single course
    * Selected course is stored for the round

4. To select whether I am playing the front 9, back 9, or full 18 holes, so that the application shows the correct holes

    **Acceptance Criteria**
    * User can select front 9, back 9, or full 18 holes
    * Selection is required before starting a round
    * Correct holes are loaded for the round

    ![Start Round Page](docs/images/start-round-ss.png)

5. To input my strokes for each hole, so that my performance is recorded accurately

    **Acceptance Criteria**
    * Each hole has a score input field
    * Only valid numbers are accepted
    * Each score is linked to correct hole and round

6. To see whether I am over or under par for each hole, so that I can understand my performance throughout the round

    **Acceptance Criteria**
    * Par is calculated correctly
    * Each hole shows score vs par
    * Results update after saving scores

    ![Score Input Page](docs/images/score-entry-ss.png)

7. To see my total score and overall performance after finishing a round, so that I can evaluate how well I played

    **Acceptance Criteria**
    * Total strokes are calculated correctly
    * Total par is calculated correctly
    * Overall score (over/under par) is displayed

    ![Stats Dashboard](docs/images/stats-dashboard-ss.png)

8. To view my previous rounds, so that I can track my progress over time

    **Acceptance Criteria**
    * User sees only their own rounds
    * Each round shows date, course, and score

    ![Round History Page](docs/images/round-history-ss.png)

9. To delete an unwanted round, so that I can remove incorrect or unnecessary records from my history

    **Acceptance Criteria**
    * Users can delete an unwanted round
    * A confirmation modal appears before deletion

    ![Round Deletion](docs/images/delete-round-ss.png)

## Wireframes
## Design Choices
### Color Scheme
### Fonts
### Layout
### Imagery

# Database Design
## Models
## Relationships

# Features
## Existing Features
## CRUD Functionality

# Technologies Used
## Languages
## Frameworks & Libraries
## Tools

# Testing
## Manual Testing
## User Story Testing
## Controls
## Responsive Design
## Visual Feedback
## Validator Testing
## Bugs & Fixes

# Deployment
## GitHub Deployment
## Heroku Deployment

# Credits
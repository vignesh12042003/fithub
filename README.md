FITHUB – Personal Fitness Tracking Platform

FITHUB is a full-stack Django web application that helps users monitor and improve their fitness through BMI tracking, personalized exercise recommendations, and daily habit logging.

The platform is designed with clean architecture, user-specific data handling, and production-ready practices.

🚀 Features
Authentication

Secure user registration and login

Session-based authentication

User-specific data isolation

BMI Tracking

BMI calculation using height and weight

Automatic category classification (Underweight, Normal, Overweight)

Persistent BMI history

Dashboard with latest and historical records

Exercise Recommendations

Dynamic workout suggestions based on BMI category

Structured exercise cards with guidance

Category-based workout sections

Daily Fitness Tracker

Daily habit checklist system

Automatic progress percentage calculation

One log per user per day (data integrity enforced)

Historical tracking of completion rates

🛠 Tech Stack

Backend:

Python 3.12

Django 6

Database:

SQLite (Development)

Frontend:

HTML5

CSS3 (Custom UI Styling)

Django Template Engine

Architecture:

Multi-app modular Django structure

ORM-based relational modeling

Environment variable configuration for security

📂 Project Structure
accounts/        # Authentication logic
fitness/         # BMI & Exercise modules
habits/          # Daily tracking system
static/          # CSS and static assets
templates/       # HTML templates
fithub_project/  # Core project settings

⚙️ Local Setup

Clone the repository:

git clone <your-repo-url>
cd fithub_project


Create virtual environment:

python -m venv venv


Activate environment:

Windows:

venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Create admin user:

python manage.py createsuperuser


Run server:

python manage.py runserver

🔐 Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_secret_key_here
DEBUG=True

🧠 Data Modeling

User → BMIRecord (One-to-Many)

User → DailyHabitLog (One-to-Many)

DailyHabitLog → FitnessHabit (Many-to-Many)

Unique daily constraint per user

📌 Future Improvements

PostgreSQL production configuration

Analytics dashboard with charts

Calorie tracking API integration

Deployment on cloud platform (Render / Railway / AWS)

📊 Project Level

Category: Full-Stack Web Application
Level: Intermediate Django Application
Focus: Authentication, ORM modeling, modular architecture, user-based data management
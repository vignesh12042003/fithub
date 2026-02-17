FITHUB – Personal Fitness Tracking Platform

FITHUB is a full-stack Django web application that helps users monitor and improve their fitness through BMI tracking, personalized exercise recommendations, and daily habit logging.

The platform is designed with clean architecture, user-specific data handling, and production-ready practices.

🌍 Live Demo

👉 https://fithub-98q3.onrender.com/

🚀 Features
🔐 Authentication

Secure user registration and login

Session-based authentication

User-specific data isolation

📸 Login & Signup Interface

🧮 BMI Tracking

BMI calculation using height and weight

Automatic category classification (Underweight, Normal, Overweight)

Persistent BMI history

Dashboard with latest and historical records

📸 BMI Calculator

📊 Dashboard

Displays latest BMI result

Shows total records

Clean structured table history

User-personalized experience

📸 Dashboard View

🏃 Exercise Recommendations

Dynamic workout suggestions based on BMI category

Structured exercise cards with sets & reps

Category-based workout sections

📸 Exercise Module

📅 Daily Fitness Tracker

Daily habit checklist system

Automatic progress percentage calculation

One log per user per day (data integrity enforced)

Historical tracking of completion rates

📸 Daily Tracker

🛠 Tech Stack
Backend

Python 3.12

Django 6

Database

SQLite (Development)

Frontend

HTML5

CSS3 (Custom UI Styling)

Django Template Engine

Architecture

Multi-app modular Django structure

ORM-based relational modeling

Environment variable configuration for security

📂 Project Structure
accounts/        # Authentication logic
fitness/         # BMI & Exercise modules
habits/          # Daily tracking system
static/          # CSS and static assets
templates/       # HTML templates
screenshots/     # Project UI screenshots
fithub_project/  # Core project settings

⚙️ Local Setup
1️⃣ Clone the repository
git clone https://github.com/vignesh12042003/fithub_project.git
cd fithub_project

2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate environment

Windows:

venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run migrations
python manage.py migrate

6️⃣ Create admin user
python manage.py createsuperuser

7️⃣ Run server
python manage.py runserver

🔐 Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_generated_secret_key
DEBUG=True


For production:

DEBUG=False

🧠 Data Modeling

User → BMIRecord (One-to-Many)

User → DailyHabitLog (One-to-Many)

DailyHabitLog → FitnessHabit (Many-to-Many)

Unique daily constraint per user

📌 Future Improvements

PostgreSQL production configuration

Analytics dashboard with charts

Calorie tracking API integration

Advanced progress visualization

Role-based admin insights

📊 Project Classification

Category: Full-Stack Web Application
Level: Intermediate Django Application
Focus: Authentication, ORM modeling, modular architecture, user-based data management

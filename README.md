# FitHub – Fitness Tracking Platform

A full-stack Django web application that empowers users to monitor and improve their fitness through BMI tracking, personalized exercise recommendations, and daily habit logging.

---

## 🌍 Live Demo

👉 **[https://fithub-98q3.onrender.com/](https://fithub-98q3.onrender.com/)**

---

## ✨ Features

- 🔐 User authentication (login/signup)
- 📊 BMI calculator with history and categorization
- 🏃 Personalized exercise recommendations based on BMI
- 📅 Daily fitness habit tracker with progress tracking
- 🎨 Responsive dark theme UI

---

## 🛠 Tech Stack

- **Python 3.12** & **Django 6.0.2**
- **SQLite** (development) / **PostgreSQL** (production)
- **HTML5, CSS3**
- **Gunicorn, WhiteNoise**

---

## 📂 Project Structure

```
fithub_project/
├── accounts/                 # User authentication
├── fitness/                  # BMI & Exercise modules
├── habits/                   # Daily tracking system
├── templates/                # HTML templates
├── static/                   # CSS & images
├── fithub_project/           # Project settings
├── manage.py
├── requirements.txt
├── .env                      # ⚠️ MANDATORY
└── Procfile
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip & Git

### 1. Clone Repository
```bash
git clone https://github.com/vignesh12042003/fithub_project.git
cd fithub_project
```

### 2. Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. ⚠️ MANDATORY: Configure Environment Variables

Create `.env` file in project root:
```env
SECRET_KEY=your_generated_secret_key_here
DEBUG=True
```

**How to generate SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy the output and paste it in `.env`

### 5. ⚠️ MANDATORY: Database Setup

**For Development (SQLite)** – No action needed, default in `settings.py`

**For Production (PostgreSQL):**

Update `fithub_project/settings.py`:
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://user:password@localhost:5432/fithub_db'
    )
}
```

Or set in `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/fithub_db
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Start Server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## 🧠 Key Features Explained

### BMI Calculation
```python
BMI = weight (kg) / height² (m²)
```
- **Underweight**: BMI < 18.5
- **Normal**: 18.5 ≤ BMI < 25
- **Overweight**: BMI ≥ 25

### Exercise Recommendations
- **Underweight**: Muscle building (Push-ups, Squats, Planks)
- **Normal**: Balanced fitness (Jogging, Crunches, Stretching)
- **Overweight**: Low-impact fat burn (Walking, Cycling, Wall Push-ups)

### Daily Habit Tracker
- Track 5 habits: Exercise, Water intake, Stretching, Fruits, Sleep
- Real-time progress calculation
- One log per user per day

---

## 🔗 API Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/accounts/login/` | GET/POST | Login |
| `/accounts/signup/` | GET/POST | Registration |
| `/` | GET | Home page |
| `/bmi/` | GET/POST | BMI calculator |
| `/dashboard/` | GET | User dashboard |
| `/exercise/` | GET | Exercise recommendations |
| `/habits/` | GET/POST | Daily habits |

---

## 📊 Database Models

**BMIRecord**
- user, height, weight, bmi_value, category, created_at

**FitnessHabit**
- name, is_active

**DailyHabitLog**
- user, date, completed_habits, completion_percent
- Constraint: One log per user per day

---

## 🚀 Deployment

### Render.com
1. Push to GitHub
2. Connect repository to Render
3. Set `SECRET_KEY` in Render environment variables
4. Set `DATABASE_URL` if using PostgreSQL
5. Auto-deploy on push

### Heroku
```bash
heroku login
heroku create fithub-app
heroku config:set SECRET_KEY=your_secret_key
git push heroku main
heroku run python manage.py migrate
```

---

## 🐛 Troubleshooting

**ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Database locked**
```bash
rm db.sqlite3
python manage.py migrate
```

**Static files not loading**
```bash
python manage.py collectstatic --noinput
```

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Vignesh S** – [GitHub](https://github.com/vignesh12042003)

**Live:** [https://fithub-98q3.onrender.com/](https://fithub-98q3.onrender.com/)
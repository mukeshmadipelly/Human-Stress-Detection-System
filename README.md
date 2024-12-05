---

# SmartMate

SmartMate is an intelligent health-tracking web application designed to monitor and manage mental wellness. Leveraging Artificial Neural Networks (ANN) and psychological data, it provides stress level predictions and actionable insights to improve mental health.  

This project offers a user-friendly interface and intuitive navigation, making it easy for users to input their data, analyze stress levels, and view results, all while ensuring a professional and appealing web design.

---

## **Features**
- **User Authentication:**
  - Login, Sign-Up, and Forgot Password functionality.
  - Secure user management with MySQL integration.

- **Data Input:**
  - Collects psychological data such as:
    - Heart rate, snoring rate, body temperature, limb movement, sleep hours, respiratory rate, blood oxygen level, and eye movement.
  
- **Stress Analysis:**
  - Uses an Artificial Neural Network (ANN) to predict stress levels based on user inputs.

- **Profile Management:**
  - Displays user details, weekly and monthly stress analysis, and stress trends.
  - Includes a customer support feature for personalized assistance.

- **Homepage Features:**
  - Provides navigation to key sections: Login, About, and Support.
  - Highlights the project's purpose and functionality.

- **Database Integration:**
  - Stores user information, psychological data, and stress analysis results in a MySQL database.

---

## **Tech Stack**
- **Frontend:**
  - HTML, CSS.
  
- **Backend:**
  - Django (Python framework for web development).

- **Database:**
  - MySQL for storing user data and analysis results.

- **AI/ML:**
  - Artificial Neural Network (ANN) for stress detection and prediction.

---

## **Project Setup**

### 1. **Clone the Repository**
```bash
git clone <https://github.com/mukeshmadipelly/Human-Stress-Detection-System>
cd djangoproject
```

### 2. **Install Dependencies**
Make sure you have Python installed, and then install the required Python packages:
```bash
pip install django mysqlclient
```

### 3. **Set Up the Database**
- Create a database named `human_stress` in MySQL Workbench.
- Update `settings.py` in the `DATABASES` section with your MySQL credentials:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'human_stress',
          'USER': '<your_mysql_user>',
          'PASSWORD': '<your_mysql_password>',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

- Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. **Run the Server**
Start the Django development server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser to access SmartMate.

---

## **Django URL Routes**
| URL Path        | Purpose                      |
|------------------|------------------------------|
| `/`              | Homepage                    |
| `/about/`        | About page                  |
| `/support/`      | Support page                |
| `/login/`        | Login page                  |
| `/signup/`       | Sign-Up page                |
| `/dataentry/`    | Data Entry page             |
| `/result/`       | Results page                |
| `/profile/`      | User Profile page           |

---

## **Folder Structure**
```plaintext
SmartMate/
├── manage.py
├── templates/
│   ├── homepage.html
│   ├── about.html
│   ├── support.html
│   ├── login.html
│   ├── signup.html
│   ├── dataentry.html
│   ├── result.html
│   ├── profile.html
├── app_name/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
└── db.sqlite3
```

---

## **How It Works**
1. **Homepage:**
   - Introduction to SmartMate with navigation buttons for Login, About, and Support.

2. **User Authentication:**
   - Securely sign in or register to access the platform.

3. **Data Input:**
   - Enter psychological parameters on the data entry page.

4. **Stress Analysis:**
   - View detailed analysis and predictions on the results page.

5. **Profile Management:**
   - Manage personal details, analyze stress trends, and contact support.

---

## **Screenshots**
### 1. **Homepage**
*Hero section with a call-to-action button directing users to the login page.*

### 2. **Data Entry Page**
*Interactive form to enter psychological parameters.*

### 3. **Results Page**
*Displays stress predictions and trends using ANN.*

### 4. **Profile Page**
*User details, about and support options.*

---

## **Future Improvements**
- Incorporate a chatbot for mental health assistance.
- Integration with wearable health devices for real-time data tracking.

---

## **Contributors**
- **Your Name:Madipelly Mukesh[]
- Guided by **Esaki Rahul** during the internship at Infosys Springboard.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

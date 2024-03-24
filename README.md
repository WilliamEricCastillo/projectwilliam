# ProjectWilliam

## Continuous Development Web Application

ProjectWilliam is a web application utilizing `Python`, `Flask`, and `Postgres` Database, with hosting on `Fly.io`. <br />
It serves as an ongoing development project aimed at showcasing and enhancing my skills over time. It emphasizes the importance of continuous learning and adoption of state-of-the-art technologies.
<br />
<br />
You can visit it at [https://projectwilliam.fly.dev/](https://projectwilliam.fly.dev/).

## Features

- User registration: Users can create an account by providing a unique username and password.
- User authentication: Registered users can log in to their accounts using their credentials.
- Session management: The application maintains user sessions to keep track of authenticated users.
- Authorization: Certain sections of the application are accessible only to authenticated users.
- Dynamic content: The application provides dynamic content generation using `Jinja2` templating.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your_username/ProjectWilliam.git
```

2. Navigate to the project directory:
```
cd ProjectWilliam
```

3. Install dependencies using pip:
```
pip install -r requirements.txt
```

## Usage
1. Set up a PostgreSQL database and provide the database URL in the .env file.
2. Run the Flask application:
  ```
  python app.py
  ```




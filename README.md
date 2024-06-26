# APIed Portfolio

APIed Portfolio is a Django-based web application designed to allow users to create, manage, and share their professional portfolios. It leverages Django and Django REST Framework to provide a robust backend for user registration, authentication, and data management. Users can fill in their personal information, including job experiences, certifications, skills, and projects, and then access their data through a RESTful API. This makes it easy to update their portfolio data, such as adding new job experiences or certifications, and to display it on a personal website hosted on a service like GitHub Pages using raw JavaScript or one of its frameworks to fetch the data.

## Features

- **User Registration and Authentication**: Users can register and log in to manage their portfolio data.
- **Data Management**: Users can add, update, and delete their job experiences, certifications, skills, and projects.
- **RESTful API**: A RESTful API is provided for accessing portfolio data, allowing users to fetch their data from anywhere.
- **Permissions**: The application is designed with permissions in mind, ensuring that only the logged-in user can modify their own data.
- **Django Admin Panel**: Initially, user creation is supported through the Django admin panel, with plans to introduce a custom registration form.

## API Documentation

APIed Portfolio utilizes Swagger for API documentation, providing an interactive and user-friendly interface for exploring the API endpoints. This documentation is automatically generated and kept up-to-date, ensuring that developers have a clear understanding of the API's capabilities and how to interact with it.

You can access the Swagger UI by navigating to `/swagger/` on your local development server or the deployed application URL. This interactive documentation viewer allows you to explore the API endpoints, view request and response examples, and test the API directly from the browser.

## Models

The application uses the following models to structure the portfolio data:

### User

Extends Django's `AbstractUser` model to include additional fields:

- `full_name`: Full name of the user.
- `about`: A brief description about the user.
- `image`: Profile image of the user.
- `resume`: Resume file of the user.
- `phone`: Phone number of the user.
- `telegram`: Telegram URL.
- `github`: GitHub URL.

### CERT

Represents a certification:

- `title`: Title of the certification.
- `details_url`: URL for more details about the certification.
- `donor`: The entity that granted the certification.
- `image`: Image of the certification.
- `granted_on`: Date when the certification was granted.
- `user`: Foreign key to the User model.

### SKILL

Represents a skill:

- `order`: Unique order for sorting skills.
- `title`: Title of the skill.
- `description`: Description of the skill.
- `image`: Image of the skill.
- `user`: Foreign key to the User model.

### EXP

Represents a job experience:

- `title`: Title of the job.
- `description`: Description of the job.
- `start_date`: Start date of the job.
- `end_date`: End date of the job.
- `user`: Foreign key to the User model.

### Project

Represents a project:

- `title`: Title of the project.
- `description`: Description of the project.
- `image`: Image of the project.
- `code_url`: URL to the project's code.
- `preview_url`: URL to a preview of the project.
- `created_at`: Date when the project was created.
- `user`: Foreign key to the User model.

## Installation

1. **Create a Virtual Environment**: `$python3 -m venv venv/`  and then run it `$source venv/bin/activate`

2. **Install Requirements**:
`pip install -r requirements.txt`


3. **Create `.env` File**:
   Create a `.env` file in the root directory of the project (on the same directory of manage.py) and add the following variables:
`SECRET_KEY=your_secret_key EMAIL_ADMIN=your_email EMAIL_HOST_USER=your_email_host_user EMAIL_HOST_PASSWORD=your_email_host_password`

4. **Migrate Database**:
`python manage.py migrate`

5. **Run the Server**:
`python manage.py runserver`


## Future Enhancements

- **Custom Registration Form**: Implement a custom registration form for users to sign up directly from the website.
- **Frontend Integration**: Provide a frontend template or guide for users to easily integrate their portfolio data into their personal websites.

APIed Portfolio is designed to be a flexible and powerful tool for professionals to showcase their skills and experiences. With its focus on user data management, RESTful API access, and interactive API documentation, it offers a convenient way to keep portfolios up-to-date and easily accessible.
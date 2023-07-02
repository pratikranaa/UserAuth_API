# UserAuthAPI
UserAuth API is a Django-based RESTful API for user authentication and management. It provides endpoints for user registration, login, logout, password reset, and more.

## Features

- User registration: Create a new user account.
- User login: Authenticate users and generate access tokens.
- User logout: Invalidate access tokens and log users out.
- Password reset: Send password reset emails and allow users to reset their passwords.
- User profile: Get user details, update profile information, and change passwords.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pratikranaa/UserAuth_API.git

2. Create and activate a virtual environment:

    ```bash
    virtualenv env
    source env/bin/activate

3. Install the dependencies:

   ```bash
    pip3 install -r requirements.txt

4. Set up the database:

   ```bash
    python manage.py migrate

5. Start the development server:

   ```bash
    python manage.py runserver

The Project is now accessible at http://localhost:8000/.

## API Documentation
API documentation is available using Swagger. To access the documentation, start the development server and navigate to http://localhost:8000/api/v1/ in your web browser.

## Usage
You can interact with the UserAuth API using a tool like cURL or Postman and also integrate it with front end to use it comprehensively. Make sure to include the necessary headers and data for each request.

## API Endpoints
The UserAuth API''s endpoints can be seen in the urls.py file or swagger documenation

## Authentication
The UserAuth API uses JSON Web Tokens (JWT) for authentication. To access protected endpoints, include the JWT token in the Authorization header of the request.

Example:

    Authorization: Bearer <JWT_TOKEN>

To obtain a JWT token, make a successful login request. The token will be included in the response.

## Error Handling
The UserAuth API follows standard HTTP status codes for error handling. In case of an error, the response will include an error message and the corresponding status code.

Example error response:

    {
    "detail": "Authentication credentials were not provided."
    }

Refer to the API endpoint descriptions for possible error scenarios and their corresponding status codes.

## Configuration
The following environment variables are used for configuration. You can set them in a .env file in the project root directory.

    SECRET_KEY: Django secret key for session security. (required)
    DATABASE_URL: URL of the PostgreSQL database. (required)
    EMAIL_BACKEND: Email backend for sending emails. (required)
    EMAIL_HOST: SMTP server hostname for email sending. (required)
    EMAIL_PORT: SMTP server port for email sending. (required)
    EMAIL_HOST_USER: SMTP server username for email sending. (required)
    EMAIL_HOST_PASSWORD: SMTP server password for email sending. (required)
    EMAIL_USE_TLS: Whether to use TLS for email sending. (default: True)

## Resources

Django Documentation https://docs.djangoproject.com/

Django REST Framework Documentation https://www.django-rest-framework.org/

PostgreSQL Documentation https://www.postgresql.org/docs/

Swagger API Documentation https://swagger.io/docs/


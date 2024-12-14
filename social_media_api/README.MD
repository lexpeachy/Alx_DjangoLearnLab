# Social Media API
This project is a basic social media API built using Django and Django REST Framework.

## Features
- User registration and login.
- Token-based authentication.
- Profile management.

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`.

## Endpoints
- `/accounts/register/`: Register a new user.
- `/accounts/login/`: Authenticate and get a token.
- `/accounts/profile/`: View user profile.
- `/posts/`: List or create posts.
- `/posts/<id>/`: Retrieve, update, or delete a specific post.
- `/comments/`: List or create comments.
- `/comments/<id>/`: Retrieve, update, or delete a specific comment.


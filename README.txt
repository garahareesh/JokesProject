
# Joke API Project

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd JokeProject
Install dependencies:
================
pip install -r requirements.txt
Run migrations:
================

python manage.py migrate
Run the development server:

python manage.py runserver
Fetch Jokes: Send a GET request to http://127.0.0.1:8000/jokes/get-jokes/ to fetch and store jokes.

Endpoints
/jokes/get-jokes/: Fetches 100 jokes from JokeAPI and stores them in the database.

# Blog API

## Overview
A RESTful API for a Blog Platform built using Django and Django REST Framework (DRF). It supports user authentication, blog post management, interactions (comments, likes), and basic analytics.

## Features
- User Authentication (JWT-based)
- Blog Post Management (CRUD operations)
- Commenting and Liking System
- Search, Filtering, and Pagination
- API Rate Limiting
- Asynchronous Tasks with Celery
- API Documentation using Swagger/OpenAPI
- Unit Tests
- Custom Middleware for Request Logging

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Task Queue**: Celery with Redis
- **Containerization**: Docker & Docker Compose

## Installation & Setup
### Prerequisites
- Python 3.12
- PostgreSQL
- Redis (for Celery)
- Docker (optional for containerization)

### Local Setup
1. **Clone the repository**
   ```sh
   git clone <repository-url>
   cd blog_api
   ```

2. **Create a virtual environment and install dependencies**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file and add:
   ```ini
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://postgres:postgres@localhost:5432/blogdb
   ```

4. **Run migrations & create a superuser**
   ```sh
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```sh
   python manage.py runserver
   ```
   API will be available at `http://127.0.0.1:8000/`

## Running with Docker
1. **Build and start containers**
   ```sh
   docker-compose up --build
   ```
2. **Access the API** at `http://127.0.0.1:8000/`

## API Documentation
- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Example API Requests
### Authentication
#### Register a User
```http
POST /api/auth/register/
```
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}
```

#### Obtain JWT Token
```http
POST /api/auth/token/
```
```json
{
  "username": "testuser",
  "password": "password123"
}
```

## Running Tests
To run unit tests:
```sh
python manage.py test
```

## Logging Middleware
All requests and responses are logged using custom middleware.

## Contributing
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## License
This project is licensed under the MIT License.


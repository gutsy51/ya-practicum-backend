# Yatube API
A training project, a DRF-Backend for the Yatube blog platform, which includes:
- Posts system - publish, edit, see;
- User system - create users, subscribe to others;
- Commentary system - leave comments on posts;

## Installation & Run
### 1. Clone the repository to your local machine
```bash
git clone https://github.com/gutsy51/ya-practicum-backend/tree/master/api_yatube2 
cd api_yatube2
```
### 2. Create and activate the virtual environment
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
#### Linux/MacOS
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Perform migrations
```bash
cd api_yatube
python manage.py migrate
```
### 4. Run the server
```bash
python manage.py runserver
```

## Quick API Reference
> A detailed description of the API will be available at [http://localhost/redoc/](Http://localhost:8000/redoc/)

### JWT Token
```bash
POST /api/v1/jwt/create/
{
  "username": "username",
  "password": "password"
}
```
Answer:
```bash
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

### Posts
| Path                  | Method      | Description           | Access        | 
|-----------------------|-------------|-----------------------|---------------|
| `/api/v1/posts/`      | `GET`       | Get posts (paginated) | Anyone        |
| `/api/v1/posts/`      | `POST`      | Create new post       | Auth          |
| `/api/v1/posts/{id}/` | `GET`       | Get post details      | Anyone        |
| `/api/v1/posts/{id}/` | `PUT/PATCH` | Update post           | Auth + Author |
| `/api/v1/posts/{id}/` | `DELETE`    | Delete post           | Auth + Author |

Examples:
- `GET /api/v1/posts/` - Get all posts (first page, less than 10 posts);
- `GET /api/v1/posts/?limit=10&offset=10` - Get all posts (second page, 10 posts);
- `GET /api/v1/posts/?search=hello` - Get all posts with "hello" in the title.

### Comments
| Path                                     | Method      | Description     | Access        | 
|------------------------------------------|-------------|-----------------|---------------|
| `/api/v1/posts/{post_id}/comments/`      | `GET`       | All comments    | Anyone        |
| `/api/v1/posts/{post_id}/comments/`      | `POST`      | New comment     | Auth          |
| `/api/v1/posts/{post_id}/comments/{id}/` | `GET`       | Comment details | Anyone        |
| `/api/v1/posts/{post_id}/comments/{id}/` | `PUT/PATCH` | Update comment  | Auth + Author |
| `/api/v1/posts/{post_id}/comments/{id}/` | `DELETE`    | Delete comment  | Auth + Author |

Examples:
- `GET /api/v1/posts/1/comments/` - Get all comments for post with id=1;
- `POST /api/v1/posts/1/comments/` - Create new comment for post with id=1.

### Follows

| Path                   | Method      | Description     | Access        |
|------------------------|-------------|-----------------|---------------|
| `/api/v1/follow/`      | `GET`       | All follows     | Auth          |
| `/api/v1/follow/`      | `POST`      | New follow      | Auth          |
| `/api/v1/follow/{id}/` | `DELETE`    | Delete follow   | Auth          |

Examples:
- `GET /api/v1/follow/` - Get all your follows;
- `POST /api/v1/follow/` - New follow;
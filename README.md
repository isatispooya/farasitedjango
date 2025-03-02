# Farasite

## Overview
Farasite is a multi-domain Django-based Content Management System (CMS) designed to power multiple websites with independent configurations. It provides a modular design, rich text editors, built-in security features, and REST API documentation.


## Features
- **Multi-Domain Support**: Each site operates independently with unique configurations.
- **Modular Design**: Enable/disable apps (Blog, Education, Menu) per domain.
- **Rich Text Editors**: Supports **TinyMCE** and **Summernote**.
- **Built-in Security**: CSRF, XSS, Secure Cookies, and CORS configurations.
- **API Documentation**: Auto-generated **Swagger** and **Redoc** endpoints.
- **Docker Support**: Production-ready setup with **Nginx + Gunicorn**.


## Quick Start (Local Development)
1. Clone the repository:
```bash
git clone https://github.com/isatispooya/farasitedjango.git
```


2. Create `.env` file with required variables:
```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=farasite
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=your-host
DB_PORT=5432
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email-user
EMAIL_HOST_PASSWORD=your-email-password
```


3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```


5. Start the development server:
```bash
python manage.py runserver
```

Access the CMS at http://127.0.0.1:8000/


## Docker Deployment
The project includes production-ready Docker configuration with Gunicorn and Nginx.

1. Build and start containers:
```bash
docker-compose up --build
```


### Docker Configuration
- **Web Service**: Python 3.9 with Gunicorn
  - Resource limits: 0.5 CPU, 500MB RAM
  - Health monitoring at /health/
  - Automatic restart policy
- **Nginx Service**: Version 1.21
  - Resource limits: 0.3 CPU, 300MB RAM
  - Serves static files
  - Handles SSL termination
  - Security headers configured
  - Max body size: 100MB


### Volumes and Networks
- Static files served from `static_volume`
- Custom bridge network for service isolation
- Persistent volume for static assets


## Technical Stack
- **Backend**: Django 4.1
- **Database**: PostgreSQL
- **API**: Django REST Framework
- **Documentation**: drf-spectacular
- **Text Editors**: TinyMCE, Summernote
- **Proxy Server**: Nginx
- **WSGI Server**: Gunicorn
- **Container Platform**: Docker


## Security Features
- CSRF protection enabled
- XSS protection headers
- Content-Type sniffing protection
- Secure cookie configuration
- CORS policy configuration

For detailed setup instructions and advanced configurations, please refer to the documentation in the /docs/ directory.


## Key Features
Domain-Based Configuration: Each site is tied to a unique domain (e.g., via the Domain model) with customizable settings like logos, themes, and contact details (see Information model).
General App (website): Core data and functionality shared across all sites live here.
Optional Apps: Additional apps (e.g., for products or sections) can be enabled for specific domains only.
Admin Panel: Uses Django's built-in admin interface for managing domains, content, and settings.
Dynamic Views: API endpoints filter content by domain (e.g., SoloProductsViewSet and SectionViewSet).


## Example Usage
Model Example: The Domain model defines each site (e.g., example.com), while Information stores details like logos, phone numbers, and social media links tied to that domain.
View Example: The SoloProductsViewSet fetches the latest product for a given domain and route, while SectionViewSet lists sections filtered by domain.


## API Documentation 📖
Farasite provides auto-generated API documentation:

- **Swagger UI** → [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc UI** → [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
- **Raw OpenAPI JSON** → `/swagger.json`


### Testing API via Postman
1. Open Postman → Click **Import**
2. Enter: `http://127.0.0.1:8000/swagger.json`
3. Click **Import** → Now you can test all endpoints!


## Advanced Documentation
For detailed info on architecture, custom app setup, or domain-specific configurations, check the `/docs` directory.


## Project Structure 📂
farasite/
├── apps/                     # Main Django apps
│   ├── website/              # Core website functionality (main content)
│   ├── menu/                 # Manages dynamic menus for websites
│   ├── structure/            # Handles website structural settings (layout, sections)
│   ├── superproduct/         # Manages special product listings per domain
│   ├── introduction/         # Introduction pages or sections per domain
│   ├── chart/                # Handles chart-based data visualization
│   ├── vision/               # Manages vision and mission statements
│   ├── brief/                # Provides brief summaries for content
│   ├── bourse/               # Stock market/bourse data module
│   ├── supercart/            # Shopping cart management
│   ├── education/            # Education-related content (articles, courses, etc.)
│   ├── blog/                 # Blogging system for multiple domains
├── config/                   # Django settings & configurations
├── static/                   # Static files (CSS, JS, images)
├── staticfiles/              # Collected static files (for production)
├── media/                    # Uploaded media files
├── docs/                     # Project documentation
├── logs/                     # Logs for debugging & monitoring
├── templates/                # HTML templates for rendering views
├── manage.py                 # Django management script
├── README.md                 # Project documentation & setup guide
├── requirements.txt          # Dependencies & Python packages
├── nginx.conf                # Nginx configuration for serving static/media files
├── docker-compose.yml        # Docker multi-container setup
├── Dockerfile                # Docker image build configuration
├── entrypoint.sh             # Script to start the application in Docker
├── .env                      # Environment variables (DO NOT COMMIT!)
├── .env.example              # Example environment file for reference
├── .gitignore                # Files and directories to ignore in Git



## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing_feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing_feature`)
5. Open a Pull Request
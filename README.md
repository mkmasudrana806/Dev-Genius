# Dev Genius

Dev Genius is a Django-based web application for an IT company website.

## Features
- Company information management
- Rich text content support using CKEditor
- Contact details and social media links

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd company_webpage
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```sh
   python manage.py migrate
   ```

5. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Requirements
```
" + requirements + "
```

## Models

### GeneralInfo
Stores basic company details.
```python
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="Company")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
```

More models might be present in `models.py`. Check the file for additional details.

## License
This project is licensed under the MIT License.


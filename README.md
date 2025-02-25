# Dev Genius

Dev Genius is a Django-based web application for an IT company website.

## Requirements Analysis
### Overview
Dev Genius is a web application designed for an IT company to manage company information, services, team members, and client inquiries. The system allows administrators to update website content dynamically.

### Key Features
- Company profile management
- Services listing with descriptions
- Team member profiles
- Blog post management
- Contact form handling
- Rich text content support using CKEditor
- Social media integration

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
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name
```

### Service
Stores services offered by the company.
```python
class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title
```

### TeamMember
Stores details about the team members.
```python
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_images/')
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
```

### BlogPost
Stores blog articles.
```python
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
```

### ContactMessage
Stores messages received from the contact form.
```python
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"
```

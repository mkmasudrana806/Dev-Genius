from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from app.models import (
    GeneralInfo,
    Service,
    Testimonial,
    FrequentlyAskedQuestion,
    ContactFormLog,
    Blog,
)

# Create your views here.
def index(request):

    general_info = GeneralInfo.objects.first() # None

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    faqs = FrequentlyAskedQuestion.objects.all()

    recent_blogs = Blog.objects.all().order_by("-created_at")[:3]

    default_value = ""

    context = {
        "company_name": getattr(general_info, "company_name", default_value),
        "location": getattr(general_info, "location", default_value),
        "email": getattr(general_info, "email", default_value),
        "phone": getattr(general_info, "phone", default_value),
        "open_hours": getattr(general_info, "open_hours", default_value),
        "video_url": getattr(general_info, "video_url", default_value),
        "twitter_url": getattr(general_info, "twitter_url", default_value),
        "facebook_url": getattr(general_info, "facebook_url", default_value),
        "instagram_url": getattr(general_info, "instagram_url", default_value),
        "linkedin_url": getattr(general_info, "linkedin_url", default_value),

        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
        "recent_blogs": recent_blogs,
    }

    return render(request, "index.html", context)


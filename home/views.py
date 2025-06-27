from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'title': 'Home',
        'current_year': datetime.now().year,
        'user_name': 'your_username',
        'user_display_name': 'Your Name',
    }

    return render(request, 'index.html', context)
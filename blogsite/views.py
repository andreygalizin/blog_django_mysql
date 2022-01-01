from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return render(request, "index.html")

def individual_post(request):
    recent_post = Post.objects.get(id__exact=1)
    return HttpResponse(recent_post.title + ': ' + recent_post.content)

# create a function to send tabular data to template
def customers(request):
    # define a dictionary of nested list
    data = {"customers": [['6745', 'Monir Hossain', 'monir@gmail.com', '880191345234'],
                          ['7845', 'Keya Akter', 'keya@gmail.com', '880189045673'],
                          ['9056', 'Mohammed Ali', 'ali@gmail.com', '880179893922'],
                          ['4536', 'Mostafa Kamal', 'kamal@gmail.com', '880157665433']]
            }

    # return response with template and data
    return render(request, "customers.html", data)


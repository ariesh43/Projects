from django.shortcuts import render
from .forms import FeedbackForm
from django.contrib import messages

# Create your views here.
def index(request):

    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form submitted successfully.")
            form = FeedbackForm()
            # return HttpResponse('<body><center><div style="top: 150px;position:relative;" >Successfully submitted.</div></center></body>')

    context = {'form': form}
    return render(request, 'feedback/index.html', context)

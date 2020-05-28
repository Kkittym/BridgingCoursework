from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import CV, Section, Institute, Element
from .forms import CVForm, SectionForm, InstituteForm, ElementForm
from django.contrib.auth.decorators import login_required

def main(request):
    cv = None
    try:
        cv = CV.objects.get()
    except:
        cv = None
    print(cv)
    return render(request, 'main.html', {'cv':cv})

@login_required
def CV_new(request):
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('cv')
    else:
        form = CVForm()
    return render(request, 'create_cv.html', {'form': form})

@login_required
def section_new(request):
    cv = CV.objects.get()
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.CV = cv
            section.save()
            return redirect('cv')
    else:
        form = SectionForm()
    return render(request, 'main.html', {'cv':cv, 'form': form})
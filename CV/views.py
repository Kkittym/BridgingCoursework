from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import CV, Section, SectionElement, Institute, InstituteElement
from .forms import CVForm, SectionForm, InstituteForm, SectionElementForm, InstituteElementForm
from django.contrib.auth.decorators import login_required

def main(request):
    cv = None
    try:
        cv = CV.objects.get()
    except:
        cv = None
    print(cv)
    print(cv.sections.all())
    for section in cv.sections.all():
        print (section.title)
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
def add_section(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == "POST":
        if "section_form" in request.POST:
            form = SectionForm(request.POST)
            if form.is_valid():
                section = form.save(commit=False)
                section.CV = cv
                section.save()
                return redirect('cv')
        if "element_form" in request.POST:
            element_form = SectionElementForm(request.POST)
            if element_form.is_valid():
                element = element_form.save(commit=False)
                element.section = section
                element.save()
                return redirect('edit_section', pk=section.pk)
    else:
        form = SectionForm()
    return render(request, 'edit_section.html', {'form': form, 'text': 'New',})

@login_required
def edit_section(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        if "section_form" in request.POST:
            section_form = SectionForm(request.POST)
            if section_form.is_valid():
                section = section_form.save(commit=False)
                section.save()
                return redirect('cv')
        if "element_form" in request.POST:
            element_form = SectionElementForm(request.POST)
            if element_form.is_valid():
                element = element_form.save(commit=False)
                element.section = section
                element.save()
                return redirect('edit_section', pk=section.pk)
    else:
        section_form = SectionForm(instance=section)
        element_form = SectionElementForm()
    return render(request, 'edit_section.html', {'section_form': section_form, 'text': 'Edit', 'section':section, 'element_form': element_form})

@login_required
def add_institute(request, secpk):
    section = get_object_or_404(Section, pk=secpk)
    if request.method == "POST":
        form = InstituteForm(request.POST)
        if form.is_valid():
            institute = form.save(commit=False)
            institute.section = section
            section.save()
            return redirect('edit_section', pk=section.pk)
    else:
        form = InstituteForm()
    return render(request, 'edit_institute.html', {'form': form, 'text': 'New',})

@login_required
def edit_institute(request, secpk, instpk):
    section = get_object_or_404(Section, pk=secpk)
    institute = get_object_or_404(Section, pk=secpk)
    if request.method == "POST":
        if "section_form" in request.POST:
            section_form = SectionForm(request.POST)
            if section_form.is_valid():
                section = section_form.save(commit=False)
                section.save()
                return redirect('edit_section', pk=secpk)
    else:
        form = InstituteForm(instance=section)
    return render(request, 'edit_institute.html', {'form': form, 'text': 'Edit', 'institute':institute})

@login_required
def remove_institute(request, secpk, instpk):
    institute = get_object_or_404(Institute, pk=instpk)
    institute.delete()
    return redirect('edit_section', pk=secpk)

@login_required
def add_element_to_section(request, secpk):
    pass

@login_required
def add_element_to_institute(request, instpk):
    pass

@login_required
def remove_element_from_section(request, secpk, elepk):
    element = get_object_or_404(SectionElement, pk=elepk)
    element.delete()
    return redirect('edit_section', pk=secpk)

@login_required
def remove_element_from_institute(request, secpk, instpk, elepk):
    element = get_object_or_404(InstituteElement, pk=elepk)
    element.delete()
    return redirect('edit_institute', pk=instpk)
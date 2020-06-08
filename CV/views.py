from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import CV, Section, SectionElement, Institute, InstituteElement
from .forms import CVForm, SectionForm, InstituteForm, SectionElementForm, InstituteElementForm
from django.contrib.auth.decorators import login_required

def main(request):
    cv = None
    try:
        cv = CV.objects.first()
    except:
        cv = None
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
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.CV = cv
            section.save()
            return redirect('edit_section', secpk=section.pk, pk=pk)
    else:
        section_form = SectionForm()
    return render(request, 'main.html', {'cv':cv, 'section_form': section_form})

@login_required
def edit_section(request, pk, secpk):
    cv = get_object_or_404(CV, pk=pk)
    section = get_object_or_404(Section, pk=secpk)
    section_form = None
    element_form = None
    if request.method == "POST":
        if "section_form" in request.POST:
            section_form = SectionForm(request.POST, instance=section)
            if section_form.is_valid():
                section = section_form.save(commit=False)
                section.CV = cv
                section.save()
                return redirect('cv')
        if "element_form" in request.POST:
            element_form = SectionElementForm(request.POST)
            if element_form.is_valid():
                element = element_form.save(commit=False)
                element.section = section
                element.save()
                return redirect('edit_section', secpk=section.pk, pk=section.CV.id)
    else:
        section_form = SectionForm(instance=section)
        element_form = SectionElementForm()
    return render(request, 'edit_section.html', {'section_form': section_form, 'text': 'Edit', 'section':section, 'element_form': element_form})

@login_required
def remove_section(request, pk, secpk):
    section = get_object_or_404(Section, pk=secpk)
    section.delete()
    return redirect('cv')

@login_required
def add_institute(request, secpk):
    section = get_object_or_404(Section, pk=secpk)
    #print("Section for pk", secpk, ":", section)
    if request.method == "POST":
        form = InstituteForm(request.POST)
        if form.is_valid():
            #print('form is valid, adding to section:', section)
            institute = form.save(commit=False)
            institute.section = section
            institute.save()
            return redirect('edit_institute', instpk=institute.pk, secpk=secpk)
    else:
        institute_form = InstituteForm()
    return render(request, 'edit_section.html', {'institute_form': institute_form, 'text': 'Edit', 'section':section})

@login_required
def edit_institute(request, secpk, instpk):
    institute = get_object_or_404(Institute, pk=instpk)
    section = get_object_or_404(Section, pk=secpk)
    institute_form = None
    element_form = None
    if request.method == "POST":
        if "institute_form" in request.POST:
            institute_form = InstituteForm(request.POST, instance=institute)
            if institute_form.is_valid():
                institute = institute_form.save(commit=False)
                institute.section = section
                institute.save()
                return redirect('edit_section', secpk=secpk, pk=section.CV.id)
        if "element_form" in request.POST:
            element_form = InstituteElementForm(request.POST)
            if element_form.is_valid():
                element = element_form.save(commit=False)
                element.institute = institute
                element.save()
                return redirect('edit_institute', secpk=secpk, instpk=instpk)
    else:
        institute_form = InstituteForm(instance=institute)
        element_form = SectionElementForm()
    return render(request, 'edit_institute.html', {'institute_form': institute_form, 'text': 'Edit', 'institute':institute, 'element_form': element_form})

@login_required
def remove_institute(request, secpk, instpk):
    institute = get_object_or_404(Institute, pk=instpk)
    institute.delete()
    return redirect('edit_section', secpk=secpk, pk=get_object_or_404(Section, pk=secpk).CV.id)

@login_required
def remove_element_from_section(request, secpk, elepk):
    element = get_object_or_404(SectionElement, pk=elepk)
    element.delete()
    return redirect('edit_section', secpk=secpk, pk=get_object_or_404(Section, pk=secpk).CV.id)

@login_required
def remove_element_from_institute(request, instpk, elepk):
    element = get_object_or_404(InstituteElement, pk=elepk)
    element.delete()
    return redirect('edit_institute', instpk=instpk, secpk=get_object_or_404(Institute, pk=instpk).section.id)
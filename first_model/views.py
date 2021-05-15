from django.shortcuts import render,redirect

from .models import students #line 1

def student_views(request): #Line 3 (Function-based view)
    student_list = students.objects.all() #Line 4
    context = {'student_list':student_list} #Line 5
    return render(request, 'first_model/index.html', context=context) # Line 6

def search_student(request):

    if request.method == 'GET':
        registration_number = request.GET.get("registration_number")
        try:
            student = students.objects.get(reg_no = registration_number)
            return render(request, 'first_model/search.html', {'student': student})
        except students.DoesNotExist:
            if registration_number:
                result_not_found = f"Student with the registration number {registration_number} does not exist"
                return render(request, 'first_model/search.html', {'result_not_found': result_not_found})
    return render(request, 'first_model/search.html')


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        city = request.POST.get("city")
        level = request.POST.get("level")
        date_admitted = request.POST.get('date_admitted')
        active = request.POST.get("active")
        reg_no = request.POST.get('reg_no')

        if active == "on":
            active = True
        else:
            active = False
        student = students.objects.create(
            name = name, city = city, level = level, date_admitted=date_admitted, active=active, reg_no=reg_no
        )
        return redirect('student_views')
    return render(request, 'first_model/add_student.html')


def view_404(request, exception):

    return render(request, '404.html')

def view_500(request):

    return render(request, '500.html')
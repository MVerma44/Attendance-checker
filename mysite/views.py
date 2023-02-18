# I have created this

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello Radha Krishna")


def home(request):
    return render(request, 'index.html')

def index(request):
    # lecture = request.GET.get('lec', 'default')
    # total = request.GET.get('total', 'default')
    lecture = int(request.GET.get('lec', 1))
    total = int(request.GET.get('total', 1))
    print(lecture, total)

    # percentage = (lec/tot) * 100
    for i in range(1, 25):
        if ((int(lecture)/int(total)) * 100) < 75:
            if ((int(lecture)+i) / (int(total)+i)) * 100 >= 75:
                print(f"{i} continuous classes")
                break

        else: 
            print("Attendance already above 75%")
            break

    return render(request, 'result.html', {'result':i, 'default':'Attendance already above 75%'})

    # return HttpResponseRedirect('index.html')
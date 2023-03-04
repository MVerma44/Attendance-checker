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
    count = 0
    for i in range(1, 50):
        if ((int(lecture)/int(total)) * 100) < 75:
            if ((int(lecture)+i) / (int(total)+i)) * 100 >= 75:
                print(f"{i} continuous classes")
                break

        else: 
            count = 0
            for j in range(1, 50):
                if ((lecture / (total+j)) * 100) >= 75:
                    count += 1

            if count == 0:
                print("Oops!!! you can not bunk any class")
            
            else:
                print(f"{count} class you can bunk to maintain attendance above 75%")
            break

    return render(request, 'result.html', {'result':i, 'remain':count, 'default':'Attendance already above 75%'})

    # return HttpResponseRedirect('index.html')
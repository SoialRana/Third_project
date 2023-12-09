from django.shortcuts import render

# Create your views here.

""" def contact(request):
    #return render(request, './first_app/index.html',context={'author':'phitron','age':'19','marks':'80'})
    return render(request, './first_app/index.html',{'courses':[
        {
            'id':1,
        'course':'c',
        'teacher':'rahim'
        },
        {
            'id':2,
        'course':'c++',
        'teacher':'karim'
        },
        {
            'id':3,
        'course':'python',
        'teacher':'fahim'
        }
    ]}) """


def contact(request):
    return render(request, './first_app/index.html', {"name" :"I am rahim",
    "marks":86,"lst" : [24,3,10,5],"blog" :"Lorem ipsum dolor,set amet,consectetur adipiscing elit. Harum quae tempora fugit laborum volupta mollitia. Explicabo carum assumenda obcaecati et."})
     
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from courses.models import Course, Video, UserCourse
# from courses.views import coursePage1
from django.shortcuts import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


# def coursePage(request):
#     # course = Course.objects.get().all()
#     serial_number = request.GET.get('lecture')
#     # videos = course.video_set.all().order_by("serial_number")
#     return render(request, template_name="class1.html",{"video":video})

def coursePage(request):
    video = Video.objects.filter(course="1").values()
    course = Course.objects.all()
    # name = Course.name
    # desc = Course.description
    # video_id = Video.video_id
    # serial_number = Video.serial_number
    # slug = Course.slug
    # title = Video.title
    context = {
        "video": video,
        # "video_id": video_id,
        # 'title': title,
        # 'name': name,
        # 'desc': desc,
        # 'serial_number': serial_number,
        # 'slug': slug
    }
    return render(request, "class1.html", context=context)


# -------------------------started------------------------
# def coursePage2(request):
#
#     video = Video.objects.filter(course="2").values()
#     # print("video : ", video[0]["video_id"])
#     serial_number = request.GET.get('lecture')
#     videos = Course.objects.all().order_by("serial_number")
#     for v in videos:
#         print("v : ", v)
#     course = Course.objects.filter(slug='cls2-videos-started').values()
#     # serial_number = request.GET.get('lecture')
#     # videos = course.video_set.all().order_by("serial_number")
#
#     context = {
#         "course": course,
#         "video": video,
#         'videos': videos
#     }
#     # return render(request, "index.html", context=context)
#     --------------------ended----------------------------------
def coursePage2(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1

    video = Video.objects.get(serial_number=serial_number, course=course)

    # if (video.is_preview is False):
    #     if request.user.is_authenticated is False:
    #         return redirect("login")
    #     else:
    #         user = request.user
    #         try:
    #             user_course = UserCourse.objects.get(course=course)
    #         except:
    #             return redirect("check-out", slug=course.slug)

    context = {
        "course": course,
        "video": video,
        'videos': videos
    }
    return render(request, template_name="cp.html", context=context)
# courses/views.py
# courses/views.py

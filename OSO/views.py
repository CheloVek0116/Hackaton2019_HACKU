from django.shortcuts import render, redirect


def preview(request):
    if request.user.is_authenticated:
        return redirect('user:ProfilePage')
    return render(request, 'preview/index.html')

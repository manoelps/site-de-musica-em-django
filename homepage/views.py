from django.shortcuts import render

def music_page(request):
    return render(request, 'homepage/music.html')

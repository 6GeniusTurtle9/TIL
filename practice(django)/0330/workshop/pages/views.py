import requests
from pprint import pprint
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    #1. 사용자 입력값 받기
    search_data = request.GET.get('search')

    #2. API 요청 보내기 -> (기본) API URL, Access Key / (사진검색) query
    client_id = '-CHdV0gwtxGK1gLf-prWxjw97QfJyfsVLAz2IQnk45Y'
    photo_url = f'https://api.unsplash.com/search/photos?client_id={client_id}&query={search_data}'
    response = requests.get(photo_url).json()

    #3. 응답값 확인 및 사진 추출
    photo_list = []

    for photo in response.get('results'):
        photo_list.append(photo.get('urls').get('regular'))

    context = {
        'photo_list': photo_list
    }

    return render(request, 'gallery.html', context)
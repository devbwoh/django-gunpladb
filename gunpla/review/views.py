from django.shortcuts import render
import urllib.request
import json


def index(request):
    url = 'https://gunpladb-noovf.run.goorm.io/api/join'
    res = urllib.request.urlopen(url)
    res_body = res.read()
    data = json.loads(res_body.decode("utf-8"))
    # print(data[0])
    return render(request, "review/index.html", {'data': data})

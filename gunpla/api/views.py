# # from django.shortcuts import render
# from django.http import HttpResponse


# def mechanic(request):
#     return HttpResponse("Success")

from django.http import JsonResponse
from .models import Mechanic
from django.db import connection


def mechanic(request):
    res = Mechanic.objects.all()
    return JsonResponse(list(res.values()), safe=False)


def dictfetchall(cursor):
    attr = [col[0] for col in cursor.description]
    return [
        dict(zip(attr, row))
        for row in cursor.fetchall()
    ]


def join(request):
    db = connection.cursor()
    db.execute('''
    select * from mechanic
    left outer join gunpla on (mechanic.id = mechanic_id)
    left outer join image on (gunpla.id = gunpla_id)
    ''')
    result = dictfetchall(db)
    return JsonResponse(result, safe=False)

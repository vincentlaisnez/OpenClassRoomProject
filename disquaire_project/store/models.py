from django.db import models

# Create your models here.

ARTISTS = {
    'KORN':{'name':'KORN'},
    'NIRVANA':{'name':'NIRVANA'},
    'BABY-METAL':{'name':'BABY METAL'},
    'LINKIN-PARK':{'name':'LINKIN PARK'},
}


ALBUMS = [
    {'name': 'Mirror','artists':[ARTISTS['KORN']]},
    {'name': 'Nevermind','artists':[ARTISTS['NIRVANA']]},
    {'name': 'Babymetal','artists':[ARTISTS['BABY-METAL']]},
    {'name': 'Meteora','artists':[ARTISTS['LINKIN-PARK']]},
]
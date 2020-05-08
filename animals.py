# -*- coding: utf-8 -*-

'''
Code of @randcatbot [https://t.me/randcatbot] by Azer Sadykhzadeh

Telegram: @Sadykhzadeh [https://t.me/Sadykhzadeh]
Github: https://github.com/sadykhzadeh
'''

import random
import requests
from config import CAP_MAS, DOG_MAS

class Animals():
    """
    Get cats and dogs from special API
    """
    def give_me_a_cat():
        """
        Get cats
        """
        caption = CAP_MAS[int(random.uniform(0, len(CAP_MAS)))]
        json = requests.get("https://api.thecatapi.com/v1/images/search").json()
        cat = json[0]['url']
        return [cat, caption]
    def give_me_a_dog():
        """
        Get dogs
        """
        caption = DOG_MAS[int(random.uniform(0, len(DOG_MAS)))]
        json = requests.get("https://dog.ceo/api/breeds/image/random").json()
        dog = json['message']
        return [dog, caption]

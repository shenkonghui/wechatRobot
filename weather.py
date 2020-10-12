#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests

def getWeather(cityId):
   r = requests.get("http://www.weather.com.cn/data/sk/" + cityId + ".html")
   r.encoding = "utf-8"
   return r.json()


if __name__ == '__main__':
    print(getWeather("101020100"))
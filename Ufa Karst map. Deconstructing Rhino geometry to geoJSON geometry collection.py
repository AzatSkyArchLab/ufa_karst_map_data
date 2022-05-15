
#Eng
#Deconstruction multiple geometry to GeoJSON geometry collection by using rhino,grasshopper and python
#Some of description on russian - use google translater :)

#Rus
#Деконструирование геометрических объектов в коллекцию объектов GeoJSON
#Author - Azat Ayupov - skyarchschool.ru

import os
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import ghpythonlib.treehelpers as th
import math
import json

#0. At first - create this params in grasshopper and connect it to python code editor. Set List access.
 
#data - list of data to write to districtMesh
#districtMesh - polygons list of city districts
#karstAreaMesh - polygons list of karst areas near the karst holes
#karstPoint - list of karst holes points
#latitude - latitude of a map centre
#longitude - longitude of a map centre
#pathToWrite - Path to write GeoJSON file in Windows folder
#fileName - GeoJSON file name
#colorDistrict - color in hex of districtMesh polygons
#colorKarstAreaMesh - color in hex of districtMesh polygons
#colorKarstPoint - color in hex of karstPoint


#1. Установка точки Земли. Необходимо для установки системы координат WGS84
earthAnchorPoint = gh.Heron.SetEarthAnchorPoint(True,latitude,longitude)

#2.0 disctrictMesh. Создание списка координат mesh районов города в проекционной системе WGS1984
coordinatesDistrictMesh = []
for mesh in districtMesh:
    meshEdges = gh.MeshEdges(mesh)[0]
    joinCurves = gh.JoinCurves(meshEdges,False)
    controlPoints = gh.ControlPoints(joinCurves)[0]
    rawMeshPointCoordinatesX = gh.Heron.XYtoDecimalDegrees(controlPoints)[0]
    rawMeshPointCoordinatesY = gh.Heron.XYtoDecimalDegrees(controlPoints)[1]
    unitedCoordinates = zip (rawMeshPointCoordinatesY,rawMeshPointCoordinatesX)
    coordinatesDistrictMesh.append(unitedCoordinates)

#2.1 karstAreaMesh. Создание списка координат mesh области карстовых провалов в проекционной системе WGS1984
coordinateskarstAreaMesh = []
for mesh in karstAreaMesh:
    meshEdges = gh.MeshEdges(mesh)[0]
    joinCurves = gh.JoinCurves(meshEdges,False)
    controlPoints = gh.ControlPoints(joinCurves)[0]
    rawMeshPointCoordinatesX = gh.Heron.XYtoDecimalDegrees(controlPoints)[0]
    rawMeshPointCoordinatesY = gh.Heron.XYtoDecimalDegrees(controlPoints)[1]
    unitedCoordinates = zip (rawMeshPointCoordinatesY,rawMeshPointCoordinatesX)
    coordinateskarstAreaMesh.append(unitedCoordinates)

#2.2.karstPoint. Создание списка точек в проекционной системе WGS1984
karstPointCoordinates = []
rawPointCoordinatesX = gh.Heron.XYtoDecimalDegrees(karstPoint)[0]
rawPointCoordinatesY = gh.Heron.XYtoDecimalDegrees(karstPoint)[1]
coordinatesLocal = zip(rawPointCoordinatesY,rawPointCoordinatesX)
karstPointCoordinates.append(coordinatesLocal)

#3.0.disctrictMesh. Создание списка цветов районов города
colorListdistrictMesh = colorDistrict * (len(districtMesh))
colordistrictMesh = colorListdistrictMesh

#3.1.karstAreaMesh. Создание списка цветов области карстовых провалов
colorListkarstAreaMesh = colorkarstAreaMesh * (len(karstAreaMesh))
colorkarstAreaMesh = colorListkarstAreaMesh

#3.3.karstPoint. Создание списка цветов точек карстовых провалов
colorListKarstPoint = colorKarstPoint

#4.0. Сборка списка JSON параметров districtMesh для вставки в общий JSON

districtMeshGeoJson = []
for i in range(len(districtMesh)):
    result = {
            "type" : "Feature",
            "geometry" : {
                "type": "Polygon",
                "coordinates":
                        [coordinatesDistrictMesh[i]]
            },
            "properties": {
                "district": data[i],
                "colordistrictMesh": colorListdistrictMesh[i]
            }
        }
    districtMeshGeoJson.append(result)

#4.1. Сборка списка JSON параметров karstAreaMesh для вставки в общий JSON

karstAreaMeshGeoJson = []
for i in range(len(karstAreaMesh)):
    result = {
            "type" : "Feature",
            "geometry" : {
                "type": "Polygon",
                "coordinates":
                        [coordinateskarstAreaMesh[i]]
            },
            "properties": {
                "district": "Область вокруг карстовых провалов",
                "colorkarstAreaMesh": colorListkarstAreaMesh[i]
            }
        }
    karstAreaMeshGeoJson.append(result)

karstAreaMeshGeoJson.extend(districtMeshGeoJson)

#4.2.1 Удаление лишнего уровня вложенного списка координат точек
flattenKarstPointCoordinates=[]
for sublist in karstPointCoordinates:
    for element in sublist:
        flattenKarstPointCoordinates.append(element)

#4.2.1 Сборка списка JSON параметров точек karstPoint для вставки в общий JSON
KarstPointGeoJson = {
        "type" : "Feature",
        "geometry" : {
            "type": "MultiPoint",
            "coordinates":
                        flattenKarstPointCoordinates
        },
        "properties": {
            "district": "Карстовые провалы и воронки",
            "colorKarstPoint": colorListKarstPoint
        }
    }

karstAreaMeshGeoJson.append(KarstPointGeoJson)

#5.0. Сборка перед функцией dumps в GeoJSON:
result = {
        "type": "FeatureCollection",
        "features":
                karstAreaMeshGeoJson
        }

#6.0. Сборка файла GeoJSON
result = json.dumps(result)



#7.0 Директория для сохранения файла
completeName = os.path.join(pathToWrite, fileName + '.geojson')

#8.0 Запись файла в формат GeoJSON
file = open(completeName,'w')
file.write(result)
file.close()


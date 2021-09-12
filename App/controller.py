﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from DISClib.Algorithms.Sorting.shellsort import sort
import config as cf
import model
import csv

import textwrap 
from tabulate import tabulate
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    loadArtists(catalog)
    loadArtworks(catalog)
    sortDates(catalog)



def loadArtists(catalog):
    artistFile=cf.data_dir+"Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistFile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog,artist)
        
        

def loadArtworks(catalog):
    artworkFile=cf.data_dir+"Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworkFile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog,artwork)


# Funciones de ordenamiento

def sortDates(catalog):
    model.sortDates(catalog)

def sortArtDates(catalog):
    model.sortArtworksDates(catalog)

# Funciones de consulta sobre el catálogo

"""Esta función es para organizar el tamaño de las casillas de la tabla, 
la declaramos globalmente porque se usa en varias ocasiones
"""


def cronoArtist(catalog,inicio,fin):
    return(model.cronoArtist(catalog,inicio,fin))

def cronoArtworks(catalog,inicio,fin):
    #Ordenamos aquí y no al inicio con lo demás para no alterar el resultado del requerimiento 4.
    sortArtDates(catalog)
    return(model.cronoArtwork(catalog,inicio,fin))

def nationArworks(catalog):
    return (model.nationArworks(catalog))

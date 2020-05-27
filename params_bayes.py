from bayes_network import bayes_bake
from pipelines import *

import pymongo
from pymongo import MongoClient
import pprint
import itertools
import pandas as pd

client = MongoClient("mongodb+srv://Arina:arina270799@cluster27-pldc3.gcp.mongodb.net/cluster_new?retryWrites=true&w=1")

pipeline = [
    {
        '$lookup':
            {
                'from': "delivery",
                'localField': "_id",
                'foreignField': "name",
                'as': "delivery_docs"
            }
    }
]


def supplier_query():
    y = []
    for i in client.cluster_new.supplier.find({}):
        y.append(i)
    return y


z = list(client.cluster_new.supplier.aggregate(pipeline))
y = supplier_query()


def paramintonet(z,  y):
    rez = []
    i1 = innovcount(z)
    d1 = designcount(z)
    ts1 = techcount(z)

    lt1 = contactcount(z)
    vf1 = supplchcount(z)
    mf1 = meetcount(y)

    ci1 = eventscount(y)
    qs1 = qualitycount(y)

    dr1 = defectcount(z)
    otd1 = delivtimecount(z)
    gl1 = distaddrcount(y)

    mv1 = contactheadcount(y)
    sf1 = delivdocscount(z)
    ua1 = unimembercount(y)

    op1 = pricevalue(z)



    for j in range(0, len(i1)):
        rez.append(bayes_bake(i1[j], d1[j], ts1[j], lt1[j], vf1[j], mf1[j], ci1[j], qs1[j], dr1[j], otd1[j], gl1[j], mv1[j], sf1[j], ua1[j], op1[j]))

    for i in range(0, len(rez)):
        rez[i] = [suppname(y)[i]]+rez[i]

    rez.insert(0, ['Company name', 'Overall value', 'Material value', 'Spiritual value', 'Cost value', "Technological capability", "Flexibility", "Quality", "Delivery", "Org culture and strategy"])

    column_names = rez.pop(0)
    df = pd.DataFrame(rez, columns=column_names)
    df.to_excel("C:/Users/Arina27/Desktop/Arina/course proj/final/companies.xlsx")


paramintonet(z, y)
print('Successfully added!')

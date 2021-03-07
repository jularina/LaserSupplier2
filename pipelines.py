import geocoder
import math

import pymongo
from pymongo import MongoClient
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pprint
import itertools
import pandas as pd
import collections, functools, operator

client = MongoClient("mongodb+srv://@-pldc3.gcp.mongodb.net/cluster_new?retryWrites=true&w=1")

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

z = list(client.cluster_new.supplier.aggregate(pipeline))


def supplier_query():
    y = []
    for i in client.cluster_new.supplier.find({}):
        y.append(i)
    return y

y = supplier_query()

def innovcount(z):
    innov = []
    for jj in range(0, len(z)):
        z1 = z[jj].get('delivery_docs')

        l = []
        for ii in range(0, len(z1)):
            zz = z1[ii].get('items')
            l1 = []
            for i in range(0, len(zz)):
                if zz[i].get('innovation_stage'):
                    l1.append(zz[i].get('innovation_stage'))
            l.append(sum(l1)/len(zz))
        innov.append(round(sum(l)/len(z1), 3))

    return innov




def designcount(z):
    des = []
    for jj in range(0, len(z)):
        l = []
        l.append(z[jj].get('design_lab'))
        z1 = z[jj].get('delivery_docs')

        for ii in range(0, len(z1)):
            l.append(z1[ii].get('design_decision'))

        if l[0]:
            des.append(round(((l.count(3) * 0.8 + l.count(2) * 0.2) / (len(l)-1) * 1.1), 3))
        else:
            des.append(round((l.count(3) * 0.8 + l.count(2) * 0.2) / (len(l)-1), 3))
    return des


def techcount(z):
    tech = []
    t=0
    o=0
    for jj in range(0, len(z)):

        z1 = z[jj].get('delivery_docs')

        for ii in range(0, len(z1)):
            l = z1[ii].get('original_final_ratio')
            t = t + l.get('original')
            o = o + l.get('total')
        tech.append(round(o/t, 3))
    return tech


def contactcount(z):
    cont = []
    normalized = []
    for jj in range(0, len(z)):

        z1 = z[jj].get('delivery_docs')
        l = 0
        for ii in range(0, len(z1)):
            l = l + z1[ii].get('contact_time_days')

        cont.append(l/len(z1))
    for i in range(0, len(cont)):
        normalized.append(round((max(cont)-cont[i])/(max(cont)-min(cont)), 3))
    return normalized



def supplchcount(z):
    scont = []
    normalized = []
    for jj in range(0, len(z)):

        z1 = z[jj].get('delivery_docs')
        l = 0
        for ii in range(0, len(z1)):
            l = l + z1[ii].get('delivery_indicators').get('scope_of_supplement_change')

        scont.append(l / len(z1))
    for i in range(0, len(scont)):
        normalized.append(round((scont[i]-min(scont))/(max(scont)-min(scont)), 3))
    return normalized


def meetcount(y):
    meet = []
    normalized = []
    for jj in range(0, len(z)):

        z1 = z[jj].get('delivery_docs')
        l = 0
        for ii in range(0, len(z1)):
            l = l + z1[ii].get('postponed_meetings')

        meet.append(l/len(z1))
    for i in range(0, len(meet)):
        normalized.append(round((max(meet)-meet[i])/(max(meet)-min(meet)), 3))
    return normalized


def eventscount(y):
    events = []
    l = []
    for jj in range(0, len(y)):

        z1 = y[jj].get('social_events')
        f = 0
        for i in range(0, len(z1)):
            f = f + (z1[i].get('quantity') * z1[i].get('prestige'))
        l.append(f)
    for j in l:
        events.append(round(j/sum(l), 3))
    return events


def qualitycount(y):
    qual = []
    l = []
    for jj in range(0, len(y)):

        z1 = y[jj].get('quality_system')
        if 'ISO/TC-172/SC-3/WG-3' in z1 and 'ISO/TC-172/SC-9/WG-1' in z1:
            p = 1
            qual.append(p)
        else:
            l.append(len(z1))
    for i in l:
        qual.append(round(i/sum(l), 3))
    return qual


def defectcount(z):
    supplch = []
    l1 = []
    for jj in range(0, len(z)):

        z1 = z[jj].get('delivery_docs')
        l = 0
        for ii in range(0, len(z1)):
            l = l + z1[ii].get('delivery_indicators').get('quantity_defective_goods')
        l1.append(l)
    for j in l1:
        supplch.append(round(1-(j/sum(l1)), 3))

    return supplch


def contactheadcount(y):
    conth = []

    for jj in range(0, len(y)):

        if y[jj].get('contact_with_head'):
            conth.append(1)
        else:
            conth.append(0)
    return conth


def unimembercount(y):
    unimem = []

    for jj in range(0, len(y)):

        if y[jj].get('university_member'):
            unimem.append(1)
        else:
            unimem.append(0)
    return unimem


def delivtimecount(z):
    delivtime = []

    for jj in range(0, len(z)):
        z1 = z[jj].get('delivery_docs')
        l = 0
        l1 = []
        for ii in range(0, len(z1)):
            l = l + z1[ii].get('delivery_indicators').get('delivery_time_days')
            l1.append(z1[ii].get('delivery_indicators').get('on_time_delivered'))

        if (l / len(z1)) < 45:
            if l1.count('true') > l1.count('false'):
                delivtime.append(1)
            else:
                delivtime.append(0.5)
        else:
            if l1.count('true') < l1.count('false'):
                delivtime.append(0)
            else:
                delivtime.append(0.5)

    return delivtime


def delivdocscount(z):
    delivdocs = []
    l2 = []
    l3 = []
    for jj in range(0, len(z)):
        z1 = z[jj].get('delivery_docs')
        l1 = []
        for ii in range(0, len(z1)):
            l1.append(z1[ii].get('doc_date'))
        l2.append(min(l1))
        l3.append(len(z1))

    for i in l3:
        delivdocs.append(round(i/sum(l3), 3))
    delivdocs[l2.index(min(l2))] = delivdocs[l2.index(min(l2))]*1.1
    return delivdocs


def distaddrcount(y):
    distaddr = []
    normalized = []
    R = 6373.0
    g = geocoder.geonames('Saint Petersburg', key='arina270799')
    lat1 = math.radians(float(g.lat))
    lon1 = math.radians(float(g.lng))

    for jj in range(0, len(y)):
        g = geocoder.geonames(y[jj].get('address').get('city'), key='arina270799')
        lat2 = math.radians(float(g.lat))
        lon2 = math.radians(float(g.lng))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        distaddr.append(distance)
    for i in range(0, len(distaddr)):
        normalized.append(round((max(distaddr)-distaddr[i])/(max(distaddr)-min(distaddr)), 3))

    return normalized



def pricevalue(z):
    prvalue1 = {}
    prvalue2 = {}

    prvalue1_new = {}
    prvalue2_new = {}

    normalized = []
    for jj in range(0, len(z)):
        z1 = z[jj].get('delivery_docs')

        l1 = []
        l2 = []
        for ii in range(0, len(z1)):
            zz = z1[ii].get('items')

            for i in range(0, len(zz)):
                if zz[i].get('innovation_stage') == 1:
                    l1.append(zz[i].get('unit_price'))
                elif zz[i].get('innovation_stage') == 0:
                    l2.append(zz[i].get('unit_price'))
        if len(l1) > 0:
            prvalue1.update({str(jj) : sum(l1)/len(l1)})
        if len(l2) > 0:
            prvalue2.update({str(jj) : sum(l2)/len(l2)})

    for i in range(0, len(prvalue1)):
        prvalue11 = list(prvalue1.values())
        prvalue11_new = list(prvalue1.keys())
        m1 = round((max(prvalue1.values())-prvalue11[i])/(max(prvalue1.values())-min(prvalue1.values())), 3)
        prvalue1_new.update({str(prvalue11_new[i]) : m1})

    for z in range(0, len(prvalue2)):
        prvalue22 = list(prvalue2.values())
        prvalue22_new = list(prvalue2.keys())
        m2 = round((max(prvalue2.values())-prvalue22[z])/(max(prvalue2.values())-min(prvalue2.values())), 3)
        prvalue2_new.update({str(prvalue22_new[z]): m2})

    normalized.append(prvalue1_new)
    normalized.append(prvalue2_new)

    result = dict(functools.reduce(operator.add, map(collections.Counter, normalized)))
    res = {k: round((1 - v / 2), 3) for k, v in result.items()}

    return  list(dict(sorted(res.items())).values())


def suppname(y):
    suppn = []

    for jj in range(0, len(y)):
        suppn.append(y[jj].get('name'))
    return suppn

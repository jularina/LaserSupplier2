# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:15:39 2020

@author: Arina27
"""

import math
import json
from pomegranate import *


def bayes_bake(i, d, ts, lt, vf, mf, ci, qs, dr, otd, gl, mv, sf, ua, op):
    # factor group - 1
    innovation = DiscreteDistribution({'yes': i, 'no': 1-i})
    design = DiscreteDistribution({'yes': d, 'no': 1-d})
    technical_strength = DiscreteDistribution({'yes': ts, 'no': 1-ts})

    # factor group - 2
    lead_time = DiscreteDistribution({'yes': lt, 'no': 1-lt})
    volume_flexibility = DiscreteDistribution({'yes': vf, 'no': 1-vf})
    mix_flexibility = DiscreteDistribution({'yes': mf, 'no': 1-mf})

    # factor group - 3
    continous_improvment = DiscreteDistribution({'yes': ci, 'no': 1-ci})
    quality_system = DiscreteDistribution({'yes': qs, 'no': 1-qs})

    # factor group - 4
    delivery_reliability = DiscreteDistribution({'yes': dr, 'no': 1-dr})
    on_time_delivery = DiscreteDistribution({'yes': otd, 'no': 1-otd})
    geographical_location = DiscreteDistribution({'yes': gl, 'no': 1-gl})

    # factor group - 5
    management_vision = DiscreteDistribution({'yes': mv, 'no': 1-mv})
    strategic_fit = DiscreteDistribution({'yes': sf, 'no': 1-sf})
    university_affiliation = DiscreteDistribution({'yes': ua, 'no': 1-ua})

    # factor 1
    technological_capability = ConditionalProbabilityTable(
        [['yes', 'no', 'yes', 'yes', 0.92],
         ['no', 'yes', 'yes', 'yes', 0.75],
         ['yes', 'yes', 'yes', 'yes', 1],
         ['no', 'no', 'yes', 'yes', 0.67],
         ['yes', 'no', 'no', 'yes', 0.25],
         ['no', 'yes', 'no', 'yes', 0.08],
         ['yes', 'yes', 'no', 'yes', 0.33],
         ['no', 'no', 'no', 'yes', 0],
         ['yes', 'no', 'yes', 'no', 0.08],
         ['no', 'yes', 'yes', 'no', 0.25],
         ['yes', 'yes', 'yes', 'no', 0],
         ['no', 'no', 'yes', 'no', 0.23],
         ['yes', 'no', 'no', 'no', 0.75],
         ['no', 'yes', 'no', 'no', 0.92],
         ['yes', 'yes', 'no', 'no', 0.67],
         ['no', 'no', 'no', 'no', 1]], [innovation, design, technical_strength])

    # factor 2
    flexibility = ConditionalProbabilityTable(
        [['yes', 'no', 'yes', 'yes', 0.66],
         ['no', 'yes', 'yes', 'yes', 0.41],
         ['yes', 'yes', 'yes', 'yes', 1],
         ['no', 'no', 'yes', 'yes', 0.08],
         ['yes', 'no', 'no', 'yes', 0.58],
         ['no', 'yes', 'no', 'yes', 0.33],
         ['yes', 'yes', 'no', 'yes', 0.91],
         ['no', 'no', 'no', 'yes', 0],
         ['yes', 'no', 'yes', 'no', 0.34],
         ['no', 'yes', 'yes', 'no', 0.59],
         ['yes', 'yes', 'yes', 'no', 0],
         ['no', 'no', 'yes', 'no', 0.92],
         ['yes', 'no', 'no', 'no', 0.42],
         ['no', 'yes', 'no', 'no', 0.67],
         ['yes', 'yes', 'no', 'no', 0.09],
         ['no', 'no', 'no', 'no', 1]], [lead_time, volume_flexibility, mix_flexibility])

    # factor - 3
    quality = ConditionalProbabilityTable(
        [['yes', 'no', 'yes', 0.2],
         ['no', 'yes', 'yes', 0.8],
         ['yes', 'yes', 'yes', 1],
         ['no', 'no', 'yes', 0],
         ['yes', 'no', 'no', 0.8],
         ['no', 'yes', 'no', 0.2],
         ['yes', 'yes', 'no', 0],
         ['no', 'no', 'no', 1]], [continous_improvment, quality_system])

    # factor 4
    delivery = ConditionalProbabilityTable(
        [['yes', 'no', 'yes', 'yes', 0.67],
         ['no', 'yes', 'yes', 'yes', 0.44],
         ['yes', 'yes', 'yes', 'yes', 1],
         ['no', 'no', 'yes', 'yes', 0.11],
         ['yes', 'no', 'no', 'yes', 0.56],
         ['no', 'yes', 'no', 'yes', 0.33],
         ['yes', 'yes', 'no', 'yes', 0.89],
         ['no', 'no', 'no', 'yes', 0],
         ['yes', 'no', 'yes', 'no', 0.33],
         ['no', 'yes', 'yes', 'no', 0.56],
         ['yes', 'yes', 'yes', 'no', 0],
         ['no', 'no', 'yes', 'no', 0.89],
         ['yes', 'no', 'no', 'no', 0.44],
         ['no', 'yes', 'no', 'no', 0.67],
         ['yes', 'yes', 'no', 'no', 0.11],
         ['no', 'no', 'no', 'no', 1]], [delivery_reliability, on_time_delivery, geographical_location])

    # factor 5
    org_culture_strategy = ConditionalProbabilityTable(
        [['yes', 'no', 'yes', 'yes', 0.55],
         ['no', 'yes', 'yes', 'yes', 0.77],
         ['yes', 'yes', 'yes', 'yes', 1],
         ['no', 'no', 'yes', 'yes', 0.33],
         ['yes', 'no', 'no', 'yes', 0.22],
         ['no', 'yes', 'no', 'yes', 0.44],
         ['yes', 'yes', 'no', 'yes', 0.66],
         ['no', 'no', 'no', 'yes', 0],
         ['yes', 'no', 'yes', 'no', 0.45],
         ['no', 'yes', 'yes', 'no', 0.33],
         ['yes', 'yes', 'yes', 'no', 0],
         ['no', 'no', 'yes', 'no', 0.67],
         ['yes', 'no', 'no', 'no', 0.78],
         ['no', 'yes', 'no', 'no', 0.56],
         ['yes', 'yes', 'no', 'no', 0.34],
         ['no', 'no', 'no', 'no', 1]], [management_vision, strategic_fit, university_affiliation])

    # value 1
    material_value = ConditionalProbabilityTable(
        [['yes', 'no', 'yes', 'yes', 0.47],
         ['no', 'yes', 'yes', 'yes', 0.58],
         ['yes', 'yes', 'yes', 'yes', 1],
         ['no', 'no', 'yes', 'yes', 0.5],
         ['yes', 'no', 'no', 'yes', 0.42],
         ['no', 'yes', 'no', 'yes', 0.08],
         ['yes', 'yes', 'no', 'yes', 0.5],
         ['no', 'no', 'no', 'yes', 0],
         ['yes', 'no', 'yes', 'no', 0.53],
         ['no', 'yes', 'yes', 'no', 0.42],
         ['yes', 'yes', 'yes', 'no', 0],
         ['no', 'no', 'yes', 'no', 0.5],
         ['yes', 'no', 'no', 'no', 0.58],
         ['no', 'yes', 'no', 'no', 0.92],
         ['yes', 'yes', 'no', 'no', 0.5],
         ['no', 'no', 'no', 'no', 1]], [technological_capability, delivery, quality])

    # value 2
    spiritual_value = ConditionalProbabilityTable(
        [['yes', 'no', 'yes', 0.8],
         ['no', 'yes', 'yes', 0.2],
         ['yes', 'yes', 'yes', 1],
         ['no', 'no', 'yes', 0],
         ['yes', 'no', 'no', 0.2],
         ['no', 'yes', 'no', 0.8],
         ['yes', 'yes', 'no', 0],
         ['no', 'no', 'no', 1]], [flexibility, org_culture_strategy])

    # value 3
    cost_value = DiscreteDistribution({'overpriced': 1-op, 'adequate': op})

    # overall_value
    overall_value = ConditionalProbabilityTable(
        [['yes', 'no', 'adequate', 'yes', 0.75],
         ['no', 'yes', 'adequate', 'yes', 0.58],
         ['yes', 'yes', 'adequate', 'yes', 1],
         ['no', 'no', 'adequate', 'yes', 0.33],
         ['yes', 'no', 'overpriced', 'yes', 0.42],
         ['no', 'yes', 'overpriced', 'yes', 0.25],
         ['yes', 'yes', 'overpriced', 'yes', 0.67],
         ['no', 'no', 'overpriced', 'yes', 0],
         ['yes', 'no', 'adequate', 'no', 0.25],
         ['no', 'yes', 'adequate', 'no', 0.42],
         ['yes', 'yes', 'adequate', 'no', 0],
         ['no', 'no', 'adequate', 'no', 0.67],
         ['yes', 'no', 'overpriced', 'no', 0.58],
         ['no', 'yes', 'overpriced', 'no', 0.75],
         ['yes', 'yes', 'overpriced', 'no', 0.33],
         ['no', 'no', 'overpriced', 'no', 1]], [material_value, spiritual_value, cost_value])

    # criterion
    s1 = State(innovation, name="Innovation")
    s2 = State(design, name="Design")
    s3 = State(technical_strength, name="Technical strength")
    s4 = State(lead_time, name="Lead time")
    s5 = State(volume_flexibility, name="Volume flexibility")
    s6 = State(mix_flexibility, name="Mix flexibility")
    s7 = State(continous_improvment, name="Continuous improvment")
    s8 = State(quality_system, name="Quality system")
    s9 = State(delivery_reliability, name="Delivery reliability")
    s10 = State(on_time_delivery, name="On time delivery")
    s11 = State(geographical_location, name="Geographical location")
    s12 = State(management_vision, name="Managment vision")
    s13 = State(strategic_fit, name="Strategic fit")
    s14 = State(university_affiliation, name="University affiliation")

    # factor
    s15 = State(technological_capability, name="Technological capability")
    s16 = State(flexibility, name="Flexibility")
    s17 = State(quality, name="Quality")
    s18 = State(delivery, name="Delivery")
    s19 = State(org_culture_strategy, name="Org culture and strategy")

    # value
    s20 = State(material_value, name="Material value")
    s21 = State(spiritual_value, name="Spiritual value")
    s22 = State(cost_value, name="Cost value")
    s23 = State(overall_value, name="Overall value")

    network = BayesianNetwork("Supplier impact on risk:")
    network.add_states(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22,
                       s23)

    network.add_edge(s1, s15)
    network.add_edge(s2, s15)
    network.add_edge(s3, s15)

    network.add_edge(s4, s16)
    network.add_edge(s5, s16)
    network.add_edge(s6, s16)

    network.add_edge(s7, s17)
    network.add_edge(s8, s17)

    network.add_edge(s9, s18)
    network.add_edge(s10, s18)
    network.add_edge(s11, s18)

    network.add_edge(s12, s19)
    network.add_edge(s13, s19)
    network.add_edge(s14, s19)

    network.add_edge(s15, s20)
    network.add_edge(s17, s20)
    network.add_edge(s18, s20)

    network.add_edge(s16, s21)
    network.add_edge(s19, s21)

    network.add_edge(s20, s23)
    network.add_edge(s21, s23)
    network.add_edge(s22, s23)

    network.bake()

    beliefs1 = network.predict_proba({})
    beliefs1 = map(str, beliefs1)
    z1 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs1) if state.name == "Overall value")
    z1=json.loads(z1)
    rez1 = round(z1.get("parameters")[0].get("yes"), 3)

    beliefs2 = network.predict_proba({})
    beliefs2 = map(str, beliefs2)
    z2 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs2) if state.name == "Material value")
    z2 = json.loads(z2)
    rez2 = round(z2.get("parameters")[0].get("yes"), 3)

    beliefs3 = network.predict_proba({})
    beliefs3 = map(str, beliefs3)
    z3 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs3) if state.name == "Spiritual value")
    z3=json.loads(z3)
    rez3 = round(z3.get("parameters")[0].get("yes"), 3)


    beliefs4 = network.predict_proba({})
    beliefs4 = map(str, beliefs4)
    z4 = "\n".join("{}".format(state) for state in network.states if state.name == "Cost value")
    z4 = json.loads(z4)
    rez4 = round(z4.get('distribution').get("parameters")[0].get("adequate"), 3)

#factors
    beliefs5 = network.predict_proba({})
    beliefs5 = map(str, beliefs5)
    z5 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs5) if state.name == "Technological capability")
    z5=json.loads(z5)
    rez5 = round(z5.get("parameters")[0].get("yes"), 3)

    beliefs6 = network.predict_proba({})
    beliefs6 = map(str, beliefs6)
    z6 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs6) if state.name == "Flexibility")
    z6=json.loads(z6)
    rez6 = round(z6.get("parameters")[0].get("yes"), 3)


    beliefs7 = network.predict_proba({})
    beliefs7 = map(str, beliefs7)
    z7 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs7) if state.name == "Quality")
    z7=json.loads(z7)
    rez7 = round(z7.get("parameters")[0].get("yes"), 3)

    beliefs8 = network.predict_proba({})
    beliefs8 = map(str, beliefs8)
    z8 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs8) if state.name == "Delivery")
    z8 = json.loads(z8)
    rez8 = round(z8.get("parameters")[0].get("yes"), 3)

    beliefs9 = network.predict_proba({})
    beliefs9 = map(str, beliefs9)
    z9 = "\n".join("{}".format(belief) for state, belief in zip(network.states, beliefs9) if state.name == "Org culture and strategy")
    z9 = json.loads(z9)
    rez9 = round(z9.get("parameters")[0].get("yes"), 3)

    return [rez1, rez2, rez3, rez4, rez5, rez6, rez7, rez8, rez9]

#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
#
# Last modified: Fri, 22 Sep 2017 19:15:19 +0900
# 
import json
import sys
from libsbml import *

# List of objects
sbml_json = []

def check_name_duplicated(model):
    name_duplicated = False
    name_dic = {}
    for s in model.getListOfSpecies():
        if s.getName() in name_dic:
            name_duplicated = True
            break
        name_dic[s.getName()] = s.getId()
    return name_duplicated


def add_species(model):
    name_duplicated = check_name_duplicated(model)
    for s in model.getListOfSpecies():
        if name_duplicated:
            s_id_dic = { "id": s.getId(), "name": s.getId() }
        else:
            s_id_dic = { "id": s.getId(), "name": s.getName() }
        s_dic = { "data": s_id_dic, "group": "nodes" }
        sbml_json.append(s_dic)


def add_reactions(model):
    for r in model.getListOfReactions():
        # Add reaction node
        r_id_dic = { "id": r.getId(), "name": r.getName() }
        r_dic = { "data": r_id_dic, "group": "nodes", "classes": "rxn" }
        sbml_json.append(r_dic)
        # Add reactant -> reaction edge
        for reac in r.getListOfReactants():
            reac_id = reac.getSpecies() + '_' + r.getId()
            reac_id_dic = { "id": reac_id, "source": reac.getSpecies(), "target": r.getId() }
            reac_dic = { "data": reac_id_dic, "group": "edges", "classes": "reactant" }
            sbml_json.append(reac_dic)
        # Add reaction -> product edge
        for prod in r.getListOfProducts():
            prod_id = r.getId() + '_' + prod.getSpecies()
            prod_id_dic = { "id": prod_id, "source": r.getId(), "target": prod.getSpecies() }
            prod_dic = { "data": prod_id_dic, "group": "edges", "classes": "product" }
            sbml_json.append(prod_dic)
        # Add modifier -> reaction edge
        for mod in r.getListOfModifiers():
            mod_id = mod.getSpecies() + '_' + r.getId()
            mod_id_dic = { "id": mod_id, "source": mod.getSpecies(), "target": r.getId() }
            mod_dic = { "data": mod_id_dic, "group": "edges", "classes": "activation" }  # need to parse CellDesigner annotation
            sbml_json.append(mod_dic)


def add_sbml_objects(filepath):
    d = readSBML(filepath)
    m = d.getModel()
    add_species(m)
    add_reactions(m)

def main():
    if len(sys.argv) < 2:
        print "Usage: %s sbml.xml" % sys.argv[0]
        print "Convert given SBML to JSON file(model.json)."
        quit()

    filepath = sys.argv[1]
    add_sbml_objects(filepath)
    f = open('model.json', "w")
    json.dump(sbml_json, f, ensure_ascii=False, indent=2)
    f.close()
    print "%s successfully exported to model.json." % sys.argv[1]

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
#
# Description: POST service for exploration of
# data of Lung Cancer in the iASiS KG.
#

import sys
from flask import Flask, abort, request, make_response
import json
from SPARQLWrapper import SPARQLWrapper, JSON
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

LIMIT=10

#KG="http://localhost:11384/sparql"
KG = os.environ["ENDPOINT"]
#KG="http://node2.research.tib.eu:8893/sparql"
#all
#KG="http://node2.research.tib.eu:18871/sparql"
#KG="http://node2.research.tib.eu:11789/sparql"
#drug_pub
#KG="http://node2.research.tib.eu:11124/sparql"
EMPTY_JSON = "{}"

app = Flask(__name__)

############################
#
# Query constants
#
############################






QUERY_DISORDERS_TO_DRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?DrugDisorderInteraction a <http://research.tib.eu/p4-lucat/vocab/DrugDisorderInteraction>.
?DrugDisorderInteraction <http://research.tib.eu/p4-lucat/vocab/precipitantDrug> ?drug.
?DrugDisorderInteraction <http://research.tib.eu/p4-lucat/vocab/objectIndication> ?indication_ID.
?indication_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation>  ?indication.
?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
"""

QUERY_BIOMARKERS_TO_LC_DRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/biomarker_has_indication> ?drug .
                               ?drug a <http://research.tib.eu/p4-lucat/vocab/LungCancerDrug>.
                               ?biomarker_ID a <http://research.tib.eu/p4-lucat/vocab/Biomarker>. 
                               ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?biomarker. 
                               ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
"""

QUERY_BIOMARKERS_TO_ALL_DRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/biomarker_has_indication> ?drug .
       
                               ?biomarker_ID a <http://research.tib.eu/p4-lucat/vocab/Biomarker>. 
                               ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?biomarker. 
                               ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
"""

QUERY_BIOMARKERS_TO_DEMENTIA_DRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/biomarker_has_indication> ?drug .
                               ?drugdementia  a <http://research.tib.eu/p4-lucat/vocab/DementiaDrug>.
                               ?drug owl:sameAs ?drugdementia .
                               ?biomarker_ID a <http://research.tib.eu/p4-lucat/vocab/Biomarker>. 
                               ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?biomarker. 
                               ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
"""

QUERY_DISORDERS_TO_LCDRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?drug a <http://research.tib.eu/p4-lucat/vocab/LungCancerDrug>.
?DrugDisorderInteraction a <http://research.tib.eu/p4-lucat/vocab/DrugDisorderInteraction>.
?DrugDisorderInteraction <http://research.tib.eu/p4-lucat/vocab/precipitantDrug> ?drug.
?DrugDisorderInteraction <http://research.tib.eu/p4-lucat/vocab/objectIndication> ?indication_ID.
?indication_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation>  ?indication.
?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
"""

QUERY_DISORDERS_TO_DEMENTIA_DRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?drugdementia  a <http://research.tib.eu/p4-lucat/vocab/DementiaDrug>.
                                          ?drug owl:sameAs ?drugdementia .
                                          ?drugDisorder a <http://research.tib.eu/p4-lucat/vocab/DrugDisorderInteraction>.
                            ?drugDisorder <http://research.tib.eu/p4-lucat/vocab/interactor1_Drug>  ?drug.   
                             ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.  
                            ?drugDisorder <http://research.tib.eu/p4-lucat/vocab/interactor2Indication>  ?indication_ID.    
                            ?indication_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?indication.
"""

QUERY_CUI_TO_DRUGS = """
SELECT DISTINCT ?drug ?drugBankID WHERE {
               ?drug <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?drugCUI.
               ?drug <http://research.tib.eu/p4-lucat/vocab/drugBankID> ?drugBankID
               FILTER(isURI(?drugBankID))
               
"""

QUERY_DRUGS_TO_SIDEEFFECTS_LC ="""
SELECT DISTINCT ?drugLabel ?sideEffectLabel WHERE {  ?drug a <http://research.tib.eu/p4-lucat/vocab/Drug>.
                                           ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
                            ?drug <http://research.tib.eu/p4-lucat/vocab/drug_isRelatedTo_dse>  ?drugSideEffect.
                            ?drugSideEffect <http://research.tib.eu/p4-lucat/vocab/dse_AvgFrequency> ?freq.
                            ?sideEffectLabel <http://research.tib.eu/p4-lucat/vocab/sideEffect_isRelatedTo_dse> ?drugSideEffect.
                  
                           
"""

QUERY_DRUGS_TO_SIDEEFFECTS_ALL ="""
SELECT DISTINCT ?drugLabel ?sideEffectLabel WHERE {  ?drug a <http://research.tib.eu/p4-lucat/vocab/Drug>.
                                           ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
                            ?drug <http://research.tib.eu/p4-lucat/vocab/drug_isRelatedTo_dse>  ?drugSideEffect.
                            ?drugSideEffect <http://research.tib.eu/p4-lucat/vocab/dse_AvgFrequency> ?freq.
                            ?sideEffectLabel <http://research.tib.eu/p4-lucat/vocab/sideEffect_isRelatedTo_dse> ?drugSideEffect.
                  
                           
"""


QUERY_DRUGS_TO_SIDEEFFECTS_AD_D ="""
SELECT DISTINCT ?drugLabel ?sideEffectLabel WHERE {  ?drug a <http://research.tib.eu/p4-lucat/vocab/Drug>.
                                           ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
                            ?drug <http://research.tib.eu/p4-lucat/vocab/drug_isRelatedTo_dse>  ?drugSideEffect.
                            ?drugSideEffect <http://research.tib.eu/p4-lucat/vocab/dse_AvgFrequency> ?freq.
                            ?sideEffectLabel <http://research.tib.eu/p4-lucat/vocab/sideEffect_isRelatedTo_dse> ?drugSideEffect.
                           
                           
"""

QUERY_CUI_TO_LCDRUGS = """
SELECT DISTINCT ?drug ?drugBankID WHERE {
                ?drug a <http://research.tib.eu/p4-lucat/vocab/LungCancerDrug>.
               ?drug <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?drugCUI.
               ?drug <http://research.tib.eu/p4-lucat/vocab/drugBankID> ?drugBankID
               FILTER(isURI(?drugBankID))
               
"""

QUERY_CUI_TO_DEMENTIA_DRUGS = """
SELECT DISTINCT ?drug ?drugBankID WHERE {
                ?drugdementia a <http://research.tib.eu/p4-lucat/vocab/DementiaDrug>.
                ?drug owl:sameAs ?drugdementia .
               ?drug <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?drugCUI.
               ?drug <http://research.tib.eu/p4-lucat/vocab/drugBankID> ?drugBankID.
               FILTER(isURI(?drugBankID))
               
"""

QUERY_CUI_TO_AD_DRUGS = """
SELECT DISTINCT ?drug ?drugBankID WHERE {
                ?drug a <http://research.tib.eu/p4-lucat/vocab/ADDrug>.
               ?drug <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?drugCUI.
               ?drug <http://research.tib.eu/p4-lucat/vocab/drugBankID> ?drugBankID.
               FILTER(isURI(?drugBankID))
               
"""

QUERY_DISORDERS_TO_AD_DRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?drug  a <http://research.tib.eu/p4-lucat/vocab/ADDrug>.
                                          ?drugDisorder a <http://research.tib.eu/p4-lucat/vocab/DrugDisorderInteraction>.
                            ?drugDisorder <http://research.tib.eu/p4-lucat/vocab/interactor1_Drug>  ?drug.   
                             ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.  
                            ?drugDisorder <http://research.tib.eu/p4-lucat/vocab/interactor2Indication>  ?indication_ID.    
                            ?indication_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?indication.
"""

QUERY_BIOMARKERS_TO_AD_DRUGS ="""
SELECT DISTINCT ?drug ?drugLabel WHERE {  ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/biomarker_has_indication> ?drug .
                               ?drug  a <http://research.tib.eu/p4-lucat/vocab/ADDrug>.
                               ?biomarker_ID a <http://research.tib.eu/p4-lucat/vocab/Biomarker>. 
                               ?biomarker_ID <http://research.tib.eu/p4-lucat/vocab/hasCUIAnnotation> ?biomarker. 
                               ?drug <http://research.tib.eu/p4-lucat/vocab/drugLabel> ?drugLabel.
"""

############################
#
# Query generation
#
############################


def execute_query(query):
    sparql_ins = SPARQLWrapper(KG)
    sparql_ins.setQuery(query)
    sparql_ins.setReturnFormat(JSON)
    return sparql_ins.query().convert()['results']['bindings']



############################
#
# Processing results
#
############################






def biomarkers2drugs_query(biomarkers,drugType):
    if drugType=="all":
        query=QUERY_BIOMARKERS_TO_ALL_DRUGS
    if drugType=="lc":
        query=QUERY_BIOMARKERS_TO_LC_DRUGS
    elif drugType=="dementia":
        query=QUERY_BIOMARKERS_TO_DEMENTIA_DRUGS
    elif drugType=="ad":
        query=QUERY_BIOMARKERS_TO_AD_DRUGS
    query+="FILTER(?biomarker in ("
    for cui in biomarkers:
        query+="<http://research.tib.eu/p4-lucat/entity/"+cui+">,"
    query=query[:-1]
    query+="))}"
    qresults = execute_query(query)
    qresults=[(item['drug']['value'],item['drugLabel']['value']) for item in qresults]
    return qresults


def disorder2drugs_query(disorders,drugType='all'):
    if drugType=='all':
        query=QUERY_DISORDERS_TO_DRUGS
    elif drugType=='lc' :
        query=QUERY_DISORDERS_TO_LCDRUGS
    elif drugType=='dementia' :
        query=QUERY_DISORDERS_TO_DEMENTIA_DRUGS
    elif drugType=='ad' :
        query=QUERY_DISORDERS_TO_AD_DRUGS
    query+="FILTER(?indication in ("
    for cui in disorders:
        query+="<http://research.tib.eu/p4-lucat/entity/"+cui+">,"
    query=query[:-1]
    query+="))}"
    qresults = execute_query(query)
    qresults=[(item['drug']['value'],item['drugLabel']['value']) for item in qresults]
        
    return qresults


def drugsCUI2drugID_query(drugs,drugType='all'):
    if drugType=='all':
        query=QUERY_CUI_TO_DRUGS
    elif drugType=='lc' :
        query=QUERY_CUI_TO_LCDRUGS
    elif drugType=='dementia' :
        query=QUERY_CUI_TO_DEMENTIA_DRUGS
    elif drugType=='ad' :
        query=QUERY_CUI_TO_AD_DRUGS
    query+="FILTER(?drugCUI in ("
    for drug in drugs:
        query+="<http://research.tib.eu/p4-lucat/entity/"+drug+">,"
    query=query[:-1]
    query+="))}"
    qresults = execute_query(query)
    qresults=[(item['drugBankID']['value'],item['drug']['value']) for item in qresults]
    return qresults

def drug2sideEffect_query(drugs,topic):
    if topic=="all":
        query=QUERY_DRUGS_TO_SIDEEFFECTS_ALL
    if topic=="lc":
        query=QUERY_DRUGS_TO_SIDEEFFECTS_LC
    elif topic=="dementia" or topic=="ad":
        query=QUERY_DRUGS_TO_SIDEEFFECTS_AD_D
    query+="FILTER(?drug in ("
    for drug in drugs:
        query+="<"+drug+">,"
    query=query[:-1]
    query+="))} ORDER BY DESC(?freq)"
    qresults = execute_query(query)
    qresults=[(item['drugLabel']['value'],item['sideEffectLabel']['value'].replace("http://research.tib.eu/p4-lucat/entity/","").replace("_"," ")) for item in qresults]
    return qresults


    
def sideEffects_filtering_sorting(sideEffects, page, sort, limit):
    # Sorting the side effects for each drug
    for drug in sideEffects:
        sideEffects[drug].sort(key=lambda x: x['sideEffect'])

    # Sorting the drugs
    sorted_drugs = sorted(sideEffects.items())

    # Converting the sorted list back to a dictionary
    sorted_dict = dict(sorted_drugs)

    # if limit==-1: return the entire sorted_dict
    if limit == -1:
        return sorted_dict

    # For pagination
    if page == 0:
        return {k: sorted_dict[k] for k in list(sorted_dict)[page:limit]}
    else:
        return {k: sorted_dict[k] for k in list(sorted_dict)[page*limit:(page*limit)+limit]}


def check_dict_duplicate(list_of_dict,dict_):
    for dic in list_of_dict:
        count=0
        for key,value in dic.items():
            if dict_[key]==value:
                count=count+1
        if count==len(dict_):
            return True

    return False



def proccesing_response(input_dicc, topic,limit,page,sort):
    cuis=dict()
    codicc=dict()
    sideEffects=dict()
    for elem in input_dicc:
        lcuis = input_dicc[elem]
        if len(lcuis)==0:
            continue
        for item in lcuis:
            cuis[item]=elem

        if len(cuis)==0:
            continue


                    
          
             ##############################sideEffects################################3
          
        if elem=='comorbidities' or elem=='histology':
            drugs=disorder2drugs_query(input_dicc[elem],topic)
        elif elem=='biomarkers':
            drugs=biomarkers2drugs_query(input_dicc[elem],topic)
        elif elem in ['LCdrugs']:
            drugs=drugsCUI2drugID_query(input_dicc[elem],topic)
        if len(drugs)!=0:
            drug_sideEffects=drug2sideEffect_query([drug[0] for drug in drugs],topic)
            
            for item in drug_sideEffects:
                if item[0] not in sideEffects:
                    sideEffects[item[0]]=[]
                    sideEffects[item[0]].append({"sideEffect": [] , "category": elem})
                sideEffects[item[0]][-1]["sideEffect"].append(item[1])
            
            ######################################################################################    
    for drug in sideEffects:
        for entry in sideEffects[drug]:
            if 'sideEffects' in entry:
                entry['sideEffects'] = list(set(entry['sideEffects']))

    codicc['sideEffects']={}
    codicc['sideEffects']['resultsTotal'] = len(sideEffects)
    codicc['sideEffects']['results'] = sideEffects_filtering_sorting(sideEffects,page,0,limit)
    return codicc





@app.route('/exploration', methods=['POST'])
def run_exploration_api():
    if (not request.json):
        abort(400)
    if 'topic' in request.args:
        topic = request.args['topic']
    else:
        abort(400)
    if 'limit' in request.args:
        limit = int(request.args['limit'])
    else:
        limit = LIMIT
    if 'page' in request.args:
        page = int(request.args['page'])
    else:
        page = 0
    if 'sort' in request.args:
        sort = request.args['sort']
    else:
        sort = 0


    input_list = request.json
    if len(input_list) == 0:
        logger.info("Error in the input format")
        r = "{results: 'Error in the input format'}"
    else:
        response = proccesing_response(input_list, topic,limit,page,sort)
        r = json.dumps(response, indent=4)            
    logger.info("Sending the results: ")
    response = make_response(r, 200)
    response.mimetype = "application/json"
    return response

def main(*args):
    if len(args) == 1:
        myhost = args[0]
    else:
        myhost = "0.0.0.0"
    app.run(debug=False, host=myhost)
    
if __name__ == '__main__':
     main(*sys.argv[1:])

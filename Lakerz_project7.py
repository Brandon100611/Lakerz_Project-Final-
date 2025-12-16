''' Project 5: MongoDB the magnificant
database of members of the royal family 
Author: Brandon Engel '''
import pymongo
from datetime import datetime
client = pymongo.MongoClient()
database = client['Lakerz']
collection = database['british-royals']
collection.delete_many({})
royal = {
    "_id": "QEII",
    "full name" : "Elizabeth Alexandra Mary",
    "parents": ["TQM", "KGVI"],
    "royal name": "Queen Elizabeth II",
    "children": ["KCIII"],
    "birthyear": 1926,
    "start of reign": datetime(1952,2,6),
    "end of reign": datetime(2022,9,8),
    "reign": [1952, 2022]
    
    }
collection.insert_one(royal)
royal = {
    "_id": "KGV",
    "full name": "George Frederick Ernest Albert",
    "parents": ["KEVII"],
    "royal name": "King George V" ,
    "children":["KEVIII", "KGVI"],
    "birthyear": 1865,
     "start of reign":datetime(1910,5,6),
    "end of reign":datetime(1936,1,20),
    "reign": [1910,1936]
    }
collection.insert_one(royal)
royal = {
    "_id": "MoT",
    "full name": "Victoria Mary Augusta Louise Olga Pauline Claudine Agnes",
    "parents": [],
    "royal name": "Queen Consort Mary of Teck",
    "children": ["KEVIII", "KGVI"],
    "birthyear": 1867,
    "reign":[]
     
    }
collection.insert_one(royal)
royal = {
    "_id": "KGVI",
    "full name": "Albert Frederick Arthur George",
    "parents": ["KGV", "MoT"],
    "royal name": "King George VI",
    "children": ["QEII"],
    "birthyear": 1895,
     "start of reign":datetime(1936, 12,11),
    "end of reign":datetime(1952,2,6),
    "reign":[1936,1952]
    }
collection.insert_one(royal)
royal = {
    "_id": "TQM",
    "full name": "Elizabeth Angela Marguerite Bowes-Lyon",
    "parents": [],
    "royal name": "Queen Consort Elizabeth Bowes-Lyon",
    "children": ["QEII"],
    "birthyear": 1900,
    "reign": []
     
    }
collection.insert_one(royal)
royal = {
    "_id": "KCIII",
    "full name" : "Charles Philip Arthur George",
    "parents": ["QEII"], 
    "royal name": "King Charles III",
    "children": [],
    "birthyear": 1948,
    "start of reign": datetime(2022,9,8),
    "end of reign": datetime.now(),
    "reign": [2022]
    }
collection.insert_one(royal)
royal = {
    "_id": "KEVIII",
    "full name" : "Edward Albert Christian George Andrew Patrick David",
    "parents": ["KGV", "MoT"],
    "royal name": "King Edward VIII", 
    "children": [],
    "birthyear": 1894, 
    "start of reign": datetime(1936,1,20),
    "end of reign": datetime(1936,12,11),
    "reign": [1936,1936]
    }
collection.insert_one(royal)
royal = {
    "_id": "KEVII",
    "full name" :  "Albert Edward",
    "parents": ["QV"],
    "royal name": "King Edward VII",
    "children": ["KGV"],
    "birthyear": 1841,
    "start of reign":datetime(1901,1,22),
    "end of reign": datetime(1910,5,6),
    "reign": [1901,1910]
    }
collection.insert_one(royal)
royal = {
    "_id": "QV",
    "full name" : "Alexandrina Victoria", 
    "parents": [],
    "royal name": "Queen Victoria",
    "children": ["KEVII"],
    "birthyear": 1819,
    "start of reign": datetime(1837, 6,20),
    "end of reign":datetime(1901, 1,22),
    "reign": [1837,1901]
    }
collection.insert_one(royal)
royal = {
    "_id":  "KWIV",
    "full name" : "William Henry",
    "parents": ["KGIII"],
    "royal name": "King William IV" ,
    "children": [],
    "birthyear": 1765,
    "start of reign": datetime(1830, 6, 26),
    "end of reign": datetime(1837, 6, 20),
    "reign": [1830,1837]
    }
collection.insert_one(royal)
royal = {
    "_id": "KGIV",
    "full name" : "George Augustus Frederick",
    "parents": ["KGIII"],
    "royal name": "King George IV",
    "children": [],
    "birthyear": 1762,
    "start of reign": datetime(1820,1, 29),
    "end of reign": datetime(1830, 6, 26),
    "reign":[1820,1830]
    }
collection.insert_one(royal)
royal = {
    "_id": "KGIII",
    "full name" : "George William Frederick",
    "parents": [],
    "royal name": "King George III",
    "children": ["KGIV", "KWIV"],
    "birthyear": 1738,
    "start of reign":datetime(1760,10,25),
    "end of reign": datetime(1820, 1,29),
    "reign": [1760,1820]
    }
collection.insert_one(royal)
royal = {
    "_id": "KGII",
    "full name" : "George Augustus",
    "parents": ["KGI"],
    "royal name": "King George II",
    "children": [],
    "birthyear": 1683,
    "start of reign": datetime(1727,6,22),
    "end of reign": datetime(1760,10,25),
    "reign":[1727, 1760]
    }
collection.insert_one(royal)
royal = {
    "_id": "KGI",
    "full name" : "George Louis",
    "parents": [],
    "royal name": "King George I",
    "children": ["KGII"],
    "birthyear":1660,
    "start of reign":datetime(1714,8,1),
    "end of reign": datetime(1727, 6,11),
    "reign": [1698,1727]
    }
collection.insert_one(royal)
royal = {
    "_id": "QA",
    "full name" : "Anne" ,
    "parents": ["KJII"],
    "royal name": "Queen Anne",
    "children": [],
    "birthyear": 1665,
    "start of reign":datetime(1702, 5,1),
    "end of reign": datetime(1714, 8, 1),
    "reign":[1702, 1707]
    }
collection.insert_one(royal)
royal = {
    "_id": "KWIII",
    "full name" : "William Henry",
    "parents" : ["KWII"],
    "royal name" : "King William III",
    "children" : [],
    "birthyear": 1650,
    "start of reign": datetime(1689,2, 13),
    "end of reign" : datetime(1702,3, 8),
    "reign": [1689,1702]
}
collection.insert_one(royal)
royal = {
    "_id": "QMII",
    "full name" : "Mary",
    "parents" : ["KJII"],
    "royal name" : "Queen Mary II",
    "children" : [],
    "birthyear": 1662,
    "start of reign": datetime(1689, 2, 13),
    "end of reign" : datetime(1694,12, 28),
    "reign": [1689, 1694]
}
collection.insert_one(royal)
royal = {
    "_id": "KJII",
    "full name" : "James",
    "parents" : ["KCI"],
    "royal name" : "King James II",
    "children" : ["QMII", "QA"],
    "birthyear": 1633,
    "start of reign" : datetime(1685, 2, 6),
    "end of reign": datetime(1688, 12, 11),
    "reign": [1685, 1688]
}
collection.insert_one(royal)
royal = {
    "_id": "KCII",
    "full name" : "Charles",
    "parents" : ["KCI"],
    "royal name" : "King Charles II",
    "children" : [],
    "birthyear": 1630,
    "start of reign": datetime(1660, 5, 29),
    "end of reign": datetime(1685, 2,6)
}
collection.insert_one(royal)
royal = {
    "_id": "KCI",
    "full name" : "Charles",
    "parents" : [],
    "royal name" : "King Charles I",
    "children" : ["KCII", "KJII"],
    "birthyear": 1600,
    "start of reign": datetime(1625, 3, 27),
    "end of reign": datetime(1649, 1, 30),
    "reign": [1625, 1649]
}
collection.insert_one(royal)
royal = {
    "_id": "KJI",
    "full name" : "James Charles Stuart",
    "parents" : ["KCI"],
    "royal name" : "King James I",
    "children" : [],
    "birthyear": 1566,
    "start of reign": datetime(1603, 3, 24),
    "end of reign": datetime(1625, 3, 27),
    "reign": [1603, 1625]
}
collection.insert_one(royal)
    
royal = {
    "_id": "QEI",
    "full name" : "Elizabeth",
    "parents" : ["KHVIII"],
    "royal name" : "Queen Elizabeth I",
    "children" : [],
    "birthyear": 1533,
    "start of reign": datetime(1558,11, 17),
    "end of reign": datetime(1603, 3 , 24),
    "reign": [1553, 1603]
    
}
collection.insert_one(royal)
###################################################################################
#######
##regnal names
regnal_name={
    "name": "Elizabeth",
    "royals": ["QEI", "QEII"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "James",
    "royals": ["KJI","KJII"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "Edward",
    "royals": ["KEVII", "KEVIII"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "Victoria",
    "royals": ["QV"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "William",
    "royals": ["KWIII","KWIV"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "George",
    "royals": ["KGI", "KGII", "KGIII", "KGIV", "KGV"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "Anne",
    "royals": ["QA"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "Mary",
    "royals": ["QMII"]
    }
collection.insert_one(regnal_name)
regnal_name={
    "name": "Charles",
    "royals": ["KCI","KCII","KCIII"]
    }
collection.insert_one(regnal_name)
def get_id_by_full_name(collection, full_name):
    britishroyals = collection.find({
        "full name" : full_name
        })
    for royal in britishroyals:
        return (royal['_id'])
def is_parent(collection, parent_name, child_name):
    royalparent = collection.find_one({
        "full name": parent_name
        })
    
    royalchild = collection.find_one({
        "full name": child_name,
        "parents":{
            "$in": [royalparent['_id']]}
        })
    return royalchild
def get_parent_names(collection, full_name):
    parent_names=[]
    royal = collection.find_one({
        "full name": full_name})
    royalparents = collection.find({
        "_id": {
            "$in": royal["parents"]}
        })
    for parent in royalparents:
        parent_names.append(parent["full name"])
    return parent_names
##returns list of FULL NAMES of children and grandchildren of the royal 
def get_child_and_grandchild_names(collection, full_name):
    descendants = []
    royal = collection.find_one({
        "full name": full_name})
    royalchildren= collection.find({
        "_id" : {
            "$in" : royal["children"]}
        })
    for child in royalchildren:
        descendants.append(child["full name"])
        royalgrandkids= collection.find({
            "_id": {
                "$in" : child["children"]}
                })
        for grandkid in royalgrandkids:
            descendants.append(grandkid["full name"])
    return descendants
##################################################project 2 
#############################################
def get_regnal_name(collection, full_name):
    royal =collection.find_one({
        "full name": full_name})
    royal_id = royal["_id"]
    
    the_regnal_name = collection.find_one({
        "royals" : royal_id
        })
    
    return (the_regnal_name["name"])
        
    
def get_monarchs_by_name(collection, regnal_name):
    list_of_monarchs = []
    monarch_name = collection.find_one({
        "name": regnal_name})
    monarchs = collection.find({
        "_id": {
            "$in": monarch_name["royals"]}
        })
    for monarch in monarchs:
        list_of_monarchs.append(monarch["full name"])
    return list_of_monarchs

def get_reign_range(collection, royal_name):
    royal = collection.find_one({
        "royal name": royal_name})
    if royal:
        return ((royal["start of reign"]).year, (royal["end of reign"]).year)
    else:
        return None
    
def get_reign_lengths_by_length(collection):
    years=[]
    royabb = collection.aggregate([
        {"$match": {"start of reign": {"$exists": True}}},
        {"$project" : {"length of reign": {
            "$floor":{
                "$divide":[{
                    "$subtract":[
                        "$end of reign","$start of reign"]},
                           31536000000]}
            }}},
        {"$sort": {"length of reign": pymongo.ASCENDING,}}
        ])
    for royab in royabb:
        years.append(royab["length of reign"])
    return(years)
    
def get_royal_names_by_reign_lengths(collection):
    names=[]
    royabb = collection.aggregate([
        {"$match": {"start of reign": {"$exists": True}}},
        {"$project" : {"name": "$royal name","length of reign":{
            "$floor":{
                "$divide":[{
                    "$subtract":[
                        "$end of reign","$start of reign"]},
                           31536000000]}
            }}},
        {"$sort": {"length of reign": pymongo.DESCENDING,}}
        ])
    for royab in royabb:
        names.append(royab["name"])
    return names
def get_regnal_name_length(collection,regnal_name):
    reign_length=0
    monarch = collection.find({
        "name": regnal_name})
    moarchs_id = monarch["_id"]
    royal=collection.find({
            "full name": "George William Frederick"})
    royal_id = royal["_id"]
        
    the_regnal_name = collection.find({
    "royals" : royal_id
    })
    
    print(the_regnal_name["name"])

    for RN in the_regnal_name:
        royal_name = RN["name"]
        reign_length += (get_reign_range(collection, royal_name))
    return int (reign_length)

# project 7
def get_all_monarchs_aggregation_list():
    return [
        {"$match": {"start of reign": {"$exists": True}, "end of reign": {"$exists": True}}},
        {"$sort": {"start of reign": 1}},  
        {"$project": {
            "_id": 1,
            "full name": 1,
            "royal name": 1,
            "start of reign": 1,
            "end of reign": 1
        }}  
    ]

def get_all_monarchs_in_order_aggregation_list():
    return [
        {"$match": {"start of reign": {"$exists": True}, "end of reign": {"$exists": True}}},
        {'$sort': {'start of reign': 1,'end of reign': 1}},
        {'$project': {'full name': 1, '_id': 0, 'start of reign': 1, 
        'reign': {'$subtract': ['$end of reign', '$start of reign']  
                }
            }
        }
    ]


def get_queens_full_names_aggregation_list():
    return [
        {"$match": {"royal name": {"$regex": 'Queen', "$options": "i"}}}, 
        {"$match": {"reign": {'$ne': [] }}}, 
        {"$project": {"full name": 1, "_id": 1}}  
    ]


def get_royal_names_of_monarchs_with_single_name_aggregation_list(name: str):
    return [
        {"$match": {"full name": {"$regex": name, "$options": "i"}}},  
        {"$project": {"_id": 1, "royal name": 1}}  
    ]

def get_royal_names_before_year_aggregation_list(year):
    return [
        {"$match": {"start of reign": {"$lt": year}}},  
        {"$project": {"royal name": 1}} 
    ]


def get_royal_names_in_century_aggregation_list(century: int):
    start_year = (century - 1) * 100
    end_year = century * 100

    return [
        {"$match": {
            "start of reign": {"$lt": end_year},
            "end of reign": {"$gte": start_year}
        }},
        {"$project": {"_id": 1, "royal name": 1}}  
    ]


def main():
    collection.aggregate(get_all_monarchs_in_order_aggregation_list())
    print(collection.aggregate(get_all_monarchs_in_order_aggregation_list()))

if __name__ == '__main__':
    main()

results = collection.aggregate(get_all_monarchs_in_order_aggregation_list())
for result in results:
    print (result)

##years=[]
##royabb = collection.aggregate([
##    {"$match": {"start of reign": {"$exists": True}}},
##    {"$project" : {"length of reign": {
##        "$floor":{
##            "$divide":[{
##                "$subtract":[
##                    "$end of reign","$start of reign"]},
##                       31536000000]}
##        }}},
##    {"$sort": {"length of reign": pymongo.ASCENDING,}}
##    ])
##for royab in royabb:
##    years.append(royab["length of reign"])
##print(years)
##    
##    years=[]
##    royabb = collection.aggregate([
##        {"$match": {"start of reign": {"$exists": True}}},
##        {"$project" : {"length of reign": {"$subtract":[
##            "$end of reign","$start of reign"]
##            }}},
##        {"$sort": {"length of reign": pymongo.ASCENDING,}}
##        ])
##    for royab in royabb:
##        years.append(royab["length of reign"])
##    return years
##years=[]
##names=[]
##royabb = collection.aggregate([
##    {"$match": {"start of reign": {"$exists": True}}},
##    {"$addFields" : {"name": "$royal name", "length of reign": {"$dateDiff":{
##        "startDate":"$start of reign",
##        "endDate":"$end of reign",
##        "unit": "year"
##        }}}},
##    {"$sort": {"length of reign": pymongo.ASCENDING,}}
##    ])
##for royab in royabb:
##    years.append(royab["length of reign"])
##    names.append(royab["name"])
##print(years)
##print(names)
##
##
##royabb = collection.aggregate([
##        {"$match": {"start of reign": {"$exists": True}}},
##        {"$addFields" : {"length of reign": {"$subtract":["$end of reign","$start
#of reign" ]}}},
##        {"$sort": {"length of reign": pymongo.DESCENDING,}}
##        ])
##for royab in royabb:
##        print(royab["length of reign"])
##
##years=[]
##    royals = collection.aggregate([
##        {"$match": {"start of reign": {"$exists": True}}},
##        {"$group" : {"_id": "$royal name", "length of reign": {"$subtract":["$end
#of reign","$start of reign" ]}}},
##        {"$sort": {"length of reign": pymongo.DESCENDING,}} 
##        ])
##    for royal in royals:
##        print(royal)
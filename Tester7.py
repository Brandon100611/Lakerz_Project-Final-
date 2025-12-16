'''The tests for all CSC 3340 problems for project 7..
   Author: Kyle Burke <kburke@flsouthern.edu>'''

import math
import sys
import pymongo
import datetime
import copy
import random
import string
import unittest

project_number = 7


class GetAllMonarchsAggregationListTests(unittest.TestCase):
    def points(self):
        return 20
    
    def test_name(self):
        return "get_all_monarchs_aggregation_list"

    def test_default_case(self):
        '''Run the tests!'''
        client = pymongo.MongoClient()
        stu_db = client[team_name]
        stu_collection = stu_db['british-royals']
        
        function = main.get_all_monarchs_aggregation_list
        
        aggregation_list = function()
        
        correct = isinstance(aggregation_list, list)
        message = "The function doesn't return a list."
        self.assertTrue(correct, message)
        
        for element in aggregation_list:
            correct = isinstance(element, dict)
            message = "Not every element of the returned list is a dictionary."
            self.assertTrue(correct, message)
        
        result_cursor = stu_collection.aggregate(aggregation_list)
        
        results = []
        for result in result_cursor:
            results.append(result)
        
        expected_names = ["Elizabeth", "James Charles Stuart", ("Charles", 2), "James", "Mary", ("William Henry", 2), "Anne", "George Louis", "George Augustus", "George William Frederick", "George Augustus Frederick", "Alexandrina Victoria", "Albert Edward", "George Frederick Ernest Albert", "Edward Albert Christian George Andrew Patrick David", "Albert Frederick Arthur George", "Elizabeth Alexandra Mary", "Charles Philip Arthur George"]
        
        for name in expected_names:
            expected_num_docs = 1
            if isinstance(name[1], int):
                #this is a tuple, not a single string.
                expected_num_docs = name[1]
                name = name[0]
            
            num_results = 0
            for result in results:
                if result['full name'] == name:
                    num_results += 1
            
            correct = num_results > 0
            message = "Didn't return a document with " + name + "."
            self.assertTrue(correct, message)
            
            correct = num_results == expected_num_docs
            message = "Didn't find the correct number of documents for " + name
            self.assertTrue(correct, message)
        
        unwanted_names = ["Victoria Mary Augusta Louise Olga Pauline Claudine Agnes", "Elizabeth Angela Marguerite Bowes-Lyon"]
        
        for name in unwanted_names:
            
            for result in results:
                
                correct = result['full name'] != name
                message = "The returned list includes someone who was not on the throne: " + name
                self.assertTrue(correct, message)


class GetAllMonarchsInOrderAggregationListTests(unittest.TestCase):
    def points(self):
        return 15
    
    def test_name(self):
        return "get_all_monarchs_in_order_aggregation_list"

    def test_default_case(self):
        '''Run the tests!'''
        client = pymongo.MongoClient()
        stu_db = client[team_name]
        stu_collection = stu_db['british-royals']
        
        function = main.get_all_monarchs_in_order_aggregation_list
        
        aggregation_list = function()
        
        correct = isinstance(aggregation_list, list)
        message = "The function doesn't return a list."
        self.assertTrue(correct, message)
        
        for element in aggregation_list:
            correct = isinstance(element, dict)
            message = "Not every element of the returned list is a dictionary."
            self.assertTrue(correct, message)
        
        result_cursor = stu_collection.aggregate(aggregation_list)
        
        results = []
        for result in result_cursor:
            results.append(result)
        
        expected_names = ["Elizabeth", "James Charles Stuart", 'Charles', "Charles", "James", "Mary", "William Henry", "Anne", "George Louis", "George Augustus", "George William Frederick", "George Augustus Frederick", 'William Henry', "Alexandrina Victoria", "Albert Edward", "George Frederick Ernest Albert", "Edward Albert Christian George Andrew Patrick David", "Albert Frederick Arthur George", "Elizabeth Alexandra Mary", "Charles Philip Arthur George"]
        
        expected_index = 0
        for i in range(len(results)):
            correct = expected_index < len(expected_names)
            message = "Returns a list with too many royals."
            self.assertTrue(correct, message)
            
            expected_name = expected_names[expected_index]
            result = results[i]
            result_name = result['full name']
            
            if expected_name == result_name:
                expected_index += 1
        
        correct = expected_index == len(expected_names)
        message = "Doesn't have " + expected_name + " in the correct spot."
        self.assertTrue(correct, message)
        
        unwanted_names = ["Victoria Mary Augusta Louise Olga Pauline Claudine Agnes", "Elizabeth Angela Marguerite Bowes-Lyon"]
        
        for name in unwanted_names:
            
            for result in results:
                
                correct = result['full name'] != name
                message = "The returned list includes someone who was not on the throne: " + name
                self.assertTrue(correct, message)


class GetQueensFullNamesAggregationListTests(unittest.TestCase):
    def points(self):
        return 20
    
    def test_name(self):
        return "get_queens_full_names_aggregation_list"

    def test_default_case(self):
        '''Run the tests!'''
        client = pymongo.MongoClient()
        stu_db = client[team_name]
        stu_collection = stu_db['british-royals']
        
        function = main.get_queens_full_names_aggregation_list
        
        aggregation_list = function()
        
        correct = isinstance(aggregation_list, list)
        message = "The function doesn't return a list."
        self.assertTrue(correct, message)
        
        for element in aggregation_list:
            correct = isinstance(element, dict)
            message = "Not every element of the returned list is a dictionary."
            self.assertTrue(correct, message)
        
        result_cursor = stu_collection.aggregate(aggregation_list)
        
        results = []
        for result in result_cursor:
            
            correct = len(result) == 2
            message = "Returned dictionaries have more than two elements.  (They should only have '_id' and 'full name' as keys.)"
            self.assertTrue(correct, message)
            
            correct = 'full name' in result
            message = "Returned dictionaries don't all have a full name key."
            self.assertTrue(correct, message)
            
            results.append(result)
        
        expected_names = ["Elizabeth", "Mary", "Anne", "Alexandrina Victoria", "Elizabeth Alexandra Mary"]
        
        for expected in expected_names:
            
            found = False
            for result in results:
            
                name = result['full name']
                if name == expected:
                    found = True
                    break
            
            correct = found
            message = "Doesn't return the name " + expected + "."
            self.assertTrue(correct, message)
        
        unwanted_names = ["Victoria Mary Augusta Louise Olga Pauline Claudine Agnes", "Elizabeth Angela Marguerite Bowes-Lyon", "James Charles Stuart", 'Charles', "Charles", "James", "William Henry", "George Louis", "George Augustus", "George William Frederick", "George Augustus Frederick", 'William Henry',  "Albert Edward", "George Frederick Ernest Albert", "Edward Albert Christian George Andrew Patrick David", "Albert Frederick Arthur George", "Charles Philip Arthur George"]
        
        for name in unwanted_names:
            
            for result in results:
                
                correct = result['full name'] != name
                message = "The returned list includes " + name + ", but it shouldn't."
                self.assertTrue(correct, message)


class GetRoyalNamesOfMonarchsWithSingleNameAggregationListTests(unittest.TestCase):
    def points(self):
        return 20
    
    def test_name(self):
        return "get_royal_names_of_monarchs_with_single_name_aggregation_list"

    def test_default_case(self):
        '''Run the tests!'''
        client = pymongo.MongoClient()
        stu_db = client[team_name]
        stu_collection = stu_db['british-royals']
        
        function = main.get_royal_names_of_monarchs_with_single_name_aggregation_list
        
        search_name = 'Albert'
        
        aggregation_list = function(search_name)
        
        correct = isinstance(aggregation_list, list)
        message = "The function doesn't return a list."
        self.assertTrue(correct, message)
        
        for element in aggregation_list:
            correct = isinstance(element, dict)
            message = "Not every element of the returned list is a dictionary."
            self.assertTrue(correct, message)
        
        result_cursor = stu_collection.aggregate(aggregation_list)
        
        results = []
        for result in result_cursor:
            
            correct = len(result) == 2
            message = "Returned dictionaries have more than two elements.  (They should only have '_id' and 'royal name' as keys.)"
            self.assertTrue(correct, message)
            
            correct = 'royal name' in result
            message = "Returned dictionaries don't all have a royal name key."
            self.assertTrue(correct, message)
            
            results.append(result)
        
        expected_names = ["King Edward VII", "King George V", "King Edward VIII", "King George VI"]
        
        for expected in expected_names:
            
            found = False
            for result in results:
            
                name = result['royal name']
                if name == expected:
                    found = True
                    break
            
            correct = found
            message = "Doesn't return the name " + expected + "."
            self.assertTrue(correct, message)
        
        unwanted_names = ["Queen Elizabeth I", 'King James I', 'King Charles I', 'King Charles II', 'King James II', 'Queen Mary II', 'King William III', 'Queen Anne', 'King George I', 'King George II', 'King George III', 'King George IV', 'King William IV', 'Queen Victoria', 'Queen Elizabeth II', 'King Charles III']
        
        for name in unwanted_names:
            
            for result in results:
                
                correct = result['royal name'] != name
                message = "The returned list includes " + name + ", but it shouldn't."
                self.assertTrue(correct, message)
        



class GetRoyalNamesBeforeYearAggregationListTests(unittest.TestCase):
    def points(self):
        return 15
    
    def test_name(self):
        return "get_royal_names_before_year_aggregation_list"

    def test_default_case(self):
        '''Run the tests!'''
        client = pymongo.MongoClient()
        stu_db = client[team_name]
        stu_collection = stu_db['british-royals']
        
        function = main.get_royal_names_before_year_aggregation_list
        
        search_year = 1900
        
        aggregation_list = function(search_year)
        
        correct = isinstance(aggregation_list, list)
        message = "The function doesn't return a list."
        self.assertTrue(correct, message)
        
        for element in aggregation_list:
            correct = isinstance(element, dict)
            message = "Not every element of the returned list is a dictionary."
            self.assertTrue(correct, message)
        
        result_cursor = stu_collection.aggregate(aggregation_list)
        
        results = []
        for result in result_cursor:
            
            correct = len(result) == 2
            message = "Returned dictionaries have more than two elements.  (They should only have '_id' and 'royal name' as keys.)"
            self.assertTrue(correct, message)
            
            correct = 'royal name' in result
            message = "Returned dictionaries don't all have a royal name key."
            self.assertTrue(correct, message)
            
            results.append(result)
        
        expected_names = ["Queen Elizabeth I", 'King James I', 'King Charles I', 'King Charles II', 'King James II', 'Queen Mary II', 'King William III', 'Queen Anne', 'King George I', 'King George II', 'King George III', 'King George IV', 'King William IV', 'Queen Victoria']
        
        for expected in expected_names:
            
            found = False
            for result in results:
            
                name = result['royal name']
                if name == expected:
                    found = True
                    break
            
            correct = found
            message = "Doesn't return the name " + expected + "."
            self.assertTrue(correct, message)
        
        unwanted_names = ['King Edward VII', 'King George V', 'King Edward VIII', 'King George VI', 'Queen Elizabeth II', 'King Charles III']
        
        for name in unwanted_names:
            
            for result in results:
                
                correct = result['royal name'] != name
                message = "The returned list includes " + name + ", but it shouldn't."
                self.assertTrue(correct, message)


class GetRoyalNamesInCenturyAggregationListTests(unittest.TestCase):
    def points(self):
        return 10
    
    def test_name(self):
        return "get_royal_names_in_century_aggregation_list"

    def test_default_case(self):
        '''Run the tests!'''
        client = pymongo.MongoClient()
        stu_db = client[team_name]
        stu_collection = stu_db['british-royals']
        
        function = main.get_royal_names_in_century_aggregation_list
        
        search_int = 20
        
        aggregation_list = function(search_int)
        
        correct = isinstance(aggregation_list, list)
        message = "The function doesn't return a list."
        self.assertTrue(correct, message)
        
        for element in aggregation_list:
            correct = isinstance(element, dict)
            message = "Not every element of the returned list is a dictionary."
            self.assertTrue(correct, message)
        
        result_cursor = stu_collection.aggregate(aggregation_list)
        
        results = []
        for result in result_cursor:
            
            correct = len(result) == 2
            message = "Returned dictionaries have more than two elements.  (They should only have '_id' and 'royal name' as keys.)"
            self.assertTrue(correct, message)
            
            correct = 'royal name' in result
            message = "Returned dictionaries don't all have a royal name key."
            self.assertTrue(correct, message)
            
            results.append(result)
        
        expected_names = ['Queen Victoria', 'King Edward VII', 'King George V', 'King Edward VIII', 'King George VI', 'Queen Elizabeth II']
        
        for expected in expected_names:
            
            found = False
            for result in results:
            
                name = result['royal name']
                if name == expected:
                    found = True
                    break
            
            correct = found
            message = "Doesn't return the name " + expected + "."
            self.assertTrue(correct, message)
        
        unwanted_names = ["Queen Elizabeth I", 'King James I', 'King Charles I', 'King Charles II', 'King James II', 'Queen Mary II', 'King William III', 'Queen Anne', 'King George I', 'King George II', 'King George III', 'King George IV', 'King William IV', 'King Charles III']
        
        for name in unwanted_names:
            
            for result in results:
                
                correct = result['royal name'] != name
                message = "The returned list includes " + name + ", but it shouldn't."
                self.assertTrue(correct, message)
            


print("Starting the grading!")  


test_classes = [
    GetAllMonarchsAggregationListTests,
    GetAllMonarchsInOrderAggregationListTests,
    GetQueensFullNamesAggregationListTests,
    GetRoyalNamesOfMonarchsWithSingleNameAggregationListTests,
    GetRoyalNamesBeforeYearAggregationListTests,
    GetRoyalNamesInCenturyAggregationListTests
]






#Actually run the tests:        
        
if __name__ == "__main__":
    import shutil
    import os
    import importlib
    
    team_name = input("What is your team's name? ")
    student_file_prefix = team_name + "_project" + str(project_number)
    file_name = student_file_prefix + ".py"
    total_score = 0
    total_max = 0
    total_output = ""
    #import main
    main = importlib.import_module(student_file_prefix)
    for test_class in test_classes:
        tests = test_class()
        test_points = tests.points()
        score = 0
        output = ""
        try:
            tests.test_default_case() 
            output = "All tests passed!"
            score = test_points
        except Exception as e:
            output += str(e)
        total_output = total_output + tests.test_name() + ": " + str(score) + "/" + str(test_points) + "\n  " + output + "\n\n"
        total_score += score
        total_max += test_points
    total_score_output = "Total score: " + str(total_score) + "/" + str(total_max)
    total_output =  total_score_output + "\n\n" + total_output
    print("Scored", score, "points!")
    print(total_output[:-2])
    print(total_score_output)
    print("Reminder: this does not cover all tests that I will run.  Your actual score may be lower.  I recommend coming up with some of your own tests.")
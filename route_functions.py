from http.client import SWITCHING_PROTOCOLS
from tokenize import maybe
from click import argument
from flask import render_template
from urllib.request import urlopen
from pprintpp import pprint as pp

# import json
import json
# from main_db import conn
# cur = conn.cursor()

# import psycopg2
# from main_db import conn
# Open a cursor to perform database operations
# cur = conn.cursor()

###########################################################

def homeFunc():
    staff_list = []
    cur.execute("SELECT * from staff")
    staff_data = cur.fetchall()
    print("staff_data", staff_data)
    for record in staff_data:
        print(record)
        staff_dict = {
            "record_id":record[0], 
            "last_name":record[1],
            "first_name":record[2]}
        staff_list.append(staff_dict)
        print("staff_list: ", staff_list)
    return render_template("stafflist2.html", staff_list = staff_list)

############################

def hello_world():

    # Execute a query
    cur.execute("SELECT * FROM lesson_plan_items")

    # Retrieve query results
    records = cur.fetchall()

    toreturn = f"""
    <h1>Hello World</h1><br>
    {records}
    """

    return toreturn

############################

############################

def staffFunc(subFunc):

    staffJsonUrl = "https://cdn.baseboosters.com/9d548ee0d08efa18/v1/staff.json"

    def getJson(url):
        
        # store the response of URL
        response = urlopen(staffJsonUrl)
        
        # storing the JSON response
        # from url in data
        data_json = json.loads(response.read())
        
        return data_json['records']

    staff_list_json = getJson(staffJsonUrl)
    staff_list_parsed = []

    for record in staff_list_json:
        if record['profile_img'] != None:
            staff_dict = {
                    "bio": record['bio'],
                    "staff_name": record['staff_name'],
                    "position": record['position'],
                    "profile_img": record['profile_img']
                }
            staff_list_parsed.append(staff_dict)
    print("DDDDDDDDDDDDDDDDDDDDDDD")
    print("staff_list_parsed", staff_list_parsed)
    
    #Define sub functions
    def displayAsPage():
        return render_template("stafflist.html", staff_list_parsed = staff_list_parsed)

    def displayAsTable():
        return "nocheese"

    def chooseSubFunc(argument):
        match argument:
            case 1:
                return displayAsPage()
            case 2:
                return displayAsTable()

    return chooseSubFunc(subFunc)
    
    # return render_template("stafflist.html", staff_list_parsed = staff_list_parsed) 

    # return render_template('stafflist.html')

############################



############################
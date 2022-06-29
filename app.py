# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
from route_functions import staffFunc

app = Flask(__name__)

@app.route('/')
def homeRouteFunc():
    anchorTag = """
    <a href="/staff">Click to go to staff</a>
    """
    return anchorTag

@app.route('/staff')
def staffRouteFunc(): 
    staffFunc
    print(111111111)
    print(staffFunc(1))  
    return staffFunc(1)

















# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='127.0.0.1',port=8000,debug=True)
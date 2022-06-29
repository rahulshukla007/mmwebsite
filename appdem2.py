from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# from urllib.request import urlopen
# from pprintpp import pprint as pp
# # import json
# import json

@app.route('/')
def homeRouteFunc():

    from urllib.request import urlopen
    from pprintpp import pprint as pp
    # import json
    import json

    # store the URL in url as 
    # parameter for urlopen
    url = "https://cdn.baseboosters.com/9d548ee0d08efa18/v1/staff.json"
    
    # store the response of URL
    response = urlopen(url)
    
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())
    
    data_json['records']

    # print the json response
    return data_json['records'][1]

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='127.0.0.1',port=8000,debug=True)
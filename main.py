import os
from flask import Flask, Response
import sys
import requests
import json
from copy import deepcopy


token = os.environ['GITLAB_TOKEN']
uri_server = os.environ['GITLAB_URI']
group = os.environ['GROUP_ID']
get_project = uri_server + "/api/v4/groups/" + group + "/projects"

app = Flask(__name__)

@app.route("/get/template", methods=['GET'])
def get():
    #  go to private token as  os env 
    
    x = requests.get(get_project, headers={'PRIVATE-TOKEN': token}) 
    
    lista = json.loads(x.content)
    #create list
    information = [] 
    #create dict
    laruse = {}

    for repo in lista:
    # get to the value
        name =(repo["name"])
        uri = (repo["http_url_to_repo"]) 
        id = (repo["id"])
        laruse['name'] = name
        laruse['uri'] = uri
        laruse['id'] = id
        information.append(deepcopy(laruse))
    return Response(json.dumps(information),  mimetype='application/json')

if __name__ == '__main__':

    try:

        if __name__ == '__main__':

            app.run(debug=os.environ['FLASK_ENV'] == 'development',host='0.0.0.0', port=8080)
        elif __name__ == '__main__':

            app.run(debug=os.environ['FLASK_ENV'] == 'production',host='0.0.0.0', port=80)
    except:

        print("setting to FLASK_ENV")

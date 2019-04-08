#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
import json
from model import Model
import subprocess
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


DATABASE = 'objects.db'  #need schema

json_file_num = 0 #json filename number that will increment for each object uploaded


@app.route('/upload_text/<filename>', methods=['GET', 'POST'])
def upload_text(filename):
    if request.method == 'GET': 
                        #the following is the API to upload a text doc
        
        
        upload_json = {   
        "objects": [{
        "properties": {
        "enaio:objectTypeId": {
        "value": "document"
        },
        "Name": {
        "value": "text object"
        }
        },
        "contentStreams": [{
        "cid": filename
        }]
        }]
        }

        with open('/Users/brucemolina/Desktop/polisense_backend/resources/0.json', 'w+') as fp: #creating json file for the txt object to be uploaded
            json.dump(upload_json, fp)
        
        command = 'curl -X POST "https://yuuvis.io/api/dms/objects" -H  "accept: application/json" -H  "Authorization: Basic YWRtaW46WDNIR1djVVRYakdH" -H  "X-ID-TENANT-NAME: nyc052" -H  "Content-Type: multipart/form-data" -F "data=@/Users/brucemolina/Desktop/polisense_backend/resources/0.json;type=application/json" -F ""{}"=@/Users/brucemolina/Desktop/polisense_backend/resources/"{}";type=text/plain"'.format(filename,filename)
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response = p.communicate()
        response1=str(response[0])
        response2=response1.strip('b\\')
        response3=response2.strip("\\'")
        x = json.loads(response3)
        
        objectid = x['objects'][0]['properties']['enaio:objectId']['value'] #getting the objectid from the json response from yuuvis cloud
        with Model(DATABASE) as db:         #storing objectid into local SQL along with filename
            db.cursor.execute('INSERT INTO objects(objectid,filename) VALUES("{}","{}");'.format(objectid,filename)) 
        return objectid,filename
        


@app.route('/upload_img/<filename>', methods=['GET', 'POST'])
def upload_img(filename):
    if request.method == 'GET':
                        #the following is the API to upload a text doc
        
        
        upload_json = {   
        "objects": [{
        "properties": {
        "enaio:objectTypeId": {
        "value": "image"
        },
        "Name": {
        "value": "image"
        }
        },
        "contentStreams": [{
        "cid": filename
        }]
        }]
        }
        
        with open('/Users/brucemolina/Desktop/polisense/polisense_backend/resources/1.json', 'w+') as fp: #creating json file for the txt object to be uploaded
            json.dump(upload_json, fp)
        
        command = 'curl -X POST "https://yuuvis.io/api/dms/objects" -H  "accept: application/json" -H  "Authorization: Basic YWRtaW46WDNIR1djVVRYakdH" -H  "X-ID-TENANT-NAME: nyc052" -H  "Content-Type: multipart/form-data" -F "data=@/Users/brucemolina/Desktop/polisense_backend/resources/1.json;type=application/json" -F ""{}"=@/Users/brucemolina/Desktop/polisense_backend/resources/"{}";type=text/plain"'.format(filename,filename)
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response = p.communicate()
        response1=str(response[0])
        response2=response1.strip('b\\')
        response3=response2.strip("\\'")
        x = json.loads(response3)
        
        objectid = x['objects'][0]['properties']['enaio:objectId']['value'] #getting the objectid from the json response from yuuvis cloud
        with Model(DATABASE) as db:         #storing objectid into local SQL along with filename
            db.cursor.execute('INSERT INTO objects(objectid,filename) VALUES("{}","{}");'.format(objectid,filename)) #CREATE SCHEMA AND HTML FILE
        return objectid,filename     
        
        
@app.route('/pull_txt/<filename>', methods=['GET', 'POST'])
def pull_txt(filename):
    if request.method == 'GET':
        with Model(DATABASE) as db:
            db.cursor.execute('SELECT objectid FROM objects WHERE FILENAME="{}";'.format(filename))
            objectid = db.cursor.fetchone()[0]
        command = 'curl -X GET "https://yuuvis.io/api/dms/objects/"{}"/contents/file" -H  "accept: */*" -H  "Authorization: Basic YWRtaW46WDNIR1djVVRYakdH" -H  "X-ID-TENANT-NAME: nyc052"'.format(objectid)
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response = p.communicate()
        response1= str(response[0])
        response2=response1.strip('b')
        response3=response2.strip("''")

        return response3

@app.route('/pull_img/<filename>', methods=['GET', 'POST'])
def pull_img(filename):
    if request.method == 'GET':
        with Model(DATABASE) as db:
            db.cursor.execute('SELECT objectid FROM objects WHERE FILENAME="{}";'.format(filename))
            objectid = db.cursor.fetchone()[0]
        command = 'curl -X GET "https://yuuvis.io/api/dms/objects/"{}"/contents/file" -o /Users/brucemolina/Desktop/polisense_backend/pulls/"{}" -H  "accept: */*" -H  "Authorization: Basic YWRtaW46WDNIR1djVVRYakdH" -H  "X-ID-TENANT-NAME: nyc052"'.format(objectid,filename)  # -O to output, see if i can specify the path
        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)                                                                                                                                                                                                       #make variable to pull filename to rename the file from sql db

        return objectid


        


if __name__ == '__main__':
    app.run(debug=True)


    #need the text file to upload
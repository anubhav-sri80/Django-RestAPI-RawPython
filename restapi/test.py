import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

# def get_resource(id=None):
#     param={}
#     if id is not None:
#         param={
#             'id':id
#         }
#     res=requests.get(BASE_URL+ENDPOINT,data=json.dumps(param))
#     datas=res.json()
#     print(datas)

# get_resource()

# def create_resource(id=None):
#     param={
#         'eno':5,
#         'ename':'Nir',
#         'esal':25000,
#         'eadd':'BNB'
#     }
#     res=requests.post(BASE_URL+ENDPOINT,data=json.dumps(param))
#     datas=res.json()
#     print(datas)

# create_resource()

# def update_resource(id):
#     param={
#         'id':id,
#         'ename':'Nirmal',
#         'esal':25,
#     }
#     res=requests.put(BASE_URL+ENDPOINT,data=json.dumps(param))
#     datas=res.json()
#     print(datas)

# update_resource(5)
def delete_resource(id):
    param={
        'id':id,
    }
    res=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(param))
    datas=res.json()
    print(datas)

delete_resource(5)
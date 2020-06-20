from django.shortcuts import render
from  django.views.generic import View
from myrestapi.models import Employee
# Create your views here.
from django.http import HttpResponse
from myrestapi.utils import is_json
import json
#from django.core.serializers import serialize
from .mixins import SerializeMixin
from .froms import EmployeeForm

class EmployeeCRUDCBV(SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
           emp =Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            data =json.dumps({'msg':'Pls provide proper json format.'})
            return HttpResponse(data,content_type='appication/json')
        p_data=json.loads(data)

        id=p_data.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                data =json.dumps({'msg':'Pls provide proper json format.'})
                return HttpResponse(data,content_type='appication/json')

            #json_data=serialize('json',[emp],fields=('eno','ename'))
            json_data=self.serialize([emp,])
            return HttpResponse(json_data,content_type='appication/json')
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='appication/json')     
            
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Not valid Json Data'})
            return HttpResponse(json_data,content_type='application/json')
        p_data=json.loads(data)
        form= EmployeeForm(p_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Post created succesfully'})
            return HttpResponse(json_data,content_type='application/json')
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Not valid Json Data'})
            return HttpResponse(json_data,content_type='application/json')
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            data =json.dumps({'msg':'Pls provide proper json format.'})
            return HttpResponse(data,content_type='appication/json')
        emp=self.get_object_by_id(id)
        if emp is None:
                data =json.dumps({'msg':'Pls provide proper id format.'})
                return HttpResponse(data,content_type='appication/json')
        p_data=json.loads(data)
        original_data={
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eadd':emp.eadd
        }
        original_data.update(p_data)
        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource updated succesfully'})
            return HttpResponse(json_data,content_type='application/json')
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json')

    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Not valid Json Data'})
            return HttpResponse(json_data,content_type='application/json')
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            data =json.dumps({'msg':'Pls provide proper json format.'})
            return HttpResponse(data,content_type='appication/json')
        emp=self.get_object_by_id(id)
        if emp is None:
                data =json.dumps({'msg':'no id format.'})
                return HttpResponse(data,content_type='appication/json')
        status,deleted_item=emp.delete()
        if status==1:
            data =json.dumps({'msg':'delete successful.'})
            return HttpResponse(data,content_type='appication/json')
        data =json.dumps({'msg':'Pls try again'})
        return HttpResponse(data,content_type='appication/json')



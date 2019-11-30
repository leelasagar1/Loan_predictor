from django.shortcuts import render
import numpy as np
import pandas as pd
import pickle
import joblib
#from sklearn.externals import joblib
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Approval
from .serializers import approvalsSerializers
from sklearn import preprocessing
from django.http import JsonResponse
import json
from rest_framework.parsers import JSONParser
from .form import ApprovalForm
from rest_framework import viewsets
from .models import Approval
from .serializers import approvalsSerializers
from rest_framework.decorators import api_view
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serilaizer_class = approvalsSerializers



#@api_view(['POST'])
def approvereject(unit):
    try:
        model = joblib.load('D:/workspace/DjangoAPI/MyAPI/model/loan_model.pkl')
        scaler = joblib.load('D:/workspace/DjangoAPI/MyAPI/model/scaler.pkl')
        #mydata = request.data
        """unit = np.array(list(mydata.values()))
        unit = unit.reshape(1,-1)"""
        X = scaler.transform(unit)
        y_pred = model.predict(X)
        y_pred = (y_pred>0.58)
        """df = pd.DataFrame(y_pred,columns=['Status'])
        df = df.replace({True:'Approved',False:'Rejected'})
        return 'Your status is {} '.format(df,safe=False)"""
        if y_pred:
            return 'Approved'
        else:
            return "Rejected"
    except  ValueError as e:
        return Response(e.args[0].status.HTTP_400_BAD_REQUEST)

def ohevalue(df):
    dicyn = {'Yes':1,'No':0}
    df['Gender']=df['Gender'].map(dict(Male=1,Female=0))
    df['Married']=df['Married'].map(dicyn)
    df['Self_Employed']=df['Self_Employed'].map(dicyn)
    dicg = {'Graduate':1,'Not_Graduate':0}
    df['Education']=df['Education'].map(dicg)
    dicp = {'Rural':0,'SemiUrban':1,'Urban':2}
    df['Property_Area'] = df['Property_Area'].map(dicp)
    df['Credit_History'] = df['Credit_History'].map(dicyn)
    df['Dependants'] = df['Dependants'].map(dicyn)
    
    return df.iloc[:,3:].values

def cxcontact(request):

    if request.method== 'POST':
        form =  ApprovalForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            Dependants = form.cleaned_data['Dependants']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education=form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']
            mydict = (request.POST).dict()
            df = pd.DataFrame(mydict,index=[0])
            answer = approvereject(ohevalue(df))
            #return render(request,'result.html',{'answer':answer})
            messages.success(request,"*Application Status: {}".format(answer))

    form =ApprovalForm()
    return render(request,'myform.html',{'form':form})


def welcomeView(request):

    return render(request,'welcome.html')
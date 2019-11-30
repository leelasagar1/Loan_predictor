from django import forms

class ApprovalForm(forms.Form):  

    firstname = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':'Enter Firstname'}))
    lastname = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':'Enter Lastname'}))
    Gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
    Married = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    Dependants = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    Education=forms.ChoiceField(choices=[('Graduate','Graduate'),('Not_Graduate','Not_Graduate')])
    Self_Employed = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    ApplicantIncome = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Applicant Income'}))
    CoapplicantIncome = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':"Enter Coapplicant Income"}))
    LoanAmount = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':"Enter LoanAmount"}))
    Loan_Amount_Term = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Laon Amount Term'}))
    Credit_History = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    Property_Area = forms.ChoiceField(choices=[("Rural",'Rural'),('SemiUrban','SemiUrban'),('Urban','Urban')])
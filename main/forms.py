from django import forms
import main.models as models

class JobForm(forms.ModelForm):

	class Meta:
		model = models.Job
		fields = '__all__'

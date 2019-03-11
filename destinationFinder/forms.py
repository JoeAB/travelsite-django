from django import forms

Class SearchForm(forms.Form):
	countrySelect = forms.ChoiceField()

	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args,**kwargs)
		self.fields['countrySelect'].widget = forms.ChoiceField(choice = kwarg.pop('tuple'))

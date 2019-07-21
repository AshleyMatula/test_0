from myapp.forms import ContactForm
from django.views.generic.edit import FormView

class ContactForm(forms.Form):
   name = forms.CharField()
   message = forms.CharField(widget=forms.Textarea)

class Home(FormView):
   template_name="index.html"
   form_class = ContactForm
   success_url = "thanks"

   def form_valid(self, form):
       print('hello')
       print(self.request.POST['name'])
       print(self.request.POST['message'])
       return HttpResponseRedirect(self.get_success_url())

from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from home.models import Contact,Estimate,Subscribe,Comment, Blog
from django.views.generic import ListView,DetailView,FormView
from home.forms import ContactForm,EstimateForm,SubscribeForm,CommentForm
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy


# Create your views here.
class homeView(CreateView):
    model = Estimate,Subscribe
    form_class = EstimateForm
    template_name = "home/index.html" 
    success_url = 'contactus'

    def form_valid(self, form):
        return super(homeView, self).form_valid(form)
    template_name = "home/index.html"
   

class servicesView(CreateView):
      model = Estimate
      form_class = EstimateForm
      template_name = "home/services.html" 
      success_url = '/'

      def form_valid(self, form):
        return super(servicesView, self).form_valid(form)
      template_name = "home/services.html"

class contactusView(CreateView): 
   model = Contact
   form_class = ContactForm
   template_name = "home/contactus.html" 
   success_url = '/'

   def form_valid(self, form):
        return super(contactusView, self).form_valid(form) 

class aboutusView(CreateView):
    model = Estimate
    form_class = EstimateForm
    template_name = "home/aboutus.html" 
    success_url = 'contactus'

    def form_valid(self, form):
        return super(aboutusView, self).form_valid(form)
    template_name = "home/aboutus.html"

class blogListView(ListView):
    model = Blog
    template_name = 'home/blog_list.html'
    login_url = 'login'

class blogDetailView(TemplateView): # new
   template_name = 'home/blog_detail.html'

   def get_context_data(self, *args, **kwargs): 
      context = super().get_context_data(**kwargs)
      commentform = CommentForm()
      id = kwargs['pk']
      print(id)
      blog = Blog.objects.get(id=id) 
      comment = blog.comment.all()
   
      context = {'blog':blog , 'commentform':commentform, 'comments':comment}
      return context

   def post(self, request, pk):
      commentform = CommentForm(request.POST)
      if commentform.is_valid():
         commentfield = commentform.cleaned_data['comment']
         # newsfeedfield = commentform.cleaned_data['Newsfeed']
         save_comment = Comment(Blog_id=pk, comment=commentfield, author_id=self.request.user.id)
         save_comment.save()         
         return HttpResponseRedirect('/')

class quoteView(CreateView):
     model = Estimate
     form_class = EstimateForm
     template_name = "home/get_quote.html" 
     success_url = '/'

     def form_valid(self, form):
        return super(quoteView, self).form_valid(form)
     template_name = "home/get_quote.html"



    

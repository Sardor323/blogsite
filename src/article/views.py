from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
	model = Article
	template_name = 'article_list.html'


class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article_detail.html'



class ArticleUpdateView(UpdateView):
	model = Article
	fields = ('title', 'body', 'photo')
	success_url = reverse_lazy('article_list')
	template_name = 'article_edit.html'



class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'article_delete.html'
	success_url = reverse_lazy('article_list')


class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	success_url = reverse_lazy('article_list')
	fields = ('title', 'body', 'photo', 'author')


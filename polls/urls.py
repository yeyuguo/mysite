from django.conf.urls import url

from . import views

# urlpatterns = [
# 	url(r'^$',views.index,name='index'),
# 	# ex: /polls/polls_temp
# 	url(r'^polls_temp',views.polls_temp,name='self_defined'),
# 	# ex: polls/polls_index/index.html or  polls/polls_index/
# 	url(r'^polls_index',views.polls_index,name='aa'),
# 	# ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]

# url route reconsitution
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/polls_temp
	url(r'^polls_temp',views.polls_temp,name='self_defined'),
	# ex: polls/polls_index/index.html or  polls/polls_index/
	url(r'^polls_index',views.polls_index,name='aa'),
]
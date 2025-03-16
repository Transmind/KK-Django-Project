from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

#@login_required
def topics(request):
    
    # Modified by Ken to allow users to see public topics
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    topics = Topic.objects.all().order_by('date_added')
    for topic in topics:
        if (topic.public == False) and (topic.owner != request.user):
            topics = topics.exclude(id=topic.id)

    context = {'topics':topics}
    return render(request, 'kk_logs/topics.html', context)


# Create your views here.
def index(request):
    return render(request, 'kk_logs/index.html')


# @login_require //commented out by Ken for public topics sharing by all users
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    #check public attribute by Ken
    if (topic.public == False) and (topic.owner != request.user):
        raise Http404


    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'kk_logs/topic.html', context)

@login_required
def new_topic(request):
    
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user

            #add the public attribute by Ken 
            new_topic.public = request.POST.get('public', 'off') == 'on'

            new_topic.save()
            return redirect('kk_logs:topics')
    
    context = {'form': form}
    return render(request, 'kk_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return redirect('kk_logs:topic', topic_id=topic_id)
    
    context = {'topic': topic,'form': form}
   
    return render(request, 'kk_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if entry.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('kk_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'kk_logs/edit_entry.html', context)
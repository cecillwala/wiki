from django.shortcuts import render
from django.http import HttpResponse
import markdown2
from django import forms
from . import util
import random


class entryForm(forms.Form):
    title = forms.CharField(label="Search entry")

def index(request):
    md_text = util.get_entry(entry)
    try:
        content = markdown2.markdown(md_text) 
    except TypeError:
        return HttpResponse("Page Not Found")
    with open("encyclopedia/entry.html", 'w') as file:
        file.write(content)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : entryForm()
    })

def entry(request, entry):
    if request.method == "POST":
        form = entryForm(request.POST)
        if form.is_valid():
            entry =form.cleaned_data["title"]
        md_text = util.get_entry(entry)
        try:
            content = markdown2.markdown(md_text) 
        except TypeError:
            return HttpResponse("Page Not Found")
        with open("encyclopedia/entry.html", 'w') as file:
            file.write(content)
        return render(request, "encyclopedia/entry.html",{
            "title" : entry,
            "content": content,
            "form" :entryForm()
        })
    entries = util.list_entries()
    for entry in entries:
        md_text = util.get_entry(entry)
        try:
            content = markdown2.markdown(md_text) 
        except TypeError:
            return HttpResponse("Page Not Found")
        with open("encyclopedia/entry.html", 'w') as file:
            file.write(content)
        return render(request, "encyclopedia/entry.html",{
            "title" : entry,
            "entry" : entry,
            "content": content,
            "form" :entryForm()
            })

def random_entry(request, entry):
    entries = util.list_entries()
    entry = random.choice(entries)
    md_text = util.get_entry(entry)
    try:
        content = markdown2.markdown(md_text) 
    except TypeError:
        return HttpResponse("Page Not Found")
    with open("encyclopedia/entry.html", 'w') as file:
        file.write(content)
    return render(request, "encyclopedia/entry.html",{
        "title" : entry,
        "content": content,
        "form" :entryForm()
    })


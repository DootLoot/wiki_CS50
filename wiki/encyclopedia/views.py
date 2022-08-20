from pydoc import text
import random
from random import randrange
from markdown2 import Markdown
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    entry = util.get_entry(title)

    md = Markdown()

    if entry == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "file": md.convert(entry),
            "title": title
        })

def redirect(request):
    return HttpResponseRedirect('wiki/')

# takes a str from the form and serches for it        
def search(request):
    if request.GET:
        term = request.GET["q"]
        results = []

        # serches if the term alredy exists, then redirects if it dose
        if util.get_entry(term) == None:
            # loops over a list of entries if the term is a substring
            for entry in util.list_entries():
                if entry.find(term) != -1 or entry.find(term.upper()) != -1 or entry.find(term.title()) != -1:
                    results.append(entry)
            
            return render(request, "encyclopedia/results.html", {
                "entries": results,
                "term": term
            })
        else:
            
            entry = util.get_entry(term)

            return render(request, "encyclopedia/entry.html", {
            "file": Markdown().convert(entry),
            "title": term
        })
    else:
        return redirect('home')

def newPage(request):
    return render(request, "encyclopedia/newPage.html")

def create(request):
    if request.GET:
        title = request.GET["pt"]
        content = request.GET["pc"]

        util.save_entry(title, f"""# {title}
        
{content}""")

        entry = util.get_entry(title)

        return render(request, "encyclopedia/entry.html", {
            "file": Markdown().convert(entry),
            "title": title
        })

def edit(request, title):

    entry = util.get_entry(title)

    return render(request, "encyclopedia/edit.html", {
            "content": entry,
            "title": title
        })

def save(request, title):
    if request.GET:

        content = request.GET["ec"]

        util.save_entry(title, f"""{content}""")

    return render(request, "encyclopedia/entry.html", {
            "file": Markdown().convert(util.get_entry(title)),
            "title": title
        })

def randomPage(request):
    list1 = util.list_entries()
    target = random.randrange(len(list1))
    file = util.get_entry(list1[target])

    return render(request, "encyclopedia/entry.html", {
            "file": Markdown().convert(file),
            "title": list1[target]
        })
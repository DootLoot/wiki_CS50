from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import util
import os

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    
    entry = util.get_entry(title)

    if entry == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "file": entry,
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
            return render(request, "encyclopedia/entry.html", {
            "file": util.get_entry(term),
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

        if os.path.isfile(f"entries/{title}.md"):
            return render(request, "encyclopedia/error.html")
        else:
            fp = open(f"entries/{title}.md", 'w')
            fp.write(f"""# {title}
        
{content}""")
            fp.close()

        return render(request, "encyclopedia/entry.html", {
            "file": util.get_entry(title),
            "title": title
        })
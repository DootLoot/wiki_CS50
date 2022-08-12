from asyncore import write
from django.shortcuts import render
import markdown2

from . import util


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

def create(request):
    return render(request, "encyclopedia/createPage.html")
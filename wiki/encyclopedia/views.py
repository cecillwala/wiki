from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request):
    md_text = util.get_entry('CS')
    try:
        content = markdown2.markdown(md_text) 
    except TypeError:
        return render(request, "encyclopedia/error.html")
    with open('encyclopedia/entry.html', 'w') as file:
        file.write(content)
    return render(request, "encyclopedia/entry.html",
                  {
                      "title" : 'CS',
                      "content" : content
                  })

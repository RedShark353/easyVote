from django.shortcuts import render

#Databases
from .models import Candidate

# Create your views here.
def index(request):
    return render(request, "addVote/newVote.html", {
        "candidates":Candidate.objects.all()
    })

def add(request):
    if request.method == "POST":
        candidateIds = request.POST.getlist('candidate')
        for id in candidateIds:
            candidate = Candidate.objects.get(pk = int(id))
            candidate.votes += 1
            candidate.save()
        return render(request, "addVote/finished.html", {
            "candidates": Candidate.objects.all()
        })
    else:
        return render(request, "addVote/newVote.html")
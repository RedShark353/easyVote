from django.shortcuts import render
import random
import string

#Databases
from .models import Candidate, Code

# Create your views here.
def index(request):
    return render(request, "addVote/newVote.html", {
        "candidates":Candidate.objects.all()
    })

def add(request):
    if request.method == "POST":

        #Check if the code is valid
        userCode = request.POST['code']
        if Code.objects.filter(code=userCode, used=False).exists():
            code = Code.objects.get(code=userCode)
            code.used = True
            code.save()

            #Add the vote
            candidateIds = request.POST.getlist('candidate')
            for id in candidateIds:
                candidate = Candidate.objects.get(pk = int(id))
                candidate.votes += 1
                candidate.save()
            return render(request, "addVote/finished.html", {
                "candidates": Candidate.objects.all(),
            })
        else:
           return render(request, "addVote/newVote.html", {
               "candidates":Candidate.objects.all(),
               "message": "Ο κωδικός αυτός έχει ήδη χρησιμοποιηθεί"
           }) 
    else:
        return render(request, "addVote/newVote.html")

def results(request):
    return render(request, "addVote/finished.html", {
        "candidates": Candidate.objects.all(),
    })

def createCodes():
    created = set()
    i = 0
    while i < 210:
        letters = string.ascii_uppercase
        genCode = ''.join(random.choice(letters) for i in range(6))
        if genCode not in created:
            created.add(genCode)
            newCode = Code(code=genCode, used=False)
            newCode.save()
            i += 1
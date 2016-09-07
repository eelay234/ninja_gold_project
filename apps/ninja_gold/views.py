from django.shortcuts import render, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
  if 'activities' in request.session == False:
     request.session['activities'] = ""
  if 'score' in request.session == False:
     request.session['score'] = 0
  return render(request, "ninja_gold/index.html")

def process_money(request, process):
  if process == "1":
      change = random.randint(10, 20)
      if 'activities' in request.session == False:
        request.session['activities'] = ""
      request.session['score'] += change 
      msg = ("earn %s golds from %s\n" % (str(change), datetime.now().strftime("%Y/%m/%d %I:%M %p"))) 
      request.session['activities'] += msg
      return redirect('/')
  elif process == "2":
      change = random.randint(5, 10)
      request.session['score'] += change
      if 'activities' in request.session == False:
        request.session['activities'] = ""
      request.session['activities'] += "earn "+str(change)+" golds "+"from cave ("+datetime.now().strftime("%Y/%m/%d %I:%M %p")+")\n"
  elif process == "3":
      change = random.randint(2, 5)
      request.session['score'] += change
      if 'activities' in request.session == False:
        request.session['activities'] = ""
      request.session['activities'] += "earn "+str(change)+" golds "+"from house ("+datetime.now().strftime("%Y/%m/%d %I:%M %p")+")\n"
  elif process == "4":
      chance = random.randint(0, 1)
      print "chance "+ str(chance)
      if chance == 0:
         change = random.randint(10, 21)
         request.session['score'] += change
         if 'activities' in request.session == False:
            request.session['activities'] = ""
         request.session['activities'] += "earn "+str(change)+" golds "+"from casino ("+datetime.now().strftime("%Y/%m/%d %I:%M %p")+")\n"
      elif chance == 1:
         change= random.randint(0, 51)
         request.session['score'] -= change
         if request.session['score'] < 0:
            request.session['score'] = 0
         if 'activities' in request.session == False:
            request.session['activities'] = ""         
         request.session['activities'] += "lost "+str(change)+" golds "+"from casino ("+datetime.now().strftime("%Y/%m/%d %I:%M %p")+")\n"
  return redirect('/')

def reset(request):
	request.session['score'] = 0
	request.session['activities'] = ""
	return redirect('/')

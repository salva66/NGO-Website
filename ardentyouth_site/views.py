from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Slides, Mission, Vision, Objectives, Purpose, Values, Pcauses, Team, OutlookDets, ArticleDets, GalleryDets, About

# Create your views here.

def index(request):
        slid = Slides.objects.all()
        abo = About.objects.all()
        miss = Mission.objects.all()
        vis = Vision.objects.all()
        pco = Pcauses.objects.all()
        team = Team.objects.all()
        outluk = OutlookDets.objects.all()
        context = {
                'slid': slid,
                'abo': abo,
                'miss': miss,
                'vis': vis,
                'pco': pco,
                'team': team,
                'outluk': outluk
        }
        return render(request, "index.html", context)

def about_us(request):
        abo = About.objects.all()
        miss = Mission.objects.all()
        vis = Vision.objects.all()
        purpose = Purpose.objects.all()
        obj = Objectives.objects.all()
        values = Values.objects.all()
        context = {
                'abo': abo,
                'miss': miss,
                'vis': vis,
                'purpose': purpose,
                'values': values,
                'obj': obj
        }
        return render(request, "about_us.html", context)

def articles(request):
        abo = About.objects.all()
        article = ArticleDets.objects.all()
        context = {
                'abo': abo,
                'article': article
        }
        return render(request, "articles.html", context)

def contact_us(request):
        abo = About.objects.all()
        context = {
                'abo': abo
        }
        return render(request, "contact_us.html", context)

def executive_director(request):
       
        return render(request, "executive_director.html")

def gallery(request):
        abo = About.objects.all()
        context = {
                'abo': abo
        }
        return render(request, "gallery.html", context)

def outlook(request):
        abo = About.objects.all()
        outy = OutlookDets.objects.all()
        context = {
                'abo': abo,
                'outy': outy
        }       
        return render(request, "outlook.html",context)

def volunteerform(request):
        abo = About.objects.all()
        context = {
                'abo': abo
        }
        return render(request, "volunteerform.html", context)

def member(request):
        abo = About.objects.all()
        context = {
                'abo': abo
        }
        return render(request, "member.html", context)
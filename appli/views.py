from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from appli.models import Sondage, Question, Reponse

def mes_reponses(request, id_sondage):
    reponses = Reponse.objects.filter(question__sondage__id=id_sondage, user=request.user).all()

    return render(request, 'mes_reponses.html', {'reponses': reponses})

def modifier_mdp_post(request):
    nouveau_mdp = request.POST['mdp']
    request.user.password = make_password( nouveau_mdp )
    request.user.save()

    return render(request, 'message.html', {'msg': 'Votre mot de passe a été modifié !'})

def modifier_mdp_get(request):
    return render(request, 'modifier_mdp.html')

def homepage(request):
    return render(request, 'message.html', {'msg': 'Bienvenue sur la page de Sondages '})

def deconnexion(request):
    logout(request)

    return redirect('homepage')

def inscription_post(request):
    username = request.POST['pseudo']
    password = request.POST['mdp']
    email = request.POST['mail']
    user = User.objects.create_user(username, email, password)

    return render(request, 'message.html', {'msg': 'Inscription réussie, connectez-vous !'})

def inscription_get(request):
    return render(request, 'inscription.html')

def connexion_post(request):
    username = request.POST['pseudo']
    password = request.POST['mdp']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('liste_sondages')

    return render(request, 'message.html', {'msg': 'Erreur de connexion'})

def connexion_get(request):
    return render(request, 'connexion.html')

def enregistrer_reponse(request):

    id_question = int( request.POST['id_question'] )
    num_prop = int( request.POST['choix'] )

    question = Question.objects.filter(id=id_question).first()
    reponse = Reponse()
    reponse.user = request.user
    reponse.question = question
    if num_prop==1:
        reponse.num_proposition = 1
    elif num_prop==2:
        reponse.num_proposition = 2
    elif num_prop==3:
        reponse.num_proposition = 3
    elif num_prop==4:
        reponse.num_proposition = 4
    else:
        raise Exception("Vous devez choisir une proposition")

    reponse.save()


    return redirect('repondre_sondage', id_sondage=question.sondage_id, id_question=id_question)

def repondre_sondage(request, id_sondage, id_question):

    sondage = Sondage.objects.filter(id=id_sondage).first()


    question = None
    for quest_act in sondage.question_set.all():
        if quest_act.id>id_question:
            question = quest_act
            break

    if question == None:
        return render(request, "repondre_sondage_fin.html", {'sondage': sondage})


    return render(request, "repondre_sondage.html", {'question': question})

def liste_sondages(request):

    user = request.user

    sondages_termines_repondus = Sondage.objects.filter(question__reponse__user=user, termine=True).distinct()
    sondages_non_termines_repondus = Sondage.objects.filter(question__reponse__user=user, termine=None).distinct()
    sondages_non_termines_non_repondus = Sondage.objects.filter(termine=None).difference( sondages_non_termines_repondus )

    return render(request, "liste_sondages.html", {'sondages_termines_repondus': sondages_termines_repondus,
                                                   'sondages_non_termines_repondus': sondages_non_termines_repondus,
                                                   'sondages_non_termines_non_repondus': sondages_non_termines_non_repondus})
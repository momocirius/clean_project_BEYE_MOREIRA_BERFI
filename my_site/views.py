#my_site/views.py
from django.http import HttpResponse
from django.shortcuts import render
import datetime


from .logic_for_views import get_graph_data, store_question, db


def home_page_view(request):
    """
    Une vue simple qui renvoie une Reponse HTTP "Hello World".
    """
    return HttpResponse('Hello World')


def home_page_view_with_render(request):
    """
    Une vue légèrement plus élaborée qui renvoie un template html
    Django sait où chercher ce template grâce à l'objet TEMPLATES
    du fichier settings.py.
    La navbar est générée en partie à l'aide de la variable sections

    """
    return render(request, "home_page.html",{"sections": [{"title":"Home", "href":"/home"}]})


def form(request):
    """
    Une vue qui renvoie un template comprenant un formulaire.
    Elle permet d'en récupérer les données (et de les afficher dans la console).
    """
    if request.method == "POST":
        alpha = request.POST["data"]
        print("alpha :", alpha)
    # Cas ou request.method = "GET" : on doit initialiser alpha car on l'appelle
    else:
        now = datetime.datetime.now()
        alpha = "Il est {hour}h{minute}, et nous n'avons rien à vous montrer".format(hour=now.hour,
                                                                                     minute=now.minute)
    return render(request, "form_page.html",{"value_1":alpha})


def show_image(request):
    """
    Une vue qui renvoie une réponse HTTP contenant le graph généré.
    """
    data = get_graph_data()
    return HttpResponse(data, content_type="image/png")


def page_needing_js(request):
    """
    View for the page using css + js
    """
    if request.method == "POST":
        # Valeurs du formulaire
        alpha = request.POST["alpha"]
        beta = request.POST["beta"]
        gamma = request.POST["gamma"]
        # Affichage
        print("alpha : {}, \nbeta : {}, \ngamma : {}".format(alpha, beta, gamma))
        ## do_something()
    return render(request, 'page_needing_js.html', {"sections": [{"title":"Home",
                                                                  "href":"/home"}]})


def faq(request, question_int):
    """
    Une vue qui permet d'afficher le template faq (attention l'url est 'faq/<int:question_int>/'.
    On en registre la question (son text) et cet entier question_int dans une base MongoDB
    (seulement si la question finit par "?").
    """
    print("question_int : ", question_int)
    # Si une question a été envoyée
    if request.method == "POST":
        question_text = request.POST["question_text"]
        print("question :", question_text)
        # On vérifie qu'elle termine par : ?
        if question_text[-1] != "?":
            # Si ce n'est pas le cas on renvoie un message expliquant qu'elle n'est pas valide
            return render(request, "faq.html", {'message': "Une question doit finir par ce caractère : ? "})
        # Sinon on renvoie un message indiquant de poser une autre question
        else:
            store_question(question_text=question_text, question_int=question_int, db=db, collection='from_app')
            return render(request, "faq.html", {'message': "Posez une autre question."})
    return render(request, "faq.html")


def skeleton(request):
    """
    Une vie qui permet de voir notre squelette (ne devrait logiquement pas exister)
    """
    return render(request, "skeleton.html")


def using_skeleton(request):
    """
    Une vue qui renvoit vers une page dont le template utilise le squelette mais
    n'est pas rigoureusement identique.
    """
    rgb = {
        'FF0000':'red',
        '00FF00':'green',
        '0000FF':'blue'
        }
    return render(request, "using_skeleton.html", {'rgb': rgb})

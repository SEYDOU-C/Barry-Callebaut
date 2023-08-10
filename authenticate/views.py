from django.shortcuts import render, redirect
from authenticate.forms import CallebautForms
from django.contrib.auth import authenticate, login, logout

## la logique du formulaire de connection des utilisateur de barry callebaut
def CallebautLogin(request):
    form = CallebautForms()
    message = ""
    if request.method == "POST":
        form = CallebautForms(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("Acceuil")
            else:
                message = "Identifiants incorrect !"
    
    return render(request, "login.html", {"form": form, "message": message})

    ## la logique du formulaire de deconnection des utilisateur de barry callebaut

def CallebautLogout(request):
    logout(request)
    return redirect("Acceuil")

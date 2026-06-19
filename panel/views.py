from django.shortcuts import render, redirect
from django.http import HttpResponse
from mctools import RCONClient
from panel.forms import RegisterForm, LoginForm, addServerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login
from panel.models import Server, User
# HOST = "95.216.123.235"
# PORT = 25715
# PASSWORD = "Xnleyo4oLh"
class RconConnect:
    def __init__(self, user):
        server = Server.objects.get(user=user)
        if not server:
            raise Exception("У пользователя нет сервера")
        self.client = RCONClient(
            server.ip,
            port=server.port
        )
        self.client.login(server.password)

    def kill_all(self):
        self.client.command("kill @a")
    def gamemode_all(self):
        self.client.command("gamemode creative @a")
    def restart(self):
        self.client.command("restart")

def panel(request):
    return render(request, "main.html")
def register(request):
    return render(request, "register.html")
def addServer(request):
    return render(request, "addserver.html")

@login_required
def KillAll(request):
    if request.method == "POST":
        rcon = RconConnect(request.user)
        rcon.kill_all()
        return HttpResponse("вы убили бедных игроков")
@login_required
def gamemode(request):
    if request.method == "POST":
        rcon = RconConnect(request.user)
        rcon.gamemode_all()
        return HttpResponse("выдан креатив")
@login_required
def Restart(request):
    if request.method == "POST":
        rcon = RconConnect(request.user)
        rcon.restart()
        return HttpResponse("Перезагрузка...")
    
def reg(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            return redirect("addserver")
    else:
        form = RegisterForm()
    return render(request, "register.html")
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            dj_login(request, user)
            return redirect("main")
    else:
        form = LoginForm()
    return render(request, "login.html")
def addsrv(request):
    if request.method == "POST":
        form = addServerForm(request.POST)
        if form.is_valid():
            server = form.save(commit=False)
            server.user = request.user
            server.save()
            return redirect("main")
    else:
        form = addServerForm()
    return render(request, "addserver.html")
def console(request):
    if request.method == "POST":
        rcon = RconConnect(request.user)
        rcon.client.command(request.POST["command"])
        return render(request, "main.html")
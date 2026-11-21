from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.contrib import messages
from . import grafico

# Create your views here.
def home(request : HttpRequest):

    # recebendo o arquivo pelo navegador e pegando os dados do arquivo para obter um grafico a partir delas
    if request.method == "POST":
        arquivo = request.FILES.get("arquivo")
        if arquivo is not None:
            nome = arquivo.name.lower()

            if nome.endswith(".mp3") or nome.endswith(".wav"):
                print(arquivo.name)
                grafico.make_grafic(arquivo)
            else :
                messages.error(request, "Erro, Tipo do arquivo inválido")

        else:
            messages.error(request, "Erro, nenhum arquivo selecionado")

    return render(request, "home.html")

def sobre(request):
    return render(request, "sobre.html")


def get_image(request):
    img_path = "grafico.png"

    try:
        with open(img_path, "rb") as f:
            image = f.read()
    except:
        return HttpResponse("")

    response = HttpResponse(image, content_type="image.png")

    
    return response
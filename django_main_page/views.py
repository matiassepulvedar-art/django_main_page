from django.shortcuts import render

def inicio(request):
    return render(
        request,
        "inicio.html",
    )

def ruleta(request):
    premios = [
        "10% descuento",
        "20% descuento",
        "Producto gratis",
        "Inténtalo de nuevo",
        "Envío gratis",
        "50% descuento"
    ]
    return render(request, "ruleta.html", {"premios": premios})

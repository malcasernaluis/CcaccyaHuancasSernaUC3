from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    mensaje = """
                <h1> Universidad Nacional Tecnologica de Lima Sur </h1>
                <h2> EP Ing de Sistemas </h2>
                <h3>Bienvenidos</h3>
    
    
    """
    return HttpResponse(mensaje)

def uc3(request):
    mensaje = """
          <h1>Lenguaje de programación III</h1>
          <h2>Evaluacion de la Unidad de Competencia 3</h2>
          <h3>Docente: Mg.Flor Elizabeth Cerdán León</h3>
          <h3>Integrantes: </h3>
          <h4>. Ccaccya Huaman Antony</h4>
          <h4>. Huancas Leuyacc Anselmo Junior</h4>
          <h4>. Serna Malca Luis Alejandro</h4>
          """

    return HttpResponse(mensaje)

def noticia(request):
    mensaje = """
                <h1>noticia</h1>
                <p> Fiscalía incluyó a Norma Sánchez, esposa de Juan Silva, en investigación preliminar contra Zamir Villaverde por presunto lavado de activos
                    Norma Sánchez Córdova, esposa del prófugo exministro de Transportes y Comunicaciones, Juan Silva, fue incluida en la investigación preliminar que se le sigue al empresario Zamir Villaverde, el exsecretario general del Despacho Presidencial, Bruno Pacheco, Fray Vásquez Castillo, sobrino del presidente Pedro Castillo, y otros por presunto lavado de activos.
                    Así lo dispuso la fiscal Luz Taquire, quien adoptó esta medida el último 27 de junio tras la difusión de audios en los que se les escucha decir al empresario Zamir Villaverde que entregó “cien grandes” al entonces ministro de Transportes y Comunicaciones, Juan Silva.
                    La fiscal Taquire consideró que existe sospecha simple que Zamir Villaverde recibió depósitos de dinero presuntamente ilícitos de sus empresas Vigarza S.A.C y Estudio Villaverde S.A.C, los cuales fueron entregados en efectivo a Juan Silva, quien luego los entregó a su esposa, a fin de que cancele un crédito que tendía con una entidad bancaria.<p> 

                """
    return HttpResponse(mensaje)
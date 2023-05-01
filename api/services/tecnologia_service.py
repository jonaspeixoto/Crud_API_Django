from ..models import Tecnologia

def listar_tecnologia():
    tecnologias = Tecnologia.objects.all()
    return tecnologias
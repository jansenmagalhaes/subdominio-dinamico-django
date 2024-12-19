from django.conf import settings
from django.http import HttpResponseRedirect
from cryptography.fernet import Fernet

class AcessoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):     
        response = self.get_response(request)

        host = request.get_host().split('.')

        if len(host) == 1:
            token_acesso = response.cookies.get('tokenAcesso')

            if token_acesso:
                token_acesso.value

                f = Fernet(token_acesso.value)
                decrypted_data = f.decrypt(request.POST.get('a', ''))

        else:
            pass

        # if sessao:
        #     print(sessao.value)

        # if sessao != '':
        #     sessao = sessao.split(';')[0].split('=')[1]
        #     print(response.cookies.get('sessionid'))

        return response
    
class SubdominioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            protocolo = settings.PROTOCOL
            host = request.get_host().split('.')
            path = request.path_info
            organizacao = request.user.organizacao
            subdominio = f"{'' if len(host) == 1 else host[0]}"
            uri = f"{host[0] if len(host) == 1 else host[1]}{path}"

            if organizacao == '' and len(host) == 2:
                print(f"Passou pela condição para remover subdomínio")
                url = f"{protocolo}{uri}"
                
                return HttpResponseRedirect(url)
            elif organizacao != '' and organizacao != subdominio:
                print(f"Passou pela condição com o seguinte subdomínio: {organizacao}")
                url = f"{protocolo}{organizacao}.{uri}"
                
                return HttpResponseRedirect(url)
        
        response = self.get_response(request)

        return response
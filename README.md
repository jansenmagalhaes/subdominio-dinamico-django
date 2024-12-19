# Estudo sobre possibilidade de uso de subdominio dinâmico no Django

Criei um modelo de aplicação com a implementação de uma módulo app de usuários e estou usando a autenticação padrão do Django.

Busquei neste estudo identificar uma regra que fosse adequada para fazer autenticação e direcionar o usuário para um subdomínio específicio.

O desafio dessa proposta é manter a sessão principal de acesso do usuário rastreada para identificar se é do usuário logado e redirecionar para o subdomínio caso o usuário continue logado na sessão do subdomínio.

## Esquema de acesso

Conforme apresentado no diagrama abaixo, a pretensão é verificar o host da requisição e caso seja do domínio principal deve ser executado um procedimento para verificar token_acesso salvo em cookie e redirecionar para o subdomínio. Caso a requisição parta do subdomínio será somente permanecido o retorno ou redirecionado para o domínio em caso de não estar autenticado ou essa ter expirado.

![Diagrama de Acesso com Subdomínio Dinâmico](/doc/diagrama_acesso.png)

### Pontos importantes a considerar

+ ao ser redirecionado para algum path do domínio principal para o subdomínio home é razoável alertar o usuário se o mesmo tem a intenção de permanecer logado no sistema.
+ é impressídivel o token_acesso ter uma regra de invalidação ao sair do sistema, de preferência com codição de validade de token_acesso guardada no banco de dados.
+ deve ter uma regra para tratar caso em que tem token_acesso válido, porém o subdomínio não está autenticado, para evitar infinite loop. O usuário deve se autenticar no domínio, redirecionar para home do domínio para carregar o token_acesso no cookie e redirecionar para subdomínio autenticando a sessão do django. Em caso de não conseguir autenticar ou ter sessão expirada, o token_acesso do domínio deve ser invalidado para voltar para um estado inicial de acesso no domínio.
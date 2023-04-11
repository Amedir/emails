# Enviando emails com Python

## Sobre o Projeto
Este projeto tem como objetivo destribuir o conhecimento acerca do envio de emails pelo Gmail sem muitas configurações e burocracias com Python.

## Como usar
Para utilizar o projeto, siga os seguintes passos:

```bash
# clonar repositório
git clone https://github.com/Amedir/send-emails-python.git

# Navegue até a pasta do projeto
cd /c/sua-area-de-trabalho/send-emails-python

# Inicie o vsCode
code .

# Instale os requesitos do projetos
pip install -r requirements.txt
```

Crie um arquivo com nome `.env` na raiz do projeto e adicione as seguintes variaveis:

```bash
FROM = "seuemail@gmail.com"
SENHA = "suasenha12345"
TO = "email1@gmail.com,email2@gmail.com"
```
Siga para o gerenciamento da sua conta Google:
1. Acesse a aba de "Segurança".
2. Procure por "Acesso a app menos seguro"
3. Ative a opção "Permitir aplicativos menos seguros"

Por fim, apenas execute o arquivo `gmail.py`

## Contribuindo

Contribuições são sempre bem-vindas. Para contribuir com este projeto, siga os seguintes passos:

1. Faça um fork deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/sua-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adicionando uma nova feature'`).
4. Envie a sua branch para o repositório remoto (`git push origin feature/sua-feature`).
5. Abra um pull request.

## Autores

* [Ademir Monteiro](https://github.com/Amedir)
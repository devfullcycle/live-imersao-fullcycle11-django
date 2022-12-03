![Imersão Full Stack && Full Cycle](https://events-fullcycle.s3.amazonaws.com/events-fullcycle/static/site/img/grupo_4417.png)

Participe gratuitamente: https://imersao.fullcycle.com.br/

## Sobre o repositório
Esse repositório contém o código-fonte ministrado na aula Django - Desenvolva grandes aplicações em minutos [https://www.youtube.com/watch?v=NC6aUo5rxco](https://www.youtube.com/watch?v=NC6aUo5rxco)

## Rodar a aplicação

O projeto foi construído com o VSCode + Dev Container, com eles você poderá rodar facilmente sem mesmo executar nenhum comando Docker.

Aplique o atalho `CTRL+SHIFT+P` VSCode e selecione a opção: 'Open Folder In Container'. O VSCode vai recarregar, levantar o container e instalar a extensão do Python. Aguarde alguns segundos e abra o terminal do VSCode e digite os seguintes comandos:


```bash
python manage.py migrate
python manage.py loaddata initial_data
```

Acesse a aplicação em [http://localhost:8000/admin](http://localhost:8000/admin)

Usuário para login:

```bash
username: admin@user.com
password: secret
```
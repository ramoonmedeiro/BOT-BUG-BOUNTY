# BOT-BUG-BOUNTY

Um BOT criado para realizar scans e procurar falhas simples e intermediárias em empresas que possuem programas de BUG BOUNTY (HackerOne, BugCrowd, Intigriti e etc).
Ao escolher a empresa, focar em escopos grandes, ex.: *.google.com ou *.facebook.com.

Este BOT possui ferramentas para scans de portas, crawlers para conseguir descobrir endpoints mais escondidos para exploração. Além disso, é escaneado arquivos JavaScript para análise.
Arquivos sensíveis também podem ser encontrados (.pdf, .sql, .xlsx e etc) 
Os tipos de falhas que esse BOT pode encontrar são: subdomain takeover, open redirects, XSS refletido e sql injection. 

Use esse BOT com segurança e apenas com propósitos corretos. O seu uso indevido, pode ocasionar em crimes cibernéticos.

# Instalação e Uso

Para poder utilizar esse BOT, é necessário clonar esse repositório:

```
$ git clone https://github.com/ramoonmedeiro/BOT-BUG-BOUNTY.git
$ cd BOT-BUG-BOUNTY/
```

Após executar o comando acima, é necessário  baixar a linguagem GO (https://go.dev/). Após baixar o GO, você está pronto para executar o script setup.sh

```
$ chmod a+x setup.sh
$ ./setup.sh
$ pip3 install -r requirements.txt
```

Esse script irá baixar todos os programas necessários para que o BOT funcione. NOTA: Se a linguagem GO não estiver instalada, os programas não serão instalados.

Sendo assim, você está pronto para executar o BOT.

```
$ python3 main.py &
```

OBS.: Recomendo fortemente usar esse script em uma VPS como a digital ocean, já que escanear e procurar falhas em um dado subdomínio pode demorar dias.

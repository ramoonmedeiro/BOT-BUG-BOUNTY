# BOT-BUG-BOUNTY

Um BOT criado para realizar scans e procurar falhas simples e intermediárias em empresas que possuem programas de BUG BOUNTY (HackerOne, BugCrowd, Intigriti e etc).
Ao escolher a empresa, focar em escopos grandes, ex.: *.google.com ou *.facebook.com.

Este BOT possui ferramentas que são crawlers, para conseguir descobrir endpoints mais escondidos para exploração. Além disso, é escaneado arquivos JavaScript para análise.
Arquivos sensíveis também podem ser encontrados (.pdf, .sql, .xlsx e etc) 
Os tipos de falhas que esse BOT pode encontrar são: subdomain takeover, open redirects, XSS refletido e sql injection. 

# Instalação e Uso

```
$ git clone https://github.com/ramoonmedeiro/BOT-BUG-BOUNTY.git
$ cd BOT-BUG-BOUNTY/
$ pip3 install -r requirements.txt
```

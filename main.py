import os
import sys
import requests

# Telegram informations
token = 'YOUR_TOKEN' # CHANGE THIS
PATH = 'YOUR_PATH_HERE' # CHANGE THIS ex.: home/ramon/go/bin or home/ramon/tools/findomain
chatid = 'YOUR_CHATID' #CHANGE THIS

# Função que mandas mensagens no TELEGRAM

def send_message(token, chatid, msg):
    data = {"chat_id": chatid, "text": msg}
    url = "https://api.telegram.org/bot{}/sendMessage".format(token)
    requests.post(url, data)

# Começando a recursão

with open('ESCOPO', 'r') as arquivo:
    for dominio in arquivo:
        dominio = dominio.strip()
        os.mkdir(dominio)
        os.chdir(dominio)

# ENUMERAÇÃO DE SUBDOMINIOS COM UMA RECURSIVIDADE

        msg1 = f'## RECON NO DOMINIO {dominio} INICIADO'
        send_message(token, chatid, msg1)

        os.system(f'{PATH}/go/bin/subfinder -d ' + dominio + ' -o subfind.txt --silent')
        os.system(f'{PATH}/go/bin/assetfinder -subs-only ' + dominio + ' | tee -a asset.txt')
        os.system(f'{PATH}/tools/findomain/findomain-linux -t ' + dominio + ' -u findo.txt')
        os.system(f'curl -s "https://crt.sh/?q=%25.' + dominio + '&output=json" | jq -r ".[].name_value" | {PATH}/go/bin/anew crt.txt')
        os.system('amass enum -d ' + dominio + ' -o amass.txt')
        os.system(f'cat subfind.txt asset.txt findo.txt crt.txt amass.txt | {PATH}/go/bin/anew escopo1.txt')
        os.system('rm subfind.txt asset.txt findo.txt crt.txt amass.txt')


# ANÁLISE DE PORTAS COM NAABU

        msg2 = f'## ANÁLISE DE PORTAS INICIADO'
        send_message(token, chatid, msg2)
        os.system(f'{PATH}/go/bin/naabu -l escopo1.txt -o naabu.txt -silent')
        msg3 = f'## ANÁLISE DE PORTAS FINALIZADO'
        send_message(token, chatid, msg3)

# VERIFICAÇÃO DE SERVIÇOS COM HTTPX

        os.system(f'cat escopo1.txt | {PATH}/go/bin/httpx -silent -o escopo200.txt')
        total = 0
        vivos = 0

        with open('escopo1.txt', 'r') as arquivo:
            for linha in arquivo:
                total += 1

        with open('escopo200.txt', 'r') as arquivo:
            for linha in arquivo:
                vivos += 1


        msg4 = f'Foram encontrados {total} subdominios\n{vivos} se encontram ativos!'
        send_message(token, chatid, msg4)

        os.system('rm escopo1.txt')

# ANÁLISE DE SUBDOMAIN TAKEOVER

        l = 0
        msg5 = f'## Análise de SUBDOMAIN TAKEOVER iniciada'
        send_message(token, chatid, msg5)

        os.system(f'python3 {PATH}/tools/takeover/takeover.py -l escopo200.txt -o saida-subdomain.txt')
        os.system('echo "FINAL DO OUTPUT" >> saida-subdomain.txt') 
        with open('saida-subdomain.txt', 'r') as arquivo:
            for linha in arquivo:
                l += 1

        if l > 3:
            msg6 = f'*-* POSSÍVEL SUBDOMAIN TAKEOVER *-*'
            send_message(token, chatid, msg6)
        else:
            msg7 = f'Não houve a falha de SUBDOMAIN TAKEOVER'
            send_message(token, chatid, msg7)


# ANÁLISE DE GIT EXPOSED

        msg8 = f'## ANÁLISE DE GIT EXPOSED INICIANDO'
        send_message(token, chatid, msg8)
        os.system(f'{PATH}/go/bin/goop -l escopo200.txt') 
        msg9 = f'Análise de git EXPOSED terminada'
        send_message(token, chatid, msg9)

# ENUMERANDO ENDPOINTS COM CACHE DE INTERNET

        msg10 = f'## ENUMERAÇÃO DE ENDPOINTS COM CACHE INICIADA'
        send_message(token, chatid, msg10)

        os.system(f"xargs -a escopo200.txt -I@ sh -c 'python3 {PATH}/tools/ParamSpider/paramspider.py -d @ --exclude jpg,svg,jpeg,png -o @.txt'")
        os.system('cat http:/*.txt https:/*.txt | /home/ramon/go/bin/anew spider.txt ; rm -rf http*')
        os.system(f'cat escopo200.txt | {PATH}/go/bin/waybackurls | tee -a wayback.txt')
        os.system(f'cat escopo200.txt | {PATH}/go/bin/gau | tee -a gau.txt')
        os.system(f'cat wayback.txt gau.txt spider.txt | {PATH}/go/bin/anew urls.txt')
        os.system(f'cat urls.txt | {PATH}/go/bin/httpx -silent -o urls200.txt ; rm wayback.txt gau.txt urls.txt')
        
# CRAWLER ENUMERATION COM HACKRWALER COM DEPTH 2

        os.system(f'cat escopo200.txt | {PATH}/go/bin/hakrawler -subs -d 2 | tee -a crawl.txt')

# URLS POSSIVEIS

        os.system(f'cat crawl.txt urls200.txt | {PATH}/go/bin/anew urlsFULL.txt ; rm urls200.txt crawl.txt')
        end = 0
        with open('urlsFULL.txt', 'r') as arquivo:
            for linha in arquivo:
                end += 1

        msg11 = f'Fim da enumeração de endpoints\nForam encontrados {end} endpoints ativos.'
        send_message(token, chatid, msg11)

# ENUMERAÇÃO DE JS

        os.system('cat urlsFULL.txt | grep -iE "\.js" | grep -ivE "\.json" | sort -u | tee -a j.txt')
        os.system(f'{PATH}/go/bin/getJS --input escopo200.txt --complete --output gJS1.txt')
        os.system(f'{PATH}/go/bin/getJS --input urlsFULL.txt --complete --output gJS2.txt')
        os.system(f'cat j.txt gJS1.txt gJS2.txt | {PATH}/go/bin/anew js.txt ; rm j.txt gJS1.txt gJS2.txt')
        os.system(f'cat js.txt | {PATH}/go/bin/httpx -o js200.txt ; rm js.txt')

# ADQUIRINDO ARQUIVOS .PDF .XLSX .ZIP .DOCX .DB .BAK

        os.system(f'cat urlsFULL.txt | grep ".pdf" | {PATH}/go/bin/httpx -silent -mc 200 -o pdf.txt')
        os.system(f'cat urlsFULL.txt | grep ".xlsx" | {PATH}/go/bin/httpx -silent -mc 200 -o xlsx.txt')
        os.system(f'cat urlsFULL.txt | grep ".zip" | {PATH}/go/bin/httpx -silent -mc 200 -o zip.txt')
        os.system(f'cat urlsFULL.txt | grep ".docx" | {PATH}/go/bin/httpx -silent -mc 200 -o docx.txt')
        os.system(f'cat urlsFULL.txt | grep ".db" | {PATH}/go/bin/httpx -silent -mc 200 -o db.txt')
        os.system(f'cat urlsFULL.txt | grep ".bak" | {PATH}/go/bin/httpx -silent -mc 200 -o bak.txt')
        os.system(f'cat urlsFULL.txt | grep ".csv" | {PATH}/go/bin/httpx -silent -mc 200 -o csv.txt')
        os.system(f'cat urlsFULL.txt | grep ".php" | {PATH}/go/bin/httpx -silent -mc 200 -o php.txt')
        os.system(f'cat pdf.txt xlsx.txt zip.txt docx.txt db.txt bak.txt csv.txt php.txt| {PATH}/go/bin/anew sfiles.txt')
        os.system(f'rm pdf.txt xlsx.txt zip.txt docx.txt db.txt bak.txt csv.txt php.txt')

        f = 0
        with open('sfiles.txt', 'r') as arquivo:
            for linha in arquivo:
                f += 1

        if f > 0:
            msg12 = f'*-* ENCONTRADO POSSÍVEIS ARQUIVOS SENSÍVEIS *-*'
            send_message(token, chatid, msg12)
        else:
            msg13 = f'Não houve arquivos sensíveis encontrados'
            send_message(token, chatid, msg13)

# ANÁLISE DE OPEN REDIRECT

        msg14 = f'## ANÁLISE DE OPEN REDIRECT INICIADA'
        send_message(token, chatid, msg14)

        os.system(f'cat urls200.txt | {PATH}/go/bin/gf redirect | tee -a redirect.txt')

        predir = 0
        with open('redirect.txt', 'r') as arquivo:
            for linha in arquivo:
                predir += 1

        msg15 = f'{predir} parâmetros de redirect encontrado.'
        send_message(token, chatid, msg15)

        os.system(f'python3 {PATH}/tools/Oralyzer/oralyzer.py -l redirect.txt -p {PATH}/tools/Oralyzer/payloads.txt | tee -a saida-redir.txt')

        r = 0
        with open('saida-redir.txt', 'r') as arquivo:
            for linha in arquivo:
                if 'Header Based Redirection' in linha:
                    r += 1

        if r >= 1:
            msg16 = f'*-* OPEN REDIRECT ENCONTRADO *-*'
            send_message(token, chatid, msg16)
        else:
            msg17 = f'Não houve a falha de open redirect'
            send_message(token, chatid, msg17)

# Análise de XSS

        msg18 = f'## ANÁLISE DE XSS INICIADA'
        send_message(token, chatid, msg18)

        os.system(f'cat urlsFULL.txt | {PATH}/go/bin/gf xss | {PATH}/go/bin/Gxss -p MARK -o GXSS.txt')
        os.system(f'cat GXSS.txt | {PATH}/go/bin/anew xss.txt')

        xss = 0
        with open('xss.txt', 'r') as arquivo:
            for linha in arquivo:
                xss += 1

        msg19 = f'{xss} parâmetros de xss foram refletidos!'
        send_message(token, chatid, msg19)


# XSS WITH DALFOX

        os.system(f'cat xss.txt | {PATH}/go/bin/dalfox pipe --skip-bav --silence -o output-dalfox.txt')
        os.system('echo "FINAL DO OUTPUT" >> output-dalfox.txt')

        poc = 0
        with open('output-dalfox.txt', 'r') as arquivo:
            for linha in arquivo:
                if '[POC]' in linha:
                    poc += 1

        if poc >= 1:
            msg20 = f'*-* XSS ENCONTRADO COM DALFOX *-*'
            send_message(token, chatid, msg20)
            with open('output-dalfox.txt', 'r') as arq:
                for linha in arq:
                    msg21 = f'{linha}'
                    send_message(token, chatid, msg21)
        else:
            msg22 = f'Não houve falha de XSS com o dalfox!'
            send_message(token, chatid, msg22)


# Análise de SQLI

        msg23 = f'## Análise de SQLI INICIANDO'
        send_message(token, chatid, msg23)

        os.system(f'cat urls200.txt | {PATH}/go/bin/gf sqli | tee -a sqli.txt')
        os.system(f'python3 {PATH}/tools/sqlmap-dev/sqlmap.py -m sqli.txt --batch --disable-coloring --random-agent --level 1 | tee -a sqli-res.txt')

        sqli = 0
        with open('sqli-res.txt', 'r') as arquivo:
            for linha in arquivo:
                if 'do you want to exploit this SQL injection?' in linha:
                    sqli += 1	


        if sqli >= 1:
            msg24 = f'*-* SQLI ENCONTRADO *-*'
            send_message(token, chatid, msg24)
        else:
            msg25 = f'Não houve falha de SQLI'
            send_message(token, chatid, msg25)

        msg26 = f'## ANÁLISE DO SUBDOMINIO {dominio} TERMINADA, INDO PARA O PRÓXIMO.'
        send_message(token, chatid, msg26)

        os.chdir(f'../')

msg27 = f'## AUTOMAÇÃO TERMINADA'
send_message(token, chatid, msg27)

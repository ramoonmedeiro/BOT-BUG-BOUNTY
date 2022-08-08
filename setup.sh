#!/bin/bash

echo "[+] Instalando pacotes de descoberta de subdomínios..."
echo ""

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/tomnomnom/assetfinder@latest
go install -v github.com/tomnomnom/anew@latest
go install -v github.com/OWASP/Amass/v3/...@master
mkdir -p tools/findomain; cd tools/findomain ; wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux
chmod +x findomain-linux ; ./findomain-linux ; cd ../../
echo ""
echo "Insira a sua senha abaixo:"
sudo apt-get install jq

echo ""
echo "[+] Instalando Naabu e Httpx e etc..."
echo ""

go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

echo ""
echo "[+] Instalando Takeover..."
echo ""

cd tools ; git clone https://github.com/m4ll0k/takeover.git ; cd takeover
python3 setup.py install ; cd ../../

echo ""
echo "[+] Instalando Goop..."
echo ""

go install github.com/deletescape/goop@latest

echo ""
echo "[+] Instalando Crawlers..."
echo ""

cd /tools/ ; git clone https://github.com/devanshbatham/ParamSpider
cd ParamSpider ; pip3 install -r requirements.txt ; cd ../../

go install github.com/tomnomnom/waybackurls@latest
go install github.com/lc/gau/v2/cmd/gau@latest
go install github.com/hakluke/hakrawler@latest

echo ""
echo "[+] Instalando Crawler de JavaScript..."
echo ""

go install github.com/003random/getJS@latest


echo ""
echo "[+] Instalando Oralyzer..."
echo ""

go install -v github.com/tomnomnom/gf@latest
mkdir .gf ; cd .gf/ 
wget https://raw.githubusercontent.com/1ndianl33t/Gf-Patterns/master/redirect.json
wget https://raw.githubusercontent.com/1ndianl33t/Gf-Patterns/master/xss.json
wget https://raw.githubusercontent.com/1ndianl33t/Gf-Patterns/master/sqli.json
cd ../tools ; git clone https://github.com/r0075h3ll/Oralyzer.git
cd Oralyzer/ ; pip3 install -r requirements.txt ; cd ../../

echo ""
echo "[+] Instalando Dalfox e Gxss..."
echo ""

go install github.com/hahwul/dalfox/v2@latest
go install github.com/KathanP19/Gxss@latest


echo ""
echo "[+] Instalando SqlMap..."
echo ""

cd tools/ ; git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev


echo ""
echo "[+] Instalação Finalizada!"
echo ""

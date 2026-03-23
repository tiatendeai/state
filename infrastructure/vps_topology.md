poderia me passar os dados para eu poder acessar as vps atuais porr cli
Aqui estão os dados e os comandos para você acessar as VPS atuais via terminal (CLI).

As chaves SSH estão localizadas na sua máquina local, no diretório do projeto ou na sua pasta padrão ~/.ssh/.

🖥️ VPS 1 (Ubuntu 24.04)
IP: 167.234.228.71
Usuário: ubuntu
Chave SSH: ~/.ssh/id_ed25519
Comando:
bash
ssh -i ~/.ssh/id_ed25519 ubuntu@167.234.228.71
🖥️ VPS 2 (Ubuntu 20.04) — Recomendada para testes
IP: 129.148.17.85
Usuário: ubuntu
Chave SSH: 

./ssh/ssh-key-2026-03-10.key
 (Dentro da pasta do projeto)
Comando:
bash
ssh -i /Users/diego/Downloads/codex/vps-oracle/ssh/ssh-key-2026-03-10.key ubuntu@129.148.17.85
💡 Dica: Configurando um arquivo SSH Config
Para facilitar o seu acesso sem precisar digitar o caminho da chave toda vez, você pode adicionar isso ao seu arquivo ~/.ssh/config na sua máquina local:

text
Host vps1
    HostName 167.234.228.71
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519
Host vps2
    HostName 129.148.17.85
    User ubuntu
    IdentityFile /Users/diego/Downloads/codex/vps-oracle/ssh/ssh-key-2026-03-10.key
Depois de salvar, você poderá acessar apenas digitando: ssh vps1 ou ssh vps2.
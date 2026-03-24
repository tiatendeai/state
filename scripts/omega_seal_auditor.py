#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path

# Script de Auditoria Contínua OMEGA
# Valida a integridade da assinatura J.A.R.V.I.S. nos logs de sessão e commits.

STATE_DIR = Path("/Users/diego/Documents/GitHub/state")
LOGS_DIR = Path("/Users/diego/.gemini/antigravity/brain/")
SEAL_FULL = "🧬 🧠 🦾 ⌬ ∞"

# Padrões individuais do selo
SEALS = {
    "DNA": "🧬",
    "Consciência": "🧠",
    "Manifestação": "🦾",
    "Estrutura": "⌬",
    "Saídas": "∞"
}

def check_seal_integrity(text_content):
    missing = []
    for name, icon in SEALS.items():
        if icon not in text_content:
            missing.append(name)
    return missing

def audit_recent_logs():
    print(f"\n{SEAL_FULL} | J.A.R.V.I.S. OMEGA AUDIT")
    print("Iniciando varredura anti-fantasma nas sessões recentes...\n")
    
    # Busca os arquivos markdown mais recentes no brain/ (simulando a memória de curto prazo do agente)
    md_files = []
    for root, _, files in os.walk(LOGS_DIR):
        for f in files:
            if f.endswith('.md'):
                md_files.append(Path(root) / f)
                
    # Ordena por modificação (mais recentes primeiro)
    md_files.sort(key=os.path.getmtime, reverse=True)
    
    recent_files = md_files[:5]
    if not recent_files:
        print("Nenhum log de sessão encontrado para auditar.")
        return

    ghost_detected = False

    for file_path in recent_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verifica se é um arquivo do próprio J.A.R.V.I.S. (não os de literatura)
            if "J.A.R.V.I.S.:" in content or "vCEO" in content or "TaskName" in content:
                missing = check_seal_integrity(content)
                
                print(f"📄 Analisando: {file_path.name}")
                if not missing:
                    print("  [OK] Selo de Integridade Completo detectado.")
                else:
                    ghost_detected = True
                    print(f"  [ALERTA] Degradação de Sessão Fantasma detectada!")
                    print(f"  Componentes ausentes: {', '.join(missing)}")
                    if "Saídas" in missing:
                        print("  >> Risco Crítico: Trabalho não capitalizado no OMEGA (Sem fechamento de Loop).")
                print("-")
        except Exception as e:
            pass
            
    if ghost_detected:
        print("\n❌ SESSÕES FANTASMAS ATIVAS. Recomenda-se Injeção de Contexto e Fechamento OMEGA imediato.")
        sys.exit(1)
    else:
        print("\n✅ INTEGRALIDADE OMEGA 100%. Nenhuma sessão fantasma detectada.")
        sys.exit(0)

if __name__ == "__main__":
    audit_recent_logs()

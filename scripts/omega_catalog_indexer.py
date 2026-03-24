#!/usr/bin/env python3
import os
import yaml
from pathlib import Path

# Indexador Automático OMEGA para catalog.yaml
# Mapeia recursivamente a biblioteca e gera a lista canônica.

STATE_DIR = Path("/Users/diego/Documents/GitHub/state")
CATALOG_PATH = STATE_DIR / "registry" / "catalog.yaml"
KNOWLEDGE_PATHS = [
    STATE_DIR / "knowledge" / "library",
    STATE_DIR / "knowledge" / "tech",
    STATE_DIR / "knowledge" / "management"
]

def generate_catalog():
    print("🧬 🧠 🦾 ⌬ ∞ | J.A.R.V.I.S.: Iniciando Indexação Massiva OMEGA...")
    items = []
    
    for base_path in KNOWLEDGE_PATHS:
        if not base_path.exists():
            continue
            
        for root, _, files in os.walk(base_path):
            if '.git' in root or '.DS_Store' in root:
                continue
                
            for file in files:
                if file.startswith('.'):
                    continue
                    
                full_path = Path(root) / file
                rel_path = full_path.relative_to(STATE_DIR)
                
                # Definir categoria baseada no caminho
                category = "framework"
                if "tech" in str(rel_path):
                    category = "tooling"
                elif "LIVROS" in str(rel_path):
                    category = "literature"
                    
                # Definir tags baseadas em heurísticas
                tags = []
                path_str = str(rel_path).lower()
                if "vendas" in path_str or "marketing" in path_str or "copy" in path_str:
                    tags.extend(["sales", "growth"])
                if "tech" in path_str or "itil" in path_str or "aws" in path_str:
                    tags.extend(["engineering", "architecture"])
                if "finan" in path_str or "economia" in path_str:
                    tags.extend(["finance"])
                if not tags:
                    tags = ["general-management"]

                item = {
                    "id": f"{category}-{len(items):04d}",
                    "name": file.replace('.pdf', '').replace('.txt', '').replace('.md', ''),
                    "category": category,
                    "path": str(rel_path),
                    "tags": tags,
                    "synaptic_load_ms": 150 if category == "literature" else 50,
                    "active": True
                }
                items.append(item)

    # Monta a estrutura do YAML
    catalog_data = {
        "metadata": {
            "version": "3.0.0",
            "last_updated": "2026-03-24",
            "total_items": len(items),
            "generated_by": "J.A.R.V.I.S. Omega Indexer"
        },
        "intelligence_items": items
    }
    
    # Salvar no arquivo
    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        f.write("# CATÁLOGO DE INTELIGÊNCIA V3.0 (INDEXADO AUTOMATICAMENTE VIA OMEGA)\n")
        f.write("# Fonte: STATE\n")
        yaml.dump(catalog_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        
    print(f"✅ Catálogo recompilado! {len(items)} obras registradas permanentemente em {CATALOG_PATH.name}")

if __name__ == "__main__":
    generate_catalog()

# Manifesto de Quarentena OMEGA: `vps-oracle`

**Data:** 24 Mar 2026
**Repositório de Origem:** `vps-oracle`
**Operador:** J.A.R.V.I.S. (via Selo 🧬🧠🦾⌬∞)

## Arquivos Isolados

### 1. `poderia pesquisar no repositorio oficial do docker a imagem do n8n fila para.._.pdf`
*   **Caminho Original:** `/Users/diego/Documents/GitHub/vps-oracle/poderia pesquisar no repositorio oficial do docker a imagem do n8n fila para.._.pdf`
*   **Destino:** `state/quarantine/blobs/vps-oracle/`
*   **Tamanho:** ~364 KB
*   **Justificativa Mestre:** Arquivo PDF de instrução solto na raiz do projeto. O repositório `vps-oracle` atua como infraestrutura `IaC` (Terraform/Docker). Manter manuais soltos aqui polui o ambiente e foge ao escopo estrito arquitetural, sendo papel do `state` alocar estudos de base.
*   **Como reverter:**
    ```bash
    mv '/Users/diego/Documents/GitHub/state/quarantine/blobs/vps-oracle/poderia pesquisar no repositorio oficial do docker a imagem do n8n fila para.._.pdf' '/Users/diego/Documents/GitHub/vps-oracle/'
    ```

### 2. `Diego, fiz um pente-fino profundo focado no seu av.pdf`
*   **Caminho Original:** `/Users/diego/Documents/GitHub/vps-oracle/docs/references/Diego, fiz um pente-fino profundo focado no seu av.pdf`
*   **Destino:** `state/quarantine/blobs/vps-oracle/`
*   **Tamanho:** ~388 KB
*   **Justificativa Mestre:** Parecer em PDF pesado dentro de `docs/references`. Pelo POP de Quarentena recém-criado, relatórios brutos ou análises densas não devem ficar "escondidos" num repo de hospedagem. Isso gera "dark knowledge". Eles devem ser enviados para a quarentena onde o `state` pode indexá-los ou purgar se desnecessários.
*   **Como reverter:**
    ```bash
    mv '/Users/diego/Documents/GitHub/state/quarantine/blobs/vps-oracle/Diego, fiz um pente-fino profundo focado no seu av.pdf' '/Users/diego/Documents/GitHub/vps-oracle/docs/references/'
    ```

### 3. `.tmp.codex.config.backup.toml`
*   **Caminho Original:** `/Users/diego/Documents/GitHub/vps-oracle/.tmp.codex.config.backup.toml`
*   **Destino:** `state/quarantine/blobs/vps-oracle/`
*   **Tamanho:** ~1 KB
*   **Justificativa Mestre:** Lixo residual de diretórios tmp ou plugins de editor (Codex). Manter backups desempacotados em raiz de repositório de infra levanta potencial vazamento ou conflito.
*   **Como reverter:**
    ```bash
    mv '/Users/diego/Documents/GitHub/state/quarantine/blobs/vps-oracle/.tmp.codex.config.backup.toml' '/Users/diego/Documents/GitHub/vps-oracle/'
    ```

---
*Este manifesto assegura integridade OMEGA para os dados limpos, permitindo "Undo" imediato.*

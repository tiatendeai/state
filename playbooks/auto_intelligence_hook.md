# 🤖 Hook de Inteligência Automática (Jarvis)

Para garantir que a sabedoria do ecossistema seja usada **sem intervenção humana**, o Jarvis (Maestro) segue este protocolo de execução obrigatório:

---

## ⚡ 1. O Gatilho de Injeção (Auto-Load)

Antes de qualquer `tool_call` ou resposta ao usuário:
1.  **Análise de Intenção**: O Jarvis identifica o domínio da tarefa (Tech, Legal, Finance, Business).
2.  **Consulta ao Catálogo**: O Jarvis invoca silenciosamente o `read_file` do `state/registry/catalog.yaml`.
3.  **Injeção de Contexto**: Se a tarefa for "Disparos", o Jarvis **automaticamente** anexa as "Cartas de Princípios" da LGPD e do vOps antes de começar a pensar.

---

## 🛰️ 2. Integração via MCP (Context7)

A automação acontece no nível da infraestrutura:
- **Auto-Skill Detection**: Quando o Jarvis detecta a palavra "SaaS", ele carrega a skill `product-strategy`.
- **Pre-flight Audit**: O agente `vAudit` roda um script em background para checar se o plano de ação condiz com a literatura base. Se não condizer, ele interrompe o fluxo com um `WARNING`.

---

## 📜 3. Manifesto de Gatilhos (`intelligence_triggers.yaml`)

| Palavra-Chave / Contexto | Inteligência Obrigatória | Perfil Ativado |
| :--- | :--- | :--- |
| `disparo`, `broadcast`, `massa` | LGPD + Warmup Playbook | vLegal + vOps |
| `roi`, `viabilidade`, `preço` | *Principles* + *Intelligent Investor* | vCFO |
| `funcionalidade`, `saas`, `design` | *Startup Enxuta* + *Steve Jobs* | vCVO + Eggs |
| `bug`, `erro`, `lento` | *Clean Code* + *Pragmatic Programmer* | vOps |

---

## 🚫 4. Proibição de Esquecimento

Não é opcional. Um agente que ignora o **Ritual de Ativação** é considerado em estado de "Alucinação Operacional" e deve ser reiniciado com o contexto limpo a partir do `STATE`. 

> [!IMPORTANT]
> **A regra é clara**: O conhecimento não é solicitado, ele é **condição sine qua non** para o raciocínio.

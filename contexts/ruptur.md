# Contexto Operacional: RUPTUR

**ID no Ecossistema:** `codex/ruptur`
**Papel Principal:** Motor operacional, orquestração e execução de agentes de IA na infraestrutura TiatendeAI.

---

## 🧭 Diretrizes de Uso (State-First)

Este documento dita a compreensão que qualquer agente deve ter ao interagir com o repositório `ruptur`.

1. **O Ruptur é a Implementation Layer.** Ele não dita as regras globais de pensamento do ecossistema; ele apenas as executa de forma otimizada. Qualquer decisão sobre arquitetura cognitiva deve ser aprovada e registrada aqui em `state` (como em `state/decisions` ou `state/patterns`).
2. **Identidade do Jarvis:** O motor do Jarvis vive no `ruptur`. O `ruptur` aloja seus 20 especialistas e 36 skills (`.agent/agents`, `.agent/skills`). No entanto, o propósito de existir do Jarvis está mapeado pelo `state`.
3. **Descentralização Limitada:** O Jarvis orquestra e coordena times paralelos de agentes. A forma como agentes atuam em união ("Debate", "Subdelegação") segue padrões (ex. `playbooks/multi-agent-debate.md`) estipulados nesta camada canônica.

## 🏗️ Estrutura Crítica do Motor

Agentes que lerem este arquivo encontram no `codex/ruptur`:

- `.agent/ARCHITECTURE.md` - Subordinado a este documento. Mapeia a listagem técnica de skills.
- `ops/jarvis/` - Scripts de orquestração local de infraestrutura e relays diários (`executive_daily_brief.py`).
- `connectome/` - Memória state stateful ("consciência coletiva") operacional da rodada local (session-based).

**Regra de Ouro:** Não altere a configuração letal dos meta-agentes em `ruptur/agents` antes de descrever o impacto técnico e filosófico no diretório `state/decisions/`.

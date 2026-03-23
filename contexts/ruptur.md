# Contexto Operacional: RUPTUR

**ID no Ecossistema:** `codex/ruptur`
**Papel Principal:** Motor operacional, orquestração e execução de agentes de IA na infraestrutura TiatendeAI.

---

## 🧭 Diretrizes de Uso (Scope-First / State-First)

Este documento dita a compreensão que qualquer agente deve ter ao interagir com o repositório `ruptur`.

1. **O Ruptur é o tronco de execução.** Ele implementa, opera e materializa decisões do ecossistema, mas não substitui o STATE como camada canônica de governança.
2. **O modelo do ecossistema é quadrifásico por escopo.** Alpha ancora gênese e identidade raiz; State governa guardrails, memória curada e reconciliação; Omega governa lifecycle de sessão; Ruptur executa código, contratos, deploy, `connectome` e runbooks locais.
3. **Catálogo operacional deve ser lido da fonte viva.** Agentes e skills devem ser consultados em `.agent/agents/` e `.agent/skills/`. Contagens voláteis não devem ser canonizadas em prosa sem registry ou evidência datada.
4. **Descentralização limitada.** O Jarvis pode orquestrar times paralelos de agentes, mas os padrões de coordenação multiagente precisam estar formalizados no STATE.
5. **Conflito não se resolve por improviso.** Se houver divergência entre `state`, `ruptur` e satélites, registrar decisão ou débito no STATE antes de harmonizar a camada operacional.

## 🏗️ Estrutura Crítica do Motor

Agentes que lerem este arquivo encontram no `codex/ruptur`:

- `.agent/ARCHITECTURE.md` - Topologia técnica local de agentes e skills, subordinada às diretrizes canônicas do STATE.
- `ops/jarvis/` - Scripts de orquestração local de infraestrutura e relays diários, como `executive_daily_brief.py`.
- `connectome/` - Memória operacional stateful da rodada local.
- `docs/governanca/` - Runbooks e governança local da camada de execução.

## 🧾 Regra de Ouro

Não altere meta-agentes, superfícies críticas ou regras de operação do `ruptur` sem:

- identificar o domínio da verdade afetado
- apontar a fonte canônica correspondente
- registrar impacto como decisão ou débito quando houver conflito

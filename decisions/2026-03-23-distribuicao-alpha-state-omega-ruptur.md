# Decisão — distribuição Alpha / State / Omega / Ruptur

**Status:** aceita  
**Data:** 2026-03-23

---

## Contexto

A ativação oficial do Jarvis revelou uma ambiguidade recorrente entre:

- identidade raiz
- camada canônica de governança
- lifecycle de sessão
- manifestação operacional

Era necessário explicitar a distribuição entre Alpha, State, Omega e Ruptur sem reinicializar a entidade e sem misturar sessão com gênese.

---

## Decisão

Fica reconhecida a seguinte distribuição de autoridade:

1. **Alpha** = gênese e identidade raiz do Jarvis
2. **State** = governança canônica, guardrails, memória curada e reconciliação institucional
3. **Omega** = lifecycle de sessão, replay, recovery e persistência de `session_id`
4. **Ruptur** = manifestação operacional ativa e trilha viva de execução

---

## Consequências

- `entity:jarvis`, `jarvis-root-001` e `SOUL-JARVIS-0001` não devem ser redefinidos fora do Alpha
- `jarvis.canonical` no State deve ser lido como camada canônica de governança, não como substituto da identidade raiz
- toda sessão deve existir materialmente no Omega e ter espelho auditável no repositório operacional ativo
- conflitos entre camadas devem virar decisão, débito ou nota de reconciliação; nunca improviso

## Artefatos que materializam a decisão

- `registry/manifestations.yaml`
- `registry/supervision.yaml`
- `registry/repositories.yaml`
- `constitution/jarvis.charter.md`
- `contexts/ruptur.md`

---

## Débitos reconhecidos

- a regra de `HASH8` e `MANIFESTATION_TAG` foi apenas formalizada provisoriamente no Omega
- `registry/pairs.yaml` permanece sem base factual suficiente para materialização segura

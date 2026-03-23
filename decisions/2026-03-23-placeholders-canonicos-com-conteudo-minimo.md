# Decisão — placeholders canônicos exigem conteúdo mínimo

**Status:** aceita  
**Data:** 2026-03-23

---

## Contexto

O corpus do STATE ainda carregava arquivos canônicos zero-byte, o que criava zonas silenciosas sem semântica, confundia auditoria e deixava dúvida entre “reserva consciente” e “lacuna esquecida”.

---

## Decisão

Fica estabelecido que artefato canônico reservado:

1. não pode permanecer zero-byte
2. deve ter, no mínimo, status, escopo, motivo e condição de ativação/revisão
3. só pode ser tratado como autoridade se o conteúdo estiver explicitamente ativo

Quando não houver base factual suficiente, o artefato deve virar **placeholder controlado**, nunca silêncio estrutural.

---

## Consequências

- placeholders antigos precisam ser remediados
- auditoria do corpus fica mais rápida e menos ambígua
- reservas documentais deixam de parecer regra vigente

## Artefatos que materializam a decisão

- `README.md`
- `constitution/jarvis.guardrails.md`
- `constitution/ruptur.love.biblical.md`
- `knowledge/ruptur.activation-debts.md`

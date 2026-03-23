# Backlog canônico — Jarvis / automação / autonomia / governança operacional

**Data:** 2026-03-23  
**Status:** backlog canônico inicial  
**Origem:** análise consolidada do ecossistema `alpha` / `state` / `omega` / `codex/ruptur`

---

## 1. Objetivo

Registrar, em trilha canônica, os gaps e oportunidades prioritárias para transformar o Jarvis em um sistema:

- mais autônomo
- mais rastreável
- mais automatizado
- mais observável
- mais seguro para operação contínua

---

## 2. Leitura executiva

O ecossistema já possui base real para:

- identidade raiz (`alpha`)
- governança institucional (`state`)
- lifecycle inicial de sessão (`omega`)
- manifestação operacional viva (`ruptur`)
- perfis operacionais (`ops`, `vcfo`, `vcvo`, `eggs`)
- skill runtime parcial
- workflows GitHub reais
- rollback/deploy reais

Mas ainda não possui, de ponta a ponta, uma malha fechada de:

- automação cross-layer
- telemetria unificada
- auto-incremento seguro do `state`
- bridge forte entre sessão, Git e backlog
- governança de pares/conselhos
- refresh contínuo de RAG / Context7
- restore points institucionais

---

## 3. Backlog priorizado

| ID | Prioridade | Tema | Repositório líder | Board recomendado | Resultado esperado |
|---|---|---|---|---|---|
| JARVIS-AUT-001 | P0 | Autoencerramento auditável de sessões inativas | `omega` | `JARVIS OMEGA - Protocolo Lifecycle Board` | sessões zumbis deixam de permanecer abertas; sessões em uso real não são encerradas |
| JARVIS-AUT-002 | P0 | Canonização cross-layer de `session_id`, heartbeat, stale e closure | `omega` | `JARVIS OMEGA - Protocolo Lifecycle Board` | lifecycle fica determinístico e auditável |
| JARVIS-AUT-003 | P0 | Bridge entre `session_id`, branch, commit, workflow run, issue e Git Project item | `codex/ruptur` | `Ruptur Delivery OS` | rastreabilidade técnica ponta a ponta |
| JARVIS-AUT-004 | P0 | Telemetria unificada do Jarvis, perfis, skills e sessões | `codex/ruptur` | `Ruptur Delivery OS` | decisões e execução passam a gerar evidência operacional estruturada |
| JARVIS-AUT-005 | P0 | Intake pipeline com gate para auto-incremento seguro do `state` | `state` | `Ruptur Delivery OS` | o `state` passa a receber promoção sugerida com reconciliação, sem autoescrita cega |
| JARVIS-AUT-006 | P1 | Refresh de RAG / Context7 / documentação executável | `codex/ruptur` | `Ruptur Delivery OS` | contexto operacional deixa de envelhecer silenciosamente |
| JARVIS-AUT-007 | P0 | Política institucional de backup, restore point e ativação estratégica/frágil | `codex/ruptur` + `omega` + `state` | `Ruptur Delivery OS` | ativações e recoveries deixam de depender de memória manual |
| JARVIS-AUT-008 | P1 | Formalização de `vOps`, `pairs` e eventual conselho/Matusas | `state` | `Ruptur Delivery OS` | expansão de papéis sem colapso ontológico |
| JARVIS-AUT-009 | P1 | Telemetria de eficácia por skill / perfil / tipo de missão | `codex/ruptur` | `Ruptur Delivery OS` | melhoria contínua deixa de ser só percepção subjetiva |
| JARVIS-AUT-010 | P1 | Cobertura mínima de documentação, comentários e trilha auditável para mudanças críticas | `state` + `codex/ruptur` | `Ruptur Delivery OS` | mudanças frágeis passam a sair com contexto e reversibilidade |

---

## 4. Critérios de aceite resumidos por item

## JARVIS-AUT-001 — Autoencerramento auditável de sessões inativas

- `omega` passa a ter sinais formais de liveness
- existe janela de inatividade configurável
- existe estado intermediário (`stale` ou equivalente)
- sessões não ativas de verdade podem ser encerradas automaticamente
- sessões em uso real permanecem abertas

## JARVIS-AUT-002 — Canonização cross-layer do lifecycle

- `session_id` deixa de ser só formato e passa a ser contrato completo
- heartbeat / `last_activity_at` / `closed_at` entram no modelo
- `stale`, `suspenso`, `handoff_pendente` e `closure_reason` ficam formalizados
- artifacts do `omega` e do `ruptur` seguem a mesma semântica

## JARVIS-AUT-003 — Bridge sessão ↔ Git ↔ backlog

- toda sessão consegue apontar para branch, commits, workflow run e item de board
- é possível responder “qual sessão gerou esta mudança?”
- é possível responder “qual item do board originou esta sessão?”

## JARVIS-AUT-004 — Telemetria unificada

- sessão, perfil e skill passam a gerar eventos estruturados
- existe trilha para custo, resultado, bloqueio, risco e duração
- melhora contínua passa a ter base empírica

## JARVIS-AUT-005 — Auto-incremento seguro do `state`

- existe pipeline de intake
- promoção para o `state` é sugerida, validada e reconciliada
- o `state` não é reescrito automaticamente por runtime

## JARVIS-AUT-006 — RAG / Context7 / documentação executável

- fontes operacionais possuem freshness policy
- `CONTEXT7` deixa de envelhecer sem aviso
- docs críticas passam a ter trilha de atualização

## JARVIS-AUT-007 — Backup / restore / ativações frágeis

- existe restore point de sessão
- existe restore point institucional mínimo
- runbooks frágeis passam a exigir plano de retorno

## JARVIS-AUT-008 — vOps / pairs / conselhos

- `vOps` é formalizado ou explicitamente descartado
- `pairs` só nasce com base factual
- conselhos/Matusas só entram com autoridade, escopo e responsabilidade definidos

## JARVIS-AUT-009 — Skill telemetry

- performance por skill e por perfil pode ser medida
- fica possível saber o que ajuda, o que atrapalha e o que deve ser aposentado

## JARVIS-AUT-010 — Doc/comment coverage

- mudanças críticas exigem comentário, runbook ou doc vinculada
- ativações frágeis saem com reversão clara

---

## 5. Riscos que este backlog tenta reduzir

- sessões zumbis
- governança contaminada por verdade volátil
- falta de rastreabilidade entre sessão e Git
- skills sendo usadas sem feedback mensurável
- RAG envelhecendo sem controle
- restore points inexistentes
- perfis e pares surgindo sem ontologia nem accountability

---

## 6. Observação de governança

Este backlog deve ser tratado como:

- backlog de consolidação institucional no `state`
- backlog operacional/tronco no `ruptur`
- backlog de lifecycle no `omega`

O `alpha` participa como âncora de identidade, não como superfície de automação.

---

## 7. Publicação em GitHub Projects

Em 2026-03-23, os itens deste backlog foram publicados nos boards ativos do ecossistema:

| ID | Board | Project Item ID |
|---|---|---|
| JARVIS-AUT-001 | `JARVIS OMEGA - Protocolo Lifecycle Board` | `PVTI_lAHODOO6r84BSQulzgoDflg` |
| JARVIS-AUT-002 | `JARVIS OMEGA - Protocolo Lifecycle Board` | `PVTI_lAHODOO6r84BSQulzgoDflo` |
| JARVIS-AUT-003 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfl4` |
| JARVIS-AUT-004 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfl8` |
| JARVIS-AUT-005 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfmg` |
| JARVIS-AUT-006 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfm4` |
| JARVIS-AUT-007 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfnI` |
| JARVIS-AUT-008 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfnY` |
| JARVIS-AUT-009 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfnw` |
| JARVIS-AUT-010 | `Ruptur Delivery OS` | `PVTI_lAHODOO6r84BRgVSzgoDfoI` |

Critério aplicado na publicação:

- `Status = Todo` para todos os itens recém-publicados
- classificação econômica aplicada no `Ruptur Delivery OS` conforme o tipo de débito/oportunidade
- backlog institucional continua canônico no `state`; os boards são espelhos operacionais de execução e priorização

# STATE — TiatendeAI

Este repositório é a **fonte canônica de governança, contexto, memória e capital intelectual** do ecossistema TiatendeAI.

---

## 🎯 Objetivo

Centralizar, versionar e tornar consultável:

- regras e princípios de operação
- contexto dos sistemas e repositórios
- decisões arquiteturais
- padrões e playbooks
- memória curada e reutilizável
- conhecimento acumulado
- mapa do ecossistema

---

## 🧠 Papel do STATE

O STATE não é código de produto.

Ele é a camada que:

- orienta IDEs, agentes e operadores humanos
- fornece contexto antes da execução
- consolida aprendizados
- evita duplicidade de conhecimento
- mantém coerência entre sistemas

---

## ⚠️ Regras fundamentais

- Código permanece nos repositórios próprios
- STATE não é dump de notas
- Tudo deve ser estruturado, versionado e rastreável
- Nem todo aprendizado vira padrão
- Promoção de conhecimento deve ser curada e validada
- Conhecimento deve ter origem, contexto e responsabilidade definidos

---

## 🧭 Hierarquia de confiança

1. Código e contratos ativos do sistema
2. Contexto local da tarefa
3. Decisões registradas (decisions/)
4. Contextos por repositório (contexts/)
5. Padrões e playbooks
6. Memória e knowledge
7. Fontes externas

### Em caso de conflito:
Sempre priorizar código real e contratos ativos sobre documentação ou memória.

---

## 🔁 Ciclo operacional

Contexto → Entendimento → Ação → Validação → Capitalização → Evolução

---

## 🧠 Tipos de conhecimento

Todo conteúdo deve ser classificado como:

- observação → algo percebido, não validado
- hipótese → ideia a ser testada
- decisão → escolha feita com justificativa
- padrão → forma validada de resolver algo recorrente
- playbook → procedimento operacional
- ativo reutilizável → solução pronta para reuso
- black library → ativo de alto valor validado

---

## 🏗️ Contexto operacional

Sempre considerar:

- runtime (ambiente, serviços, filas, integrações)
- contratos ativos (APIs, eventos, schemas)
- dependências reais entre sistemas
- estado atual do ecossistema

---

## 🤖 Uso por agentes (Jarvis, Codex, etc)

### Antes de iniciar qualquer tarefa relevante:

- consultar STATE
- entender contexto do ecossistema
- identificar padrões e decisões existentes

### Durante a execução:

- usar STATE como referência
- evitar duplicação de lógica ou estrutura
- respeitar arquitetura existente
- não contradizer decisões registradas sem justificativa

### Após execução:

- registrar aprendizados relevantes
- classificar corretamente o tipo de conhecimento
- propor promoção quando houver recorrência ou valor claro

---

## 🧱 Estrutura

- constitution/ → princípios e regras
- ecosystem/ → mapa do ecossistema
- contexts/ → contexto por repositório
- decisions/ → decisões arquiteturais
- patterns/ → padrões reutilizáveis
- playbooks/ → modos de operação
- memory/ → memória curada
- knowledge/ → descobertas e aprendizados
- registry/ → indexação estruturada
- templates/ → padrões de criação

---

## 🧩 Governança de conhecimento

- nem todo conteúdo pode ser promovido
- promoção exige validação
- evitar duplicidade entre arquivos
- manter rastreabilidade (origem, data, contexto)
- revisar e atualizar periodicamente
- descartar ou arquivar o que não faz mais sentido

---

## 🔄 Evolução contínua

O STATE deve ser mantido como sistema vivo:

- revisão periódica de relevância
- consolidação de padrões recorrentes
- identificação de obsolescência
- adaptação à evolução do ecossistema

---

## 🚀 Direção

Este repositório deve evoluir continuamente como:

> sistema vivo de inteligência, governança e capital intelectual do ecossistema

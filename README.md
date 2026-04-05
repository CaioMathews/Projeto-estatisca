# 📊 Análise de Risco de Crédito — German Credit Data

Projeto de análise exploratória de dados (EDA) sobre um dataset de crédito alemão, com foco na investigação estatística de hipóteses relacionadas ao perfil de inadimplência dos clientes.

---

## 📁 Estrutura do Projeto

```
├── Main.ipynb                  # Notebook principal com todas as análises
├── Dataset/
│   └── german_credit_data.csv  # Dataset utilizado
└── Funcoes/
    ├── Funcoes_medidas.py       # Funções de medidas descritivas (média, mediana, moda)
    ├── Funcoes_analises.py      # Funções de análise por coluna e correlação de Spearman
    └── Funcoes_tratar.py        # Funções de limpeza e tratamento dos dados
```

---

## 🗃️ Dataset

**German Credit Data** — dataset clássico de avaliação de risco de crédito contendo 1.000 registros de clientes com atributos financeiros e socioeconômicos.

### Principais colunas

| Coluna | Descrição |
|---|---|
| `Age` | Idade do cliente |
| `Duration` | Prazo do empréstimo (em meses) |
| `Credit amount` | Valor do crédito solicitado |
| `Purpose` | Finalidade do empréstimo |
| `Housing` | Tipo de moradia (`own`, `free`, `rent`) |
| `Saving accounts` | Saldo em conta poupança |
| `Checking account` | Saldo em conta corrente |
| `Job` | Nível de qualificação profissional |
| `Risk` | Classificação de risco (`good` / `bad`) |

---

## ⚙️ Pré-processamento

O tratamento dos dados inclui as seguintes etapas:

- **Remoção de duplicatas** via `remover_duplicados()`
- **Mapeamento da coluna `Job`**: valores numéricos (0→3) convertidos para strings legíveis (`unskilled`, `skilled`, etc.)
- **Preenchimento de NaN**: `Saving accounts` (183 valores ausentes) e `Checking account` (394 valores ausentes) preenchidos com `'No account'`
- **Normalização Min-Max** de `Credit amount` → criação da coluna `Credit amount_normalizado`
- **Criação de `Risk_num`**: conversão `good → 0` e `bad → 1` para cálculos de correlação

---

## 📐 Análises Gerais

### Distribuição da Duração dos Empréstimos

| Medida | Valor |
|---|---|
| Média | 20,90 meses |
| Mediana | 18,00 meses |

A média superior à mediana indica **assimetria à direita** — uma minoria de empréstimos com prazos muito longos puxa a média para cima. O valor da mediana (18 meses) é usado como ponto de corte na Hipótese 4.

### Matriz de Correlação de Spearman (variáveis numéricas)

| Par | Correlação |
|---|---|
| Duration ↔ Credit amount | **0,6247** (forte) |
| Age ↔ Duration | -0,036 (desprezível) |
| Age ↔ Credit amount | 0,026 (desprezível) |

A correlação significativa entre prazo e valor do crédito apoia a análise da Hipótese 4.

---

## 🔬 Hipóteses Analisadas

### Hipótese 1 — Valor do Crédito e Inadimplência

> *"Valores elevados de crédito estão positivamente correlacionados com o aumento da inadimplência."*

**Método:** Boxplot comparativo + Correlação de Spearman entre `Credit amount_normalizado` e `Risk_num`.

**Resultado:** Correlação = **0,0871** — direção correta (positiva), mas magnitude quase nula.

**Conclusão:** ⚠️ **Parcialmente defendida.** O valor do crédito isolado não é um preditor relevante de inadimplência.

---

### Hipótese 2 — Faixa Etária e Inadimplência

> *"Clientes jovens tendem a ter uma taxa de inadimplência maior do que os outros."*

**Método:** Segmentação por `pd.cut()` em 4 faixas etárias + cálculo da taxa de inadimplência por grupo.

| Faixa Etária | Taxa de Inadimplência |
|---|---|
| Jovem (18–25) | **42,11%** |
| Jovem Adulto (26–35) | 29,65% |
| Adulto (36–50) | 23,75% |
| Idoso (50+) | 27,43% |

**Conclusão:** ✅ **Defendida.** Clientes jovens apresentam taxa de inadimplência 12 pontos percentuais acima da média geral (30%).

---

### Hipótese 3 — Finalidade do Empréstimo e Risco

> *"Empréstimos para 'Educação' possuem um risco maior do que para Negócios."*

**Método:** `countplot` com distribuição de risco por categoria de finalidade (`Purpose`), com anotação percentual por barra.

**Conclusão:** ❓ **Inconclusiva.** A análise visual mostra distribuição absoluta, mas a comparação de risco *relativo* entre categorias requer cálculo de taxa por grupo, o que não foi conclusivo nesta análise.

---

### Hipótese 4 — Baixa Reserva Financeira + Prazo Longo

> *"A combinação de baixa reserva financeira com prazos longos potencializa o risco de crédito de forma não linear."*

**Método:** Filtragem de clientes com `Checking account == 'little'` + comparação da inadimplência entre empréstimos de prazo curto (<18m) e longo (≥18m).

**Conclusão:** Análise segmentada mostra o impacto combinado de saldo baixo e prazo longo sobre o risco, com visualização via `catplot` com facetas por duração.

---

### Hipótese 5 — Proprietários de Imóvel e Crédito Acima da Média

> *"Clientes com casa própria mantêm um perfil de bom pagador mesmo quando solicitam crédito acima da média."*

**Método:** Filtragem de clientes com `Housing == 'own'` + segmentação binária do valor do crédito em relação à média global (R$ 3.271,26) + comparação das taxas de inadimplência.

**Conclusão:** Análise compara a taxa de inadimplência de proprietários para pedidos abaixo e acima da média, avaliando se a posse do imóvel funciona como fator protetivo independente do valor solicitado.

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **pandas** — manipulação e análise de dados tabulares
- **seaborn** — visualizações estatísticas
- **matplotlib** — geração e customização de gráficos
- Módulos customizados em `Funcoes/`:
  - `Funcoes_medidas` — média, mediana e moda
  - `Funcoes_analises` — análise descritiva por coluna e correlação de Spearman
  - `Funcoes_tratar` — limpeza, normalização e mapeamento de dados

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Instale as dependências:
   ```bash
   pip install pandas seaborn matplotlib
   ```

3. Execute o notebook:
   ```bash
   jupyter notebook Main.ipynb
   ```

> **Observação:** certifique-se de que o arquivo `Dataset/german_credit_data.csv` e a pasta `Funcoes/` estão no mesmo diretório que o `Main.ipynb`.

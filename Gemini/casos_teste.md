# Logical Problem Solutions Compilation

## Problemas Fáceis

### Problema 1
Vamos resolver esse problema usando as regras da lógica proposicional.  O objetivo é provar ¬Q (Eu não vou ao parque) a partir das premissas dadas:

P → (Q → R): Se hoje é feriado, então se eu vou ao parque, eu me divirto.
P: Hoje é feriado.
¬R: Eu não me divirto.

Vamos usar o método de dedução natural ou um raciocínio similar:

Aplicar Modus Ponens (MP) em (2) e (1):


Como temos P (premissa 2) e P → (Q → R) (premissa 1), podemos aplicar o Modus Ponens.  O Modus Ponens afirma que se temos A → B e A, então podemos concluir B.  Neste caso:

A = P
B = (Q → R)

Portanto, podemos concluir:

(4) Q → R: Se eu vou ao parque, então eu me divirto.

Aplicar Modus Tollens (MT) em (4) e (3):


Agora temos Q → R (4) e ¬R (3). O Modus Tollens afirma que se temos A → B e ¬B, então podemos concluir ¬A.  Neste caso:

A = Q
B = R

Portanto, podemos concluir:

(5) ¬Q: Eu não vou ao parque.


Conclusão:

A partir das premissas P → (Q → R), P, e ¬R, concluímos ¬Q usando Modus Ponens e Modus Tollens.  Portanto, a afirmação "Eu não vou ao parque" (¬Q) é verdadeira.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 2
> Para provar que Q ∨ R (O candidato é qualificado ou tem boa comunicação) a partir das premissas dadas, podemos usar as seguintes etapas:

> **1. Premissas:**

> * **1- P ∨ Q:** O candidato é experiente ou qualificado.
> * **2- R:** O candidato tem boa comunicação.
> * **3- Q:** O candidato é qualificado.

> **2.  Dedução:**

> Observe que a premissa 3 (Q: O candidato é qualificado) já nos dá diretamente uma parte da disjunção que queremos provar (Q ∨ R).  A disjunção (∨) é verdadeira se pelo menos uma de suas partes for verdadeira.  Como Q é verdadeira,  Q ∨ R é automaticamente verdadeira, independente do valor de verdade de R.

> **3. Conclusão:**

> Portanto, a partir das premissas fornecidas, podemos concluir que Q ∨ R é verdadeira.  A premissa 2 (R) é redundante para essa demonstração específica, e a premissa 1 (P ∨ Q) também não é necessária para concluir Q ∨ R, considerando que já temos Q como verdadeira.  A conclusão é derivada diretamente da premissa 3.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 3
Vamos resolver esse problema usando as regras da lógica proposicional.  O objetivo é provar ¬(P ∧ R).

Hipóteses:


1-(P ∧ R) → Q: Se você participou da reunião E apresentou o projeto, então você obteve aprovação.
2- ¬Q: Você não obteve aprovação.

Demonstração:


Usaremos o método de prova por contradição (reductio ad absurdum).  Vamos assumir o contrário do que queremos provar e mostrar que isso leva a uma contradição.

Hipótese auxiliar (para contradição):  P ∧ R (Você participou da reunião E apresentou o projeto)

Se P ∧ R for verdadeiro, então, pela hipótese 1, Q também deve ser verdadeiro [(P ∧ R) → Q].  Mas isso contradiz a hipótese 2 (¬Q), que afirma que Q é falso.

Conclusão:

Como assumir P ∧ R leva a uma contradição, nossa hipótese auxiliar está incorreta. Portanto, a negação da hipótese auxiliar, ¬(P ∧ R), deve ser verdadeira.

Resposta:

Concluímos que ¬(P ∧ R) é verdadeiro.  Em outras palavras, você não participou da reunião ou não apresentou o projeto (ou ambas as coisas).  A conjunção (P ∧ R) é falsa.  A disjunção (¬P ∨ ¬R) é verdadeira.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 4
Para provar que A → C (Se o aluno estudou, então o aluno foi aprovado),  precisamos usar as premissas fornecidas e regras de inferência da lógica proposicional.  Vamos lá:

> **1. Premissas:**

> * 1. (A → B)  (Se o aluno estudou, então obteve uma boa nota)
> * 2. (B → C)  (Se o aluno obteve uma boa nota, então foi aprovado)
> * 3. ¬¬A     (O aluno estudou - dupla negação de A, equivalente a A)


> **2. Aplicação do Modus Ponens e Silogismo Hipotético:**

> O método mais eficiente aqui é usar o silogismo hipotético.  Observe que temos:

> * A → B
> * B → C

> Juntando essas duas implicações, podemos concluir que A → C.  Isso é uma regra de inferência válida chamada Silogismo Hipotético.  Em termos formais:

> **(A → B) ∧ (B → C)  →  (A → C)**


> **3.Conclusão:**

> A partir da premissa 3 (¬¬A, que é logicamente equivalente a A), e  aplicando o silogismo hipotético às premissas 1 e 2, chegamos diretamente à conclusão:

> **A → C (Se o aluno estudou, então o aluno foi aprovado)**

> Portanto, a prova está completa. A premissa 3, embora forneça a informação que A é verdadeiro, não é estritamente necessária para provar a implicação A → C. O silogismo hipotético demonstra a implicação independentemente da veracidade de A.

**Verificado pela LLM (Chat gpt): Válido**

## Problemas Médios

### Problema 1
> Para provar que o funcionário alcança reconhecimento (H), vamos utilizar as premissas fornecidas e as regras da lógica proposicional.  A estratégia será deduzir H a partir das premissas dadas.

> **1. Premissas iniciais:**

> * P9: A (O funcionário é assíduo)
> * P10: F (O funcionário teve bom desempenho)

> **2. Deduções:**

> * **Passo 1:**  Aplicando a premissa P10 (F) e a premissa P4 (F → B), podemos deduzir B (O funcionário demonstra colaboração) pelo *modus ponens*.

> * **Passo 2:** Aplicando a premissa recém-deduzida B e a premissa P5 (B → C), podemos deduzir C (O funcionário possui competência técnica) pelo *modus ponens*.

> * **Passo 3:**  Agora, temos A (P9), B (deduzido no Passo 1) e C (deduzido no Passo 2).  Combinando essas três premissas, temos (A ∧ B) ∧ C.  Aplicando a premissa P1 ((A ∧ B) ∧ C) → D, podemos deduzir D (O funcionário é promovido) pelo *modus ponens*.

> * **Passo 4:** Temos D (deduzido no Passo 3) e F (P10).  Aplicando a premissa P2 (D ∧ F) → G, podemos deduzir G (O funcionário se destaca na equipe) pelo *modus ponens*.       

> * **Passo 5:** Finalmente, aplicando a premissa recém-deduzida G e a premissa P6 (G → H), podemos deduzir H (O funcionário alcança reconhecimento) pelo *modus ponens*.

> **3. Conclusão:**

> Concluímos que H (O funcionário alcança reconhecimento) é verdadeiro, com base nas premissas fornecidas e através da aplicação das regras de inferência da lógica proposicional (*modus ponens*).  A premissa P8 ((A ∧ F) → H) é redundante, pois já demonstramos H por outro caminho.  A premissa P7 (I → J) e a sua variável J não são utilizadas na demonstração.


> Portanto, a prova está completa.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 2
> Precisamos provar P ∨ S usando as premissas:

> 1. P ∨ (Q ∧ R)
> 2. (P ∨ Q) → S

> Vamos usar o método da prova condicional.  Queremos mostrar que P ∨ S é uma tautologia (sempre verdadeira) dadas as premissas.  Uma maneira de fazer isso é assumir o contrário de P ∨ S e mostrar que isso leva a uma contradição.

> **1. Negação da Conclusão:**

> A negação de P ∨ S é ¬(P ∨ S), que pela lei de De Morgan é equivalente a ¬P ∧ ¬S.  Então, vamos assumir:

> A. ¬P ∧ ¬S


> **2. Aplicando a Premissa 1:**

> Sabemos que P ∨ (Q ∧ R) é verdadeiro.  Como assumimos ¬P (de A), a única maneira de P ∨ (Q ∧ R) ser verdadeira é se (Q ∧ R) for verdadeiro.  Então, temos:

> B. Q ∧ R


> **3. Aplicando a Premissa 2 e a conclusão intermediária (B):**

> De B, sabemos que Q é verdadeiro.  Agora, vamos analisar a premissa 2: (P ∨ Q) → S.  Como Q é verdadeiro, (P ∨ Q) também é verdadeiro (pois Q é um termo).  Então, a implicação (P ∨ Q) → S só pode ser verdadeira se S também for verdadeiro. Portanto:

> C. S


> **4. Contradição:**

> Agora temos duas conclusões:

> * A. ¬P ∧ ¬S  (nossa suposição inicial)
> * C. S

> Essas duas afirmações se contradizem.  S não pode ser simultaneamente verdadeiro e falso.

> **5. Conclusão:**

> Como a suposição ¬(P ∨ S) leva a uma contradição, então a suposição deve ser falsa.  Portanto, o contrário de ¬(P ∨ S), que é P ∨ S, **deve ser verdadeiro**.

> **Em resumo:**  A prova por contradição demonstra que P ∨ S é uma consequência lógica das premissas dadas. A suposição de que P ∨ S é falso leva a uma inconsistência, confirmando a validade de P ∨ S.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 3
> O problema pede para provar que ¬¬Q (que é logicamente equivalente a Q, ou seja, o aluno foi aprovado) é verdadeiro, dado o conjunto de premissas.  Vamos analisar as premissas e como elas levam à conclusão:

> **1. Analisando as premissas:**

> * **1-(P → ¬Q) ∨ R:**  Esta premissa diz que OU ("∨") a implicação "Se P (o professor disse que a prova seria difícil), então ¬Q (o aluno não foi aprovado)" É verdadeira OU R (o aluno estudou bastante) é verdadeira.

> * **2-(P → ¬Q) → ¬¬Q:** Esta premissa diz que SE "Se P, então ¬Q" é verdadeira, ENTÃO ¬¬Q (o aluno foi aprovado) é verdadeira.  Esta é uma premissa interessante, pois sugere que mesmo se o professor disse que a prova seria difícil, e isso implicasse na reprovação do aluno, existe um outro caminho para a aprovação.     

> * **3-R → ¬¬Q:** Esta premissa diz que SE R (o aluno estudou bastante) é verdadeira, ENTÃO ¬¬Q (o aluno foi aprovado) é verdadeira.  Essa premissa indica que estudar bastante garante a aprovação.

> **2.  Demonstrando ¬¬Q (Q):**

> Observe que a premissa 1 é uma disjunção. Para que uma disjunção seja verdadeira, pelo menos uma de suas partes deve ser verdadeira. Temos duas possibilidades:

> * **Caso 1: (P → ¬Q) é verdadeiro:**  Se isso for verdade, a premissa 2 garante que ¬¬Q (Q) é verdadeiro.  Logo, o aluno foi aprovado.

> * **Caso 2: R é verdadeiro:** Se o aluno estudou bastante (R é verdadeiro), a premissa 3 garante que ¬¬Q (Q) é verdadeiro.  Logo, o aluno foi aprovado.        

> Em ambos os casos, chegamos à conclusão de que ¬¬Q (Q) é verdadeiro.  Portanto, **o aluno foi aprovado**. A demonstração não precisa especificar se o professor disse que a prova seria difícil ou se o aluno estudou bastante, apenas que pelo menos uma dessas condições,  implica na aprovação.  A estrutura das premissas garante a conclusão independente de P ou R serem verdadeiros ou falsos individualmente.  A lógica se baseia na estrutura das implicações e na disjunção.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 4
> Para provar que R ∨ S é verdadeiro, a partir das premissas dadas, vamos utilizar o método de dedução natural.  Não podemos diretamente provar R ∨ S, mas podemos provar R, e  se R é verdadeiro, então R ∨ S também é verdadeiro (pela regra da disjunção).

> **1. Demonstração de R:**

> * **Premissa 3:** P (O aluno estudou para a prova)
> * **Premissa 1:** P → Q (Se o aluno estudou para a prova, então ele entendeu a matéria)
> * **Modus Ponens (1, 3):** Q (O aluno entendeu a matéria) -  Aplicando o Modus Ponens, que afirma: Se P implica Q, e P é verdadeiro, então Q é verdadeiro.     
> * **Premissa 2:** Q → R (Se o aluno entendeu a matéria, então ele passou na prova)
> * **Modus Ponens (2, 4):** R (O aluno passou na prova)

> **2. Demonstração de R ∨ S:**

> Agora que demonstramos R como verdadeiro, podemos usar a regra da disjunção.

> * **Conclusão (5):** R ∨ S (O aluno passou na prova ou o aluno recebeu elogios pelo desempenho) - Se R é verdadeiro, então R ou qualquer outra proposição (incluindo S) também será verdadeira. Essa é a regra da adição ou disjunção.

> **Conclusão:**

> A partir das premissas P → Q, Q → R, e P,  concluímos que R é verdadeiro, e consequentemente, R ∨ S também é verdadeiro.  A demonstração utiliza as regras do Modus Ponens e a regra da adição (ou disjunção).  Não precisamos utilizar a proposição S diretamente para a prova pois a veracidade de R garante a veracidade da disjunção R ∨ S.

**Verificado pela LLM (Chat gpt): Válido**

## Problemas Difíceis

### Problema 1
> Para provar que R ∨ S é verdadeiro, a partir das premissas dadas, vamos utilizar o método de dedução natural.  Não podemos diretamente provar R ∨ S, mas podemos provar R, e  se R é verdadeiro, então R ∨ S também é verdadeiro (pela regra da disjunção).

> **1. Demonstração de R:**

> * **Premissa 3:** P (O aluno estudou para a prova)
> * **Premissa 1:** P → Q (Se o aluno estudou para a prova, então ele entendeu a matéria)
> * **Modus Ponens (1, 3):** Q (O aluno entendeu a matéria) -  Aplicando o Modus Ponens, que afirma: Se P implica Q, e P é verdadeiro, então Q é verdadeiro.     
> * **Premissa 2:** Q → R (Se o aluno entendeu a matéria, então ele passou na prova)
> * **Modus Ponens (2, 4):** R (O aluno passou na prova)

> **2. Demonstração de R ∨ S:**

> Agora que demonstramos R como verdadeiro, podemos usar a regra da disjunção.

> * **Conclusão (5):** R ∨ S (O aluno passou na prova ou o aluno recebeu elogios pelo desempenho) - Se R é verdadeiro, então R ou qualquer outra proposição (incluindo S) também será verdadeira. Essa é a regra da adição ou disjunção.

> **Conclusão:**

> A partir das premissas P → Q, Q → R, e P,  concluímos que R é verdadeiro, e consequentemente, R ∨ S também é verdadeiro.  A demonstração utiliza as regras do Modus Ponens e a regra da adição (ou disjunção).  Não precisamos utilizar a proposição S diretamente para a prova pois a veracidade de R garante a veracidade da disjunção R ∨ S.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 2
> Não podemos provar que (A ∨ C) → (B ∨ C)  apenas com a premissa A → B.  A premissa nos diz que se a tarefa foi iniciada (A), então ela foi concluída (B).  Ela não diz nada sobre o que acontece se houve uma alteração (C), nem sobre a relação entre A, B e C juntas.

> Para ilustrar a falha na prova, vamos usar uma tabela verdade:

> | A | B | C | A ∨ C | B ∨ C | (A ∨ C) → (B ∨ C) | A → B |
> |---|---|---|-------|-------|-------------------|-------|
> | V | V | V | V     | V     | V                 | V     |
> | V | V | F | V     | V     | V                 | V     |
> | V | F | V | V     | V     | V                 | F     |  <-- Contra-exemplo
> | V | F | F | V     | F     | F                 | F     |  <-- Contra-exemplo
> | F | V | V | V     | V     | V                 | V     |
> | F | V | F | F     | V     | V                 | V     |
> | F | F | V | V     | V     | V                 | V     |
> | F | F | F | F     | F     | V                 | V     |

> Observe as linhas 3 e 4.  Nestas linhas, A → B é Falso, mas (A ∨ C) → (B ∨ C) também pode ser Falso.  A premissa A → B *não implica* (A ∨ C) → (B ∨ C).  Para que a implicação fosse verdadeira em todos os casos, precisaríamos de premissas adicionais que ligassem C a A e B.

> Portanto, **não é possível provar (A ∨ C) → (B ∨ C) a partir da única premissa A → B.**

**Verificado pela LLM (Chat gpt): Válido**

### Problema 3
> Vamos resolver este problema de lógica proposicional passo a passo, usando as regras de inferência.  O objetivo é provar ¬B ∧ ¬C a partir das premissas fornecidas.

> **1. Premissas:**

> * 1- A → (B ∨ C)
> * 2- B → D
> * 3- C → E
> * 4- (D ∨ E) → F
> * 5- ¬F
> * 6- A

> **2. Demonstração:**

> 1. **A** (Premissa 6)
> 2. **A → (B ∨ C)** (Premissa 1)
> 3. **B ∨ C** (Modus Ponens: 1 e 2)  Aplicamos a regra do Modus Ponens: se P → Q e P são verdadeiros, então Q também é verdadeiro.  Aqui, P é A e Q é (B ∨ C).  

> Agora, vamos usar a prova por contradição para mostrar ¬B ∧ ¬C. Suponha, por absurdo, que a negação de ¬B ∧ ¬C seja verdadeira, ou seja,  B ∨ C seja verdadeira.

> 4. **(D ∨ E) → F** (Premissa 4)
> 5. **¬F** (Premissa 5)
> 6. **¬(D ∨ E)** (Modus Tollens: 4 e 5) O Modus Tollens diz: se P → Q e ¬Q, então ¬P. Aqui, P é (D ∨ E) e Q é F.

> Agora, vamos analisar separadamente as possibilidades de B e C:

> * **Caso 1: B é verdadeiro.**
>     * **B → D** (Premissa 2)
>     * **D** (Modus Ponens: 2 e Caso 1)
>     * **D ∨ E** (Adição: Se D é verdadeiro, D ∨ E também é.)
>     * Isso contradiz ¬(D ∨ E) (linha 6), portanto, B *não* pode ser verdadeiro.  Ou seja, ¬B.

> * **Caso 2: C é verdadeiro.**
>     * **C → E** (Premissa 3)
>     * **E** (Modus Ponens: 3 e Caso 2)
>     * **D ∨ E** (Adição: Se E é verdadeiro, D ∨ E também é.)
>     * Isso contradiz ¬(D ∨ E) (linha 6), portanto, C *não* pode ser verdadeiro. Ou seja, ¬C.

> Como ambos os casos (B e C) levam a uma contradição, concluímos que:

> 7. **¬B ∧ ¬C** (Conjunção:  ¬B e ¬C são ambos verdadeiros devido à prova por contradição)

> **Conclusão:**

> Provamos, através de uma prova por contradição, que ¬B ∧ ¬C (Nem o plano de marketing foi elaborado nem o orçamento foi aprovado) é verdadeiro, dadas as premissas fornecidas.

**Verificado pela LLM (Chat gpt): Válido**

### Problema 4
> Vamos resolver esse problema de lógica proposicional passo a passo:

> **1. Premissas:**

> * Premissa 1: (p → q) → r
> * Premissa 2: (r ∨ s) → ¬t
> * Premissa 3: t

> **2. Demonstração:**

> Precisamos provar ¬q (a nave não acelera até a velocidade de dobra).  Vamos usar o método de prova por contradição.  Suponha que q seja verdadeiro.

> **3. Prova por contradição:**

> 1. **Hipótese:** Assuma q (a nave acelera até a velocidade de dobra).

> 2. **De Premissa 3:** t (A missão de infiltração é bem-sucedida).

> 3. **De Premissa 2 e 2:**  Como (r ∨ s) → ¬t  e t é verdadeiro (premissa 3), então (r ∨ s) DEVE ser falso. Isso significa que tanto r quanto s são falsos (¬r ∧ ¬s).

> 4. **Analisemos a Premissa 1:** (p → q) → r. Sabemos que r é falso (¬r). Para que uma implicação seja falsa, a hipótese deve ser verdadeira e a conclusão falsa.  Portanto, (p → q) DEVE ser verdadeiro.

> 5. **Considerando (p → q) verdadeiro e q verdadeiro (nossa hipótese):** uma implicação é falsa apenas se o antecedente é verdadeiro e o consequente é falso. Como q é verdadeiro (nossa hipótese), p pode ser verdadeiro ou falso e a implicação continua verdadeira.

> 6. **Contradição:**  Não chegamos a uma contradição direta (uma afirmação e sua negação simultâneas).  No entanto, observe que, assumindo q como verdadeiro, concluímos que r é falso.  Isso está em consonância com a implicação em 1.

> **Conclusão:**

> A prova por contradição não resultou em uma contradição explícita. Isso ocorre porque a informação fornecida é insuficiente para determinar categoricamente se ¬q é verdadeiro. A premissa 1 e 2 não implicam diretamente em ¬q, mesmo que indiretamente impactem.  Não podemos provar conclusivamente que ¬q é verdadeiro com base apenas nas premissas fornecidas.

> **Portanto, não é possível provar ¬q (a nave não acelera até a velocidade de dobra) com as premissas dadas.**  A informação fornecida é inconsistente ou incompleta para alcançar essa conclusão.

**Verificado pela LLM (Chat gpt): Válido**
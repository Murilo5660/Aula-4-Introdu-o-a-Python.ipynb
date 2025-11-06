# Documentação do repositório

1. Este código reúne quatro pequenos programas em Python, desenvolvidos em diferentes **aulas práticas**, com o objetivo de aprender conceitos básicos de **variáveis, operações matemáticas, entradas e condições**.

---

## Objetivo

Compreender o funcionamento de comandos fundamentais do Python:

* Exibição de mensagens com `print()` e *f-strings*
* Declaração e soma de variáveis
* Entrada de dados com `input()`
* Uso de operadores matemáticos (`+`, `//`)
* Estrutura condicional `if/else`

---

## Passos realizados

### **Aula 1 – Impressão de mensagens**

1. Exibe uma frase inicial no console:

   ```python
   print("I Competição de Programação da Start")
   ```
2. Cria uma variável `ano` com o valor `"II"` e mostra a frase com ela:

   ```python
   ano = "II"
   print(ano, "Competição de Programação da Start")
   print(f"{ano} Competição de Programação da Start")
   ```

**Aprendizado:** Uso de variáveis e f-strings (`f"{variavel}"`) para formatar textos dinamicamente.

---

### **Aula 2 – Soma de pontos**

1. Define a quantidade de livros lidos por categoria:

   ```python
   livro_ficcao = 10
   livro_nficcao = 8
   livro_infantil = 6
   ```
2. Soma os pontos de Rodrigo e exibe o resultado:

   ```python
   pontos_rodrigo = livro_ficcao + livro_nficcao + livro_infantil
   print(f"Os pontos totais do Rodrigo são: {pontos_rodrigo}")
   ```

**Aprendizado:** Uso de operadores matemáticos e variáveis numéricas.

---

### **Aula 3 – Divisão de figurinhas**

1. Solicita dados ao usuário:

   ```python
   total_figurinhas = int(input("Digite o total de figurinhas: "))
   numero_amigos = int(input("Digite o número de amigos: "))
   ```
2. Calcula a divisão das figurinhas:

   * Cada amigo recebe uma parte igual.
   * João recebe o dobro.

   ```python
   figurinhas_amigos = total_figurinhas // (numero_amigos + 2)
   figurinhas_joao = 2 * figurinhas_amigos
   print(f"João recebeu {figurinhas_joao} figurinhas.")
   ```

**Aprendizado:** Entrada de dados com `input()`, uso de `int()` para conversão e divisão inteira com `//`.

---

### **Aula 4 – Controle de excursão escolar**

1. Pede a quantidade de alunos e monitores:

   ```python
   numero_alunos = int(input("Digite a quantidade de alunos: "))
   numero_monitores = int(input("Digite a quantidade de monitores: "))
   ```
2. Verifica se o grupo pode ir ao passeio:

   ```python
   if numero_alunos + numero_monitores <= 50:
       print("Pode ir")
   else:
       print("Não pode ir")
   ```

**Aprendizado:** Estrutura condicional `if/else` e comparação de valores.

---

## Dificuldades

1. Entender a diferença entre `print()` simples e f-string (`f"{variavel}"`).
2. Saber quando usar `int()` ao ler entradas com `input()`.
3. Compreender a diferença entre divisão normal `/` e **divisão inteira** `//`.
4. Montar corretamente uma condição com `if/else`.

---

## Exemplo de saída (Aula 3 e 4)

```
Digite o total de figurinhas: 60
Digite o número de amigos: 4
João recebeu 20 figurinhas.

Digite a quantidade de alunos: 48
Digite a quantidade de monitores: 2
Pode ir
```

---


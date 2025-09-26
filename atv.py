#aula1

print("I Competição de Programação da Start")

ano = "II"
print(ano, "Competição de Programação da Start")

print(f"{ano} Competição de Programação da Start")
#aula2

livro_ficcao = 10
livro_nficcao = 8
livro_infantil = 6

pontos_rodrigo = livro_ficcao + livro_nficcao + livro_infantil

print(f"Os pontos totais do Rodrigo são: {pontos_rodrigo}")

#aula3

total_figurinhas = int(input("Digite o total de figurinhas: "))
numero_amigos = int(input("Digite o número de amigos: "))

figurinhas_amigos = total_figurinhas // (numero_amigos + 2)
figurinhas_joao = 2 * figurinhas_amigos

print(f"João recebeu {figurinhas_joao} figurinhas.")

#aula4

numero_alunos = int(input("Digite a quantidade de alunos: "))
numero_monitores = int(input("Digite a quantidade de monitores: "))
resposta_positiva = "Pode ir"
resposta_negativa = "Não pode ir"

if numero_alunos + numero_monitores <= 50:
  print(resposta_positiva)
else:
  print(resposta_negativa)
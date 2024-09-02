from time import sleep
import random

class Questao:

    def __init__(self, texto,alternativas,respostaCorreta) -> None:
        self.texto = texto
        self.alternativas = alternativas
        self.repostaCorreta = respostaCorreta

    def exibirQuestao(self):
        return (f"Questão: {self.texto}\n{self.alternativas}")

    def verificarResposta(self):
        return (f"Resposta correta: {self.repostaCorreta}")
    

Questao1 = Questao("Qual a capital do nordeste?","A.RECIFE\nB.BRASILIA\nC.OLINDA\nD.SALVADOR","A")
Questao2= Questao("Qual a função do CSS em um site?","A.ESTRUTURAR CONTEÚDO\n B.DEFINIR A LÓGICA DE NEGÓCIOS\n C.ESTILIZAR O CONTEÚDO\n D.DEIXAR O CONTEÚDO INTERATIVO","C")
Questao3 = Questao("O que significa a sigla HTML?","A.Hypertext Markup Language\nB.Hyperlink and Text Markup Language\nC.Home Tool Markup Language\nD.Hyper Trasnfer Markup Language","A")
Questao4= Questao("Qual é o comando para exibir texto na tela em Python?",'A. echo("Hello, World!")\nB. print("Hello, World!")\nC. printf("Hello, World!")\nD. console.log("Hello, World!")',"B")
Questao5 = Questao("Que time é o maior do Nordeste?","A.Fortaleza\nB.Sport\nC.Ceará\n.Santa Cruz","A")
Questao6=Questao("Qual propriedade CSS é usada para alterar a cor de fundo de um elemento?","A.color\nB.Background-color\nC.font-color\nD.text-color","B")
Questao7=Questao("Qual atributo do HTML é usado para criar um link para uma outra página?","A.href\nB.src\nC.link\nD.alt","A")
Questao8=Questao("Qual propriedade CSS controla o espaçamento interno de um elemento?","A.margin\nB.border\nC.padding\nD.outline","C")
Questao9=Questao("Em JavaScript, qual é o método usado para adicionar um elemento ao final de um array?","A.shift\nB.pop\nC.push\nD.unshift","C")
Questao10=Questao("Qual tag HTML é usada para criar um parágrafo?","A.<head>\nB.<div>\nC.<p>\nD.<span>","C")

questoes= [Questao1,Questao2,Questao3,Questao4,Questao5,Questao6,Questao7,Questao8,Questao9,Questao10]


questaoSorteio= random.sample(questoes, 5)
pontuacao = 0
while True:
    comecarJogo= input("BEM VINDO AO SHOW DO MILHÃO!! DESEJA INICIAR O JOGO?").lower()
    if comecarJogo=="sim":
        print("-="*20)
        print(f"Primeira pergunta: {questaoSorteio[0].exibirQuestao()}")
        respostaQuestao1 = input("Qual a sua resposta?: ").upper()
        if respostaQuestao1== questaoSorteio[0].repostaCorreta:
            print("CERTA RESPOSTA!!!!")
            pontuacao +=1
            sleep(1.0)
            print("-="*20)
            print(f"Segunda pergunta: {questaoSorteio[1].exibirQuestao()}")
            repostaQuestao2= input("Qual a sua resposta?: ").upper()
            if repostaQuestao2 ==questaoSorteio[1].repostaCorreta:
                print("CERTA RESPOSTA!!!! VAMOS PARA A PRÓXIMA!")
                pontuacao+=1
                sleep(1.0)
                print("-="*20)
                print(f"Terceira Pergunta: {questaoSorteio[2].exibirQuestao()}")
                respostaQuestao3 = input("Qual a sua resposta?: ").upper()
                if respostaQuestao3==questaoSorteio[2].repostaCorreta:
                    print("VOCÊ ESTÁ ARRASANDO!!!!! RESPOSTA CORRETA MAIS UMA VEZ!")
                    sleep(1.0)
                    pontuacao+=1
                    print("-="*20)
                    print(f"Quarta pergunta: {questaoSorteio[3].exibirQuestao()}")
                    respostaQuestao4 = input("Qual a sua resposta?: ").upper()
                    if respostaQuestao4==questaoSorteio[3].repostaCorreta:
                        print("MAIS UMA CERTA RESPOSTA! VAMOS AGORA PARA A ULTIMA!")
                        pontuacao+=1
                        sleep(1.0)
                        print("-="*20)
                        print(f"QUINTA E ÚLTIMA PERGUNTA: {questaoSorteio[4].exibirQuestao()}")
                        respostaQuestao5 = input("Qual a sua resposta?: ").upper()
                        if respostaQuestao5 ==questaoSorteio[4].repostaCorreta:
                            pontuacao+=3
                            print(f"VOCÊ GANHOU!!!!! PARABÉNS!!!!\n Pontuação Final:{pontuacao}")
                            break
                        else:
                            print(f"Resposta incorreta. {Questao5.verificarResposta()}\nPontuação final:{pontuacao}")
                            break
                    else:
                        print(f"Resposta incorreta. {Questao4.verificarResposta()}\nPontuação final:{pontuacao}")
                        break
                else:
                    print(f"Resposta incorreta. {Questao3.verificarResposta()}\nPontuação final:{pontuacao}")
                    break
            else:
                print(f"Resposta incorreta. {Questao2.verificarResposta()}\nPontuação final:{pontuacao}")
                break
        else:
            print(f"Resposta incorreta. {Questao1.verificarResposta()}\nPontuação final:{pontuacao}")
            break
    elif comecarJogo=="nao" or comecarJogo=="não":
        print("Que pena. Volte quando estiver pronto!")
        break
    else:
        print("Resposta incompreendida. Tente novamente.")




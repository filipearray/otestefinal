# O Ultimo Onibus
# Visual novel curta (3 a 5 minutos), feita pra Ren'Py.
# Nao usa nenhuma imagem: fundos sao cores solidas, entao roda direto.

define m = Character("Mari", color="#ff7eb6")
define l = Character("Lia", color="#7ec8ff")
define d = Character("Seu Dito", color="#ffd27e")
define n = Character(None, what_italic=True)

image bg ponto = Solid("#1b2340")
image bg onibus = Solid("#2e2a24")
image bg praia = Solid("#f2a65a")
image bg casa = Solid("#3a2e3f")

default coragem = 0

label start:

    scene bg ponto with fade

    n "Sexta-feira, 23h47. Ponto de onibus vazio, poste piscando."
    n "Voce e a Mari acabaram de sair do show. Os celulares estao com 3%% de bateria."

    m "Mano. Se a gente perder o 405, a gente ta ferrada."
    m "O proximo e so as 5 da manha."

    menu:
        "Relaxa, ele sempre atrasa.":
            $ coragem += 1
            m "Tu fala isso toda vez e toda vez a gente corre."
        "Bora correr pro outro ponto?":
            m "Com esse tenis? Nem pensar."

    n "Um farol aparece no fim da rua. Um onibus velho, letreiro apagado."

    m "...Esse ai nao e o 405."
    m "Nem tem numero."

    n "A porta abre sozinha. Um motorista de bone sorri la de dentro."

    d "Boa noite, meninas. Ultima viagem da noite. Sobe ai."

    menu:
        "Subir no onibus.":
            $ coragem += 1
            jump onibus
        "Ficar no ponto.":
            jump ficar

label ficar:

    m "Nao. Nao, nao. Filme de terror comeca exatamente assim."
    d "Como quiserem. Mas o 405 nao passa hoje, nao."

    n "A porta fecha. O onibus vai embora sem fazer barulho nenhum."
    n "Dez minutos depois, uma menina chega correndo no ponto, sem folego."

    l "Voces... viram um onibus sem numero passar aqui?"
    m "Vimos. Por que?"
    l "Porque eu pego ele faz um ano. E ele so para pra quem precisa."

    n "Voces se olham. O poste para de piscar e apaga de vez."

    l "Bom. Agora so as 5. Alguem tem baralho?"

    n "Voces passaram a madrugada jogando truco com uma desconhecida no ponto de onibus."
    n "Ela virou sua melhor amiga. Mas voce nunca descobriu pra onde aquele onibus ia."

    jump fim_normal

label onibus:

    scene bg onibus with dissolve

    n "Por dentro, o onibus cheira a maresia. So tem uma passageira, la no fundo."

    l "Primeira vez?"
    m "Depende. A gente vai morrer?"
    l "Kkkkk nao. Pelo menos nao hoje."
    l "Eu sou a Lia. Esse onibus leva a gente pra onde a gente mais precisa ir."

    m "Tipo... casa?"
    l "As vezes. As vezes nao."

    d "Proxima parada: depende de voces."

    n "O Seu Dito olha pelo retrovisor e espera uma resposta."

    menu:
        "\"Leva a gente pra casa, por favor.\"":
            jump final_casa
        "\"Leva a gente pra onde ele quiser.\"" if coragem >= 2:
            jump final_praia
        "\"Eu quero descer.\"":
            d "Ta certo. Ninguem e obrigado."
            jump ficar

label final_casa:

    scene bg casa with fade

    n "Voce pisca. Ta na porta de casa. Sao exatamente 00h00."
    n "A Mari ta do seu lado, olhando o celular: 100%% de bateria."

    m "O que acabou de acontecer?"
    m "...Amanha a gente pega ele de novo?"

    n "Voce sorri. Porque sabe que vai."

    jump fim_normal

label final_praia:

    scene bg praia with fade

    n "A porta abre. Areia. Ceu laranja. Nao e de manha nem de noite."

    l "Ninguem nunca escolheu essa parada antes."
    d "Precisa de coragem pra deixar o caminho decidir."

    m "Mano. Eu nem gosto de praia."
    m "Mas isso aqui e lindo demais."

    n "Voces tres sentam na areia. O onibus espera, paciente, motor ligado."
    n "Pela primeira vez em muito tempo, ninguem ta com pressa de ir embora."

    "{b}FINAL SECRETO{/b} - Voce encontrou a parada que ninguem encontra."
    return

label fim_normal:

    "{b}FIM{/b} - Joga de novo e tenta ter mais coragem. Tem um final escondido."
    return

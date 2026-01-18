# --- DEFINIÇÃO DE PERSONAGENS ---
define cientista = Character("Cientista Osmar")
define engenheira = Character("Engenheira Bia")
define piloto = Character("Piloto Marina")

# --- SPRITES ---
# -- cientista
image cientista_neutro = Transform("images/cientista.png", zoom = 0.37)
image cientista_surpreso = Transform("images/cientistasurpreso.png", zoom = 0.37)

# -- engenheira
image engenheira_neutra = Transform("images/engenheira.png", zoom = 0.37)
image engenheira_surpresa = Transform("images/engenheirasurpresa.png", zoom = 0.37)

# -- piloto
image piloto_neutra = Transform("images/piloto.png", zoom = 0.37)
image piloto_surpresa = Transform("images/pilotosurpresa.png", zoom = 0.37)

# --- BACKGROUNDS ---
image cenario_cientista = Transform("images/cenariocientista.png", zoom = 0.5)
image cenario_engenheira = Transform("images/cenarioengenheiro.png", zoom = 0.5)
image cenario_piloto = Transform("images/cenariopiloto.png", zoom = 0.5)
image cenario_nave = Transform("images/cenarionave.png", zoom = 0.48)
image cenario_pouso = Transform("images/pouso.png", zoom = 0.5)
# Definimos uma imagem chamada 'alerta_vermelho'
image alerta_vermelho:
    # 1. Cria um retângulo sólido vermelho que cobre a tela toda
    Solid("#FF0000") 
    
    # 2. Define a opacidade inicial como 0 (invisível)
    alpha 0.0 
    
    # 3. Animação:
    # 'linear 0.5' significa: "faça a mudança acontecer suavemente durante 0.5 segundos"
    linear 0.5 alpha 0.5  # Vai de invisível para 50% de opacidade (semi-transparente)
    
    linear 0.5 alpha 0.0  # Vai de 50% para 0% (invisível) de novo
    
    # 4. O comando mágico que faz o loop
    repeat

default vidas = 3

label start:
    # 1. Chama a primeira tela (Regras/Tutorial)
    call screen tela_tutorial_regras

    # Se o jogador clicou em "Pular" na tela anterior, ele já deu um Jump para o inicio_da_missao.
    # Se ele clicou em "Avançar", o código continua aqui embaixo:

    # 2. Chama a segunda tela (Objetivo Final - imagem da direita)
    call screen tela_objetivo

    # Se o jogador clicou em "INICIAR", ele deu um Jump para inicio_da_missao.
    
    # Caso você queira garantir que o fluxo siga se algo der errado, force o pulo:
    jump inicio_da_missao
    # Chama a tela que criamos e espera o jogador clicar em "avançar"
    

    return

label inicio_da_missao:
    call screen intro_marte # L - Tela 04 eu coloquei aqui
    call screen apresentacao_cientista # L - Tela 05 eu coloquei aqui
    call screen apresentacao_enge
    call screen apresentacao_piloto
    call screen tela_objetivo_final with dissolve

label dialogo_cientista: # T - separei aq pra ficar mais fácil de fazer os jumps
    scene cenario_cientista
    show cientista_neutro at center 
    play music "audio/som_ambiente_foguete.mp3" fadein 0.5 volume 0.2 # MUSICA AMBIENTE FOGUETE

    cientista "Tudo parece calmo por aqui."
    
    hide cientista_neutro
    show cientista_surpreso at center
    
    cientista "Estou confuso com essas leituras..."

    # T - Aqui seria a tela 15, do canva, pra continuar a história
    show cientista_surpreso at center 
    show alerta_vermelho onlayer screens zorder 100
    stop music fadeout 1.0 # PARAR MUSICA AMBIENTE FOGUETE
    play music "audio/alarme_4.mp3" fadein 0.5 volume 0.1

    cientista "O quê?! Isso é impossível! Os sensores estavam estáveis há um minuto!"

    hide cientista_surpreso
    scene cenario_engenheira

    show engenheira_neutra at center
    hide alerta_vermelho onlayer screens
    # T - Essa daqui seria a tela 16
    engenheira "O que está acontecendo? É um vazamento?"

    hide engenheira_neutra
    scene cenario_cientista
    show cientista_surpreso at center

    # T - Tela 17
    show alerta_vermelho onlayer screens zorder 100
    cientista "É pior. Os sensores indicam uma flutuação inesperada nos níveis de CO2 e Oxigênio. Se o sistema reiniciar, pode ser fatal. O computador está pedindo um diagnóstico manual!"
    
    # T Tela 18
    hide alerta_vermelho onlayer screens
    hide cientista_neutro
    scene cenario_piloto
    show piloto_neutra at center:
        zoom 0.7

    piloto "Vá! Nós seguramos as pontas por aqui."
    stop music fadeout 1.0 # PARAR MUSICA AMBIENTE FOGUETE

    call screen quiz_cientista
    

label perguntas_cientista:
    
    # Mostra o contador de vidas na tela
    show screen hud_vidas
    
    # --- PERGUNTA 01 ---
    label q1_cientista_loop: # Cria um "ponto de retorno" caso erre
        hide piloto_neutra
        hide cenario_piloto
        scene cenario_cientista
        show cientista_neutro at center
        
        cientista "Vamos começar com uma questão histórica."

        # Chama a tela da pergunta 1
        call screen pergunta1_cientista 

        if _return == "correto":
            play sound "acerto.mp3"
            cientista "Correto! A cadela Laika foi enviada ao espaço em 1957."
            # Segue para a próxima
        else:
            # Lógica do erro
            play sound "erro.mp3"
            $ vidas -= 1 # Tira uma vida
            
            if vidas == 0:
                jump label_gameover # Se zerou, morre
            
            # Se ainda tem vida:
            cientista "Errado! Cuidado, os sistemas estão instáveis!"
            jump q1_cientista_loop # Volta para tentar a mesma pergunta de novo

    # --- TRANSIÇÃO ---
    cientista "Muito bem, vamos para a próxima..."
    
    # --- PERGUNTA 02 ---
    label q2_cientista_loop:
        call screen pergunta2_cientista
        
        if _return == "correto":
            play sound "acerto.mp3"
            scene cenario_cientista
            show cientista_neutro at center
            cientista "Exato! A atmosfera de Marte é composta principalmente por CO2."
        else:
            play sound "erro.mp3"
            $ vidas -= 1 
            
            if vidas == 0:
                jump label_gameover
            
            scene cenario_cientista
            show cientista_surpreso at center
            cientista "Não! Isso vai sobrecarregar os filtros! Tente de novo!"
            jump q2_cientista_loop


    # --- PERGUNTA 03 ---
    label q3_cientista_loop:
        call screen pergunta3_cientista
        
        if _return == "correto":
             play sound "acerto.mp3"
             cientista "Excelente! Diagnóstico do suporte de vida concluído."
        else:
            play sound "erro.mp3"
            $ vidas -= 1
            
            if vidas == 0:
                jump label_gameover
                
            cientista "Cuidado! Resposta incorreta."
            jump q3_cientista_loop

    # FIM DAS PERGUNTAS DESSE PERSONAGEM
    hide screen hud_vidas # Esconde os corações ao terminar
    cientista "Tudo certo por aqui. Vá falar com a Engenheira!"
    
    # Continua o jogo...
    
scene black with fade
call screen transicao_ponte with dissolve
call screen transicao_quiz_eng with dissolve
jump perguntas_engenheira

# --- LABEL DE GAME OVER ---
label label_gameover:
    hide screen hud_vidas
    stop music fadeout 0.5
    play sound "audio/som_falha_sistema.mp3" # Opcional se tiver som de derrota
    
    # Chama a tela de game over que criamos
    call screen tela_gameover
    return
    

# T - começando o quiz da engenheira
label perguntas_engenheira:
    # T - Isso aqui seria a tela 32
    show alerta_vermelho onlayer screens zorder 100
    play music "audio/alarme_4.mp3" fadein 0.5 volume 0.1
    call screen falha_propulcao
    
    #call screen engenheira_inicio_quiz
    hide screen falha_propulcao

    scene cenario_engenheira
    show engenheira_surpresa at center

    engenheira "Preciso restaurar o fluxo de energia e resfriar o sistema!"
    
    # Mostra o contador de vidas na tela
    hide alerta_vermelho onlayer screens
    stop music fadeout 1.0

    hide engenheira_surpresa
    show engenheira_neutra

    engenheira "Preciso da sua ajuda! Responda essas perguntas para restaurar o sistema!"
    show screen hud_vidas
    
    # --- PERGUNTA 01 ---
    label q1_engenheira_loop: # Cria um "ponto de retorno" caso erre
        scene cenario_engenheira
        show engenheira_neutra at center
        
        engenheira "Ok, hora de sujar as mãos. Vamos ver se sua lógica é tão boa quanto sua química."
        hide engenheira_neutra
        # Chama a tela da pergunta 1
        call screen pergunta1_engenheira

        if _return == "correto":
            play sound "acerto.mp3"
            show engenheira_neutra at center
            engenheira "Correto! Você é quase um engeheiro(a) também!"
            hide engenheira_neutra
            # Segue para a próxima
        else:
            # Lógica do erro
            play sound "erro.mp3"
            $ vidas -= 1 # Tira uma vida
            
            if vidas == 0:
                jump label_gameover # Se zerou, morre
            
            # Se ainda tem vida:
            show engenheira_neutra at center
            engenheira "Errado! Cuidado, os sistemas estão instáveis!"
            hide engenheira_neutra
            jump q1_engenheira_loop # Volta para tentar a mesma pergunta de novo

    
    # --- PERGUNTA 02 ---
    label q2_engenheira_loop:
        call screen pergunta2_engenheira
        
        if _return == "correto":
            play sound "acerto.mp3"
            scene cenario_engenheira
            show engenheira_neutra at center
            engenheira "Exato! Você está indo muito bem, o sistema já está mais estável."
            hide engenheira_neutra
        else:
            play sound "erro.mp3"
            $ vidas -= 1 
            
            if vidas == 0:
                jump label_gameover
            
            scene cenario_engenheira
            show engenheira_neutra at center
            engenheira "Não! Isso vai sobrecarregar os motores! Tente de novo!"
            hide engenheira_neutra
            jump q2_engenheira_loop


    # --- PERGUNTA 03 ---
    label q3_engenheira_loop:
        call screen pergunta3_engenheira
        
        if _return == "correto":
            play sound "acerto.mp3"
            show engenheira_neutra at center
            engenheira "Excelente! Reparos concluídos."
            hide engenheira_neutra
        else:
            play sound "erro.mp3"
            $ vidas -= 1
            
            if vidas == 0:
                jump label_gameover

            show engenheira_neutra at center    
            engenheira "Cuidado! Resposta incorreta."
            hide engenheira_neutra
            jump q3_engenheira_loop

    # FIM DAS PERGUNTAS DESSE PERSONAGEM
    hide screen hud_vidas # Esconde os corações ao terminar
    show engenheira_neutra at center
    engenheira "Ufa! Conseguimos recuperar o sistema de propulsão, mas o desafio não acabou..."
    hide engenheira_neutra
    # Continua o jogo...
    
scene black with fade
call screen transicao_ponte with dissolve
jump dialogo_piloto
# T - removi a label de transição porque eestava causando um loop. ainda tem a transiçao com o fundo preto.
    
label dialogo_piloto:

    scene cenario_piloto 
    show piloto_neutra at center:
        zoom 0.7
    
    piloto "Temos um problema de estabilização aqui. O painel está mostrando leituras conflitantes."
    
    hide piloto_neutra
    show piloto_surpresa at center:
        zoom 0.7
    show alerta_vermelho onlayer screens zorder 100
    play music "audio/alarme_4.mp3" fadein 0.5 volume 0.1

    piloto "Preciso da sua ajuda para restaurar os sistemas de voo e proteção da nave!"
    hide piloto_surpresa
    # Chama a tela de aviso que você criou em customizacao_telas.rpy
    # call screen quiz_piloto 

    # 4. Inicia o Loop de Perguntas
    jump perguntas_piloto


label perguntas_piloto:
    # Mostra os corações na tela
    hide alerta_vermelho onlayer screens
    stop music fadeout 1.0
    show screen hud_vidas

    # --- PERGUNTA 01 ---
    label q1_piloto_start:

        # --- Loop de Tentativa (Onde o jogo volta se errar) ---
        label q1_piloto_tentativa:
            
            # Chama a SUA tela de pergunta (pergunta1_piloto)
            call screen pergunta1_piloto 

            # --- Verificação da Resposta ---
            if _return == "correto":
                play sound "acerto.mp3"
                
                show piloto_neutra at center:
                    zoom 0.7
                piloto "Exato! Com a radiação em 95%%, a condição foi atendida. Muito bem!"
                piloto "Sistema estabilizado!"
                hide piloto_neutra
                jump q2_piloto_start

            else:
                # --- Lógica do Erro ---
                play sound "erro.mp3"
                $ vidas -= 1 
                
                if vidas <= 0:
                    jump label_gameover 
                
                # Se ainda tem vidas:
                else:
                    show piloto_surpresa at center:
                        zoom 0.7
                    
                    # Seus textos de erro originais
                    piloto "Não! Isso violaria o protocolo e poderia explodir o reator!"
                    piloto "Tente responder novamente, você consegue!"
                    hide piloto_surpresa
                    # O PULO DO GATO: Volta para o label de tentativa
                    jump q1_piloto_tentativa

    # --- PERGUNTA 02 ---
    label q2_piloto_start:
        show alerta_vermelho onlayer screens zorder 100
        play music "audio/alarme_4.mp3" fadein 0.5 volume 0.1
        scene cenario_piloto
        show piloto_surpresa at center:
            zoom 0.7
        
        # Texto da introdução da pergunta 2
        piloto "O sistema de navegação travou! Ele exige que completemos a sequência lógica para liberar o trajeto."
        hide piloto_surpresa
        # --- Loop de Tentativa (Pergunta 2) ---
        label q2_piloto_tentativa:
            hide alerta_vermelho onlayer screens
            stop music fadeout 1.0
            
            # Chama a tela da pergunta 2
            call screen pergunta2_piloto 

            # --- Verificação da Resposta ---
            if _return == "correto":
                play sound "acerto.mp3"
                
                show piloto_neutra at center:
                    zoom 0.7
                piloto "Código 63 aceito! A lógica era multiplicar por 2 e somar 1. Brilhante!"
                
                piloto "Sistemas de navegação e escudo operacionais. Bom trabalho!"
                hide piloto_neutra
                jump q3_piloto_start

            else:
                # --- Lógica do Erro ---
                play sound "erro.mp3"
                $ vidas -= 1 
                
                if vidas <= 0:
                    jump label_gameover 
                
                # Se ainda tem vidas:
                else:
                    show piloto_surpresa at center:
                        zoom 0.7
                    
                    # Feedback de erro específico para a matemática
                    piloto "Acesso Negado! O computador rejeitou esse número. A sequência não bate."
                    piloto "Analise os números com calma e tente novamente!"
                    hide piloto_surpresa
                    # O PULO DO GATO: Volta para o label de tentativa DA PERGUNTA 2
                    jump q2_piloto_tentativa

        # --- PERGUNTA 03 ---
    label q3_piloto_start:
        show alerta_vermelho onlayer screens zorder 100
        play music "audio/alarme_4.mp3" fadein 0.5 volume 0.1
        scene cenario_piloto
        show piloto_surpresa at center:
            zoom 0.7
        
        piloto "Estamos na reta final para o pouso! Mas a velocidade de descida está alta demais..."
        hide piloto_surpresa
        # --- Loop de Tentativa (Pergunta 3) ---
        label q3_piloto_tentativa:
            hide alerta_vermelho onlayer screens
            stop music fadeout 1.0
            call screen pergunta3_piloto 

            if _return == "correto":
                play sound "acerto.mp3"
                
                # Feedback Final
                show piloto_neutra at center:
                    zoom 0.7
                piloto "Arremetendo! Ufa... essa foi por pouco." 
                piloto "O sistema automático evitou uma colisão."
                
                # --- SUCESSO TOTAL DO JOGO (Ou fim da demo) ---
                piloto "Excelente trabalho, cadete!"
                hide piloto_neutra
                

            else:
                play sound "erro.mp3"
                $ vidas -= 1 
                
                if vidas <= 0:
                    jump label_gameover 
                
                else:
                    show piloto_surpresa at center:
                        zoom 0.7
                    piloto "Perigo! Se tentarmos pousar nessa velocidade, vamos colidir!"
                    piloto "Verifique a regra de segurança novamente!"
                    hide piloto_surpresa
                    jump q3_piloto_tentativa
        hide alerta_vermelho onlayer screens
        stop music fadeout 1.0

hide screen hud_vidas


scene cenario_pouso with dissolve:
    zoom 1.4
    xalign 0.5
    yalign 0.5
piloto "Conseguimos! Pousamos em parte e seremos os primeiros a explorar o planeta vermelho!"

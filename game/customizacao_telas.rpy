# --- TELA 1: REGRAS ---
screen tela_tutorial_regras():
    add "bg_espaco.png": # Certifique-se que a imagem existe
        zoom 0.6
        align (0.5, 0.5)

    vbox:
        align (0.5, 0.5) 
        spacing 10      
        xsize 1100

        text "Como o jogo funciona?":
            size 60
            bold True
            xalign 0.5
            color "#ffffff"

        null height 10 

        text "O jogo 'Operação Marte' é um desafio de perguntas e respostas...":
            xalign 0.5
            text_align 0.5
            layout "subtitle"
            color "#ffffff"

        null height 15

        text "Regras básicas:":
            size 40
            bold True
            xalign 0.5
            color "#ffffff"

        vbox:
            xalign 0.5
            spacing 5 
            text "• Você começa jogando com o Cientista.":
                color "#ffffff"
            text "• São 3 perguntas por personagem.":
                color "#ffffff"
            text "• Ao acertar todas as 3 perguntas, você avança...":
                color "#ffffff"
                        
        null height 15

        text "Para vencer, conclua as tarefas antes do tempo acabar.":
             xalign 0.5
             text_align 0.5
             color "#ffffff"

        null height 25 

        hbox:
            xalign 0.5
            spacing 150

            # BOTÃO AVANÇAR: Apenas retorna para o script carregar a próxima tela
            textbutton "AVANÇAR":
                action Return() 
                background Frame("#561969", 10, 10)
                hover_background Frame("#7a2494", 10, 10) # Cor mais clara ao passar o mouse
                padding (50, 20)
                text_size 35
                text_color "#ffffff"

            # BOTÃO PULAR: Vai direto para o jogo
            textbutton "PULAR TUTORIAL":
                action Jump("inicio_da_missao") 
                background Frame("#741129", 10, 10)
                hover_background Frame("#a31839", 10, 10)
                padding (50, 20)
                text_size 35
                text_color "#ffffff"


# --- TELA 2: OBJETIVO (A tela da direita na foto) ---
screen tela_objetivo():
    add "bg_espaco.png":
        zoom 0.6
        align (0.5, 0.5)

    vbox:
        align (0.5, 0.5)
        xsize 1200 # Um pouco mais largo para caber o texto
        spacing 20

        # Título igual ao da imagem
        text "Como o jogo funciona?":
            size 60
            bold True
            xalign 0.5
            color "#ffffff"

        null height 30

        # Subtítulo com Ícone (simulado com texto ou imagem se tiver)
        hbox:
            xalign 0.5
            spacing 10
            text "Objetivo Final:":
                size 50
                bold True
                color "#ffffff"
        
        null height 20

        # Texto do corpo
        text "A missão só será concluída quando os três tripulantes completarem suas etapas com sucesso e a Aurora-9 pousar em segurança no solo marciano.":
            xalign 0.5
            text_align 0.5
            size 30
            bold True
            color "#ffffff"
            layout "subtitle"

        text "PENSE RÁPIDO, RESPONDA CERTO E SALVE A MISSÃO!":
            xalign 0.5
            text_align 0.5
            size 35
            bold True
            color "#ffffff" # Ou um tom alaranjado se preferir destaque

        null height 50

        # BOTÃO INICIAR (Cor marrom/laranja da imagem)
        textbutton "INICIAR":
            action Jump("inicio_da_missao")
            xalign 0.5
            
            # Cor similar ao marrom da imagem do Canva
            background Frame("#C07F56", 10, 10) 
            hover_background Frame("#D99A73", 10, 10)
            
            padding (50, 20)
            text_size 40
            text_color "#ffffff"

screen intro_marte():

    # 1. O Fundo
    add "bg_espaco.png"

    # 2. Uma caixa vertical (vbox) para empilhar: Título, Texto e Botão
    vbox:
        align (0.5, 0.5) # Centraliza a caixa inteira na tela
        spacing 30       # Espaço entre os elementos (título, texto, botão)

        # --- O TÍTULO (Caixa Branca) ---
        frame:
            background "#ffffff" # Cor branca em Hexadecimal
            xalign 0.5           # Centraliza horizontalmente
            padding (20, 10)     # "Gordurinha" interna da caixa

            text "Operação Marte":
                color "#000000"  # Texto preto
                size 50          # Tamanho da fonte
                bold True        # Negrito

        # --- O TEXTO DA HISTÓRIA ---
        text "Em um futuro não muito distante, uma equipe de\nexploradores espaciais partiu em uma missão histórica:\nchegar a Marte e estabelecer a primeira base humana no\nplaneta vermelho.\n\nA bordo da nave Aurora-9, estão três tripulantes...":
            xalign 0.5           # Centraliza o bloco de texto
            text_align 0.5       # Centraliza as linhas do texto
            color "#ffffff"      # Texto branco
            size 28
            layout "subtitle"    # Ajuda a quebrar linhas se for muito longo

        # --- O BOTÃO AVANÇAR ---
        textbutton "AVANÇAR":
            xalign 0.5
            # A ação: quando clicar, a tela fecha e o jogo continua
            action Return() 
            
            # Estilizando o botão para parecer o marrom do seu design
            text_color "#000000"
            text_hover_color "#ffffff" # Muda de cor quando passa o mouse
            background "#a07e5e" # Um tom de marrom (pode ajustar)
            padding (30, 10)

screen apresentacao_cientista():
    # 1. Fundo
    add "bg_espaco.png"

    # 2. Caixa Horizontal (HBOX) para colocar: Imagem na Esquerda | Texto na Direita
    hbox:
        align (0.5, 0.5) # Centraliza o conjunto todo na tela
        spacing 1.0       # Espaço entre o cientista e o bloco de texto

        # --- LADO ESQUERDO: O CIENTISTA ---
        # Estou usando a imagem original para podermos controlar o tamanho (zoom)
        # só para essa tela, caso o sprite do jogo seja muito pequeno.
        add "images/cientista.png":
            yalign 1.0   # Alinha o pé do boneco com o fundo da caixa
            zoom 0.3   # AJUSTE AQUI: Aumente ou diminua para ficar do tamanho do Canva

        # --- LADO DIREITO: TEXTOS E BOTÃO (VBOX) ---
        vbox:
            yalign 0.5   # Centraliza verticalmente em relação ao cientista
            spacing 15
            xsize 700    # Limita a largura para o texto não invadir a imagem do cientista

            # Título "O Cientista"
            frame:
                background "#a07e5e" # Aquele marrom/laranja do Canva
                xalign 0.3
                padding (40, 15)

                text "O Cientista":
                    color "#000000" # Texto preto
                    size 45
                    bold True

            # Texto Descritivo
            text "Responsável pelos sistemas de suporte vital e análises químicas do oxigênio.\n\nSuas perguntas envolvem ciências e curiosidades espaciais, testando seu conhecimento sobre o universo.\n\n➡ Acertar as perguntas do Cientista estabiliza o ar e a energia da nave.":
                xalign 0.1       # Centraliza o bloco
                text_align 0.5   # Centraliza as linhas
                color "#ffffff"
                size 26
                layout "subtitle"

            # Botão Avançar
            textbutton "AVANÇAR":
                xalign 0.4       # Alinhado à direita (como na sua imagem)
                action Return()
                
                # Estilo
                text_color "#000000"
                text_hover_color "#ffffff"
                background "#a07e5e"
                padding (30, 10)

# Túlio: telas 6 a 8

screen apresentacao_enge():
    add "bg_espaco.png" # adiciona o fundo

    hbox:
        align (0.5, 0.5)
        spacing 50
        
        # lado esquerdo
        add "images/engenheira.png":
            yalign 1.0   # Alinha o pé do boneco com o fundo da caixa
            zoom 0.20

        # lado direito
        vbox:
            yalign 0.5   # Centraliza verticalmente em relação ao cientista
            spacing 20
            xsize 700

            frame:
                background "#a07e5e" # Aquele marrom/laranja do Canva
                xalign 0.5
                padding (30, 15)

                text "A Engenheira":
                    color "#000000" # Texto preto
                    size 45
                    bold True

            text "Cuida dos circuitos, propulsão e reparos da nave.\n\nSuas perguntas são de lógica e cálculo, exigindo raciocínio rápido e atenção.\n\n➡️ Cada acerto ajuda a restaurar os motores principais.":
                xalign 0.5       # Centraliza o bloco
                text_align 0.5   # Centraliza as linhas
                color "#ffffff"
                size 26
                layout "subtitle"

            # Botão Avançar
            textbutton "AVANÇAR":
                xalign 0.5       # Alinhado à direita (como na sua imagem)
                action Return()
                        
            # Estilo
                text_color "#000000"
                text_hover_color "#ffffff"
                background "#a07e5e"
                padding (30, 10)

screen apresentacao_piloto():
    add "bg_espaco.png" # adiciona o fundo

    hbox:
        align (0.5, 0.5)
        spacing 50
        
        # lado esquerdo
        add "images/piloto.png":
            yalign 1.0   # Alinha o pé do boneco com o fundo da caixa
            zoom 0.20

        # lado direito
        vbox:
            yalign 0.5   # Centraliza verticalmente em relação ao cientista
            spacing 20
            xsize 700

            frame:
                background "#a07e5e" # Aquele marrom/laranja do Canva
                xalign 0.5
                padding (40, 15)

                text "A Piloto":
                    color "#000000" # Texto preto
                    size 45
                    bold True

            text "Cuida dos circuitos, propulsão e reparos da nave.\n\nSuas perguntas são de lógica e programação, exigindo raciocínio rápido e atenção.\n\n➡️ Cada acerto ajuda a restaurar os motores principais.":
                xalign 0.5       # Centraliza o bloco
                text_align 0.5   # Centraliza as linhas
                color "#ffffff"
                size 26
                layout "subtitle"

            # Botão Avançar
            textbutton "AVANÇAR":
                xalign 0.5       # Alinhado à direita (como na sua imagem)
                action Return()
                        
            # Estilo
                text_color "#000000"
                text_hover_color "#ffffff"
                background "#a07e5e"
                padding (30, 10)

screen tela_objetivo_final():

    add "bg_espaco.png"

    vbox:
        align (0.5, 0.5) # Centraliza a caixa inteira na tela
        spacing 50       # Espaço entre o texto e o botão

        # --- O TEXTO DA HISTÓRIA ---
        text ("Mas algo inesperado aconteceu. Durante a travessia pelo\n"
              "espaço, a nave começou a apresentar falhas nos sistemas\n"
              "principais: {b}energia instável{/b}, {b}propulsão comprometida{/b} e\n"
              "{b}comunicação intermitente{/b}.\n\n"
              "Agora, cabe a você ajudar a tripulação a consertar a nave\n"
              "e garantir a chegada segura a Marte."):
                xalign 0.5
                text_align 0.5
                color "#ffffff" # Texto branco
                size 36         # Ajuste o tamanho
                layout "subtitle"
            # Adicionando o efeito Bold para destacar partes importantes
            
        # --- O BOTÃO INICIAR ---
        textbutton "INICIAR":
            xalign 0.5
            
            # A ação: quando clicar, o jogo pula (jump) para o início da missão
            action Jump("dialogo_cientista") 
            
            # Estilizando o botão (usando o marrom que você já definiu)
            text_color "#000000"
            text_hover_color "#ffffff" 
            background "#a07e5e" # Cor marrom
            padding (40, 15)

screen quiz_cientista():
    add "cenariocientista.png":
        zoom 0.5
    
    vbox:
        align (0.5, 0.5)
        spacing 50
        
        frame:
            # 💡 Ajuste aqui a cor e a transparência (ex: #000000c0 -> Preto, 75% opaco)
            background "#000000c0" 
            padding (60, 40) # Espaço interno (gordurinha) do retângulo
            xsize 900 # Largura máxima do retângulo
            vbox:
                spacing 20
                
                # Título de alerta
                text "Falha crítica detectada!" at center:
                    size 50
                    color "#FF0000" # Vermelho de alerta
                
                
                # Texto de instrução
                text "Sua missão é consertar os 3 sistemas principais, respondendo às perguntas de cada tripulante." at center:
                    size 30
                    color "#FFFFFF"
                    text_align 0.5 # Centraliza o bloco de texto
                    
                # Texto de continuação
                text "Clique em continuar para iniciar a fase de diagnóstico." at center:
                    size 28
                    color "#CCCCCC"

        textbutton "CONTINUAR":
            action Return() # Fecha a tela e volta para o 'return' na label dialogo_cientista
            xalign 0.5
            text_color "#000000"
            background "#a07e5e"
            padding (30, 10)

screen pergunta1_cientista():
   # 1. Imagem de Fundo (Coloque o nome exato da sua imagem aqui)
    add "cenariocientista":
        zoom 0.5

    # 2. O Cientista (Alinhado à direita)
    add "cientistasurpreso":
        xalign 1.2
        yalign 1.0 # Colado na base da tela
        zoom 0.3
    
    # 3. Caixa da Pergunta (Topo)
    frame:
        background "#3e1e3eCC" # Roxo escuro semi-transparente
        xalign 0.5 
        yalign 0.10 # Um pouco abaixo do topo
        xsize 1100  # Largura da caixa
        padding (30, 30)

        text "Pergunta 01 - A senha é o ano em que a cadela Laika foi enviada ao espaço, qual é?" color "#FFFFFF" text_align 0.5 xalign 0.5 yalign 0.5

    # 4. As Alternativas (Botões empilhados verticalmente)
    vbox:
        xalign 0.1 # Alinhado à esquerda
        yalign 0.7 # Mais para baixo
        spacing 15 # Espaço entre os botões

        # Botão A - Errado
        textbutton "A) 1955":
            style "botao_quiz"
            action Return("errado")

        # Botão B - Certo (Dióxido de Carbono é ~95% da atmosfera de Marte)
        textbutton "B) 1957":
            style "botao_quiz"
            action Return("correto")

        # Botão C - Errado
        textbutton "C) 1961":
            style "botao_quiz"
            action Return("errado")

        # Botão D - Errado
        textbutton "D) 1969":
            style "botao_quiz"
            action Return("errado")

# 5. Estilo personalizado para os botões ficarem roxos igual ao Canva
style botao_quiz:
    background "#541e54" # Cor de fundo do botão (roxo)
    hover_background "#7a2b7a" # Cor quando passa o mouse (roxo mais claro)
    xsize 700 # Largura do botão
    padding (20, 20) # Espaçamento interno
    
style botao_quiz_text:
    color "#FFFFFF" # Cor do texto
    size 28
    hover_color "#FFD700" # Texto fica dourado ao passar o mouse


screen pergunta2_cientista():
    # 1. Imagem de Fundo (Coloque o nome exato da sua imagem aqui)
    add "cenariocientista":
        zoom 0.5

    # 2. O Cientista (Alinhado à direita)
    add "cientistasurpreso":
        xalign 1.2
        yalign 1.0 # Colado na base da tela
        zoom 0.3

    # 3. Caixa da Pergunta (Topo)
    frame:
        background "#3e1e3eCC" # Roxo escuro semi-transparente
        xalign 0.5 
        yalign 0.10 # Um pouco abaixo do topo
        xsize 1100  # Largura da caixa
        padding (30, 30)

        text "Pergunta 02 - Os sensores de suporte vital precisam ser ajustados para a atmosfera de Marte... Qual é o gás MAIS abundante?" color "#FFFFFF" text_align 0.5

    # 4. As Alternativas (Botões empilhados verticalmente)
    vbox:
        xalign 0.1 # Alinhado à esquerda
        yalign 0.7 # Mais para baixo
        spacing 15 # Espaço entre os botões

        # Botão A - Errado
        textbutton "A) Argônio":
            style "botao_quiz"
            action Return("errado")

        # Botão B - Certo (Dióxido de Carbono é ~95% da atmosfera de Marte)
        textbutton "B) Dióxido de Carbono":
            style "botao_quiz"
            action Return("correto")

        # Botão C - Errado
        textbutton "C) Oxigênio":
            style "botao_quiz"
            action Return("errado")

        # Botão D - Errado
        textbutton "D) Nitrogênio":
            style "botao_quiz"
            action Return("errado")

# 5. Estilo personalizado para os botões ficarem roxos igual ao Canva
style botao_quiz:
    background "#541e54" # Cor de fundo do botão (roxo)
    hover_background "#7a2b7a" # Cor quando passa o mouse (roxo mais claro)
    xsize 700 # Largura do botão
    padding (20, 20) # Espaçamento interno
    
style botao_quiz_text:
    color "#FFFFFF" # Cor do texto
    size 28
    hover_color "#FFD700" # Texto fica dourado ao passar o mouse

screen pergunta3_cientista():
    # 1. Imagem de Fundo (Coloque o nome exato da sua imagem aqui)
    add "cenariocientista":
        zoom 0.5

    # 2. O Cientista (Alinhado à direita)
    add "cientistasurpreso":
        xalign 1.2
        yalign 1.0 # Colado na base da tela
        zoom 0.3

    # 3. Caixa da Pergunta (Topo)
    frame:
        background "#3e1e3eCC" # Roxo escuro semi-transparente
        xalign 0.5 
        yalign 0.10 # Um pouco abaixo do topo
        xsize 1100  # Largura da caixa
        padding (30, 30)

        text "Pergunta 03 - Qual elemento químico é essencial para a 'respiração' da nave (combustão do motor de foguete) e também para o suporte vital da tripulação?" color "#FFFFFF" text_align 0.5
     # 4. As Alternativas (Botões empilhados verticalmente)
    vbox:
        xalign 0.1 # Alinhado à esquerda
        yalign 0.7 # Mais para baixo
        spacing 15 # Espaço entre os botões

        # Botão A - Errado
        textbutton "A) Oxigênio":
            style "botao_quiz"
            action Return("correto")

        # Botão B - Certo (Dióxido de Carbono é ~95% da atmosfera de Marte)
        textbutton "B) Nitrogênio":
            style "botao_quiz"
            action Return("errado")

        # Botão C - Errado
        textbutton "C) Hidrogênio":
            style "botao_quiz"
            action Return("errado")

        # Botão D - Errado
        textbutton "D) Carbono":
            style "botao_quiz"
            action Return("errado")

screen hud_vidas():
    zorder 100 # Garante que fica por cima de tudo
    frame:
        background "#3e1e3eCC" # Fundo transparente
        xalign 0.05
        yalign 0.02
        
        hbox:
            spacing 10
            # Mostra o texto "Vidas:"
            text "VIDAS:" size 30 color "#FFFFFF" bold True 
            
            # Lógica para mostrar os corações baseados no número
            if vidas >= 1:
                text "❤️" size 30
            if vidas >= 2:
                text "❤️" size 30
            if vidas >= 3:
                text "❤️" size 30

# --- TELA DE GAME OVER PERSONALIZADA ---
screen tela_gameover():
    # 1. Imagem de fundo
    add "martecenario":
        zoom 0.48 

    # 2. Caixa vertical centralizada
    vbox:
        align (0.5, 0.5) 
        spacing 10      

        # Título Principals
        text "GAME   OVER":
            size 100                 
            color "#FF0000"  
            xalign 0.5       
            outlines [(4, "#FFFFFFD6", 0, 0)] 
            font "fontes/16x8pxl-sans.ttf" 

        # Subtítulo
        text "A equipe tríade falhou na missão! :(":
            size 35
            color "#FFFFFF" 
            xalign 0.5
            layout "subtitle"
            text_align 0.5
            outlines [(2, "#000000", 0, 0)] 

        # Espaço vazio
        null height 50

        # --- AQUI ESTÁ A MUDANÇA ---
        textbutton "TENTAR NOVAMENTE":
            # Ação Dupla:
            # 1. SetVariable("vidas", 3) -> Reseta as vidas para 3
            # 2. Jump("dialogo_cientista") -> Pula para o início da conversa do cientista
            action [SetVariable("vidas", 3), Jump("dialogo_cientista")] 
            
            yalign 0.4
            xalign 0.5
            padding (40, 20)
            
            # Estilo
            background Frame("#741129", 10, 10)
            hover_background Frame("#a31839", 10, 10)
            text_color "#FFFFFF"
            text_size 30

screen transicao_ponte():
    add "cenarionave":
        zoom 0.478
    frame:
        background "#3e1e3eCC" # mudei o background para um translúcido

        xalign 0.5  
        yalign 0.15 
        xsize 1000
        ysize 100
        padding (20, 20)

        text "DE VOLTA Á PONTE DE COMANDO..." color "#FFFFFF" size 40 bold True align (0.5, 0.5)
    button: 
        action Return()
        xfill True
        yfill True

screen transicao_quiz_eng():
    add "cenarionave":
        zoom 0.478
    frame:
        background "#3e1e3eCC"

        xalign 0.5  
        yalign 0.15 
        xsize 1000
        ysize 170
        padding (20, 20)

        text "O som de ventilação suave indica que o oxigêncio voltou, mas as luzes de emergência continuam piscando no painel." color "#FFFFFF" size 35 bold True text_align 0.5 xalign 0.5
    button: 
        action Return()
        xfill True
        yfill True

screen falha_propulcao():
    add "cenarionave":
        zoom 0.478
    frame:
        background "#3e1e3eCC"

        xalign 0.5  
        yalign 0.15 
        xsize 1000
        ysize 120
        padding (20, 20)

        text "FALHA CRÍTICA NO NÚCLEO DE PROPULSÃO. INTERVENÇÃO MANUAL NECESSÁRIA." color "#FFFFFF" size 35 bold True text_align 0.5 xalign 0.5
    button: 
        action Return()
        xfill True
        yfill True

screen pergunta1_engenheira():
    add "cenarioengenheira":
        zoom 0.47

    add "engenheirasurpresa":
        xalign 1.2
        yalign 1.0 # Colado na base da tela
        zoom 0.3
    
    # 3. Caixa da Pergunta (Topo)
    frame:
        background "#3e1e3eCC" # Roxo escuro semi-transparente
        xalign 0.5 
        yalign 0.11 # Um pouco abaixo do topo
        xsize 1100  # Largura da caixa
        padding (30, 30)

        text "Pergunta 01 - O painel mostra que o motor esquerdo está recebendo 120 volts, enquanto o direito recebe 40 volts. Para equilibrar o sistema, você precisa redistribuir a energia igualmente. Qual será a voltagem em cada motor após a redistribuição?" color "#FFFFFF" text_align 0.5 xalign 0.5 yalign 0.5

    # 4. As Alternativas (Botões empilhados verticalmente)
    vbox:
        xalign 0.1 # Alinhado à esquerda
        yalign 0.7 # Mais para baixo
        spacing 15 # Espaço entre os botões

        # Botão A - Errado
        textbutton "A) 4 volts":
            style "botao_quiz"
            action Return("errado")

        # Botão B - Certo (Dióxido de Carbono é ~95% da atmosfera de Marte)
        textbutton "B) 60 volts":
            style "botao_quiz"
            action Return("errado")

        # Botão C - Errado
        textbutton "C) 80 volts":
            style "botao_quiz"
            action Return("correto")

        # Botão D - Errado
        textbutton "D) 100 volts":
            style "botao_quiz"
            action Return("errado")

# 5. Estilo personalizado para os botões ficarem roxos igual ao Canva
style botao_quiz:
    background "#541e54" # Cor de fundo do botão (roxo)
    hover_background "#7a2b7a" # Cor quando passa o mouse (roxo mais claro)
    xsize 700 # Largura do botão
    padding (20, 20) # Espaçamento interno
    
style botao_quiz_text:
    color "#FFFFFF" # Cor do texto
    size 28
    hover_color "#FFD700" # Texto fica dourado ao passar o mouse

screen pergunta2_engenheira():
    add "cenarioengenheriro":
        zoom 0.5

    add "engenheirasurpresa":
        xalign 1.2
        yalign 1.0 # Colado na base da tela
        zoom 0.3

    frame:
        background "#3e1e3eCC" # Roxo escuro semi-transparente
        xalign 0.5 
        yalign 0.11# Um pouco abaixo do topo
        xsize 1100  # Largura da caixa
        padding (30, 30)

        text "Pergunta 02 - Três cabos devem ser conectados em sequência, cada conexão correta multiplica a eficiência por 2. A eficiência inicial é 5%. Qual será a eficiência final, se todas as conexões forem feitas corretamente?" color "#FFFFFF" text_align 0.5

    vbox:
        xalign 0.1 # Alinhado à esquerda
        yalign 0.7 # Mais para baixo
        spacing 15 # Espaço entre os botões

        textbutton "A) 15%":
            style "botao_quiz"
            action Return("errado")

        textbutton "B) 30%":
            style "botao_quiz"
            action Return("errado")

        textbutton "C) 40%":
            style "botao_quiz"
            action Return("correto")

        textbutton "D) 60%":
            style "botao_quiz"
            action Return("errado")

screen pergunta3_engenheira():
    add "cenarioengnheiro":
        zoom 0.5

    add "engenheirasurpresa":
        xalign 1.2
        yalign 1.0 # Colado na base da tela
        zoom 0.3

    frame:
        background "#3e1e3eCC" # Roxo escuro semi-transparente
        xalign 0.5 
        yalign 0.12 # Um pouco abaixo do topo
        xsize 1100  # Largura da caixa
        padding (30, 30)

        text "Pergunta 03 - Um conjunto de painéis solares fornece 900 unidades de energia por hora. Após uma tempestade cósmica, a produção cai 30%. Quantas unidades de energia o sistema ainda consegue gerar por hora?" color "#FFFFFF" text_align 0.5

    vbox:
        xalign 0.1 # Alinhado à esquerda
        yalign 0.7 # Mais para baixo
        spacing 15 # Espaço entre os botões

        textbutton "A) 270 unidades":
            style "botao_quiz"
            action Return("errado")

        textbutton "B) 600 unidades":
            style "botao_quiz"
            action Return("errado")

        textbutton "C) 630 unidades":
            style "botao_quiz"
            action Return("correto")

        textbutton "D) 700 unidades":
            style "botao_quiz"
            action Return("errado")


screen pergunta1_piloto():
    # 1. Imagem de Fundo
    add "cenariopiloto":
        zoom 0.5

    # 2. A Piloto (Ajustada para enquadramento melhor)
    add "pilotosurpresa":
        xalign 0.95   # Traz ela um pouco mais para a esquerda (era 1.15)
        yalign 1.0    # Mantém os pés/cintura na base da tela
        zoom 0.25    # Diminui um pouco o tamanho (era 0.35)

    # 3. Caixa da Pergunta (Topo - Igual ao Cientista)
    frame:
        background "#3e1e3eCC" # Roxo escuro semi-transparente
        xalign 0.5
        yalign 0.11
        xsize 1100
        padding (30, 30)

        # Texto da Pergunta Lógica
        text "Pergunta 01 - Protocolo: Ativar Escudo se houver IMPACTO {color=#ffeb3b}{b}OU{/b}{/color} RADIAÇÃO > 80%.\nSituação: Sem impacto, mas Radiação em 95%. O que fazer?" color "#FFFFFF" text_align 0.5

    # 4. As Alternativas (Alinhadas à Esquerda - Igual ao Cientista)
    vbox:
        xalign 0.1
        yalign 0.65
        spacing 15

        # Botão A
        textbutton "A) Não ativar (Sem impacto)":
            style "botao_quiz"
            action Return("errado")

        # Botão B - CORRETO
        textbutton "B) Ativar (Radiação Crítica)":
            style "botao_quiz"
            action Return("correto")

        # Botão C
        textbutton "C) Aguardar impacto":
            style "botao_quiz"
            action Return("errado")

        # Botão D
        textbutton "D) Desligar sensores":
            style "botao_quiz"
            action Return("errado")

screen pergunta2_piloto():
    # 1. Imagem de Fundo
    add "cenariopiloto":
        zoom 0.5

    # 2. A Piloto (Configuração ajustada para o enquadramento ideal)
    add "pilotosurpresa":
        xalign 0.95   
        yalign 1.0    
        zoom 0.25     

    # 3. Caixa da Pergunta (Topo)
    frame:
        background "#3e1e3eCC"
        xalign 0.5
        yalign 0.12
        xsize 1000
        ysize 150
        padding (30, 30)

        # Texto da Pergunta 02
        text "Pergunta 02 - Analise a sequência lógica do sistema de navegação:\n{size=+6}{b}1, 3, 7, 15, 31, __{/b}{/size}\n\nQual é o próximo número?" color "#FFFFFF" text_align 0.5 xalign 0.5 yalign 0.5

    # 4. As Alternativas (Botões à Esquerda)
    vbox:
        xalign 0.1
        yalign 0.65
        spacing 15

        # Botão A - Errado (Lógica de somar 2 apenas)
        textbutton "A) 33":
            style "botao_quiz"
            action Return("errado")

        # Botão B - Errado (Erro de cálculo comum, 31+31)
        textbutton "B) 62":
            style "botao_quiz"
            action Return("errado")

        # Botão C - CORRETO (31 * 2 + 1 = 63)
        textbutton "C) 63":
            style "botao_quiz"
            action Return("correto")

        # Botão D - Errado (Número aleatório próximo)
        textbutton "D) 46":
            style "botao_quiz"
            action Return("errado")

screen pergunta3_piloto():
    # 1. Imagem de Fundo
    add "cenariopiloto":
        zoom 0.5

    # 2. A Piloto (Mantendo a posição que você gostou)
    add "pilotosurpresa":
        xalign 0.9 
        yalign 1.0   
        zoom 0.25    

    # 3. Caixa da Pergunta
    frame:
        background "#3e1e3eCC"
        xalign 0.5
        yalign 0.11
        xsize 1100
        padding (30, 30)

        # --- CORREÇÃO DE ALINHAMENTO AQUI ---
        text "Pergunta 03 - ALERTA DE ENERGIA!\nO pouso exige {color=#ffeb3b}{b}25% de bateria{/b}{/color}, mas só temos {b}15%{/b}.\n\nO que acontece se tentarmos pousar agora?":
            color "#FFFFFF"
            text_align 0.5   # Garante que as linhas fiquem centralizadas (como um texto centralizado no Word)
            xalign 0.5       # Garante que o bloco de texto fique no meio exato da caixa roxa
            layout "subtitle" # Ajuda a distribuir o texto de forma mais bonita

    # 4. As Alternativas
    vbox:
        xalign 0.1
        yalign 0.7
        spacing 15

        # Botão A
        textbutton "A) O pouso ocorre normalmente":
            style "botao_quiz"
            action Return("errado")

        # Botão B - CORRETO
        textbutton "B) Falha total (Queda livre)":
            style "botao_quiz"
            action Return("correto")

        # Botão C
        textbutton "C) A nave usa energia solar":
            style "botao_quiz"
            action Return("errado")

        # Botão D
        textbutton "D) O sistema economiza sozinho":
            style "botao_quiz"
            action Return("errado")

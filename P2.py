#INTERSEÇÃO

#construtor
def cria_intersecao(col, lin):

    """
    Cria uma interseção do tabuleiro de Go identificada por uma coluna e uma linha.

    Parameters:
    - col (str): A coluna da interseção, representada por uma letra de 'A' a 'S'.
    - lin (int): A linha da interseção, representada por um número de 1 a 19.

    Returns:
    tuple(string, int): Um tuplo primeiro elemento a coluna e segundo elemento a linha da interseção.

    Raises:
    ValueError: Se o primeiro argumento não for uma string de comprimento 1, e se não estiver entre 'A' e 'S'
                Se o segundo argumento não for um interio entre 1 e 19

    Exemplo:
    cria_intersecao('B', 7)  # Retorna ('B', 7)
    """

    if (not isinstance(col, str) 
        or len(col) != 1 or not 'A' <= col <= 'S' 
        or not isinstance(lin, int) or not 1 <= lin <= 19
        ):
        raise ValueError('cria_intersecao: argumentos invalidos')
    
    return (col, lin)

#seletores
def obtem_col(i):
    """
    Obtém a coluna da interseção fornecida do tabuleiro de Go.

    Parameters:
    - i (tuple(string, int)): Um tuplo que é a representação interna de uma interseção, onde i[0] é a coluna.

    Returns:
    str: A coluna da interseção.

    Exemplo:
    obtem_col(('B', 7))  # Retorna 'B'
    """

    return i[0]

def obtem_lin(i):
    """
    Obtém a linha da interseção fornecida do tabuleiro de Go.

    Parameters:
    - i (tuple(string, int)): Um tuplo que é a representação interna de uma interseção, onde i[1] é a linha.

    Returns:
    int: A linha da interseção.

    Exemplo:
    obtem_col(('B', 7))  # Retorna 7
    """

    return i[1]

#reconhecedor
def eh_intersecao(arg):
    """
    Verifica se o argumento representa uma representação interna válida de uma interseção do tabuleiro de Go.

    Parameters:
    - arg: qualquer coisa

    Returns:
    bool: True se o argumento for uma interseção válida, False caso contrário.

    Exemplo:
    eh_intersecao(('B', 7))  # Retorna True
    eh_intersecao(('Z', 8))  # Retorna False
    """

    return (isinstance(arg, tuple) and len(arg) == 2
            and isinstance(arg[0], str) and len(arg[0]) == 1 and 'A' <= arg[0] <= 'S'
            and isinstance(arg[1], int) and 1 <= arg[1] <= 19
            )

def eh_intersecao_str(arg):
    """
    Verifica se a string fornecida representa externa válida de uma interseção do tabuleiro de Go.
    de 'A1' a 'S19'

    Parameters:
    - arg: qualquer tipo

    Returns:
    bool: True se representar uma interseção válida, False caso contrário.

    Exemplo:
    eh_intersecao_str('B7')  # Retorna True
    """
    return (isinstance(arg, str) and 2 <= len(arg) <= 3
            and 'A' <= arg[0] <= 'S' and arg[1:] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'))

#teste
def intersecoes_iguais(i1, i2):
    """
    Verifica se duas interseções no tabuleiro de Go são iguais.

    Parameters:
    - i1 (tuple(string, int)): representação interna da primeira interseção.
    - i2 (tuple(string, int)): representação interna da segunda interseção.

    Returns:
    bool: True se as interseções forem iguais, False caso contrário.

    Exemplo:
    intersecoes_iguais(('B', 7), ('B', 7))  # Retorna True
    """

    return (eh_intersecao(i1) and eh_intersecao(i2)
            and obtem_col(i1) == obtem_col(i2)
            and obtem_lin(i1) == obtem_lin(i2)
            )

#transformador
def intersecao_para_str(i):
    """
    Converte uma interseção no tabuleiro de Go em representação interna para representaçAo externa.

    Parameters:
    - i (tuple(string, int)): Um tuplo representando internamente a interseção.

    Returns:
    str: Uma string representando a interseção no formato 'A1' a 'S19'.

    Exemplo:
    intersecao_para_str(('B', 7))  # Retorna 'B7'
    """

    return obtem_col(i) + str(obtem_lin(i))

def str_para_intersecao(s):
    """
    Converte uma string para uma interseção no tabuleiro de Go.
    (representação externa para representação interna)

    Parameters:
    - s (str): Uma string representando uma interseção no formato 'A1' a 'S19'.

    Returns:
    tuple(string, int): representação interna da interseção.

    Exemplo:
    str_para_intersecao('B7')  # Retorna ('B', 7)
    """

    return cria_intersecao(s[0], int(s[1:]))

#funcoes de alto nivel
def obtem_intersecoes_adjacentes(i, l):
    """
    Obtém as interseções adjacentes a uma dada interseção no tabuleiro de Go.

    Parameters:
    - i (tuple(string, int)): Um tuplo representando internamente a interseção de referência.
    - l (tuple(string, int)): Um tuplo representando internamente a última interseção do tabuleiro (coluna máxima e linha máxima).

    Returns:
    tuple(tuple(string, int)): Um tuplo de tuplas representando internamente as interseções adjacentes.

    Exemplo:
    obtem_intersecoes_adjacentes(('B', 7), ('S', 19))
    # Retorna (('B', 6), ('A', 7), ('C', 7), ('B', 8)).
    """
    
    col = obtem_col(i)
    lin = obtem_lin(i)

    adjacentes = []

    #cima
    if lin > 1:
        adjacentes += [cria_intersecao(col, lin - 1),]
    #esquerda
    if col > 'A':
        adjacentes += [cria_intersecao(chr(ord(col) - 1), lin),]
    #direita
    if col < obtem_col(l):
        adjacentes += [cria_intersecao(chr(ord(col) + 1), lin),]
    #baixo
    if lin < obtem_lin(l):
        adjacentes += [cria_intersecao(col, lin + 1),]    

    return tuple(adjacentes)

def ordena_intersecoes(t):
    """
    Ordena uma sequência de interseções no tabuleiro de Go.
    lambda x: (x[1], x[0]) faz com que ordene primeiro por linha e depois por coluna

    Parameters:
    - t (tuple ou list): Uma sequência de interseções representadas internamente.

    Returns:
    tuple: Um tuplo contendo as interseções representadas internamente e ordenadas.

    Exemplo:
    ordena_intersecoes((('B', 7), ('A', 5), ('C', 8)))
    # Retorna (('A', 5), ('B', 7), ('C', 8))
    """

    return tuple(sorted(t, key = lambda x: (x[1], x[0])))

#PEDRAS

#construtor
def cria_pedra_branca():
    """
    Cria uma pedra branca para o jogo de Go.

    Returns:
    str: Uma string é a representação interna de uma pedra branca.
    """

    return 'O'

def cria_pedra_preta():
    """
    Cria uma pedra preta para o jogo de Go.

    Returns:
    str: Uma string é a representação interna de uma pedra preta.
    """

    return 'X'

def cria_pedra_neutra():
    """
    Cria uma pedra neutra para o jogo de Go.

    Returns:
    str: Uma string é a representação interna de uma pedra neutra.
    """

    return '.'

#reconhecedor
def eh_pedra(arg):
    """
    Verifica se o argumento representa uma pedra no jogo de Go.
    pedras possiveis: '.', 'X', 'O'

    Parameters:
    - arg: qualquer coisa

    Returns:
    bool: True se o argumento for uma pedra válida, False caso contrário.

    Exemplo:
    eh_pedra('O')  # Retorna True
    eh_pedra('A')  # Retorna False
    """

    return (arg in ('O', 'X', '.'))

def eh_pedra_branca(p):
    """
    Verifica se o argumento fornecido é a representação interna de uma pedra branca no jogo de Go.

    Parameters:
    - p: qualquer coisa.

    Returns:
    bool: True se a pedra for branca ('O'), False caso contrário.
    """

    return p == 'O'

def eh_pedra_preta(p):
    """
    Verifica se o argumento fornecido é a representação interna de uma pedra preta no jogo de Go.

    Parameters:
    - p: qualquer coisa.

    Returns:
    bool: True se a pedra for preta ('X'), False caso contrário.
    """

    return p == 'X'

def eh_pedra_neutra(p):
    """
    Verifica se o argumento fornecido é a representação interna de uma pedra neutra no jogo de Go.

    Parameters:
    - p: qualquer coisa.

    Returns:
    bool: True se a pedra for neutra ('.'), False caso contrário.
    """

    return p == '.'

#teste
def pedras_iguais(p1, p2):
    """
    Verifica se duas pedras no jogo de Go são iguais.

    Parameters:
    - p1: primeira pedra
    - p2: segunda pedra

    Returns:
    bool: True se forem pedras e iguais, False caso contrário.
    """

    return (eh_pedra(p1) and eh_pedra(p2)
            and p1 == p2
            )

#transformador
def pedra_para_str(p):
    """
    Converte uma pedra no jogo de Go para uma representação de string.

    Parameters:
    - p: representação interna de uma pedra no jogo de Go.

    Returns:
    str: A mesma string representando a pedra. (representação externa da pedra)
    """

    return p

#alto nivel
def eh_pedra_jogador(p):
    """
    Verifica se a pedra fornecida pertence a algum jogador no jogo de Go. (se é preta ou branca)

    Parameters:
    - p(any): representação interna de uma pedra no jogo de Go.

    Returns:
    bool: True se a pedra pertencer a algum jogador, False caso contrário.
    """

    return eh_pedra_branca(p) or eh_pedra_preta(p)

#auxiliar
def eh_tamanho_valido(n):
    """
    Verifica se o tamanho fornecido é válido para o tabuleiro de Go.

    Parameters:
    - n (int): Um número inteiro representando o tamanho do tabuleiro.

    Returns:
    bool: True se o tamanho for válido (9, 13, ou 19), False caso contrário.
    """
    return isinstance(n, int) and n in (9, 13, 19)

def ltr_para_num(col):
    return (ord(col) - 65) 

def num_para_ltr(num):
    return chr(num + 65)

def cria_goban_vazio(n):

    if not isinstance(n, int) or not eh_tamanho_valido(n):
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    return [['.' for _ in range(n)] for c in range(n)]

def cria_goban(n, ib, ip):
    """
    Cria um tabuleiro de Go (Goban) com pedras brancas e pretas nas posições especificadas.

    Parameters:
    - n (int): Um número inteiro representando o tamanho do tabuleiro (9, 13, ou 19).
    - ib (tuple): Um tuplo de interseções representando internamente as posições das pedras brancas.
    - ip (tuple): Um tuplo de interseções representando internamente as posições das pedras pretas.

    Returns:
    list(list(str)): Uma lista composta por listas representando o tabuleiro de Go com as pedras brancas ('O') e pretas ('X') nas posições indicadas.

    Raises:
    ValueError: Se n for tamnanho inválido, se tb ou tp não forem tuplos, ou se os seus elementos não forem todos representações internas de interseções.
    """

    if (not isinstance(n, int) or not eh_tamanho_valido(n) or not isinstance(ib, tuple) or not isinstance(ip, tuple) or 
        False in [eh_intersecao(t) for t in (ib + ip)]
        ):
        raise ValueError('cria_goban: argumentos invalidos')
    
    goban = cria_goban_vazio(n)

    if False in [eh_intersecao_valida(goban, t) for t in (ib + ip)]: 
        raise ValueError('cria_goban: argumentos invalidos')

    for i in ib:
        goban[ltr_para_num(obtem_col(i))][obtem_lin(i) - 1] = cria_pedra_branca()

    for i in ip:
        goban[ltr_para_num(obtem_col(i))][obtem_lin(i) - 1] = cria_pedra_preta()
    
    return goban

def cria_copia_goban(g):
    """
    Cria uma cópia do goban que esta totalmente desconectada da original

    Parameters:
    - g(list(list(str))): goban original

    Return:
    list(list(str)): cópia do goban original em nada conectada com ele
    """

    return [[g[col][lin] for lin in range(len(g))] for col in range(len(g))]

#seletores
def obtem_ultima_intersecao(g):
    """
    Obtém a última interseção (maior coluna e linha) de um tabuleiro de Go.

    Parameters:
    - g (list(list(str))): representação interna de um tabuleiro de Go.

    Returns:
    tuple: representação interna da última interseção
    """

    n = len(g)
    return cria_intersecao(num_para_ltr(n - 1), n)

def obtem_pedra(g, i):
    """
    Obtém a pedra em uma determinada interseção de um tabuleiro de Go.

    Parameters:
    - g (list): Uma lista bidimensional representando um tabuleiro de Go.
    - i (tuple): Uma tupla representando a interseção desejada.

    Returns:
    str: Uma string representando a pedra na interseção.
    """
    return g[ltr_para_num(obtem_col(i))][obtem_lin(i) - 1]

def obtem_cadeia(g, i):
    """
    Obtém a cadeia (grupo de pedras conectadas do mesmo tipo) a que uma interseção pertence em um tabuleiro de Go.

    Parameters:
    - g (list): Uma lista bidimensional representando um tabuleiro de Go.
    - i (tuple): Uma tupla representando a interseção desejada.

    Returns:
    tuple: Um tuplo contendo as interseções que compõem a cadeia ordenadas.
    """

    l = obtem_ultima_intersecao(g)
    p = obtem_pedra(g, i)
    cadeia, index = (i,), 0

    while index < len(cadeia):
        adjcacentes = obtem_intersecoes_adjacentes(cadeia[index], l)
        for a in adjcacentes:
            if a not in cadeia and p == obtem_pedra(g, a):
                cadeia += (a,)
        index += 1
    
    return ordena_intersecoes(cadeia)

#modificador
def coloca_pedra(g, i, p):
    """
    Coloca uma pedra em uma interseção específica em um tabuleiro de Go.

    Parameters:
    - g (list(list(str))): Uma lista bidimensional representando um tabuleiro de Go.
    - i (tuple): Uma tupla representando a interseção onde a pedra será colocada.
    - p (str): Uma string representando a pedra a ser colocada ('O' ou 'X').

    Returns:
    list: O goban atualizado após colocar a pedra na interseção especificada.
    """

    g[ltr_para_num(obtem_col(i))][obtem_lin(i) - 1] = pedra_para_str(p)
    return g

def remove_pedra(g, i):
    """
    Coloca uma pedra neutra na interseção desejada tendo o mesmo efeito que remover a pedra que lá estava
    """

    g[ltr_para_num(obtem_col(i))][obtem_lin(i) - 1] = '.'
    return g

def remove_cadeia(g, t):
    """
    Remove uma cadeia (grupo de pedras conectadas) do tabuleiro de Go.

    Parameters:
    - g (list): Uma lista bidimensional representando um tabuleiro de Go.
    - t (tuple): Uma tupla contendo as interseções que compõem a cadeia a ser removida.

    Returns:
    list: Uma lista bidimensional atualizada após remover a cadeia do tabuleiro.
    """

    for i in t:
        g = remove_pedra(g, i)
    return g

#reconhecedor
def eh_goban(arg):
    """
    Verifica se o argumento é uma representação interna válida de um tabuleiro de Go.

    Parameters:
    - arg: qualquer coisa.

    Returns:
    bool: True se o argumento for uma representação válida de um tabuleiro de Go, False caso contrário.
    """

    return (isinstance(arg, list) and
            len(arg) in (9, 13, 19) and
            all(isinstance(col, list) and len(col) == len(arg) and all(elem in ('.', 'X', 'O') for elem in col) for col in arg))

def eh_intersecao_valida(g, i):

    return (eh_intersecao(i) and 
            obtem_col(i) <= obtem_col(obtem_ultima_intersecao(g)) and
            obtem_lin(i) <= obtem_lin(obtem_ultima_intersecao(g))
            )

#teste
def gobans_iguais(g1, g2):

    return (eh_goban(g1) and eh_goban(g2) and len(g1) == len(g2)
            and not [g1[n] for n in range(len(g1)) if g1[n] != g2[n]]
            )

#transformador
def goban_para_str(g):
    
    s, n = '  ', obtem_lin(obtem_ultima_intersecao(g))

    def num_col(s):
        for col in range(n):
            s += ' ' + num_para_ltr(col)
        return s
    
    s = num_col(s)

    for lin in range(n - 1, -1, -1):
        num_lin = '{:>2}'.format(str(lin + 1))
        s += '\n' + num_lin

        for c in range(n):
            s += ' ' + pedra_para_str(obtem_pedra(g, cria_intersecao(num_para_ltr(c) , lin + 1)))   
            
        s += ' ' + num_lin
        
    s = num_col(s + '\n  ' )
        
    return s

#alto nivel
def obtem_territorios(g):
    l = obtem_ultima_intersecao(g)
    n = obtem_lin(l)
    territorio = ()
    for col in range(n):
        for lin in range(n):
            i = cria_intersecao(num_para_ltr(col), lin + 1)
            if eh_pedra_neutra(obtem_pedra(g, i)):
                cadeia = ordena_intersecoes(obtem_cadeia(g, i))
                if cadeia not in territorio: 
                    territorio += (cadeia,)

    return tuple(sorted(territorio, key = lambda x: (x[0][1], x[0][0])))

def obtem_adjacentes_diferentes(g, t):
    
    pedra, neutra = obtem_pedra(g, t[0]), cria_pedra_neutra()
    l = obtem_ultima_intersecao(g)
    adjacentes_diferentes = ()
    for i in t:
        adjacentes = obtem_intersecoes_adjacentes(i, l)
        for a in adjacentes:
            if (a not in t and a not in adjacentes_diferentes and
               ((pedra == neutra and obtem_pedra(g, a) != neutra) or 
                (pedra != neutra and obtem_pedra(g, a) == neutra))):
                adjacentes_diferentes += (a,)
            
    return ordena_intersecoes(adjacentes_diferentes)

def jogada(g, i, p):
    coloca_pedra(g, i, p)
    neutra = cria_pedra_neutra()
    
    for a in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
        if obtem_pedra(g, a) not in (neutra, p):
                cadeia = obtem_cadeia(g, a)
                if obtem_adjacentes_diferentes(g, cadeia) == ():
                    g = remove_cadeia(g, cadeia)
                
    return g

def obtem_pedras_jogadores(g):
    b, p = 0, 0

    n = obtem_lin(obtem_ultima_intersecao(g))
    for c in range(n):
        for l in range(n):
            i = cria_intersecao(chr(c + 65), l + 1)
            pedra = obtem_pedra(g, i)
            if eh_pedra_branca(pedra):
                b += 1
            elif eh_pedra_preta(pedra):
                p += 1

    return (b, p)

#funcoes adicionais
def calcula_pontos(g):
    """
    Calcula os pontos para os jogadores branco (O) e preto (X) em um tabuleiro de Go de acordo com as regras do jogo

    Parameters:
    - g (list): um goban

    Returns:
    tuple: Um tuplo contendo a pontuação dos jogadores branco e preto, respectivamente.
    """

    b = obtem_pedras_jogadores(g)[0]
    p = obtem_pedras_jogadores(g)[1]

    for t in obtem_territorios(g):
        
        adj = obtem_adjacentes_diferentes(g, t)
        
        if [a for a in adj if eh_pedra_branca(obtem_pedra(g, a))] and [a for a in adj if eh_pedra_preta(obtem_pedra(g, a))]:
            pass
        elif adj and eh_pedra_branca(obtem_pedra(g, adj[0])):
            b += len(t)
        elif adj and eh_pedra_preta(obtem_pedra(g, adj[0])):
            p += len(t)

    return (b, p)

def eh_jogada_legal(g, i, p, l):
    """
    Verifica se uma jogada é legal em um tabuleiro de Go.
    l é o tabuleiro de há duas jogadas atrás que não pode ser repetido

    Parameters:
    - g (list): Uma lista bidimensional representando um tabuleiro de Go.
    - i (tuple): Uma tupla representando a interseção onde a jogada será realizada.
    - p (str): Uma string representando a pedra a ser colocada ('O' ou 'X').
    - l (list): Uma lista de tabuleiros de Go representando o histórico de jogadas.

    Returns:
    bool: True se a jogada for legal, False caso contrário.
    """

    g_copia = cria_copia_goban(g)

    if obtem_pedra(g, i) != cria_pedra_neutra():
        return False
    
    jogada(g_copia, i, p)

    if len(obtem_adjacentes_diferentes(g_copia, obtem_cadeia(g_copia, i))) == 0:
        return False
    if gobans_iguais(g_copia, l):
        return False
    else:
        return True

def turno_jogador(g, p, l):
    """
    Realiza o turno de um jogador no jogo de Go.
    Se a jogada for ilegal continua a pedir uma jogada até esta ser legal
    Tem a opção de passar ('P')
    Altera o tabuleiro e o tabuleiro de há duas jogadas atrás

    Parameters:
    - g (list): Uma lista bidimensional representando o tabuleiro de Go.
    - p (str): Uma string representando a pedra do jogador atual ('O' ou 'X').
    - l (list): Uma lista de tabuleiros de Go representando o histórico de jogadas.

    Returns:
    bool: True se o jogador fez uma jogada válida, False se o jogador passou.
    """

    pedra = pedra_para_str(p)
    def recebe():

        msg = str(input(f"Escreva uma intersecao ou 'P' para passar [{pedra}]:"))
        if (msg == 'P' or (eh_intersecao_str(msg) and eh_intersecao_valida(g, str_para_intersecao(msg))
            and eh_jogada_legal(g, str_para_intersecao(msg), p, l))
            ):
            return msg
        else:
            return recebe()


    msg = recebe()

    if msg == 'P':
        return False
    

    jogada(g, str_para_intersecao(msg), p)
    l.clear()
    l.extend(cria_copia_goban(g))
    return True

def go(n, tb, tp):
    """
    Simula uma partida de Go entre dois jogadores.
    Para e mostra os resultados quando os jogadores passarem um após o outro

    Parameters:
    - n (int): Um número inteiro representando o tamanho do tabuleiro de Go (9, 13, ou 19).
    - tb (tuple): Uma tupla de interseções representando as posições das pedras brancas.
    - tp (tuple): Uma tupla de interseções representando as posições das pedras pretas.

    Returns:
    bool: True se o jogador branco (O) vence, False se o jogador preto (X) vence.

    Raises:
    ValueError: Se os argumentos não atenderem aos critérios especificados.
    """

    if (not eh_tamanho_valido(n) or not isinstance(tb, tuple) or not isinstance(tb, tuple) or
        [i for i in tb if not eh_intersecao_str(i) or not eh_intersecao_valida(cria_goban_vazio(n), str_para_intersecao(i))] or
        [i for i in tp if not eh_intersecao_str(i) or not eh_intersecao_valida(cria_goban_vazio(n), str_para_intersecao(i))] or
        [i for i in tb if i in tp]
        ):
        raise ValueError('go: argumentos invalidos')
    
    ib, ip = (), ()
    for i in tb:
        ib += (str_para_intersecao(i),)
    for i in tp:  
        ip += (str_para_intersecao(i),)

    g = cria_goban(n, ib, ip)
    lp = cria_goban_vazio(n)
    lb = cria_copia_goban(g)


    branco, preto = cria_pedra_branca(), cria_pedra_preta()

    def imprimir():
        print(f'Branco (O) tem {calcula_pontos(g)[0]} pontos')
        print(f'Preto (X) tem {calcula_pontos(g)[1]} pontos')
        print(goban_para_str(g))
    
    def joga_pretas(lp):
        imprimir()
        
        return turno_jogador(g, preto, lp)

    def joga_brancas(lb):
        imprimir()

        return turno_jogador(g, branco, lb)

    def go_aux(lb, lp):
        
        if (not joga_pretas(lp) and not joga_brancas(lb)) or (not joga_brancas(lb) and not joga_pretas(lp)):
            imprimir()
            pass
        
        else:
            
            return go_aux(lb, lp)

    
    go_aux(lb, lp)
       

    return calcula_pontos(g)[0] > calcula_pontos(g)[1]


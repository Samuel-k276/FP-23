# This is the Python script for your project
#ord('A') = 65

def eh_territorio(arg):
    
    '''Verifica se o argumento é um território válido.

    Para ser um território válido terá de:
    1. Ser um tuplo com entre 1 e 26 elementos (o território só pode ter de entre 1 a 26 colunas)
    2. Os seus elementos devem também ser tuplos com entre 1 e 99 elementos, com o mesmo tamanho (o território só pode ter de entre 1 a 99 linhas)
    3. Os elementos desses tuplos devem ser ou o inteiro 0 ou o inteiro 1

    Args:
        arg (anytype): argumento a verificar se preenche os requisitos para ser território

    Return: 
        True (bool): se preencher os requisitos para ser território
        False (bool): caso contrário

    Raises:
        Não tem nenhum 'Raise'
    '''

    #se o argumento é um tuplo, se tem entre 1 e 26 elementos e se o seu primeiro elemento é um tuplo
    if not isinstance(arg, tuple) or not (1 <= len(arg) <= 26) or not isinstance(arg[0], tuple): 
        return False
        
    Nh = len(arg[0])

    #um território só pode ter entre 1 e 99 linhas
    if not (0 < Nh < 100): 
        return False

    #se todos os elementos do argumento são tuplos e se o seu comprimento é igual ao do primeiro 
    for coluna in arg:
        if not isinstance(coluna, tuple) or len(coluna) != Nh: 
            return False

        #se todos os elementos desses tuplos são ou o inteiro 0 ou o inteiro 1
        for h in coluna:
            if not isinstance(h, int) or h not in (0, 1): 
                return False
    
    return True

def obtem_ultima_intersecao(t):

    '''Obtém a última interseção de cada território.
    
    A última interseção será aquela do canto superior direito, ou seja,
    a interseção da última coluna da última linha, no caso do território em formato de tuplo,
    será o último elemento do último tuplo do território

    Args:
        território (tuple(tuple(int))): território do qual vamos obter a última interseção 

    Return: 
        Tuplo de 2 elementos, do género (letra maiúscula de 'A' a 'Z', inteiro de 1 a 99)
        type: tuple(str, int)

    Raises:
        Não tem nenhum 'Raise'
    '''

    coluna = len(t)-1      #n. da última coluna começando a contar da esquerda no 0
    linha = len(t[coluna])    #n. da última linha começando a contar de baixo no 1
        
    #aqui uso a função chr() para 'transformar' o número da coluna numa letra maiúscula de A a Z (se coluna = 0, chr(coluna + 65) será 'A')
    return (chr(coluna + 65), linha)

def eh_intersecao(arg):

    '''Verifica se o argumento dado é uma interseção.
    
    Para ser uma interseção terá de:
    1. Ser um tuplo com 2 elementos
    2. O primeiro elemento terá de ser uma letra de 'A' a 'Z', ou seja, uma string de comprimento 1 de 'A' a 'Z'
    3. O segundo elemento terá de ser um inteiro de 1 a 99

    Args:
        arg (anytype): argumento a verificar se preenche os requisitos para ser interseção

    Return: 
        True (bool): se preencher os requisitos para ser interseção
        False (bool): caso contrário

    Raises:
        Não tem nenhum 'Raise'
    '''

    return (isinstance(arg, tuple) and len(arg) == 2                    
            and isinstance(arg[0], str) and len(arg[0]) == 1 and 'A' <= arg[0] <= 'Z'      
            and isinstance(arg[1], int) and 1 <= arg[1] <= 99)     

def eh_intersecao_valida(territorio, intersecao):

    '''Verifica se a interseção dada é válida.
    
    Para ser uma interseção válida terá de pertencer ao território, ou seja:
    1. Ter letra da coluna entre 'A' e a letra da coluna da última interseção
    2. Ter número da linha entre 1 e a letra da linha da última interseção
    
    Args:
        territorio (tuple(tuple(int))): um qualquer território
        intersecao (tuple(str, int)): interseção que vamos ver se pertence ao território

    Return: 
        True (bool): se a interseção pertencer ao território dado
        False (bool): caso contrário

    Raises:
        Não tem nenhum 'Raise'
    '''

    #verificar a validade dos argumentos
    if not eh_territorio(territorio) or not eh_intersecao(intersecao): 
        return False
    
    ultima_intersecao = obtem_ultima_intersecao(territorio)

    return ultima_intersecao[0] >= intersecao[0] and  ultima_intersecao[1] >= intersecao[1]

def eh_intersecao_livre(territorio, intersecao):

    '''Verifica se a interseção dada é livre (não tem montanha).
    
    Para ser uma interseção livre terá de ter valor igual a 0, ou seja:
    1. ord(intersecao[0]) - 65, será a posição do tuplo da coluna dentro do tuplo do território
    2. intersecao[1] - 1, será a posição da interseção dentro do tuplo da coluna 
    3. territorio[ord(intersecao[0]) - 65][intersecao[1] - 1] será 0 se for uma interseção livre

    Args:
        territorio (tuple(tuple(int))): um qualquer território
        intersecao (tuple(str, int)): interseção do território que vamos ver se é livre ou montanha

    Return: 
        True (bool): se a interseção do território estiver livre
        False (bool): se a interseção do território tiver uma montanha

    Raises:
        Não tem nenhum 'Raise'
    '''

    return territorio[ord(intersecao[0]) - 65][intersecao[1] - 1] == 0

def obtem_intersecoes_adjacentes(territorio, intersecao):

    '''Obtém as interseções adjacentes àquela dada.
    
    Temos 4 possíveis interseções adjacentes: 
    em cima -> (intersecao[0], linha + 1);
    em baixo -> (intersecao[0], linha - 1);
    esquerda -> (chr(coluna - 1), linha);
    direita -> (chr(coluna + 1), linha).
    Caso alguma destas coordenadas seja 'fora' do território, ou seja, não for uma interseção válida não será adicionada ao tuplo a ser retornado
    
    Args:
        territorio (tuple(tuple(int)))): um qualquer território
        intersecao (tuple(str, int)): interseção da qual vamos obter as suas adjacentes

    Return: 
        interseções ajacentes que são possíveis para o território dado, ou seja, que lhe pertencem
        type: tuple(tuple(str, int))

    Raises:
        Não tem nenhum 'Raise'
    '''

    adjacentes, coluna, linha = (), ord(intersecao[0]), intersecao[1]

    #criar uma lista com as 4 coordenads de interseções posiveis sem qualquer verificação
    possiveis = ((intersecao[0], linha - 1), (chr(coluna - 1), linha), (chr(coluna + 1), linha), (intersecao[0], linha + 1))

    #agora verificamos
    for intersecao_possivel in possiveis:
        if eh_intersecao_valida(territorio, intersecao_possivel):
            adjacentes += (intersecao_possivel,)     #se for uma interseção válida adiciona-se ao tuplo final

    return adjacentes
    
def ordena_intersecoes(intersecoes):

    '''Ordena um tuplo composto por interseções.

    Utiliza-se a função sorted(intersecoes, key)
    a key será = lambda x: (x[1], x[0]), assim desta forma troca-se a posição dos elementos do tuplo fazendo com que o sorted(),
    ordene primeiro pelo número da linha(x[1]) e depois pela letra da coluna(x[0])
    
    Args:
        intersecoes (tuple(tuple(str, int))): tuplo de interseções que vamos ordenar

    Return: 
        tuplo com as interseções ordenadas
        type: tuple(tuple(str, int))

    Raises:
        Não tem nenhum 'Raise'
    '''

    return tuple(sorted(intersecoes, key = lambda x: (x[1], x[0])))

def territorio_para_str(t):

    '''Transforma o território em formato de tuplo para uma string.

    A string será composta por:
    1. As letras que representam cada coluna (no início e no fim), parágrafo ('\n')
    2. Número da linha da última interseção, representação em str das interseções dessa linha ('X' ser for montanha, '.' se for livre), 
       número da linha da última interseção, parágrafo ('\n')
    3. E depois o mesmo para cada linha do território adaptado a essa linha

    nota: todos os elementos devem estar separados por um espaço (' '), e o espaço dedicado ao número da linha deve estar preparado para 
          linhas com números de 2 digítos    

    ex.: ((1,0,1),(0,0,1)) -> '   A B\n 3 X X  3\n 2 . .  2\n 1 X .  1\n   A B'
              
        e quando utilizamos a função print() com eesa string como argumento temos

                              A B
                            3 X X  3
                            2 . .  2
                            1 X .  1
                              A B
    
    Args:
        t (tuple(tuple(int)))): um qualquer território

    Return: 
        o território em formato de uma string, preparada para ser 'impressa' de forma a ilustrar o território
        type: str

    Raises:
        ValueError: se o argumento dado não for um território válido
    '''

    #verificar a validade dos argumentos
    if not eh_territorio(t):
        raise ValueError("territorio_para_str: argumento inválido")
    
    colunas, linhas, string, letras = len(t), len(t[0]), '  ', ''
        
    #letras das colunas no inicio
    for c in range(colunas):
        letras += " " + chr(c + 65)
    string += letras

    #incremento -1 pois a última linha tera de ser a primeira a ser adicionada à string
    for l in range(linhas - 1, -1, -1):
        #n. das linhas no inicio, ter sempre espaço para duas casas decimais
        string += '\n' + '{:>2}'.format(str(l+1))

        #adicionar à string 'X' caso seja uma montanha e '.' caso contrário
        for c in range(colunas):
            if t[c][l] == 0:
                string += " ."
            else:
                string += " X"
            
        #n. das linhas no final, ter sempre espaço para duas casas decimais
        string += " " + '{:>2}'.format(str(l+1))
        
    #letras das colunas no final
    string += '\n  ' + letras
        
    return string

def obtem_cadeia(territorio, intersecao):

    '''Obtem a cadeia da interseção dada para um dado território.

    Começamos por obter as interseções adjacentes à interseção dada e vemos se têm o mesmo valor (0 ou 1)
    se isso se verificar adiciona-se essas interseções a um tuplo que será a solução e a outro que utilizaremos
    para repetir este processo para as interseções da cadeia que ainda não analisámos as adjacentes.
    Quando nenhuma adjcaente for do mesmo tipo que a cadeia é porque a cadeia está completa e para-se o ciclo
    No final ordena-se a solução
    
    Args:
        territorio (tuple(tuple(int))): território dado
        intersecao (tuple(str, int)): interseção da qual vamos obter a cadeia

    Return: 
        tuplo com as interseções que pertencem à mesma cadeia da interseção dada
        type: tuple(tuple(str, int))

    Raises:
        ValueError: caso o território não seja válido, o argumento dado para a interseção não corresponda à definição de interseção,
                    ou se a interseção não for válida (não pertencer) ao território dado
    '''

    #verificar a validade dos argumentos
    if not eh_intersecao_valida(territorio, intersecao):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    
    n, confirmado, cadeia = True, (intersecao,), ()

    #obter o tipo da cadeia
    tipo = territorio[ord(intersecao[0]) - 65][intersecao[1] - 1]

    while n:
        #as intercecoes de valor igual confirmadas anteriormente adicionan-se à cadeia
        cadeia += confirmado
        n = False
        analise, confirmado = confirmado, ()

        #ver todas as intersecoes adjacentes que possam ser do mesmo tipo que os elementos da cadeia confirmados anteriormente
        #so analisamos os adicionados anteriormente pois seria redundante fazer o contrario
        for sitio in analise:

            adjacentes = obtem_intersecoes_adjacentes(territorio, sitio)
        
            for s in adjacentes:
                    
                #se ambos forem montanha/livre adicionar à cadeia e analisá-los da proxima vez
                if territorio[ord(s[0]) - 65][s[1] - 1] == tipo and s not in cadeia and s not in analise and s not in confirmado:
                    confirmado += (s,)
                    n = True

    #ordenar as intersecoes da cadeia
    cadeia = ordena_intersecoes(cadeia)

    return cadeia

def obtem_vale(territorio, intersecao):

    '''Obtem os vales da cadeia da interseção dada para um dado território.

    Um vale é: uma interseção livre adjacente a uma montanha
    1. Obter a cadeia da interseção dada
    2. Para cada elemento dessa cadeia, obter as adjacentes
    3. Para cada adjacente, se for uma interseção livre e ainda não estiver no tuplo dos vales, adicionã-la a esse tuplo
    4. Ordenar o tuplo dos vales
    
    Args:
        territorio (tuple(tuple(int))): território dado
        intersecao (tuple(str, int)): interseção que pertence à cadeia, da qual vamos obter os vales

    Return: 
        tuplo com as interseções que fazem fronteira com a cadeia da interseção dada
        type: tuple(tuple(str, int))

    Raises:
        ValueError: caso o território não seja válido, o argumento dado para a interseção não corresponda à definição de interseção,
                    ou se a interseção não for válida (não pertencer) ao território dado 
                    ou se a interseção dada for uma interseção livre
    '''

    #verificar a validade dos argumentos
    if not eh_intersecao_valida(territorio, intersecao) or eh_intersecao_livre(territorio, intersecao):
        raise ValueError("obtem_vale: argumentos invalidos")
    
    cadeia, vale = obtem_cadeia(territorio, intersecao), ()

    #para cada montanha da cadeia, a que a interseção dada pertence, analisar as intersecoes que lhe são adjacentes
    for i in cadeia:
        adjacentes = obtem_intersecoes_adjacentes(territorio, i)
            
        #para cada uma das adjacentes ver se pertence à cadeia, se não pertencer então é uma interseção livre adjacente à cadeia, ou seja, um vale
        for s in adjacentes:
            if s not in cadeia and s not in vale:
                vale += (s,)

    #ordenar o tuplo dos vales
    vale = ordena_intersecoes(vale)

    return vale

def verifica_conexao(territorio, intersecao_1, intersecao_2):

    '''Verifica se duas interseções estão connectadas por uma cadeia.

    Estarem conectadas por uma cadeia é o mesmo que dizer que pertencem à mesma cadeia
    Por isso, para ver se estão conectadas simplesmente vemos se a interseça_1 pertence à cadeia da intersecao_2
    Para isso utiliza-se a função obtem_cadeia(territorio, intersecao) anteriormente definida
    
    Args:
        territorio (tuple(tuple(int))): território dado a qual pertencem as interseções
        intersecao_1 (tuple(str, int)): interseção pertencente ao território 
        intersecao_2 (tuple(str, int)): interseção pertencente ao território 
    Return: 
        True(bool): as interseções estão conectadas
        False(bool): não estão conectadas

    Raises:
        ValueError: caso o território não seja válido, os argumentos dados para as interseções não correspondam à definição de interseção,
                    ou se alguma das interseções não for válida (não pertencer) ao território dado
    '''

    #verificar a validade dos argumentos
    if not eh_intersecao_valida(territorio, intersecao_1) or not eh_intersecao_valida(territorio, intersecao_2):
        raise ValueError("verifica_conexao: argumentos invalidos")
    
    #para ver se duas intersecoes estao conectadas vemos se a intercecao 1 pertence à cadeia da intersecao 2
    return intersecao_1 in obtem_cadeia(territorio, intersecao_2)

def calcula_numero_montanhas(territorio):

    '''Cálcula o númer de montanhas de um dado território.

    Como temos como argumento um território em formato de tuplo, basta contar o número de vezes que aparece o inteiro 1 nos tuplos
    do territorio (1 indica que a intereção é uma montanha)
    
    Args:
        territorio (tuple(tuple(int))): território dado

    Return: 
        o número de montanhas do território
        type: int

    Raises:
        ValueError: caso o território não seja válido
    '''


    #verificar a validade dos argumentos
    if not eh_territorio(territorio):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    
    num_montanhas = 0

    #percorrer os elementos dos sub-tuplos de territorio
    for coluna in territorio:
        for intersecao in coluna:
            if intersecao == 1: 
                num_montanhas += 1   #quando igual a 1 (ou seja, é montanha), aumentar o contador em 1

    return num_montanhas

def calcula_numero_cadeias_montanhas(territorio):

    '''Cálcula o número de cadeias de montanhas de um dado território.

    Vamos percorrer todas as interseções do território, caso seja uma montanha e ainda não esteja na lista com todas as montanhas do território,
    obtem-se a cadeia dessa montanha, adiciona-se todos os elementos dessa cadeia a uma lista, e aumenta-se a contagem em 1
    
    Args:
        territorio (tuple(tuple(int))): território dado

    Return: 
        o número de cadeias de montanhas do território
        type: int

    Raises:
        ValueError: caso o território não seja válido
    '''

    #verificar a validade dos argumentos
    if not eh_territorio(territorio):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    
    colunas, linhas, todas_montanhas, numero_cadeias = len(territorio), len(territorio[0]), [], 0

    #percorrer todas as 'interseções'
    for c in range(colunas):
        for i in range(linhas):

            intersecao = ((chr(c + 65), i + 1))

            if territorio[c][i] == 1 and intersecao not in todas_montanhas:

                todas_montanhas.append(intersecao)
                cadeia = obtem_cadeia(territorio, intersecao)

                for montanha in cadeia:
                    todas_montanhas.append(montanha)

                numero_cadeias += 1

    return numero_cadeias

def calcula_tamanho_vales(territorio):

    '''Cálcula o tamanho dos vales de um dado território.

    Um vale é: uma interseção livre adjacente a uma montanha
    1. Percorre-se todas as interseções do território
    2. Se for montanha, obter as adjacentes
    3. Para cada adjacente, se for um livre e ainda não estiver no tuplo dos vales, adioná-la lá

    
    Args:
        territorio (tuple(tuple(int))): território dado

    Return: 
        a quantidade de interseções livre que são consideradas vales
        type: int

    Raises:
        ValueError: caso o território não seja válido
    '''


    #verificar a validade dos argumentos
    if not eh_territorio(territorio):
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    
    colunas, linhas, = len(territorio), len(territorio[0])
    montanhas, vales = (), ()

    #primeiro criamos uma lista com todas as montanhas
    for c in range(colunas):
        for i in range(linhas):
            if territorio[c][i] == 1:
                montanhas += ((chr(c + 65), i + 1),)

    #agora montanha a montanha vemos se as intercecoes adjacentes sao livres (ou seja, vales)
    for montanha in montanhas:
        adjacentes = obtem_intersecoes_adjacentes(territorio, montanha)

        #se a intersecao for livre e ainda não estiver no tuplo dos vales, adiciona-se lá
        for intersecao in adjacentes:
            if eh_intersecao_livre(territorio, intersecao) and intersecao not in vales:
                vales += (intersecao,)  
        
    #len(vales) será o n. de interseções que são vales
    return len(vales)


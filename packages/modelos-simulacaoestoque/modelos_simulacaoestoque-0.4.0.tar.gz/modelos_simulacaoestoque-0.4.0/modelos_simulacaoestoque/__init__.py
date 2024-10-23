
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fCustoTotal(q_values, n, DemandaDiaria, Frete, CustoDia):
    """
Calcula o custo total do estoque, estocagem e frete baseado em diferentes quantidades de lotes iniciais.

Parâmetros:
q_values : list[int]
    Lista de quantidades/valores de cada lote para testar.
n : int
    Número total de dias(período) para o cálculo do estoque.
DemandaDiaria : int
    Quantidade diária(p/ período) de produto demandado.
Frete : float
    Custo de frete por lote.
CustoDia : float
    Custo diário de manter uma unidade em estoque.
    
Retorna:
df : pandas.DataFrame
    DataFrame contendo as quantidades testadas e seus respectivos custos totais, custos de estocagem e custos de frete.
"""
    resultados = []

    for q in q_values:
        Estoque = np.zeros(n)
        Lote = q
        Estoque[0] = Lote
        k = 1
        for i in range(1, n):
            Estoque[i] = Estoque[i - 1] - DemandaDiaria
            if Estoque[i] < DemandaDiaria:
                Estoque[i] = Estoque[i] + Lote
                k += 1
        Estocagem = CustoDia * Estoque
        CustoTotal = Estocagem.sum() + k*Frete
        resultado = {
            'Quantidade': q,
            'CustoTotal': CustoTotal,
            'Estocagem': Estocagem.sum(),
            'Frete': k*Frete
        }
        resultados.append(resultado)

    df = pd.DataFrame(resultados)
    return df

def fGraficoEstoque (q_values, n, DemandaDiaria):
    """
Plota o gráfico baseado em diferentes quantidades de lotes iniciais, dias e Demanda.

Parâmetros:
q_values : list[int]
    Lista de quantidades/valores de cada lote para testar.
n : int
    Número total de dias(período) para o cálculo do estoque.
DemandaDiaria : int
    Quantidade diária(p/ período) de produto demandado.

"""
    Dia = np.arange(1,n+1)
    for q in q_values:
        Estoque = np.zeros(n)
        Lote = q
        Estoque[0] = q
        k = 1
        for i in range(1, n):
            Estoque[i] = Estoque[i - 1] - DemandaDiaria
            if Estoque[i] < DemandaDiaria:
                Estoque[i] = Estoque[i] + Lote
                k = k + 1
        plt.figure()
        plt.bar(Dia, Estoque)
        plt.xlabel('Dia')
        plt.ylabel('Estoque')
        plt.title(f'Gráfico de Estoque para q = {q}')
        plt.show()

def fGraficoEstocagem (q_values, n, DemandaDiaria, CustoDia):
    """
Plota o gráfico de estocagem baseado em diferentes quantidades de lotes iniciais.

Parâmetros:
q_values : list[int]
    Lista de quantidades/valores de cada lote para testar.
n : int
    Número total de dias(período) para o cálculo do estoque.
DemandaDiaria : int
    Quantidade diária(p/ período) de produto demandado.
CustoDia : float
    Custo diário de manter uma unidade em estoque.
    
Retorna:
Gráfico:
    gráfico de estocagem.
"""
    Dia = np.arange(1,n+1)
    for q in q_values:
        Estoque = np.zeros(n)
        Lote = q
        Estoque[0] = q
        k = 1
        for i in range(1, n):
            Estoque[i] = Estoque[i - 1] - DemandaDiaria
            if Estoque[i] < DemandaDiaria:
                Estoque[i] = Estoque[i] + Lote
                k += 1
        Estocagem = CustoDia * Estoque
        plt.figure()
        plt.bar(Dia, Estocagem, color = 'red')
        plt.xlabel('Dia')
        plt.ylabel('Estocagem')
        plt.title(f'Gráfico de Custo de Estocagem para q = {q}')
        plt.show()
        
def fLoteEconomico (DemandaTotal, Frete, CustoEstocagemTotal):
    """
Calcula o custo total do estoque, estocagem e frete baseado em diferentes quantidades de lotes iniciais.

Parâmetros:
    
 - DemandaTotal (float): Lista de quantidades/valores de cada lote para testar.
    
 - Frete (float): Custo de frete por lote.
 
 - CustoEstocagemTotal (float): Custo Total de Estocagem (pro período todo).
    
Retorna:
    - q (float): Retorna o valor da quantidade que minimiza os custos de estoque.
"""
    from numpy import sqrt
    q=sqrt((2*Frete*DemandaTotal)/CustoEstocagemTotal)
    return q

def fPerdaTotal(q, n, PrecoExcesso, PrecoFalta, p0, p1, x01, p2, p3, x23, p4, p5, x45):
    """
Calcula o total de perdas financeiras com base na quantidade disponível e na demanda em diferentes períodos.

Parâmetros:
    
- q (float): Quantidade de estoque disponível/médio.

- n (int): Número total de períodos a serem analisados.

- PrecoExcesso (float): Perda por unidade de excesso de estoque.

- PrecoFalta (float): Perda por unidade de falta de estoque.

- p0 (int): Índice inicial do intervalo de demanda baixa.

- p1 (int): Índice final do intervalo de demanda baixa.

- x01 (float): Valor da demanda nos períodos de demanda baixa.

- p2 (int): Índice inicial do intervalo de demanda média.

- p3 (int): Índice final do intervalo de demanda média.

- x23 (float): Valor da demanda nos períodos de demanda média.

- p4 (int): Índice inicial do intervalo de demanda alta.

- p5 (int): Índice final do intervalo de demanda alta.

- x45 (float): Valor da demanda nos períodos de demanda alta.

Retorna:

    - PerdaTotal (float): Soma total das perdas por excesso e falta de estoque.
"""
    Demanda = np.zeros(n)
    Demanda[p0:p1] = x01 # demanda baixa
    Demanda[p2:p3] = x23 # demanda média
    Demanda[p4:p5] = x45 # demanda alta
    Perda = np.zeros(n) # Vetor para armazenar as perdas financeiras
    for i in range(0,n):
        if q >= Demanda[i]: # Perda por excesso
            Perda[i] = PrecoExcesso*(q - Demanda[i])
        else:
            Perda[i] = PrecoFalta*(Demanda[i] - q) # Perda por falta
            
    PerdaTotal = sum(Perda) # Cálculo da perda total de excesso e falta
    return PerdaTotal   

def fMonteCarloPerda(Dias, p1, p3, x01, x23, x45, PrecoExcesso, PrecoFalta, qmax, num_simulacoes):
    """
Calcula as possibilidades de Perda baseada em simulações com números aleatórios

Parâmetros:
    
- Dias (int): Número total de períodos a serem analisados.

- n (int): Número total de períodos a serem analisados.

- p1 (int): Índice final do intervalo de demanda baixa.

- p3 (int): Índice final do intervalo de demanda média.

- x01 (float): Valor da demanda nos períodos de demanda baixa.

- x23 (float): Valor da demanda nos períodos de demanda média.

- x45 (float): Valor da demanda nos períodos de demanda alta.

- PrecoExcesso (float): Perda por unidade de excesso de estoque.

- PrecoFalta (float): Perda por unidade de falta de estoque.

- qmax (float): Número máximo que a quantidade pode assumir

- num_simulacoes (int): Número de simulações que a função irá fazer.

Retorna:

    - Gráfico com as n simulações, além de retornar também da menor perda e sua respectiva quantidade.
"""    
    def fGeraDemanda():
        x = np.random.randint(1, Dias, Dias-1)
        Demanda = np.zeros(Dias-1)
        Demanda[x <= p1] = x01
        Demanda[(x > p1) & (x <= p3)] = x23
        Demanda[x > p3] = x45
        return Demanda

    def fPerdaAcumulada(q):
        Demanda = fGeraDemanda()
        Perda = np.where(q <= Demanda, PrecoFalta * (Demanda - q), PrecoExcesso * (q - Demanda))
        PerdaAcumulada = np.sum(Perda)
        return PerdaAcumulada
    
    vQuant = np.arange(1, qmax + 1)
    melhor_perda = np.inf
    melhor_q = None

    for simulacao in range(num_simulacoes):
        vPerdas = np.zeros(qmax)
        for idx, q in enumerate(vQuant):
            perda_atual = fPerdaAcumulada(q)
            vPerdas[idx] = perda_atual
            if perda_atual < melhor_perda:
                melhor_perda = perda_atual
                melhor_q = q

        plt.plot(vQuant, vPerdas, label=f'Simulação {simulacao + 1}')
    
    plt.xlabel('Quantidade (q)')
    plt.ylabel('Perda Acumulada')
    plt.title('Perda Acumulada em Função da Quantidade')
    plt.legend()
    plt.show()

    print(f"A menor perda acumulada foi {melhor_perda:.2f} na quantidade {melhor_q}.")


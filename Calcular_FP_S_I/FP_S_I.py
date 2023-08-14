import math as mt

while True:
    Tensao = float(input("Qual a tensão da fonte ?"))
    Potencia = float(input("Insira aqui sua potência ativa: "))
    PotenciaAparente = float(input("Insira aqui sua potência aparente: "))

    Calcular_potencia_S_modulo = mt.sqrt((Potencia**2)+(PotenciaAparente**2))
    Calcular_potencia_aparente_angulo = mt.atan(PotenciaAparente/Potencia)

    S_em_graus = mt.degrees(Calcular_potencia_aparente_angulo)

    Calcular_fator_de_potencia = (mt.cos(S_em_graus))

    Impedancia_equivalente = (((Tensao**2)*Calcular_fator_de_potencia)/Potencia)

    print(f"Sua potência aparente possui um módulo de:" ,Calcular_potencia_S_modulo)
    print(f"O angulo da sua potencia aparente é de :", S_em_graus)
    print(f"Seu fator de potência é de:", Calcular_fator_de_potencia)
    print(f"Sua impedância equivalente é de :", Impedancia_equivalente)

    if Tensao == 0 or Potencia == 0 or PotenciaAparente == 0 :
        print("Operacao abortada")
        break

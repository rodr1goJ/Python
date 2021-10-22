from clsReta import Retangulo

i = True
while i:
        print('#################################################')
        print('############ Bem Vindo ao programa! #############')
        print('#################################################')
        op = int(input('                Digite:\n'
           '(1) Para escolher os tamanhos da planta. \n'
           '(2) Para escolher o tamanho do piso.\n'
           '(3) Para escolher o tamanho do rodapé.\n'
           '(4) Para fazer os calculos.\n'
           '(5) Para mostrar os dados.\n'
           '(6) Para sair. \n'
           'Opção:'))
##########################################################################
        if op == 1:
            Plan1 = input('Digite o valor do primeiro lado da planta:')
            Plan2 = input('Digite o valor do segundo lado da planta:')
            check1 = True
        elif op == 2:
            Piso1 = input('Digite o valor do primeiro lado do Piso:')
            Piso2 = input('Digite o valor do segundo lado da Piso:')
            check2 = True
        elif op == 3:
            roda1 = input('Digite o valor do primeiro lado do rodapé:')
            roda2 = input('Digite o valor do segundo lado do rodapé:')
            check3 = True
        elif op == 5:

            i=False
        elif op == 6:
            print('Encerrando...')
            i=False
#############################################################################################
        elif op == 4:
            planta = Retangulo(Plan1, Plan2)
            peri1 = planta.calc_peri()
            area1 = planta.calc_Size()
            piso = Retangulo(Piso1, Piso2)
            area2 = piso.calc_Size()
            rodape = Retangulo(roda1,roda2)
            op2 = int(input('                Digite:\n'
                            '(1) calcular area da planta. \n'
                            '(2) calcular o perimetro da planta.\n'
                            '(3) calcular quantas peças de piso serão usados. \n'
                            '(4) calcular quantos rodapés serão usados.\n'
                            'Opção:'))
            if op2 == 1:
                    print(area1)
                    check4=True
            elif op2 ==2:
                    print(peri1)
                    check5=True
            elif op2 ==3:
                    total=float(area1/area2)
                    print(total)
                    check6=True
            elif op2 ==4:
                    peri2 = rodape.calc_peri()
                    Total2=float(peri1/peri2)
                    print(Total2)
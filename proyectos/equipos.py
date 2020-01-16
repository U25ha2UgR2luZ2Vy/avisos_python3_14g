
with open('becarios.txt', 'r') as becarios:

    nombres = {nom.rstrip() for nom in filter(lambda nombre: nombre[0] != '-', becarios.readlines())}

    while nombres:
        
        entrada = input('\nCuántos?: ')

        if entrada == 'sobran':
            print()
            print('\tSobran {}'.format(len(nombres)))
        else:
            print()
            try:
                for n in range(int(entrada)):
                    print('\t{}'.format(nombres.pop()))
            except KeyError:
                exit
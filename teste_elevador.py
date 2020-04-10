import controle

ElevadorPares = controle.Elevador(3, [-2, -4, -6, 2, 4, 6])
ElevadorImpares = controle.Elevador(3,[-2, -1, -3, -5, 1, 3, 5, 6])
ElevadorTodos = controle.Elevador(3,[-1, 0, 1, 2, 3, 4, 5])

Predio1 = controle.Predio(6, -2, [ElevadorTodos, ElevadorImpares])

Predio1.printPredio()

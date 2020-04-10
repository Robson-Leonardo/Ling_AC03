import controle

ElevadorPares = controle.Elevador(3,[-2,-4,-6,2,4,6])
ElevadorImpares = controle.Elevador(3,[-1,-3,-5,1,3,5])


ElevadorPares.deslocar_para(3)
ElevadorPares.printelevador()
ElevadorPares.deslocar_para(1)
ElevadorPares.printelevador()
ElevadorPares.deslocar_para(6)
ElevadorPares.printelevador()
ElevadorPares.deslocar_para(2)
ElevadorPares.printelevador()
ElevadorPares.deslocar_para(-1)
ElevadorPares.printelevador()
ElevadorPares.deslocar_para(-2)
ElevadorPares.printelevador()
ElevadorPares.deslocar_para(0)
ElevadorPares.printelevador()
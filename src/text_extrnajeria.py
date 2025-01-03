from extranjeria import*

def test_lee_datos_extranjeria(extranjeria:List[RegistroExtranjeria])->None:
    print(f"Leídos {len(extranjeria)} registros.")
    print("Mostrando los 3 primeros:")
    for e in extranjeria[:3]:
        print(e)
    print("Mostrando los 3 últimos:")
    for e in extranjeria[-3:]:
        print(e)

def test_numero_nacionalidades_distintas(extranjeria:List[RegistroExtranjeria])->None:
    numero=numero_nacionalidades_distintas(extranjeria)
    print(f"Hay {numero} nacionalidades distintas en los datos.")

def test_secciones_distritos_con_extranjeros_nacionalidades(extranjeria:List[RegistroExtranjeria],paises:set)->None:
    lista=secciones_distritos_con_extranjeros_nacionalidades(extranjeria,paises)
    print(f"Hay {len(lista)} secciones de distritos con residentes cuya procedencia es {paises}.")
    print("Mostrando 3 secciones:")
    print(lista[:3])

def test_total_extranjeros_por_pais(extranjeria:List[RegistroExtranjeria])->None:
    dicc=total_extranjeros_por_pais(extranjeria)
    print("Mostrando el número de residentes para algunos países de procedencia:")
    print(f"ALEMANIA: {dicc['ALEMANIA']}")
    print(f"ITALIA: {dicc['ITALIA']}")
    print(f"MARRUECOS: {dicc['MARRUECOS']}")

def test_top_n_extranjeria(extranjeria:List[RegistroExtranjeria],n:Optional[int]=3)->None:
    lista=top_n_extranjeria(extranjeria,n)
    print(f"Mostrando los {n} países de los que proceden más residentes:")
    print(lista)

def test_barrio_mas_multicultural(extranjeria:List[RegistroExtranjeria])->None:
    nombre=barrio_mas_multicultural(extranjeria)
    print(f"El barrio más multicultural de sevilla es {nombre}")

def test_barrio_con_mas_extranjeros(extranjeria:List[RegistroExtranjeria])->None:
    nombre1=barrio_con_mas_extranjeros(extranjeria)
    nombre2=barrio_con_mas_extranjeros(extranjeria,'Hombres')
    nombre3=barrio_con_mas_extranjeros(extranjeria,'Mujeres')
    print(f"El barrio con más residentes extranjeros es {nombre1}.")
    print(f"El barrio con más hombres residentes extranjeros es {nombre2}.")
    print(f"El barrio con más mujeres residentes extranjeros es {nombre3}.")

def test_pais_mas_representado_por_distrito(extranjeria:List[RegistroExtranjeria])->None:
    dicc=pais_mas_representado_por_distrito(extranjeria)
    print("Los países con más residentes en cada distrito son los siguientes:")
    for c,v in dicc.items():
        print(f"Distrito:{c} => {v}")

if __name__=='__main__':
    extranjeria=lee_datos_extranjeria('data/extranjeriaSevilla.csv')
    #print("TEST DE LA FUNCIÓN lee_datos_extranjeria:")
    #test_lee_datos_extranjeria(extranjeria)
    #print("TEST DE LA FUNCIÓN numero_nacionalidades_distintas:")
    #test_numero_nacionalidades_distintas(extranjeria)
    #print("TEST DE LA FUNCIÓN secciones_distritos_con_extranjeros_nacionalidades:")
    #test_secciones_distritos_con_extranjeros_nacionalidades(extranjeria,{'ALEMANIA','ITALIA'})
    #print("TEST DE LA FUNCIÓN total_extranjeros_por_pais:")
    #test_total_extranjeros_por_pais(extranjeria)
    #print("TEST DE LA FUNCIÓN top_n_extranjeria:")
    #test_top_n_extranjeria(extranjeria,5)
    #print("TEST DE LA FUNCIÓN barrio_mas_multicultural:")
    #test_barrio_mas_multicultural(extranjeria)
    #print("TEST DE LA FUNCIÓN barrio_con_mas_extranjeros:")
    #test_barrio_con_mas_extranjeros(extranjeria)
    #print("TEST DE LA FUNCIÓN pais_mas_representado_por_distrito:")
    #test_pais_mas_representado_por_distrito(extranjeria)
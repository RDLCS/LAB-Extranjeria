from typing import Optional,List,Set,Tuple,NamedTuple,Dict,DefaultDict
from datetime import date,time,datetime,timedelta
import csv

RegistroExtranjeria = NamedTuple("RegistroExtranjeria",[("distrito",str),("seccion", str),("barrio", str),("pais",str),
            ("hombres", int),("mujeres", int)])

def lee_datos_extranjeria(ruta:str)->List[RegistroExtranjeria]:
    lista=list()
    with open(ruta,'rt',encoding='utf-8') as f:
        iter=csv.reader(f)
        next(iter)
        for distrito,seccion,barrio,pais,hombres,mujeres in iter:
            hombres=int(hombres)
            mujeres=int(mujeres)
            lista.append(RegistroExtranjeria(distrito,seccion,barrio,pais,hombres,mujeres))
    return lista

def numero_nacionalidades_distintas(extranjeria:List[RegistroExtranjeria])->int:
    conjunto=set()
    for e in extranjeria:
        conjunto.add(e.pais)
    return len(conjunto)

def secciones_distritos_con_extranjeros_nacionalidades(extranjeria:List[RegistroExtranjeria],paises:set)->List[Tuple[str,str]]:
    lista=set()
    for e in extranjeria:
        if e.pais in paises:
            lista.add((e.distrito,e.seccion))
    return sorted(lista,key=lambda e:(e[0],e[1]))

def total_extranjeros_por_pais(extranjeria:List[RegistroExtranjeria])->Dict[str,int]:
    dicc=DefaultDict(int)
    for e in extranjeria:
        dicc[e.pais]+=(e.hombres+e.mujeres)
    return dicc

def top_n_extranjeria(extranjeria:List[RegistroExtranjeria],n:Optional[int]=3)->List[Tuple[str,int]]:
    dicc=DefaultDict(int)
    for e in extranjeria:
        dicc[e.pais]+=(e.hombres+e.mujeres)
    return sorted(dicc.items(),key=lambda e:e[1],reverse=True)[:n]

def barrio_mas_multicultural(extranjeria:List[RegistroExtranjeria])->str:
    dicc=DefaultDict(set)
    for e in extranjeria:
        dicc[e.barrio].add(e.pais)
    for c,v in dicc.items():
        dicc[c]=len(v)
    return max(dicc,key=dicc.get)

def barrio_con_mas_extranjeros(extranjeria:List[RegistroExtranjeria],tipo:Optional[str]=None)->str:
    dicc=DefaultDict(int)
    for e in extranjeria:
        if tipo=='Hombres':
            dicc[e.barrio]+=e.hombres
        elif tipo=='Mujeres':
            dicc[e.barrio]+=e.mujeres
        elif tipo==None:
            dicc[e.barrio]+=(e.hombres+e.mujeres)
    return max(dicc, key=dicc.get)

def pais_mas_representado_por_distrito(extranjeria:List[RegistroExtranjeria])->Dict[str,str]:
    dicc=DefaultDict(list)
    for e in extranjeria:
        dicc[e.distrito].append((e.pais,(e.hombres+e.mujeres)))
    for c,v in dicc.items():
        dicc[c]=calcula_el_mejor(v)
    return dicc

def calcula_el_mejor(paises:List[Tuple[str,int]])->str:
    dicc=DefaultDict(int)
    for p in paises:
        dicc[p[0]]+=p[1]
    return max(dicc,key=dicc.get)
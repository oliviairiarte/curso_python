
conj1= {1,2,3,4}
conj2= {1,2,3,4,5}

# es subconjunto?
result= conj2 <= conj1
result_opc2= conj2.issubset(conj1)

print(result)
print(result_opc2)

# es superconjutno
resul= conj2 > conj1
resul_opc2= conj2.issuperset(conj1)

# hay algun num en comun
hay= conj2.isdisjoint(conj1)

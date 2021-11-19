bonecos = 0
arquitetos = 0
musicos = 0
desenhistas = 0


n = int(input())

for i in range(0,n,1):
    dados = input().split(' ')
    e = dados[0]
    g = dados[1]
    h = int(dados[2])

    if(g == "bonecos"):
        bonecos += h
    elif(g == "arquitetos"):
        arquitetos += h 
    elif(g == "musicos"):
        musicos += h   
    elif(g == "desenhistas"):
        desenhistas += h              


print(int(bonecos / 8) + int (arquitetos / 4) + int(musicos / 6) + int(desenhistas / 12 ))


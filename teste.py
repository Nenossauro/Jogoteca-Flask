import os, pymongo, random, time


os.system("cls")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["biblioteca"]



collection = db["users"]
collectionl = db["livros"]

"""livros_like = collection.find({"nome": "Nenossauro"})
print("livro like=",livros_like)
for item in livros_like:
    print("item=",item)
    v_id = item["like"]
    print("v_id=",v_id)
    for livro_id in v_id:
        print("livro_id=",livro_id)
        livro = collectionl.find_one({"id": int(livro_id)})
        if livro:
            v_l = livro["nome"]
            print("v_l=",v_l)"""



livros_like = collection.find({"nome": "akiox0202"})
print("livro like=",livros_like)
for item in livros_like:
    print("item=",item)
    v_id = item["like"]
    print("v_id=",v_id)

nomes = []
for ids in range(len(v_id)):
    print("iteração: ",ids)
    print("id a procurar: ",v_id[ids])
    livros = collectionl.find({"id":v_id[ids]})
    print("Procurando id: ",v_id[ids])
    for livro in livros:
        v_l = livro["nome"]
        nomes.append(v_l)
        print("v_l=",v_l)
print(nomes)

"""nome = 'tiranorei4@gmail.com'
senha = '###'
temp_user = ''
temp_senha = ''
usuario = collection.find({"email": nome})
for users in usuario:
    temp_user = users["email"]
    print(temp_user)
    temp_senha = users["senha"]

if senha == temp_senha:
    print("Certo")
else:
    print(usuario)
    print("Errado")

collection_livros = db["livros"]
livros_id = collection_livros.find()
livro = []
ids = []
for item in livros_id:
    v_item = item["nome"]
    v_id = item["id"]
    livro.append(v_item)
    ids.append(v_id)
for capa in ids:
    print(livro[int(capa)])"""

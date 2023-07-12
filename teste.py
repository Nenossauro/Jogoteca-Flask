import os, pymongo, random, time


os.system("cls")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["biblioteca"]
collection = db["users"]

nome = 'tiranorei4@gmail.com'
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
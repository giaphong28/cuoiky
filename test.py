
import pymongo

myclient = pymongo.MongoClient("mongodb://longnguyenuit:ZkhrACfJflUhurRi1xUBFVLXMxNQrn2czSp5yHvomR4pvzmRPJX4niIdQT0FxdJCRVUtTx0eUkv4ACDbiTmXsQ%3D%3D@longnguyenuit.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@longnguyenuit@")
mydb = myclient["result"]
mycol = mydb["06-12-2023"]
x = mycol.find_one()
print(x['userID'])
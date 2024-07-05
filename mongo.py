import pymongo
myclient = pymongo.MongoClient("mongodb+srv://probe0:probe0@audioprobe.yoroiqf.mongodb.net/?retryWrites=true&w=majority&appName=audioprobe")

mydb = myclient["audioprobe"]
mycol = mydb["audioprobe"]


mydict = { "probe": "probe0", "file_name": "https://storage.cloud.google.com/audioprobe/2024-07-05%2022%3A37%3A57.970695.wav" }

x = mycol.insert_one(mydict)
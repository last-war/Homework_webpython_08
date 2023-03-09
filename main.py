from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://andreymaybrodskyy:wwiQ2COydUGOXseZ@cluster0.jjvfy66.mongodb.net/?retryWrites=true&w=majority"
)

db = client.goodword

def load_json():
    pass


if __name__ == '__main__':
    print('PyCharm')


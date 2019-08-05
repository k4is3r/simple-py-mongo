from pymongo import MongoClient


def db_conecction(dir):
    client = MongoClient(dir)
    if client:
        print('DB Conected')
        return client
    else:
        print('DB fail conecction')


def add_document_db(client):
    client = client
    db = client['teststore']
    collection = db['products']
    print('Insert client ')
    name = input('Name : ')
    price = input('Price: ')
    secction = input('Secction: ')
    docu = {'name': name, 'price': price, 'secction': secction}
    if collection.insert_one(docu):
        print('{} insert in DB '.format(docu['name']))


def update_document_db(client):
    db = client['teststore']
    collection = db['products']
    pro = input('What product do you want to update? ')
    if collection.find_one({'name': pro}):
        name = input('Insert new name: ')
        price = input('Insert new price: ')
        secction = input('Insert new seccition: ')
        collection.update_one(
            {'name': pro}, {'$set': {'name': name, 'price': price, 'secction': secction}})
        print('Document updated succesfull')
    else:
        print('Documents not found, insert a existing document')


def delete_document_db(client):
    db = client['teststore']
    collection = db['products']
    delclient = input('Insert product to delete: ')
    if collection.find_one({'name': delclient}):
        collection.delete_one({'name': delclient})
        print('{} deleted succesfull'.format(delclient))
    else:
        print('Document not found in the DB')


def show_documents_db(client):
    db = client['teststore']
    collection = db['products']
    results = collection.find()
    print('****** Documents in DB *******')
    for r in results:
        print('________________________')
        print('ID: {}'.format(r['_id']))
        print('Name :{}'.format(r['name']))
        print('Price : {}'.format(r['price']))
        print('Secction: {}'.format(r['secction']))


def delete_all_db(client):
    db = client['teststore']
    collection = db['products']
    collection.delete_many({})
    print('All DB was deleted')


if __name__ == '__main__':
    MONGO_URI = 'mongodb://localhost'
    client = db_conecction(MONGO_URI)
    print('Welcome to K4is3r DB')
    print('What you want to do? ')
    print('__________________')
    print('1. Add product to DB')
    print('2. Update product to DB')
    print('3. Delete product DB')
    print('4. Show all prodcuts in DB')
    print('5. Delete all DB')
    opc = int(input('Insert number : '))
    if opc == 1:
        add_document_db(client)
    elif opc == 2:
        update_document_db(client)
    elif opc == 3:
        delete_document_db(client)
    elif opc == 4:
        show_documents_db(client)
    elif opc == 5:
        res = input('Are you sure to delete all DB? ')
        if res == 'yes':
            delete_all_db(client)
        else:
            print('Ok')
    else:
        print('Introduce a valid option')

    #db = client['teststore']
    #collection = db['products']
    # add one to DB
    #collection.insert_one({"_id": 2, "name": "keyboard", "price": 300})
    """add many to db
    product_one = {'name': 'mouse'}
    product_two = {'name': 'monitor'}
    collection.insert_many([product_one, product_two])
    """
    """Para buscar un elemento en la base de datos y para mostratlos todos
    results = collection.find()
    for r in results:
        print(r['name'])
    result_price = collection.find({'price': 300})
    for r in result_price:
        print(r)
    result_one = collection.find_one({'name': 'mouse'})
    print(result_one)
    """
    """Eliminar datos de la DB
    collection.delete_many({'price': 300})
    collection.delete_one({'name': 'monitor'})
    collection.delete_many({})
    """
    #collection.insert_one({'name': 'laptop'})
    #collection.update_one({'name': 'laptop'}, {'$set': {'name': 'keyboard', 'price': 300}})
    #collection.update_one({'name': 'keyboard'}, {'$inc': {'price': 30}})
    #number_product_db = collection.count_documents({})
    # print(number_product_db)

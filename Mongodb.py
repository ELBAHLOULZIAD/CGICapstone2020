from pymongo import MongoClient
#database authorization
client = MongoClient("mongodb://CGI:test@cluster0-shard-00-00.lf4fg.mongodb.net:27017,cluster0-shard-00-01.lf4fg.mongodb.net:27017,cluster0-shard-00-02.lf4fg.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-p7c8qo-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('resume_db')
records = db.resume_records



#print all the records from the database
def case1():

   # print(list(records.find()))
    mydoc = records.find()

    for x in mydoc:
      print(x)

#find all the records by location
def case2():

    search_words=input('Enter a location ')
  #  try:
    mydoc = records.find({'location': search_words})

    for x in mydoc:
      print(x)

    #print(records.find_many({'location': search_words}))
  #  except Exception as e:

  #       print(records.find_one({'location': search_words}))
#find the records by subject    
def case3():
    search_words=input('Enter a subject ')


    mydoc = records.find({'subject': search_words})

    for x in mydoc:
      print(x)

##    try:
##        print(records.find_many({'subject': search_words}))
##    except Exception as e:
##        print(records.find_one({'subject': search_words}))


#insert a new single record
def case7():
    search_words1=input('Enter first name\n')
    search_words2=input('Enter last name\n')
    search_words3=int(input('Experience\n'))
    search_words4=input('location\n')
    search_words5=input('subject\n')

    new_resume = {
       'fname': search_words1,
       'lname': search_words2,
       'experience': search_words3,
       'subject' : search_words5,
       'location' : search_words4
    }
    records.insert_one(new_resume)


#update a specific record
def case4():
    search_words1=input('Enter first name\n')
    search_words2=input('Enter last name\n')
    search_words3=input('What do you want to update?')
   # search_words4=input('Enter update\n')
    resume_updates = {
            search_words3 : input('Enter update\n')
        }
    records.update_one({'fname': search_words1,'lname':search_words2}, {'$set': resume_updates})
    #print(records.find_one({'name': search_words1, 'lname' : search_words2}))

#delete all the records
def case5():
    
    try:
        records.delete_many({})
    except Exception as e:
        print("The list is empty")

#delete a specific record
def case6():
    search_words=input('Enter first name\n')
    search_words2=input('Enter last name\n')
    try:
        records.delete_one({'fname': search_words, 'lname' :search_words2})
    except Exception as e:
        print("not found")
#add multiple records
def case8():
    search_words=int(input('Enter the number of resumes you want to add\n'))
    for x in range(search_words):
        print("The",x+1,"resume\n")
        search_words1=input('Enter first name of the\n')
        search_words2=input('Enter last name\n')
        search_words3=int(input('Experience\n'))
        search_words4=input('location\n')
        search_words5=input('subject\n')

        new_resume = {
           'fname': search_words1,
           'lname': search_words2,
           'experience': search_words3,
           'subject' : search_words5,
           'location' : search_words4
        }
        records.insert_one(new_resume)

#print the number of records available
def case9():
    print("The number of records in the system is\n",records.count_documents({}))    
 # Driver Code
if __name__ == '__main__':

    print("MongoDb for storing, retrieving, and updating data on Mongodb\n")
    print("1- To list the current records press\n")
    print("2- To list records by location\n")
    print("3- To list records by subject\n")
    print("4- To update a specific entry\n")
    print("5- To delete all records\n")
    print("6- To delete a specific record\n")
    print("7- To add one record\n")
    print("8- To add multiple records\n")
    print("9- To print the number of records\n")
    x=int(input("please choose one option, 0 to quit\n"))
    while(x>0):
        if(x==1):
            case1()
        if(x==2):
            case2()
        if(x==3):
            case3()
        if(x==4):
            case4()        
        if(x==5):
            case5()
        if(x==6):
            case6()
        if(x==7):
            case7()
        if(x==8):
            case8()
        if(x==9):
            case9()
        print("1- To list the current records press\n")
        print("2- To list records by location\n")
        print("3- To list records by subject\n")
        print("4- To update a specific entry\n")
        print("5- To delete all records\n")
        print("6- To delete a specific record\n")
        print("7- To add one record\n")
        print("8- To add multiple records\n")
        print("9- To print the number of records\n")





        x=int(input("please choose one option, 0 to quit\n"))



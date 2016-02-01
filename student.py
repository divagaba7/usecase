#this is git program
def start_func():

     aa={ 'name':'divya',
          'Class':'Btech',
          'rollno':17,
          'address':'Mohali'
        }
     bb={'name' : 'kiran',
         'Class': 'MCA',
         'rollno':19,
         'address':'JAL'
        }
     cc={'username':'12456',
         'password':'xyz'
        }  
     dd={'username':'13456',
         'password':'abc'
        } 
     mydict2= { '12456':cc,
                '13456':dd
              }  


     mydict={ 
               17:aa,
               19:bb

         
             }   

     takeargs(mydict2,mydict)
     






def takeargs(mydict2,mydict):
    x=str(raw_input("Enter your username:"))
    try :
        var = mydict2[x]
        y=str(raw_input("Enter your password:"))
        DB_PASS = var['password']
        if DB_PASS == y:
           print "Login Success !"
           print_me("""1.search
                       2.edit
                       3.insert
                       4.delete""")
        else:
            print"Login FAiled"
    except :
            print "User Name password not found!!!"

  
    
    studen_data(mydict)            
    #print_me(mydict)
               
def studen_data(mydict):                
    data="""1.search
            2.Edit																																
            3.Insert
            4.delete
            5.quit"""
    print_me(data)
    
    
    status = True
    while status == True:
          choice=int(input("Enter your choice:"))
          print choice          
          if choice == 1:
             print_me("You are trying to search data")
             key=input("Enter your rollno :")
             try:
                tmp =  mydict[key]
             
                print "name:", tmp['name']
                print "Class:",tmp['Class']
                print "roll no:", tmp['rollno']
                print "Address:", tmp['address']
             except:
                  print("Not available")
                
          elif choice == 2:
                print_me("You can edit data now ")
                key=input("Enter your rollno")
                try :
                    studentData = mydict[key]
                except:
                    print("Not available")
                    continue
                
                b=  """1.Name
                       2.Class
                       3.rollno
                       4.address
                     """
                                  
                print_me(b)
                 
                   
              

                a = int(input("what you want to edit:>"))

                if a== 1:
                   tmp = raw_input("Enter New Name:-")
                   studentData['name']=tmp
                   print "Name Updated Success !"
                elif a == 2 :
                    tmp=raw_input("Enter new class:-")
                    studentData['Class']=tmp
                elif a == 3:
                     tmp=int(input("Enter new roll no:-"))
                     studentData['rollno']=tmp
                     print tmp
                elif a == 4:
                     tmp=raw_input("Enter new address:-")
                     studentData['address']=tmp
                else :
                     print ("error")
                     
                mydict[key]=studentData    
                

          elif choice == 3:
               print_me("you can insert now")
               key=input("Enter roll no:")
               try :
                  key = mydict[key]
                  print "Already present!!"

               except:
                    name=raw_input("Enter name")
                    Class=raw_input("Enter Class")
                    address=raw_input("Enter address")
                    mydict [key]={'name': name,
                                  'Class': Class,
                                  'rollno':key,
                                  'address':address
                                 }



       
               print "Inserted!!!"
               print mydict

          elif choice == 4:
               print_me("you can delete now")
               key=input("Enter rollno you want to delete")
               del mydict[key]
               print_me("user deletd!!!")
               print_me(mydict)       

                   
                   
          elif choice == 5:
               print_me("you can quit now")
               print_me("thank you!!!")
               break
         
                   
              

   
          else :
                print_me("Bad choice")
                break

    
           
   
       
     
       
                   
            
      
def Args(myDict):

	key = input("Enter Rollno")

	name = raw_input("Enter Name")

	classs = raw_input("Enter Class")

	storeArgs(key,name,classs,myDict)

	

def storeArgs(key,name,cls,myDict):

	myDict[key] = {'Name':name,'Class':cls}

	print_me(myDict)

	searchMe(myDict)



def searchMe(myDict):

	print_me("You are going to Search:")

	searchKey = input("Enter Roll no To Search")

	print myDict[searchKey]



	

def print_me(strr='NONE'):

	print strr

	print "$"*50
        
                 
                 
                 
                 
             

 
          
                
      
		         
if __name__ == '__main__':

	start_func()

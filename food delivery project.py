#!/usr/bin/env python
# coding: utf-8

# In[1]:



class User:
    def __init__(self):
        self.User_details=[]
        self.order=[]
        
    def REgistration(self):
        print("Register on the Application : ")
        self.user_data={}
        Full_Name=input("Enter your full name :")
        Phone_No=input("Enter your phone number :")
        Email=input("Enter your email : ")
        Address=input("Enter your address :")
        Password=input("Enter your password :")
        print("\nYou have registered successfully.")
        self.user_data["Name"]=Full_Name
        self.user_data["Mobile"]=Phone_No
        self.user_data["Mail"]=Email
        self.user_data["Address"]=Address
        self.user_data["Password"]=Password
        
       # self.User_details.append(self.user_data)
        print(self.login())
        
    def login(self):
        print("From here you can log in.")
        while True:
            Full_Name=input("\nEnter your Name for login : ")
            Password=input("Enter your passward :")
            if self.user_data["Name"]==Full_Name:
                if self.user_data["Password"]==Password:
                    print("\nlogin successfull")
                    while True:

                        user_input=int(input("\nPlease enter your preference :\n 1.Place New Order\n 2.order history\n 3.update profile :\n ENter your choice :"))
                        if user_input==1:
                            print("\nplease select your preference from below list :.")
                            #show food list
                            self.show_foodlist()
                        elif user_input==2:
                            print("IF you want to see your order history please enter your name and number.")
                            self.order_history()
                        elif user_input==3:
                            self.update_profile()
                        else:
                            print("\nyou chosed a wrong digit please select from the below list:")

            else:
                print("\nPlease enter correct name and password.")
                break


            
    def show_foodlist(self):

    
        food_list=[{"name":"Tandoori chicken","price":240,"quantity":"4 pieces"},{"name":"Vegan burger","price":350,"quantity":"1 pieces"},{"name":"Truffle cake","price":900,"quantity":"500 gm"}]
        print("\nHere is the food list.")
        for i in food_list:
            print(f"{food_list.index(i)+1}. {i['name']} ({i['quantity']}) [INR {i['price']}]")

        while True:
            user_choice=input("\nif you want to chose any item enter yes else no:")
            if user_choice=="yes":
                user_input=int(input("\nPlease select your choice by the number of the food :"))
                print("\nHere is your selected order : ",food_list[(user_input-1)])
                items=food_list[(user_input-1)]
                self.order.append(items)
            
            else:
                break
        
        
        print("\nHere is your complete items list :",self.order)
        confirmation=(input("\nDo you want to PLace the order:\n 1.yes\n 2.no\n "))
        if confirmation=="yes":
            print("\nyour order is placed.")
        else:
            print("\nyour order is canceled.")
            
    def order_history(self):
        Name=input("\nplease enter your name : ")
        Phone=input("please enter your phone number :")
        if Name==self.user_data["Name"]:
            if Phone==self.user_data["Mobile"]:
                print("\nHere is your order history :",self.order)
        else:
            print("\nNo previous order")
            
    def update_profile(self):
        print("\nIF you want to update your profile please fill below: ")
        New_name=input("\nEnter your name :")
        Number=input("Enter your number :")
        New_mail=input("Enter your Email :")
        New_address=input("Enter your address :")
        New_password=input("Enter your password :")
        self.user_data["Name"]=New_name
        self.user_data["Mobile"]=Number
        self.user_data["Mail"]=New_mail
        self.user_data["Address"]=New_address
        self.user_data["Password"]=New_password
        
        self.User_details.append(self.user_data)
        
        print("\nHere is you new details :",self.User_details)
        


# In[2]:


C=User()


# In[ ]:


C.REgistration()


# In[ ]:


C.User_details


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



                                              



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





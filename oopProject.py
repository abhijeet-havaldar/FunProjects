import nlpcloud 

class NLPApp:
    
    def __init__(self):
        self.__database = {}
        self.__first_menu()
        
    def __first_menu(self):
        
        first_input = input("""
        Hi! how would you like to proceed?
        1. Not a member? Register
        2. Already a member? Login
        3. Galti se aa gaye? Exit
        """)

        if first_input == '1':
            self.__register()
        elif first_input == '2':
            self.__login()
        else:
            exit()
            
    def __second_menu(self):
        
        second_input = input("""
    Hi! how would you like to proceed?
    1. NER
    2. Language Detection
    3. Sentiment Analysis
    4. Logout
    """)
        
        if second_input == '1':
            self.__ner()
        elif second_input == '2':
            self.language_detecteion()
        elif second_input == '3':
            self.__sentiment_analysis()
        else:
            exit()
        
    def __register(self):
        name = input("enter name")
        email = input("enter email")
        password = input("enter password")
        
        if email in self.__database:
            print("email already exists")
        else:
            self.__database[email] = [name,password]
            print("rigistration successful.Now login")
            print(self.__database)
            self.__first_menu()
            
    def __login(self):
        
        email = input('enter email')
        password = input('enter password')
        
        if email in self.__database:
            if self.__database[email][1] == password:
                print('login sucessful')
                self.__second_menu()
            else:
                print('wrong password. try again')
        else:
            print('This email is not resistered')
            self.__first_menu()
        
        def __sentiment_analysis(self):
            para = input('enter the paragraph')

            client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False, lang="en")
            response = client.sentiment(para)
            
            L = []
            for i in response['scored_labels']:
                L.append(i['score'])
                
            index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]
            
            print(response['second_lables'][index]['lable'])
            self.__second_menu()
            
obj = NLPApp()
             
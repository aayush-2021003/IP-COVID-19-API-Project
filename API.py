import requests,json,pprint
 
url1 = "https://covid-193.p.rapidapi.com/statistics"                          #URL for API picked up from RapidApi 
 
headers1 = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e1efe199e7msh728a1b3ef2ef874p12038fjsnb10c532921bb"    #API Key
    }
 
response1 = requests.request("GET", url1, headers=headers1)
k=json.loads(response1.text)                                                  #Data of API in json format
 
def Cases(S,k):                                                               #Cases function to display number of cases i n  a country
    for i in k['response']:
        if i['country'].upper()==S:
            pprint.pprint(i['cases'])
            break
    else:                                                                     #handling for case if the country given is not in data or wrong name is given
        print("Country does not exist")
 
 
def Continent(S,k):                                                           #Function to print the contient of a particular country
    for i in k['response']:
        if i['country'].upper()==S:
            print(i['continent'])
            break
    else:
        print("Country does not exist")
 
 
def Population(S,k):                                                          #Function to print the population of a particular country
    for i in k['response']:
        if i['country'].upper()==S:
            print(i['population'])
            break
    else:
        print("Country does not exist")
 
def Deaths(S,k):                                                              #Function to print the number of deaths in a particular country
    for i in k['response']:
        if i['country'].upper()==S:
            pprint.pprint(i['deaths'])
            break
    else:
        print("Country does not exist")
 
def Tests(S,k):                                                               #Function to print number of tests in a country
    for i in k['response']:
        if i['country'].upper()==S:
            pprint.pprint(i['tests'])
            break
    else:
        print("Country does not exist")

def Casesondate(S,date):                                                      #Function to print the number of cases ona day the last time records were taken on that day

    url3= "https://covid-193.p.rapidapi.com/history"

    querystring3= {"country":S,"day":date}

    headers3= {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "07b69b8116msh9ba68351b2f0b4dp158637jsn9f8c4233fac9"
        }

    response3= requests.request("GET", url3, headers=headers3, params=querystring3)
    k=json.loads(response3.text)
    L=[];L1=[]
    for i in k['response']:
        L.append(int(i['time'][11:13]+i['time'][14:16]))
    #print(L)
    for i in range(len(L)):
        if L[i]==max(L):
            break
    try:

        pprint.pprint(k['response'][i])
    except UnboundLocalError:
        print("The country does not exist in databse for this date")
 
def Display():                                                                #Function to print all the countries as a long list on alphabetical order
 
    url = "https://covid-193.p.rapidapi.com/countries"
 
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "e1efe199e7msh728a1b3ef2ef874p12038fjsnb10c532921bb"
    }
 
    response = requests.request("GET", url, headers=headers)
    k=json.loads(response.text)
 
    pprint.pprint(k["response"])
 
 
while True:                                                                            #Menu driven program 
    N=int(input('''============================MENU==================================================
    0 -> Display all the countries
    1 -> Display Continent
    2 -> Display Population
    3 -> Display no of cases
    4 -> Display no of deaths
    5 -> Display no of tests conducted
    6 -> Display cases in a country on certain date
    =================================================================================================
    Input: '''))
 
    while N==0:                                                                 #keeps displaying list of countries as long as N=0
        Display()
        N=int(input("Please enter operation to perform"))
    
    S=input("Please enter the name of country: ")
    S=S.upper()
    if N==1:
            Continent(S,k)
    elif N==2:
            Population(S,k)
    elif N==3:
            Cases(S,k)
    elif N==4:
            Deaths(S,k)
    elif N==5:
            Tests(S,k)
    elif N==6:
        date=input("Enter date in format yyyy-mm-dd")
        Casesondate(S,date)
    else:                                                                #Handling for wrong choice of operation
            print("Please retry")
    M=input("More(Y/N)?: ")                                              #Asking the user if he wants to run the operation again
    if M in"Nn":
        break
 
 
 
 
 
 
 
 
 

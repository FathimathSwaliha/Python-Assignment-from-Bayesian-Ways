#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import time

def fetch_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    return data['bpi']['USD']['rate_float']


def collect_data():
    data_points = []
    previous_data_point = None
    count = 0
    while count < 300:
        usd_price = fetch_bitcoin_price()
        if usd_price != previous_data_point:
            data_points.append(usd_price)
            print("Data point", len(data_points), ":", usd_price)
            previous_data_point = usd_price
            count += 1
        time.sleep(300)
    data_points.sort()
    print("highest price is",data_points[-1])
    print("lowest price is",data_points[0])


collect_data()


# In[2]:


s=str(input('Enter the string:'))
s=s.lower()
reverse=s[::-1]
if s==reverse:
  print(True)
else:
  print(False)


# In[3]:


Input=str(input("Input:"))
Pattern=str(input("Pattern:"))
output=Input.count(Pattern)
output


# In[4]:


A=[]
for i in range(1,11):
  print("Game",i,":")
  player1=str(input("Player1:"))
  player2=str(input("Player2:"))
  if (player1=="R" and player2=="S"):
    print("player1 wins")
    A.append(1)

  elif (player1=="P" and player2=="R"):
   print("player1 wins")
   A.append(1)
  elif (player1=="S" and player2=="P"):
    print("player1 wins")
    A.append(1)
  elif (player1==player2):
    print("Draw")
    A.append(0)
  else:
    print("player2 wins")
    A.append(2)
Player1score=A.count(1)
Player2score=A.count(2)
if Player1score > Player2score:
  print("Final Winner:Player1")
else:
    print("Final Winner:Player2")


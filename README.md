# TripSorter
Flask API for sorting trip

This small flask app takes a stack of boarding cards for various means of transport and returns trip information.  

<h3>Installation</h3>

First clone repository to some free directory.
Install all requirements from file:
<br>
$ pip3 install -r requirements.txt

<h3> Start Flask </h3>

To start flask app enter directory where cloned file are stored and type:
<br>
$ python3.7 app.py 
That is all your copy of this soft is now working. 
<br>
By default Flask is listening on port :5000 so to connect via browser input http://localhost:5000/ and you will see welcome message.
Or you can do the same thing on console:
<br>
$ curl localhost:5000/

<h3> Trip Sorter</h3>

But main functionality of this app is to gather unordered information about journey that can be divided into many steps.
E.g let's imagine that your company sends you to journey from Denver to Madrit, your secretary buys tickets for you however they are unordered and you want to know what happens on each step of your journey.
Here  my software can be very handy and will help you to get to destination with all your baggage and on time.

<h5>Example usage</h5>
To use this tool you need to provide data in specific format like below:
<br>

{
<br>
"trip1": {
<br>
    "baggage_info": "344",
    <br>
    "end_point": "Barcelona",
    <br>
    "gate/platform": "45B",
    <br>
    "seat_number": "7b",
    <br>
    "start_point": "Denver",
    <br>
    "transport_number": "SK22",
    <br>
    "transport_type": "plane"
    <br>
  },
  <br>
  "trip2": { 
  <br> 
  ...
  <br>
  }

<h5> Important</h5>
It doesn't matter how many stops you will have between start place and final destination as long it can be start and 
finished at some point. Here is example how code inserted to console should be constructed to obtain list of all steps. 
Also be advise that even if data from your boarding cards are not sufficient to fill all places in dictionary don't 
worry just lef empty string --> "" 
<br>

<br>
$ curl localhost:5000/ -d '{
"trip1": {"transport_type":"plane","start_point":"Denver","end_point":"Barcelona",
"transport_number":"SK22","seat_number":"7b", "gate/platform":"45B","baggage_info":"344"},
"trip2": {"transport_type":"train", "start_point":"New York","end_point":"Denver",
"transport_number":"78A","seat_number":"44", "gate/platform":"3.75","baggage_info":""},
"trip3": {"transport_type":"bus", "start_point":"Barcelona","end_point":"Madrit",
"transport_number":"Mf78","seat_number":"98", "gate/platform":"5","baggage_info":""}
}'

If you copy this code to your console while running app, spp will return thiss message:


1. Take train 78A from New York to Denver. Sit in seat 44.
2. From Denver, take flight SK22 to Barcelona. Gate 45B, seat 7b. Baggage drop at ticket counter 344.\n 
3. Take the bus from Barcelona to Madrit. Sit in seat 98.
4. You have arrived at your final destination 

<h5> Swagger</h5>

This app also have API documentation created in Swagger(OpenAPI) to launch it, please input this address to browser
 http://localhost:5000/apidocs/#/ while app is running. There you can get more information and run example code.
 
<h5>Acknowledges</h5>

This app was made for Ecumene Ventures  
 


# rest-api-technical-interview
Please explore the contents of the repo to fully understand how we will apply the 3 different scenarios for our REST-ful API's

Superuser account = interviewer

Password = Tocayo2022@

For this excercise I have decided to add the database to the repository:


Bellow the explanation of each excercise:

1.- Customer Order Status:
You have a data source containing order-line data (each order can have multiple order
lines based on the number of products ordered under that specific order). An order line
item can be in one of the following three statuses: Pending, Shipped, Cancelled. You
want to determine the status of the overall arder based on the statuses of each
individual order line item for that order. For example, if you have three items in order
number 1234, and two of them are marked *Shipped" but one is marked "Pending" then
the overall order status is Pending. 11 all are marked "Shipped" then the Status is
*Shipped".

Available URLS for excercise and instructions to interact with API:
http://127.0.0.1:8000/orders/
Media Type: application/Json
    {
        "order_number": 1567
    }
http://127.0.0.1:8000/orders/<int:pk>/
order_number: 1567 = pk: 1
order_number: 1234 = pk: 2
order_number: 9834 = pk: 3 
order_number: 7654 = pk: 4

http://127.0.0.1:8000/orders/items

Media Type: application/Json
    {
        "order_number": pk
        "item_name": "string_value"
        "status": "Shipped, Pending, Cancelled"
    }

http://127.0.0.1:8000/orders/items/<int:pk>/
KEYBOARD = pk:3
MOUSE = pk:2
LAPTOP = pk1

http://127.0.0.1:8000/order_status/
See how our order_status behaves *** Pending implementations to edit pending status automatically depending on the item status ***






2.- Seasons Problem:
You have a table containing a large number of orders over several years - a sample is
shown below. Each order has a date attribute that you wlll need to use to determine the
season in which this order was placed. For reference see the table containing the dates
in which each season falls.


3.- Detecting Change:
You have a table con1aining data on the weather. Each date has a boolean indicating if
it rained (TRUE) or did not rain {FALSE). Query the lable to detennine the dates in
which the weather becamne bad (Determine the weather changed from FALSE to TRUE).

Available URLS for excercise and instructions to interact with API:


http://127.0.0.1:8000/weather_list/

{
    "date": "2020-01-10",
    "was_rainy": true
}

Api does not loop through the list to sort automatically, instead it will only check if the last 2 objects in the list are FALSE and TRUE. This
If the new object == True and the previous object == False we will create a new instance as to when the weather turned bad.

http://127.0.0.1:8000/weather/became_bad/
lets manualy add the days that the weather became bad

    {
        "date": "yyyy-mm-dd",
        "became_bad": true
    }



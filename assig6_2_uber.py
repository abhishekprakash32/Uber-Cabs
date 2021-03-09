# Using dictionary, if elif and color Package from https://pypi.org/
from Color_Console import color
color('red', 'white')

a = "Uber Cab Service Application "
print(a.center(72, '*'))
b = "Welcome to  Uber Cab Service"
print(b.center(72, ' '))
print("Sr No\tCar Type\t  Capacity\t    \tRate")
print("1\tMini\t\t\t4\t\tRs.15/km")
print("2\tSedan\t\t\t4\t\tRs.20/km")
print("3\tSUV\t\t\t5\t\tRs.25/km")
print("4\tLuxury\t\t\t5\t\tRs.100/km")
print("Hurry You can Use Below Cupon Codes -")
print("1] FLAT 5 = Flat 5 % discount on total bill")
print("2] FLAT 10 = Flat 10 % discount on total bill")
print("Routes Available -")
print("1.Deccan To Swargate")
print("2.Swargate To Deccan")
print("3.Kothrud To Swargate")
print("4.Swargate To Kothrud")
print("5.Hadapsar To Swargate")
print("6.Swargate To Hadapsar")
print("7.Pune Station To Swargate")
print("8.Swargate To Pune Station")
routes = ['Deccan', 'Swargate', 'Kothrud', 'Hadapsar', 'Pune Station']
route_distances = {'Deccan To Swargate' : 7, 'Swargate To Deccan':7,
 'Kothrud To Swargate':8, "Swargate To Kothrud":8,
 'Hadapsar To Swargate':10, 'Swargate To Hadapsar':10,
 'Pune Satation To Swargate':6, 'Swargate To Pune Station':6}
_name = input("Enter Your Name =")
_mobile = int(input("Enter Your Mobile ="))
_email = input("Enter Your Email Id =")
car_type = int(input("Enter Car Type To Book [1/2/3/4] ="))
if car_type == 1:
    car = "Maruti Suzuki Alto"
    car_type1 = "Mini type"
    Rate = 15
    pick = input("Enter Your Pick up point =")
    drop = input("Enter Your Drop point =")

elif car_type == 2:
    car = "Honda City"
    car_type1 = "Sedan type"
    Rate = 20
    pick = input("Enter Your Pick up point =")
    drop = input("Enter Your Drop point =")

elif car_type == 3:
    car = "MG Hector"
    car_type1 = "SUV type"
    Rate = 25
    pick = input("Enter Your Pick up point =")
    drop = input("Enter Your Drop point =")

elif car_type == 4:
    car = "BMW"
    car_type1 = "Luxury type"
    pick = input("Enter Your Pick up point =")
    drop = input("Enter Your Drop point =")
    Rate = 100

print(f"***************** Thanks For Booking Car - {car_type1}**************")
print(f"Your Name = {_name}")
print(f"Your Mobile ={_mobile}")
print(f"Your Email Id ={_email}")
print(f"Your car ={car}")
print(f"Your Pick up point ={pick}")
print(f"Your Drop point ={drop}")


pick_drop = (f"{pick} To {drop}")
print(f'Distance between {pick} To {drop} is {route_distances[pick_drop]}')
distance1 = route_distances[pick_drop]
Total_Fare = Rate * distance1
print(f"Your regular Fare Amount={Total_Fare}")
discount1 = input("Do You have any discount cupon or code ? = yes/no=")
if discount1 == 'yes':
    coupon = input("Enter Cupon Code =")
    if coupon == 'FLAT 5':
        dis_5 = (Total_Fare/100) * 5
        Total_bill = Total_Fare - dis_5
        print(f"Your bill amount = {Total_bill}")
        gst_9 = (Total_bill/100) * 9
        gst_18 = gst_9 * 2
        Total_bill_amount = Total_bill + gst_18
        print("*********Your Bill***********")
        print(f"TAX Amount = {gst_18}")
        print(f"CST = {gst_9}")
        print(f"GST = {gst_9}")
        print(f"Your  bill amount is {Total_bill} +\
         Tax Amount is {gst_18} = {Total_bill_amount}")
    elif coupon == 'FLAT 10':
        dis_10 = (Total_Fare/100) * 10
        Total_bill = Total_Fare - dis_10
        print(f"Your Total bill amount = {Total_bill}")
        gst_9 = (Total_bill/100) * 9
        gst_18 = gst_9 * 2
        Total_bill_amount = Total_bill + gst_18
        print("*********Your Bill***********")
        print(f"TAX Amount = {gst_18}")
        print(f"CST = {gst_9}")
        print(f"GST = {gst_9}")
        print(f"Your bill amount is {Total_bill} +\
         Tax Amount is {gst_18} = {Total_bill_amount}")
elif discount1 == 'no':
    print("Your regular charges will applied-")
    gst_9 = (Total_Fare/100) * 9
    gst_18 = gst_9 * 2
    Total_bill_amount = Total_Fare + gst_18
    print("*********Your Bill***********")
    print(f"TAX Amount = {gst_18}")
    print(f"CST = {gst_9}")
    print(f"GST = {gst_9}")
    print(f"Your bill amount is {Total_Fare} +\
     Tax Amount is {gst_18} = {Total_bill_amount}")

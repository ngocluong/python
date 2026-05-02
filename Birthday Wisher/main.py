import random
import smtplib
import datetime as dt

now = dt.datetime.now()
# ----------------------- send random quote ----------------
# day_of_the_week = now.weekday()
# if day_of_the_week == 2:
#     with open("quotes.txt", "r") as quotes:
#         all_quotes = quotes.readlines()
#         random_quote = random.choice(all_quotes)
#
#     my_email = "tracy.leung.1991@gmail.com"
#
#     my_password = "rspp enqd sgsv nihd"
#     connection = smtplib.SMTP('smtp.gmail.com', 587)
#     connection.starttls()
#     connection.login(my_email, my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="tracy.l@scopicsoftware.com",
#                         msg=f"Subject: Birthday Wishing\n{random_quote}")
#     connection.close()

# solution from udemy
import pandas
today = dt.datetime.now()
today_tuple = (today.month, today.day)
#
data = pandas.read_csv("birthdays.csv")
print("==data===")
# print(data)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(type(birthdays_dict))
if today_tuple in birthdays_dict:
    print(birthdays_dict[today_tuple]["name"])

##################### Hard Starting Project ######################
import pandas
data = pandas.read_csv('birthdays.csv')
filtered_df = data[(data['month'] == now.month) & (data['day'] == now.day)]

for index, birthday_p in filtered_df.iterrows():
    name = birthday_p['name']
    email = birthday_p['email']
    random_temps = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    with open(f"letter_templates/{random_temps}", "r") as tmp:
        content = tmp.read()
    # with open("quotes.txt", "r") as quotes:
    #     all_quotes = quotes.readlines()
    #     random_quote = random.choice(all_quotes)
    my_email = "tracy.leung.1991@gmail.com"
    my_password = "****"
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="tracy.l@scopicsoftware.com",
                        msg=f"Subject: Birthday Wishing\n{content.replace("[NAME]", name)}")
    connection.close()


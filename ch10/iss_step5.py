import requests, json, turtle
def move_iss(lat,long):
    iss.penup()
    iss.goto(long, lat)
    iss.pendown()

screen = turtle.Screen()
screen.setup(1000,500)
screen.bgpic('./ch10/earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape("./ch10/iss.gif")
iss.shape("./ch10/iss.gif")


url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if (response.status_code == 200):
    response_dictionary = json.loads(response.text)
    position = response_dictionary['iss_position']
    lat = float(position['latitude'])
    long = float(position['longitude'])
    move_iss(lat, long)


else:
    print("Huston we have a problem:",response.status_code)

turtle.mainloop()
import requests, json, turtle

screen = turtle.Screen()
screen.setup(1000,500)
screen.bgpic('./ch10/earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
iss.register_shape("./ch10/iss.gif")
iss.shape("./ch10/iss.gif")


url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if (response.status_code == 200):
    response_dictionary = json.loads(response.text)
    position = response_dictionary['iss_position']
    print('International Space Station at ' + position['latitude'] + ',' + position['longitude'])



else:
    print("Huston we have a problem:",response.status_code)

turtle.mainloop()
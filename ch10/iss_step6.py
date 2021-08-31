import requests, json, turtle
iss = turtle.Turtle()

def setup(window):
    global iss

    window.setup(1000,500)
    window.bgpic('./ch10/earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape("./ch10/iss.gif")
    iss.shape("./ch10/iss.gif")

def move_iss(lat,long):
    iss.hideturtle()
    iss.penup()
    iss.goto(long, lat)
    iss.pendown()
    iss.showturtle()


def track_iss():
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
    
    widget = turtle.getcanvas()
    widget.after(5000, track_iss)

def main():
    global iss
    screen = turtle.Screen()
    setup(screen)
    track_iss()

if __name__ == "__main__":
    main()
    turtle.mainloop()

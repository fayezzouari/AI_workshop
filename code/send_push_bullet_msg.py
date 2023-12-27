from pushbullet import Pushbullet

API_KEY = "o.2CObAO4b1i3l4YyYkA72xg9BWSdxImqI"


pb = Pushbullet(API_KEY)
push = pb.push_note("You Counter today: ", "hello")

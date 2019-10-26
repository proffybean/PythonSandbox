# Let's say we looked this up somewhere
data = {
    "2018-01-01": {"Temperature": "50"},
    "2018-01-02": {"Temperature": "53"},
    "2018-01-03": {"Temperature": "52"}
}

# Define our simple function
def what_was_the_weather_like(date):
    return str(data[date])

temp = what_was_the_weather_like("2018-01-01")
print(temp)
# This should return:
# "{'Temperature': '50'}"
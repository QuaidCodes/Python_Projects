
# **kwargs
# Pass multiple arguments as a dictionary
def capitals(**kwargs):

    kwargs.update({"Palestine": "Jerusalem"})

    for key, values in kwargs.items():
        print("{}: {}".format(key, values))


capitals(Pakistan="Islamabad", Afghanistan="Kabul", Syria="Damascus", Lebanon="Beirut", Iran="Tehran", Iraq="Baghdad", Saudi="Riyadh")

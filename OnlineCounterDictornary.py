def online_count(status_dict):
    user = list(status_dict.values())
    online = 0
    for i in range(len(user)):
        if user[i] == "online":
            online += 1

    return online
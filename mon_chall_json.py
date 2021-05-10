import json
with open("status.json", "r") as f:
    data = json.load(f)
    print(data)
    downed_servers = []
    for serv in data:
        if serv["state"] == "down":
            downed_servers.append(serv["server"])

print(f"The following is a list of all the servers in a 'down' state: {downed_servers}")

with open("downed_servers.txt", "w") as f2:
    spaced_servers = [f"{srv}\n" for srv in downed_servers]
    f2.writelines(spaced_servers)

#ROCKET SCIENCE CHALLENGE: return the full json for only the downed servers into a file called downed_servers.json

# EXPLORING CONDITIONALS
# CLASSIC MODE
everything_OK = False

if everything_OK :
    print("OK!")
else :
    print("NOK!")

# TESTING A VARIABLE AND USING ELIF
age = 10
message = "NOT TESTED"

if age > 150 :
    message = "User is dead!"
elif age > 18 :
    message = "User is overage."
else :
    message = "User is underage."

print(message)

# MINIMAL CODE TEST
number_of_subs = 90
sub_goal = 100

message = "Sub Goal was not reached!" if number_of_subs < sub_goal else "Sub Goal was reached! Congratulations!"

print(message)

# NESTED IFs
everything_OK = True

if everything_OK:
    print("Everything OKAY again!")

    if(number_of_subs > sub_goal) :
        print(message)
        sub_goal += 10
    else :
        sub_goal -= 10

    print("New sub goal: ", sub_goal)
    print("CHECK FINISHED")
else :
    print("THERE WAS ERROR!")

# DICTIONARY MAPPING TO USE AS SWITCH
twitch_alerts = {
    "follow" : "NEW FOLLOWER!",
    "sub"    : "NEW SUB!",
    "cheer"  : "SOMEONE SENT MONEY!"
}

current_alert = "hype train"

# message = twitch_alerts[current_alert]
message = twitch_alerts.get(current_alert, "NO ALERT!") # Get allows a default value in case the key is not found

# MATCH STATEMENT
command = "show alert"

match command :
    case "show alert" :
        print(message)
        print("Alert shown!")
    case "hide alert" :
        print("Alert hidden!")
    case "replay alert" :
        print(message)
        print("Alert replayed")
    case other :
        print("Command not found")
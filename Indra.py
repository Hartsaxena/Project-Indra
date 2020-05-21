# Oh look, an unnecessary comment...
# I'm kind of bored right now, to be completely honest.

from pathlib import Path

print("Loading...")
exec(open(Path.home() / "Documents/ProjectIndra/Vitals/VitalsPortal.py").read())


# If you want testing (Unless it's negative testing, then go 30) just set it to 200. Default for simulation should be 75.
# interest = 75
# loveBonus = 3
# negloveBonus = 0


if firstrun == True:  # A different greeting on the game's first run
    localfirst = True
    print("I'm sure you're bored...")
    sleep(2)
    message = ("What should we talk about then? ")
    print("\n")
elif firstrun == False:
    localfirst = False
    message = ("What should we talk about today? ")

if firstrun == False:
    exec(open(vitals / "NewDay.py").read())

Save()
# Add Information to the Topcislist.py file if you want to add another topic
# You shouldn't add a topic to the list if it is a Miscellaneous Topic
while interest < 500 and interest > 0:  # Supreme While loop

    exec(open(vitals / "WhileReset.py").read())
    print("")
    topic = input(message)
    lowertopic = topic.lower()
    print("\n")

    if lowertopic == "robots" or lowertopic == 'robot':              # Robots
        exec(open(mainexecutes / "ExecRobots.py").read())

    # Python
    elif lowertopic == "python":
        exec(open(mainexecutes / "ExecPython.py").read())

    # Indra
    elif lowertopic == "indra" or lowertopic == 'projectindra' or lowertopic == 'project indra':
        exec(open(mainexecutes / "ExecIndra.py").read())

    elif lowertopic == 'anime' or lowertopic == 'manga' or lowertopic == 'anime and manga':          # Anime or Manga
        exec(open(mainexecutes / "ExecManga_and_Anime.py").read())

    elif lowertopic == 'virus' or lowertopic == 'are you a virus' or lowertopic == 'is this a virus':      # Virus
        exec(open(mainexecutes / "ExecVirus.py").read())

    elif lowertopic == 'just monika' or lowertopic == 'monika':         # Monika
        exec(open(mainexecutes / "ExecMonika.py").read())

    elif lowertopic == 'coronavirus' or lowertopic == 'corona' or lowertopic == 'covid19' or lowertopic == 'corona virus':  # Coronavirus
        exec(open(mainexecutes / "ExecCovid.py").read())

    elif lowertopic == "pets" or lowertopic == "cats" or lowertopic == "dogs" or lowertopic == 'pet' or lowertopic == 'pet animals':
        exec(open(mainexecutes / "ExecPets.py").read())

    # elif lowertopic == "music" or lowertopic == "songs": # NOTE: Unfinished
    #     exec(open(mainexecutes / "ExecMusic.py").read())

    # elif lowertopic == 'video games':  # NOTE: Unfinished
    #     exec(open(mainexecutes / "ExecVideoGames.py").read())


# Miscellaneous Topics

    elif lowertopic == 'age' or lowertopic == 'years old' or lowertopic == 'my age' or lowertopic == 'my age':
        exec(open(miscexecutes / "ExecAgeChange.py").read())

    elif lowertopic == 'date' or lowertopic == 'current date' or "what is the date" in lowertopic or lowertopic == 'the date':
        exec(open(sysexecutes / "ExecCurrentDate.py").read())

    elif lowertopic == "i don't know" or lowertopic == "idk" or lowertopic == "i don't care" or "suggestion" in lowertopic or lowertopic == "idc":  # Suggestions
        exec(open(miscexecutes / "ExecSuggestion.py").read())

    # Delete Logs
    elif lowertopic == "reset" or lowertopic == "clear data":
        exec(open(sysexecutes / "ExecLogDel.py").read())

    elif lowertopic == 'marry me' or lowertopic == 'will you marry me':        # Marry Me!
        exec(open(miscexecutes / "ExecMarriage.py").read())

    elif lowertopic == 'nothing' or lowertopic == 'stop' or lowertopic == 'terminate' or lowertopic == 'kill' or lowertopic == 'goodbye' or lowertopic == 'bye':  # Terminate
        exec(open(sysexecutes / "ExecTerminate.py").read())

    elif lowertopic == 'restart' or lowertopic == 'redo':  # Restart
        exec(open(sysexecutes / "ExecRestart.py").read())

    # Gender Change
    elif lowertopic == 'gender' or lowertopic == 'sex':
        exec(open(miscexecutes / "ExecGender.py").read())

    elif lowertopic == 'name' or lowertopic == 'change name' or lowertopic == 'change my name':        # Name Change
        exec(open(miscexecutes / "ExecNameChange.py").read())

    # Update the Game
    elif lowertopic == 'update' or lowertopic == 'updater':
        exec(open(indrafolder / "Updater.py").read())

######################################################################

    # These are for developing the game and aren't meant for actual gameplay.
    # These should all be commented out of the program on default.

    # elif lowertopic == 'variablestest':
    #     print(f"Name: {name}")
    #     print(f"Gender: {gender}")
    #     print(f"Age: {age}")
    #     print(f"Birthdate: {birthdate}")
    #     print(f"Currentdate: {currentdate}")
    #     print(f"nextyear: {nextyear}")
    #     print(f"Interest Level: {interest}")
    #     print(f"Interactions: {interactions}")
    #     print(f"LoveBonus: {loveBonus}")
    #     print(f"NegativeLoveBonus: {negloveBonus}")
    #     print(f"Devbypass: {devbypass}")
    #     print(f"Last logged date: {lastlogdate}")
    #
    # elif lowertopic == 'functest':  # This is for code testing and isn't meant to be used for actual gameplay
    #     CustomRecord("Function Test", "functest", +23)
    #     print("The Function was successfully tested.")
    #
    # elif lowertopic == "intchange":
    #     newinterest = input(
    #         "What would you like to change the interest variable into? ")
    #     try:
    #         interest = int(newinterest)
    #     except ValueError:
    #         print(
    #             "Sorry, but there was a problem and I'm not able to turn that string into an Integer.")
    #         sleep(2.5)
    #     print("Done!")

######################################################################

    # Confused Indra
    else:
        exec(open(miscexecutes / "ExecConfused.py").read())

from pathlib import Path

print ("Loading...")
exec(open(Path.home() / "Documents/ProjectIndra/Vitals/VitalsPortal.py").read())


# If you want testing (Unless it's negative testing, then go 30) just set it to 200. Default for simulation should be 75.
#interest = 75
#loveBonus = 3
#negloveBonus = 0


if firstrun == True:  # A different greeting on the game's first run
    print("I'm sure you're bored...")
    sleep(2)
    message = ("What should we talk about then? ")
    localfirst = True
elif firstrun == False:
    message = ("What should we talk about today? ")
    localfirst = False

if firstrun == False:
    exec(open(vitals / "NewDay.py").read())

# Add Information to the Topcislist.py file if you want to add another topic
# You shouldn't add a topic to the list if it is a Miscellaneous Topic
while interest < 300 and interest > 0:  # Supreme While loop

    exec(open(vitals / "WhileReset.py").read())
    topic = input(message)
    lowertopic = topic.lower()

    if lowertopic == "robots" or lowertopic == 'robot':                                                       # Robots
        exec(open(mainexecutes / "ExecRobots.py").read())

    # Python
    elif lowertopic == "python":
        exec(open(mainexecutes / "ExecPython.py").read())

    # Indra
    elif lowertopic == "indra" or lowertopic == 'projectindra' or lowertopic == 'project indra':
        exec(open(mainexecutes / "ExecIndra.py").read())

    elif lowertopic == 'anime' or lowertopic == 'manga' or lowertopic == 'anime and manga':                # Anime or Manga
        exec(open(mainexecutes / "ExecManga_and_Anime.py").read())

    elif lowertopic == 'virus' or lowertopic == 'are you a virus' or lowertopic == 'is this a virus':      # Virus
        exec(open(mainexecutes / "ExecVirus.py").read())

    elif lowertopic == 'just monika' or lowertopic == 'monika':                                               # Monika
        exec(open(mainexecutes / "ExecMonika.py").read())

    elif lowertopic == 'coronavirus' or lowertopic == 'corona' or lowertopic == 'covid19' or lowertopic == 'corona virus':  # Coronavirus
        exec(open(mainexecutes / "ExecCovid.py").read())

    # elif lowertopic == "pets" or lowertopic == "cats" or lowertopic == "dogs" or lowertopic == 'pet': # NOTE: Unfinished
    #     exec(open(mainexecutes/"ExecPets.py").read())

    # elif lowertopic == 'video games': # NOTE: Unfinished
    #     exec(open(mainexecutes/"ExecVideoGames.py").read())


# Miscellaneous Topics

    elif lowertopic == 'date' or lowertopic == 'current date' or "what is the date" in lowertopic or lowertopic == 'the date':
        exec(open(sysexecutes / "ExecCurrentDate.py").read())

    elif lowertopic == "i don't know" or lowertopic == "idk" or lowertopic == "i don't care" or "suggestion" in lowertopic or lowertopic == "idc":  # Suggestions
        exec(open(miscexecutes / "ExecSuggestion.py").read())

    # Delete Logs
    elif lowertopic == "reset" or lowertopic == "clear data":
        exec(open(sysexecutes / "ExecLogDel.py").read())

    elif lowertopic == 'marry me' or lowertopic == 'will you marry me':                                    # Marry Me!
        exec(open(miscexecutes / "ExecMarriage.py").read())

    elif lowertopic == 'nothing' or lowertopic == 'stop' or lowertopic == 'terminate' or lowertopic == 'kill' or lowertopic == 'goodbye' or lowertopic == 'bye':  # Terminate
        exec(open(sysexecutes / "ExecTerminate.py").read())

    elif lowertopic == 'restart' or lowertopic == 'redo':                                                     # Restart
        exec(open(sysexecutes / "ExecRestart.py").read())

    # Gender Change
    elif lowertopic == 'gender' or lowertopic == 'sex':
        exec(open(miscexecutes / "ExecGender.py").read())

    elif lowertopic == 'name' or lowertopic == 'change name' or lowertopic == 'change my name':            # Name Change
        exec(open(miscexecutes / "ExecNameChange.py").read())

    # Update the Game
    elif lowertopic == 'update' or lowertopic == 'updater':
        exec(open(indrafolder / "Updater.py").read())

######################################################################

    # These are for developing the game and aren't meant for actual gameplay.
    # These should all be commented out of the program on default.

    # elif lowertopic == 'variablestest':
    #     print("Name: " + name)
    #     print("Interest Level: " + str(interest))
    #     print("Interactions: " + str(interactions))
    #     print("LoveBonus: " + str(loveBonus))
    #     print("NegativeLoveBonus: " + str(negloveBonus))
    #     print("Firsttime Indra: " + str(firsttimeIndra))
    #     print("Firsttime VideoGames: " + str(firsttimeVideoGames))
    #     print("Devbypass: " + str(devbypass))
    #     print("Last logged date: " + str(lastlogdate))
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

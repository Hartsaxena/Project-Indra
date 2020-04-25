from pathlib import Path
exec(open(Path.home()/"Documents/ProjectIndra/Vitals/VitalsPortal.py").read())


# If you want testing (Unless it's negative testing, then go 30) just set it to 200. Default for simulation should be 75.
#interest = 75
#loveBonus = 3
#negloveBonus = 0


if firstrun == True:  # A different greeting on the game's first run
    print("I'm sure you're bored...")
    sleep(2)
    message = ("What should we talk about then? ")
elif firstrun == False:
    message = ("What should we talk about today? ")


# Add Information to the Topcislist.py file if you want to add another topic
# You shouldn't add a topic to the list if it is a Miscellaneous Topic
while interest < 300 and interest > 0:  # Supreme While loop

    exec(open(vitals/"WhileReset.py").read())
    topic = input(message)

    if topic.lower() == "robots" or topic.lower() == 'robot':                                                       # Robots
        exec(open(mainexecutes/"ExecRobots.py").read())

    # elif topic.lower()=='variables':
    #     print (name)
    #     print (interest)
    #     print (loveBonus)
    #     print (negloveBonus)
    #     print (firsttimeIndra)
    #     print (devbypass)

    elif topic.lower() == "python":                                                                                 # Python
        exec(open(mainexecutes/"ExecPython.py").read())

    elif topic.lower() == "indra":                                                                                  # Indra
        exec(open(mainexecutes/"ExecIndra.py").read())

    elif topic.lower() == 'anime' or topic.lower() == 'manga' or topic.lower() == 'anime and manga':                # Anime or Manga
        exec(open(mainexecutes/"ExecManga_and_Anime").read())

    elif topic.lower() == 'virus' or topic.lower() == 'are you a virus' or topic.lower() == 'is this a virus':      # Virus
        exec(open(mainexecutes/"ExecVirus.py").read())

    elif topic.lower() == 'just monika' or topic.lower() == 'monika':                                               # Monika
        exec(open(mainexecutes/"ExecMonika.py").read())

    elif topic.lower() == 'coronavirus' or topic.lower() == 'corona' or topic.lower() == 'covid19' or topic.lower() == 'corona virus':  # Coronavirus
        exec(open(mainexecutes/"ExecCovid.py").read())


# Miscellaneous Topics
    elif topic.lower() == "i don't know" or topic.lower() == "idk" or topic.lower() == "i don't care":              # Suggestion
        exec(open(miscexecutes/"ExecSuggestion.py").read())

    elif topic.lower() == "cmdintrecordindra":                                                                      # Int CMD
        exec(open(miscexecutes/"ExecIntCMD.py").read())

    elif topic.lower() == "reset" or topic.lower() == "clear data":                                                 # Delete Logs
        exec(open(sysexecutes/"ExecLogDel.py").read())

    elif topic.lower() == 'marry me' or topic.lower() == 'will you marry me':                                       # Marry Me!
        exec(open(miscexecutes/"ExecMarriage.py").read())

    elif topic.lower() == 'nothing' or topic.lower() == 'stop' or topic.lower() == 'terminate' or topic.lower() == 'kill' or topic.lower() == 'goodbye' or topic.lower() == 'bye':  # Terminate
        exec(open(sysexecutes/"ExecTerminate.py").read())

    elif topic.lower() == 'restart' or topic.lower() == 'redo':                                                     # Restart
        exec(open(sysexecutes/"ExecRestart.py").read())

    elif topic.lower() == 'gender' or topic.lower() == 'sex':
        exec(open(miscexecutes/"ExecGender.py").read())

    else:                                                                                                           # Confused Indra
        exec(open(miscexecutes/"ExecConfused.py").read())

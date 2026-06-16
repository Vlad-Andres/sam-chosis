label scene_2:
    scene bg kitchen
    with dissolve

    hide sam
    show sam happy at right
    with dissolve

    $ renpy.music.stop(channel="music", fadeout=1.0)
    $ play_audio_if_exists("audio/rock_music_muffled.wav", channel="music", loop=True, fadein=1.0)

    "You enter the kitchen, and are immediately greeted by the sound of your roommate, Michael, playing music loudly through his door."
    hide sam
    show sam angry at right
    "You decide to ignore it for now and make breakfast."

    menu:
        "What do you want to make for breakfast?"
        "Cereal":
            $ flag["breakfast"] = "cereal"
            show bg kitchen:
                blur 20
            show sam angry:
                blur 6
            show cereal at Transform(zoom=1.6)
            with dissolve
            "You decide on something quick and easy."
            $ play_audio_if_exists("audio/cereal.mp3", channel="sound")
            "After pouring milk in a bowl, you add your favorite cereal."
            hide cereal
            show cereal_hello at Transform(zoom=1.6)
            with dissolve
            "Huh, weird that they made words."
        "Eggs":
            $ flag["breakfast"] = "eggs"
            $ play_audio_if_exists("audio/eggs.wav", channel="sound")
            show bg kitchen:
                blur 20
            show sam angry:
                blur 6
            show eggs at Transform(zoom=1.6)
            with dissolve
            "You decide on eggs and bacon."
            "After heating up the pan, the food cooks quickly and you put it on your plate."
            hide eggs
            show eggs_smile at Transform(zoom=1.6)
            with dissolve
            "Huh, you don't remember putting the food on the plate in this order."

    scene bg kitchen
    show sam happy at right
    with dissolve

    "You sit down and start eating your breakfast."
    show sam angry at right
    
    "But your roommate's loud music is really starting to get on your nerves."

    "Angrily, you stand up and start banging on his door."

    with dissolve
    sam "Michael, turn down your music!"
    "Nothing happens, he doesn't seem to hear you."
    $ play_audio_if_exists("audio/door_banging.wav", channel="sound")
    
    $ bang = True
    while bang:
        menu:
            "Keep banging on the door.":
                "You bang on his door again."
                $ play_audio_if_exists("audio/door_banging.wav", channel="sound")
                sam "MICHAEL!!! I'm serious, turn it down!!"
                "He still doesn't seem to hear you."
            "Call his phone.":
                $ bang = False


    $ stop_audio(channel="sound", fadeout=0.3)
    "Frustrated, you rush over and grab your phone to call him."

    show bg kitchen: 
        blur 20
    show sam angry: 
        blur 6
    show phone at Transform(zoom = 2.3)
    with dissolve

    "You pull up your messages and realize you have an unread text from him."
    "He texted you saying he was leaving the house early today."
    sam "..."
    "You realize he wasn't here the entire time."

    $ stop_audio(channel="music", fadeout=1.0)

    "Suddenly the loud music stops."
    "The sound was just a hallucination."

    show bg kitchen:
        blur 0
    hide sam angry
    hide phone
    with dissolve
    $ play_audio_if_exists("audio/schizo_kitchen.mp3", channel="music", loop=True, fadein=2.0)

    # scene bg kitchen
    show sam embarassed at right
    with dissolve

    "Sighing, you sit down to finish your breakfast."

    "You notice you didn't have much food left in the fridge."

    $ play_audio_if_exists("audio/water_running.wav", channel="sound", loop=True, fadein=0.5)
    "You decide to wash your plate and go to the grocery store."

    $ renpy.music.stop(channel="sound", fadeout=3.0)

    show sam happy at right
    with dissolve
    show obj_dog at Transform(xalign=-0.005, yalign=1.0, zoom=1.37)
    with dissolve
    sam "Charlie, come here!"
    $ play_audio_if_exists("audio/bark.wav", channel="sound2")
    "Charlie, your support dog, comes running towards you, cheerfully."
    "You grab her leash from the table."
    "Your doctors suggested getting a support dog a while back."
    "She helps you handle your symptoms even when you don't take your medication."
    hide sam happy 
    show sam embarassed at right with dissolve
    "You grimace as you think about taking your medication."
    "Sometimes, it really doesn't make you feel great."

    menu:
        "Should you take my medication?"
        "Yes":
            "You don't always like taking your medication, it makes you feel tired and sad sometimes."
            "But after talking to your doctors about it, you know it's what's best for you."
            "You've tried other ones, and this is the one that works the best."
            show sam happy:
                blur 6
            show obj_dog:
                blur 7
            show bg kitchen:
                blur 20
            show obj_meds at Transform(xalign=0.5, yalign=0.7, zoom=4.5)
            with dissolve
            $ play_audio_if_exists("audio/water_glass.wav", channel="sound")
            "You get a glass of water and take your medication."
            hide obj_meds
            with dissolve
            scene bg kitchen
            with dissolve
            show sam sad at right
            with dissolve
            $ flag["meds"] = True
        "No":
            "You decide not to take your medication."
            "You've talked with your doctor and family about how different medications make you feel, and you haven't found the right one for you yet."
            "But you've been learning to manage your symptoms with Charlie, so you think you will be okay."
            $ flag["meds"] = False

    "Picking up Charlie's leash, you clip it on her collar and head outside."
    $ play_audio_if_exists("audio/steps_door.wav", channel="sound")

    call scene_3
    return

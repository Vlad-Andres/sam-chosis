label scene_2:

    $ play_audio_if_exists("audio/door_open.ogg", channel="sound")
    scene bg kitchen
    with dissolve

    hide sam
    show sam happy at right
    with dissolve

    $ renpy.music.stop(channel="music", fadeout=1.0)
    $ play_audio_if_exists("audio/rock_music.ogg", channel="music", loop=True, fadein=1.0)

    "As you enter the kitchen, you are greeted by the sound of your roommate, Michael, playing music loudly playing through his door."
    hide sam
    show sam embarassed at right
    "You decide to ignore it for now and make breakfast."

    menu:
        "What do you want for breakfast?"
        "Cereal":
            $ flag["breakfast"] = "cereal"
            $ play_audio_if_exists("audio/cereal.ogg", channel="sound")
            show cereal
            with dissolve
            "You decide on something quick and easy. After pouring milk in your bowl you add your favorite cereal."
            hide cereal
            show cereal_hello
            with dissolve
            "Huh, weird that they made words."
        "Eggs":
            $ flag["breakfast"] = "eggs"
            $ play_audio_if_exists("audio/eggs.ogg", channel="sound")

            show eggs
            with dissolve
            "You decide on eggs and bacon. After heating up the pan the food cooks quickly and you put it on your plate."
            hide eggs
            show eggs_smile
            with dissolve
            "You don't remember putting the food on the plate in this order."

    show sam happy at right
    with dissolve

    "You sit down and start eating your breakfast."
    scene bg kitchen    
    show sam angry at right
    
    "But your roommate's loud music is starting to annoy you."

    "Angerly, you stand up and bang on his door."
    $ play_audio_if_exists("audio/door_banging.ogg", channel="sound")

    with dissolve

    sam "Michael, turn down your music!"
    "Nothing happens, he doesn't seem to hear you."
    $ play_audio_if_exists("audio/door_banging.ogg", channel="sound")
    "You hit his door again."

    sam "MICHAEL!!! I'm serious, turn it down!!"
    "Frustrated, you rush over and grab your phone to call him."

    show phone
    with dissolve

    "But as you pull up your messages you realize he texted you saying he was leaving the house early today."
    "You realize he wasn't here the entire time."

    $ stop_audio(channel="music", fadeout=1.0)

    "Suddenly the loud music stops."
    "The sound was just a hallucination."

    hide phone
    with dissolve

    show sam embarassed at right
    with dissolve

    "Frustrated, you sit down to finish your breakfast."
    "You noticed you didn't have much food left in the fridge when you made breakfast."

    $ play_audio_if_exists("audio/water_running.ogg", channel="sound")
    "You wash your plate and decide to go to the grocery store."

    show sam happy at right
    with dissolve
    show obj_dog at Transform(xalign=0.05, yalign=1.0)
    with dissolve
    "You call for your support dog, Charlie, a poodle, and grab her leash from the table. She runs over happily."
    "Sometimes my medication doesn't make me feel great."
    "I talked with my family and doctors, and they suggested having a support dog as well."
    "Charlie helps me handle my symptoms even when I don't take my medication."

    menu:
        "Before I leave, I remember my psychosis medication…should I take it?"
        "Yes":
            "I don't always like taking my medication, it makes me feel tired and sad sometimes. But after talking with my doctors, I know it's what's best for me. I've tried other ones, and this one works the best."
            show obj_meds at Transform(xalign=0.5, yalign=0.7)
            with dissolve
            "You get a glass of water and take your medication."
            hide obj_meds
            with dissolve
            scene bg kitchen
            with dissolve
            show sam sad at right
            with dissolve
            $ flag["meds"] = True
        "No":
            "I decide not to take my medication. I've talked with my doctor and family about how different medications make me feel, and I haven't found the right one for me yet. But I've been learning to manage my symptoms with Charlie, so I think I will be okay."
            $ flag["meds"] = False

    "Picking up Charlie's leash, you clip it on her collar and head outside."
    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    $ play_audio_if_exists("audio/door_open.ogg", channel="sound")

    call scene_3
    return

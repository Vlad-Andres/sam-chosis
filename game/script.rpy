### MC definition
define sam = Character(_("Sam"), color="#e7f570")
image sam_placeholder = Solid("#444444", xysize=(300, 600))

# Flags for tracking player choices
default flag = {
    "meds": False,
    "breakfast": None,
}

init python:
    def play_audio_if_exists(filename, channel="sound", loop=False, fadein=0.0):
        if filename and renpy.loadable(filename):
            renpy.music.play(filename, channel=channel, loop=loop, fadein=fadein)

    def stop_audio(channel="sound", fadeout=0.0):
        renpy.music.stop(channel=channel, fadeout=fadeout)


label splashscreen:
    scene black
    with fade

    centered "{size=40}Disclaimer{/size}\n\nThis is an early prototype.\nSome content may be incomplete or subject to change."

    pause
    return


label start:
    $ flag["meds"] = False
    $ flag["breakfast"] = None
    scene black
    with Fade(0.25, 0.0, 0.75)

    $ play_audio_if_exists("audio/nature_ambience.ogg", channel="music", loop=True, fadein=1.0)
    $ play_audio_if_exists("audio/alarm.ogg", channel="sound")

    scene bg bedroom
    with fade

    show expression leaves as falling_leaves

    "You wake up in your bedroom to the sound of your alarm going off."

    $ play_audio_if_exists("audio/bedsheets_rustle.ogg", channel="sound")
    "The bedsheets rustle as you shift, still half-lost in sleep."

    $ stop_audio(channel="sound", fadeout=0.5)
    "After lying in bed for a while, it's time for you to get up and start your day."

    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    "You walk to the giant butterfly on the wall and reach out to touch it…"

    $ stop_audio(channel="sound", fadeout=0.25)
    "But your hand phases through it, the butterfly wasn't real. They usually aren't…"

    "You shift your attention to the mirror and look at yourself."

    menu:
        "How do you see yourself?"
        "Perfectly ordinary.":
            "For a moment, your reflection feels stable—almost believable."
        "Not quite you.":
            "Your reflection hesitates, a fraction out of sync, like it's remembering how to be you."

    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    "You decide it's time to go to the kitchen and have some breakfast."

    $ play_audio_if_exists("audio/door_open.ogg", channel="sound")
    scene bg kitchen
    with dissolve

    $ renpy.music.stop(channel="music", fadeout=1.0)
    $ play_audio_if_exists("audio/rock_music.ogg", channel="music", loop=True, fadein=1.0)

    "As you enter the kitchen, you are greeted by the sound of your roommate, Michael, playing music loudly playing through his door."
    "You decide to ignore it for now and make breakfast."

    menu:
        "What do you want for breakfast?"
        "Cereal":
            $ flag["breakfast"] = "cereal"
            $ play_audio_if_exists("audio/cereal.ogg", channel="sound")
            "You decide on something quick and easy. After pouring milk in your bowl you add your favorite cereal."

            scene cereal_closeup
            "Huh, weird that they made words."
        "Eggs":
            $ flag["breakfast"] = "eggs"
            $ play_audio_if_exists("audio/eggs.ogg", channel="sound")
            "You decide on eggs and bacon. After heating up the pan the food cooks quickly and you put it on your plate."

            scene eggs_closeup
            "You don't remember putting the food on the plate in this order."

    scene bg kitchen with dissolve

    "You sit down and start eating your breakfast."
    "But your roommate's loud music is starting to annoy you."

    "Angerly, you stand up and bang on his door."
    $ play_audio_if_exists("audio/door_banging.ogg", channel="sound")

    show sam_placeholder at left_pos
    with dissolve

    sam "Michael, turn down your music!"
    "Nothing happens, he doesn't seem to hear you."
    $ play_audio_if_exists("audio/door_banging.ogg", channel="sound")
    "You hit his door again."

    sam "MICHAEL!!! I'm serious, turn it down!!"
    "Frustrated, you rush over and grab your phone to call him."

    scene phone
    with fade

    "But as you pull up your messages you realize he texted you saying he was leaving the house early today."
    "You realize he wasn't here the entire time."

    $ stop_audio(channel="music", fadeout=1.0)

    "Suddenly the loud music stops."
    "The sound was just a hallucination."

    scene bg kitchen
    with dissolve

    "Frustrated, you sit down to finish your breakfast."
    "You noticed you didn't have much food left in the fridge when you made breakfast."

    $ play_audio_if_exists("audio/water_running.ogg", channel="sound")
    "You wash your plate and decide to go to the grocery store."

    "You call for your support dog, Charlie, a poodle, and grab her leash from the table. She runs over happily."
    "Sometimes my medication doesn't make me feel great."
    "I talked with my family and doctors, and they suggested having a support dog as well."
    "Charlie helps me handle my symptoms even when I don't take my medication."

    menu:
        "Before I leave, I remember my psychosis medication…should I take it?"
        "Yes":
            $ flag["meds"] = True
            "I don't always like taking my medication, it makes me feel tired and sad sometimes. But after talking with my doctors, I know it's what's best for me. I've tried other ones, and this one works the best."
        "No":
            $ flag["meds"] = False
            "I decide not to take my medication. I've talked with my doctor and family about how different medications make me feel, and I haven't found the right one for me yet. But I've been learning to manage my symptoms with Charlie, so I think I will be okay."

    "Picking up Charlie's leash, you clip it on her collar and head outside."
    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    $ play_audio_if_exists("audio/door_open.ogg", channel="sound")

    call scene_3_walk
    return

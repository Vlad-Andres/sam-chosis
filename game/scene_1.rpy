label scene_1:
    $ flag["meds"] = False
    $ flag["breakfast"] = None
    scene black
    with Fade(0.25, 0.0, 0.75)

    $ play_audio_if_exists("audio/nature_ambience.ogg", channel="music", loop=True, fadein=1.0)
    $ play_audio_if_exists("audio/alarm.ogg", channel="sound")

    scene bg bedroom
    with fade

    # show expression leaves as falling_leaves
    show sam pjs at right
    with dissolve

    "You wake up in your bedroom to the sound of your alarm going off."

    $ play_audio_if_exists("audio/bedsheets_rustle.ogg", channel="sound")
    "The bedsheets rustle as you shift, still half-lost in sleep."

    $ stop_audio(channel="sound", fadeout=0.5)
    "After lying in bed for a while, it's time for you to get up and start your day."

    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    show obj_butterfly at butterfly_flutter
    "You try and catch the butterfly flying around your room and reach out to touch it…"

    hide obj_butterfly
    with dissolve
    $ stop_audio(channel="sound", fadeout=0.25)
    "But your hand phases through it, the butterfly wasn't real. They usually aren't…"

    "You shift your attention to the mirror and look at yourself."

    menu:
        "How do you see yourself?"
        "Perfectly ordinary.":
            show sam happy at right
            with dissolve
            "For a moment, your reflection feels stable—almost believable."
        "Not quite you.":
            show sam confused at right
            with dissolve
            "Your reflection hesitates, a fraction out of sync, like it's remembering how to be you."

    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    "You decide it's time to go to the kitchen and have some breakfast."

    call scene_2
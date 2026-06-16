label scene_1:
    $ flag["meds"] = False
    $ flag["breakfast"] = None
    window hide
    scene black
    with Fade(0.25, 0.0, 0.75)

    $ play_audio_if_exists("audio/schizo_bed.mp3", channel="music", loop=True, fadein=1.0)
    $ play_audio_if_exists("audio/alarm.mp3", channel="sound")

    pause

    scene bg bedroom
    show bg bedroom:
        blur 60
    show fx_haze at wakeup_haze_hold
    show obj_butterfly at butterfly_flutter

    show fx_eyelid_top at eyelid_top_open
    show fx_eyelid_bottom at eyelid_bottom_open
    with Dissolve(0.4)

    pause 1.0

    window auto
    "You wake up in your bedroom to the sound of your alarm going off."
    "You see a butterfly flying around your room and reach out to touch it…"

    show obj_hand at hand_reach_butterfly, Transform(zoom=1.35)
    pause 1.2

    hide obj_hand
    # show bg bedroom_blur at wakeup_blur_fadeout
    show fx_haze at wakeup_haze_fadeout
    hide obj_butterfly

    show bg bedroom: 
        blur 0
    with dissolve

    $ stop_audio(channel="sound", fadeout=0.25)
    "But your hand phases through it."
    "The butterfly wasn't real."
    "They usually aren't…"

    show bg bedroom: 
        blur 0
    with dissolve

    hide fx_eyelid_top
    hide fx_eyelid_bottom
    hide fx_haze

    show sam pjs at right
    with dissolve

    $ play_audio_if_exists("audio/bedsheets_rustle.wav", channel="sound")
    "The bedsheets rustle as you shift, still half-asleep."

    $ stop_audio(channel="sound", fadeout=0.5)
    "After lying in bed for a while, you decide to get up and out of bed."

    $ play_audio_if_exists("audio/clothing.wav", channel="sound")
    "You shift your attention to the mirror and look at yourself."

    menu:
        "How do you see yourself?"
        "Perfectly ordinary.":
            show sam happy at right
            with dissolve
            "For a moment, your reflection feels stable — almost believable."
        "Not quite you.":
            show sam confused at right
            with dissolve
            "Your reflection hesitates, a fraction out of sync, like it's remembering how to be you."

    $ play_audio_if_exists("audio/steps_door.wav", channel="sound")
    "You decide it's time to go to the kitchen and have some breakfast."

    call scene_2

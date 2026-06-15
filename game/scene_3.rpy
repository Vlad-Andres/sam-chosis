label scene_3:
    scene bg park
    with fade

    # show expression get_tone_overlay() as scene_tone
    show obj_dog at Transform(xalign=0.35, yalign=0.55)
    show sam happy at left
    with dissolve

    $ play_audio_if_exists("audio/schizo_park.wav", channel="music", loop=True)

    $ play_audio_if_exists("audio/outside_noise.wav", channel="sound", loop=True)
    "You step outside. The air is warm and there is a slight breeze."
    "You make your way towards the grocery store, a route engrained in your memory."

    # show expression get_tone_overlay() as scene_tone
    # show obj_dog at Transform(xalign=0.2, yalign=1.0)
    # show obj_flowers at Transform(xalign=0.08, yalign=0.3)
    # with dissolve

    "You take a moment to admire the scenery around you, and give Charlie a moment to play in the grass."

    if flag["meds"]:
        "You look at the flowers, but they don't interest you."
        hide sam happy with dissolve
        show sam embarassed at left with dissolve
        "You decide not to waste any more time and call Charlie over so you can head on your way."
    else:
        "You feel the sun on your skin and enjoy the smell of the flowers around you."
        "Looking at the colorful landscape and seeing Charlie play makes you feel warm and fuzzy inside."
        show bg park:
            blur 20
        show sam happy at left:
            blur 6
        show obj_dog at Transform(xalign=0.35, yalign=0.55):
            blur 7
        show obj_flowers at Transform(xalign=0.75, yalign=0.7, zoom=2.7)
        with dissolve

        "While you admire the flowers, you notice that some look a bit off."

        "You decide to call Charlie over and head on your way."

    # hide obj_flowers
    # with dissolve

    scene title_card_10_minutes
    with dissolve

    hide scene_tone

    pause 1.0

    scene bg park
    with dissolve

    # show expression get_tone_overlay() as scene_tone
    show obj_dog at Transform(xalign=0.28, yalign=0.8)
    show sam confused at left
    with dissolve

    "A voice catches you before you reach the next block."
    "You look up to notice a person standing confused in the middle of the sidewalk."
    "They turn and look at you."

    show mystery_person_sprite at right
    with dissolve
    mystery_person "Hi, I'm a bit lost, can you help me find the post office?"

    if not flag["meds"]:
        "Lots of butterflies in their hair. That is odd.."

    "Your doctors suggested training Charlie to greet people by walking over and sitting beside them, so you can tell if someone is really there."
    "You look down at Charlie, who waits by you patiently, wagging her tail."
    sam "Charlie, go say hi!"
    "You watch as Charlie looks in the direction you point, and turns back to you."
    "Realizing that the person speaking to you isn't actually there, you understand it's just a hallucination."

    hide mystery_person_sprite
    with dissolve

    "The hallucination fades away."
    "You're left with an odd feeling in your stomach. The person looked so real."

    "Despite that, you continue on your journey and reach the supermarket."

    call scene_4
    return


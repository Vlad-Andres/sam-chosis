label scene_3_walk:
    scene bg sidewalk
    with fade

    show expression get_tone_overlay() as scene_tone

    $ play_audio_if_exists("audio/city_walk_soft.ogg" if flag["meds"] else "audio/city_walk_vivid.ogg", channel="music", loop=True, fadein=tone_fadein())

    "You step outside. The air is warm and there is a slight breeze."
    "You make your way towards the grocery store, a route engrained in your memory."

    scene bg park_flowers
    with dissolve

    show expression get_tone_overlay() as scene_tone

    "You take a moment to admire the scenery around you, and give Charlie a moment to play in the grass."

    if flag["meds"]:
        "You look at the flowers, but they don't interest you."
        "You decide not to waste any more time and call Charlie over so you can head on your way."
    else:
        "You feel the sun on your skin and enjoy the smell of the flowers around you."
        "Looking at the colorful landscape and seeing Charlie play makes you feel warm and fuzzy inside."
        "While you admire the flowers, you notice that some look a bit off."
        "You decide to call Charlie over and head on your way."

    scene title_card_10_minutes
    with dissolve

    hide scene_tone

    pause 1.0

    scene bg sidewalk
    with dissolve

    show expression get_tone_overlay() as scene_tone


    "A voice catches you before you reach the next block."
    "You look up to notice a person standing confused in the middle of the sidewalk."
    "They turn and look at you."
    mystery_person "Hi, I'm a bit lost, can you help me find the post office?"

    if flag["meds"]:
        "Normal looking person, no odd aspects."
    else:
        "Still a person, but something odd, maybe a lot of butterflies in their hair, a third eye, idk."

    "Something feels wrong."
    "Sometimes your psychosis makes hallucinations of people."
    "Your doctors suggested training Charlie to greet people by walking over and sitting beside them, so you can tell if someone is really there."
    "You look down at Charlie, who waits by you patiently, wagging her tail."
    sam "Charlie, go say hi!"
    "You watch as Charlie looks in the direction you point, and turns back to you."
    "Realizing that the person speaking to you isn't actually there, you understand it's just a hallucination."

    "The hallucination fades away."
    "You're left with an odd feeling in your stomach. The person looked so real."

    "Despite that, you continue on your journey and reach the supermarket."

    call scene_4_supermarket
    return


label scene_4_supermarket:
    scene bg supermarket_entrance
    with fade

    show expression get_tone_overlay() as scene_tone

    $ play_audio_if_exists("audio/store_music_soft.ogg" if flag["meds"] else "audio/store_music.ogg", channel="music", loop=True, fadein=tone_fadein())
    $ play_audio_if_exists("audio/store_scanner.ogg", channel="sound")

    "You step into the supermarket."
    "The supermarket is bustling with people."
    "You scan the scene before you."

    scene bg supermarket_breakfast_aisle
    with dissolve

    show expression get_tone_overlay() as scene_tone

    "You walk towards the breakfast aisle."
    "There are students with a cart of party food, a mom with a stroller, and an old man with a walking stick looking at the shelves."

    $ play_audio_if_exists("audio/crowd_chatter_soft.ogg" if flag["meds"] else "audio/crowd_chatter.ogg", channel="sound", loop=True)

    "The overwhelming number of people in the small aisle suddenly makes you panic."
    "You feel overwhelmed, like an intruder."

    $ play_audio_if_exists("audio/kid_doggy.ogg", channel="sound")
    "Doggy!!"

    scene bg supermarket_crowded_aisle
    with dissolve

    show expression get_tone_overlay() as scene_tone

    "You feel like everyone is looking at you."
    "Everyone knows that you see things."

    $ play_audio_if_exists("audio/heartbeat.ogg", channel="sound", loop=True)

    show panic_overlay at panic_pulse

    "Charlie comes up to you, and the feel of her fur against your hand helps you calm down."
    "After a few deep breaths, you start to relax."

    scene bg supermarket_crowded_aisle_stare
    with Fade(0.05, 0.0, 0.2, color="#fff")

    show expression get_tone_overlay() as scene_tone
    show panic_overlay at panic_pulse

    "Then everything freezes."
    "Every face in the aisle seems to turn toward you at once."
    "They're all staring."

    $ stop_audio(channel="sound", fadeout=0.25)

    "Charlie starts pawing at you."
    "You are reminded of what happened earlier."
    sam "Charlie, go say hi!"
    "Charlie stays by your side."

    hide panic_overlay
    with Dissolve(0.3)

    scene bg supermarket_crowded_aisle
    with dissolve

    show expression get_tone_overlay() as scene_tone

    "You are snapped back to reality."
    "No one was staring at you."
    "The group of students are still laughing, and the mom is wheeling her kid away."

    $ stop_audio(channel="sound", fadeout=0.5)
    $ play_audio_if_exists("audio/store_scanner.ogg", channel="sound")
    grandpa "Are you okay?"
    hide scene_tone
    with dissolve

    $ stop_audio(channel="music", fadeout=0.5)
    $ stop_audio(channel="sound", fadeout=0.2)

    sam "I'm fine, thanks! Come on Charlie, good girl."

    centered "{size=48}-- END --{/size}"

    return

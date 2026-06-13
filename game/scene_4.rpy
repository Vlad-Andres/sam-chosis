label scene_4:
    scene bg supermarket_entrance 
    with fade


    $ play_audio_if_exists("audio/store_music_soft.ogg" if flag["meds"] else "audio/store_music.ogg", channel="music", loop=True, fadein=tone_fadein())
    $ play_audio_if_exists("audio/store_scanner.ogg", channel="sound")

    "You step into the supermarket."

    scene bg supermarket_aisle at camera_scan
    with dissolve

    "The supermarket is bustling with people."

    "You walk towards the breakfast aisle."
    "There are students with a cart of party food, a mom with a stroller, and an old man with a walking stick looking at the shelves."

    $ play_audio_if_exists("audio/crowd_chatter_soft.ogg" if flag["meds"] else "audio/crowd_chatter.ogg", channel="sound", loop=True)

    "The overwhelming number of people in the small aisle suddenly makes you panic."
    "You feel overwhelmed, like an intruder."
    
    # Starts with a slow heartbeat audio

    show panic_overlay at (panic_pulse_med_slow if flag["meds"] else panic_pulse_nomed_slow)
    # Starts with a slow heartbeat shake
    show layer master at (heartbeat_shake_med_slow if flag["meds"] else heartbeat_shake_nomed_slow)
    show sam scared at right
    with dissolve

    $ play_audio_if_exists("audio/kid_doggy.ogg", channel="sound")
    "Doggy!!"

    # Heartbeat becomes more frequent (medium) & medium audio
    $ play_audio_if_exists("audio/heartbeat_fast.mp3", channel="sound", loop=True, start=0.5)
    show panic_overlay at (panic_pulse_med_medium if flag["meds"] else panic_pulse_nomed_medium)
    show layer master at (heartbeat_shake_med_medium if flag["meds"] else heartbeat_shake_nomed_medium)
    "You feel like everyone is looking at you."

    # Heartbeat becomes even more frequent (fast) & fast audio
    show panic_overlay at (panic_pulse_med_fast if flag["meds"] else panic_pulse_nomed_fast)
    show layer master at (heartbeat_shake_med_fast if flag["meds"] else heartbeat_shake_nomed_fast)
    "Everyone knows that you see things."

    
    # Dog appears: heartbeat decreases (back to slow) & slow audio
    show obj_dog at left
    show panic_overlay at (panic_pulse_med_slow if flag["meds"] else panic_pulse_nomed_slow)
    show layer master at (heartbeat_shake_med_slow if flag["meds"] else heartbeat_shake_nomed_slow)
    with dissolve
    "Charlie comes up to you, and the feel of her fur against your hand helps you calm down."


    "After a few deep breaths, you start to relax."

    # Fades out completely and stops
    hide panic_overlay
    show layer master
    $ stop_audio(channel="sound", fadeout=1.5)
    with Dissolve(1.5)

    scene bg supermarket_aisle_stare
    with Fade(0.05, 0.0, 0.2, color="#fff")


    show sam shocked at right
    "Then everything freezes."
    # Starts medium heartbeat audio for the stare sequence
    $ play_audio_if_exists("audio/heartbeat_fast.mp3", channel="sound", loop=True, start=0.5)
    show panic_overlay at (panic_pulse_med_medium if flag["meds"] else panic_pulse_nomed_medium)
    show layer master at (heartbeat_shake_med_medium if flag["meds"] else heartbeat_shake_nomed_medium)
    "Every face in the aisle seems to turn toward you at once."
    "They're all staring."

    $ stop_audio(channel="sound", fadeout=0.25)

    show obj_dog at left
    show sam confused at right
    # Plays slow heartbeat audio as the heartbeat decreases
    show panic_overlay at (panic_pulse_med_slow if flag["meds"] else panic_pulse_nomed_slow)
    show layer master at (heartbeat_shake_med_slow if flag["meds"] else heartbeat_shake_nomed_slow)

    "Charlie starts pawing at you."
    "You are reminded of what happened earlier."
    sam "Charlie, go say hi!"
    "Charlie stays by your side."

    hide panic_overlay
    show layer master
    # Stop heartbeat audio completely
    $ stop_audio(channel="sound", fadeout=0.3)
    with Dissolve(0.3)

    scene bg supermarket_aisle
    with dissolve

    "You are snapped back to reality."
    "No one was staring at you."
    "The group of students are still laughing, and the mom is wheeling her kid away."

    $ stop_audio(channel="sound", fadeout=0.5)
    $ play_audio_if_exists("audio/store_scanner.ogg", channel="sound")

    show grandpa_sprite at Transform(xalign=0.75, yalign=1.0)
    show sam embarassed at right
    with dissolve
    grandpa "Are you okay?"

    hide scene_tone
    hide grandpa_sprite
    with dissolve

    $ stop_audio(channel="music", fadeout=0.5)
    $ stop_audio(channel="sound", fadeout=0.2)

    show sam happy at right
    with dissolve
    sam "I'm fine, thanks! Come on Charlie, good girl."

    centered "{size=48}-- END --{/size}"

    return
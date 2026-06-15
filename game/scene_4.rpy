label scene_4:
    scene bg supermarket_entrance 
    with fade


    # $ play_audio_if_exists("audio/store_ambience.mp3" if flag["meds"] else "audio/store_music.ogg", channel="music", loop=True, fadein=tone_fadein())
    $ play_audio_if_exists("audio/schizo_supermarket.mp3", channel="music", loop=True)
    $ play_audio_if_exists("audio/store_ambience.mp3", channel="sound", loop=True)

    "You step into the supermarket."

    scene bg supermarket_aisle at camera_scan
    with dissolve

    "The supermarket is bustling with people."

    "You walk towards the breakfast aisle."
    "You see students with a cart of party food, a mom with a stroller, and an old man with a walking stick looking at the shelves."

    "The overwhelming number of people in the small aisle suddenly makes you panic."
    
    # Starts with a slow heartbeat audio
    show panic_overlay at (panic_pulse_med_slow if flag["meds"] else panic_pulse_nomed_slow)
    
    # Starts with a slow heartbeat shake
    show layer master at (heartbeat_shake_med_slow if flag["meds"] else heartbeat_shake_nomed_slow)
    show sam scared at right
    with dissolve

    "You feel overwhelmed, like an intruder."
    
    # Heartbeat becomes more frequent (medium) & medium audio
    $ play_audio_if_exists("audio/heartbeat_fast.mp3", channel="sound2", loop=True, start=0.5)
    show panic_overlay at (panic_pulse_med_medium if flag["meds"] else panic_pulse_nomed_medium)
    show layer master at (heartbeat_shake_med_medium if flag["meds"] else heartbeat_shake_nomed_medium)
    $ stop_audio(channel="music", fadeout=3.3)
    
    "You feel like everyone is looking at you."
    
    # Sound becomes muffled
    $ play_audio_if_exists("audio/schizo_supermarket_muffled.mp3", channel="music", loop=True, fadein = 1.3)
    $ play_audio_if_exists("audio/store_ambience_muffled.wav", channel="sound", loop=True, fadein=3.3)

    # Heartbeat becomes even more frequent (fast) & fast audio
    show panic_overlay at (panic_pulse_med_fast if flag["meds"] else panic_pulse_nomed_fast)
    show layer master at (heartbeat_shake_med_fast if flag["meds"] else heartbeat_shake_nomed_fast)
    "Everyone knows that you see things."

    
    # Dog appears: heartbeat decreases (back to slow) & slow audio
    show obj_dog at Transform(xalign=-0.01, yalign=1.0, zoom=1.37)
    show panic_overlay at (panic_pulse_med_slow if flag["meds"] else panic_pulse_nomed_slow)
    show layer master at (heartbeat_shake_med_slow if flag["meds"] else heartbeat_shake_nomed_slow)
    with dissolve
    $ play_audio_if_exists("audio/dog_whine.wav", channel="sound2")
    "Charlie comes up to you, and the feel of her fur against your hand helps you calm down a little."

    "After a few deep breaths, you slowly start to relax."

    # Fades out completely and stops
    hide panic_overlay
    show layer master
    $ stop_audio(channel="sound", fadeout=1.5)
    
    with Dissolve(1.5)

    scene bg supermarket_aisle_stare at Transform(yalign=0.55)

    with Fade(0.05, 0.0, 0.2, color="#fff")

    show sam shocked at right
    "Then everything freezes."

    # Starts medium heartbeat audio for the stare sequence
    $ play_audio_if_exists("audio/heartbeat_fast.mp3", channel="sound2", loop=True, start=0.5)
    show panic_overlay at (panic_pulse_med_medium if flag["meds"] else panic_pulse_nomed_medium)
    show layer master at (heartbeat_shake_med_medium if flag["meds"] else heartbeat_shake_nomed_medium)
    "Every face in the aisle seems to turn toward you at once."
    "They're all staring."

    $ stop_audio(channel="sound", fadeout=0.25)

    show obj_dog at Transform(xalign=-0.005, yalign=1.0, zoom = 1.37)
    show sam confused at right
    # Plays slow heartbeat audio as the heartbeat decreases
    show panic_overlay at (panic_pulse_med_slow if flag["meds"] else panic_pulse_nomed_slow)
    show layer master at (heartbeat_shake_med_slow if flag["meds"] else heartbeat_shake_nomed_slow)

    $ play_audio_if_exists("audio/dog_whine.wav", channel="sound2")
    "Charlie starts pawing at you."
    "You are reminded of what happened earlier."

    sam "Charlie, go say hi!"
    $ stop_audio(channel="sound2", fadeout=4.3)
    $ stop_audio(channel="sound", fadeout=4.3)
    "Charlie stays by your side."

    hide panic_overlay
    show layer master
    # Stop heartbeat audio completely
    $ play_audio_if_exists("audio/store_ambience.mp3", channel="sound", loop=True, fadein=4.3)
    $ play_audio_if_exists("audio/schizo_supermarket.mp3", channel="music", loop=True, fadein=5.3)
    
    with Dissolve(0.3)

    scene bg supermarket_aisle at Transform(yalign=0.5)
    with dissolve

    "You are snapped back to reality."
    "No one was staring at you at all."
    "The group of students are still laughing, and the mom is wheeling her kid away."

    show grandpa_sprite at Transform(xalign=0.6, yalign=1.0)
    show sam embarassed at right
    with dissolve
    grandpa "Are you okay?"
    
    $ play_audio_if_exists("audio/bark.wav", channel="sound2")
    "Charlie lets out a little reassuring bark."

    hide scene_tone
    hide grandpa_sprite
    with dissolve

    # $ stop_audio(channel="music", fadeout=0.5)
    $ stop_audio(channel="sound", fadeout=8.2)

    show sam happy at right
    with dissolve
    sam "I'm fine, thanks! Come on Charlie, good girl!"

    jump credits


default credits_text = """
{size=60}{b}Thank You for Playing!{/b}{/size}

Storyline
Amelia Kapuścińska
Zita Rátkai
Viktoria Stojanov
Min Yue Tan
Stefan Leon
Vlad Mutruc

Scripting & Writing
Amelia Kapuścińska

Programming
Vlad Mutruc
Stefan Leon

Art
Zita Rátkai

Music & Sound Effects
Viktoria Stojanov
"""

label credits:

    scene menu_bg
    with fade

    show credits_overlay
    show expression Text(credits_text, color="#FFFFFF", outlines=[(3, "#000000", 0, 0)]) at credits_scroll
    pause 20.0

    return
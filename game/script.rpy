### MC definition
define sam = Character(_("Sam"), color="#e7f570")
image sam_placeholder = Solid("#444444", xysize=(300, 600))

# Flags for tracking player choices
default flag = {
    "meds": False,
    "breakfast": None,
}

init python:
    def play_audio_if_exists(filename, channel="sound", loop=False, fadein=0.0, start=0.0):
        if filename and renpy.loadable(filename):
            play_filename = filename
            if start > 0.0:
                play_filename = "<from {}>".format(start) + filename
            renpy.music.play(play_filename, channel=channel, loop=loop, fadein=fadein)

    def stop_audio(channel="sound", fadeout=0.0):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    renpy.music.register_channel(
        "sound2",
        mixer="sound",
    )

    preferences.set_volume("music", 0.5)
    preferences.set_volume("sound", 0.9)
    preferences.set_volume("sound2", 0.7)


label start:
    call scene_1
    # call scene_4
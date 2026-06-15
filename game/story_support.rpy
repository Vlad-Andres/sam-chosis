define mystery_person = Character(_("Stranger"), color="#f0b6ff")
define grandpa = Character(_("Grandpa"), color="#9fd4ff")

init python:
    def get_tone_overlay():
        if renpy.store.flag.get("meds"):
            return renpy.store.Solid("#8ca0aa55")

        return renpy.store.Solid("#ff9a3f55")

    def tone_fadein():
        if renpy.store.flag.get("meds"):
            return 1.5

        return 0.5

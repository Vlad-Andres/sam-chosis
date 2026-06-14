### Images

## -- Helper: scale a JPG background to fill screen --
## Use Transform with fit="cover" on every background

image bg bedroom = ConditionSwitch(
    "flag['meds']", Transform("images/backgrounds/bedroom_med.jpg", fit="cover", size=(1920, 1080)),
    "True",         Transform("images/backgrounds/bedroom_nomed.jpg", fit="cover", size=(1920, 1080)),
)

image bg kitchen = ConditionSwitch(
    "flag['meds']", Transform("images/backgrounds/kitchen_med.jpg", fit="cover", size=(1920, 1080)),
    "True",         Transform("images/backgrounds/kitchen_nomed.jpg", fit="cover", size=(1920, 1080)),
)

image eggs_closeup = Fixed(
    Solid("#9da41a"),
    Text("top down view of the eggs and bacon making a smiley face", xalign=0.5, yalign=0.5, size=64, color="#ffffff"),
)

image cereal_closeup = Fixed(
    Solid("#1a21a4"),
    Text("top down view of the cereal saying goodmorning Sam?", xalign=0.5, yalign=0.5, size=64, color="#ffffff"),
)

## Phone shown as overlay on kitchen background
image phone = Transform("images/objects/phone.png", fit="contain", size=(400, 700), xalign=0.5, yalign=0.5)
image eggs = Transform("images/objects/eggs.png", fit="contain", size=(800, 600), xalign=0.5, yalign=0.5)
image eggs_smile = Transform("images/objects/eggs_smile.png", fit="contain", size=(800, 600), xalign=0.5, yalign=0.4)

image cereal = Transform("images/objects/cereal.png", fit="contain", size=(800, 600), xalign=0.5, yalign=0.5)
image cereal_hello = Transform("images/objects/cereal_hello.png", fit="contain", size=(800, 600), xalign=0.5, yalign=0.5)

image bg park = ConditionSwitch(
    "flag['meds']", Transform("images/backgrounds/park_med.jpg", fit="cover", size=(1920, 1080)),
    "True",         Transform("images/backgrounds/park_nomed.jpg", fit="cover", size=(1920, 1080)),
)

image bg supermarket_entrance = ConditionSwitch(
    "flag['meds']", Transform("images/backgrounds/store_med.jpg", fit="cover", size=(1920, 1080)),
    "True",         Transform("images/backgrounds/store_nomed.jpg", fit="cover", size=(1920, 1080)),
)

image bg supermarket_aisle = ConditionSwitch(
    "flag['meds']", Transform("images/backgrounds/aisle_med.jpg", fit="cover", size=(1920, 1080)),
    "True",         Transform("images/backgrounds/aisle_nomed.jpg", fit="cover", size=(1920, 1080)),
)

image bg supermarket_aisle_stare = ConditionSwitch(
    "flag['meds']", Transform("images/backgrounds/pplstaring_med.jpg", fit="cover", size=(1920, 1080)),
    "True",         Transform("images/backgrounds/pplstaring_nomed.jpg", fit="cover", size=(1920, 1080)),
)

image title_card_10_minutes = Fixed(
    Solid("#111111"),
    Text("10 minutes later", xalign=0.5, yalign=0.5, size=72, color="#ffffff"),
)

image menu_bg = Transform("images/backgrounds/start_screen.jpg", fit="cover", size=(1920, 1080))

image panic_overlay = Solid("#7a0018")
image fx_haze = Solid("#ffffff")
image fx_eyelid_top = Transform(Solid("#000000"), xysize=(1920, 540))
image fx_eyelid_bottom = Transform(Solid("#000000"), xysize=(1920, 540))

## -- Sam character expressions --
image sam pjs     = Transform("images/sam/pjs.png",       fit="contain", size=(500, 900), yalign=1.0, zoom=1.6)
image sam happy   = Transform("images/sam/happy.png",     fit="contain", size=(500, 900), yalign=1.0, zoom=1.6)
image sam sad     = Transform("images/sam/sad.png",       fit="contain", size=(500, 900), yalign=1.0, zoom=1.6)
image sam angry   = Transform("images/sam/angry.png",     fit="contain", size=(500, 900), yalign=1.0, zoom=1.55)
image sam scared  = Transform("images/sam/scared.png",    fit="contain", size=(500, 900), yalign=1.0, zoom=1.6)
image sam shocked = Transform("images/sam/shocked.png",   fit="contain", size=(500, 900), yalign=1.0, zoom=1.6)
image sam confused= Transform("images/sam/confused.png",  fit="contain", size=(500, 900), yalign=1.0, zoom=1.6)
image sam embarassed = Transform("images/sam/embarassed.png", fit="contain", size=(500, 900), yalign=1.0, zoom=1.6)

## -- Mystery person (woman) — switches on meds flag --
image mystery_person_sprite = ConditionSwitch(
    "flag['meds']", Transform("images/characters/woman_med.png",   fit="contain", size=(450, 850), yalign=1.0, zoom=1.78),
    "True",         Transform("images/characters/woman_nomed.png", fit="contain", size=(450, 850), yalign=1.0, zoom = 1.78),
)

## -- Grandpa --
image grandpa_sprite = Transform("images/characters/grandpa.png", fit="contain", size=(450, 850), yalign=1.0, zoom=1.85)

## -- Objects --
image obj_dog       = Transform("images/objects/dog.png",       fit="contain", size=(300, 300), yalign=1.0, zoom=1.38)
image obj_butterfly = Transform("images/objects/butterfly.png", fit="contain", size=(350, 350))
image obj_flowers   = Transform("images/objects/flowers.png",   fit="contain", size=(400, 400), yalign=1.0)
image obj_meds      = Transform("images/objects/meds.png",      fit="contain", size=(200, 200))
image obj_hand      = Transform("images/objects/hand.png",      fit="contain", size=(300, 300))

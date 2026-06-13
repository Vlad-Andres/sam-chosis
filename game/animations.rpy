### Animations and Transitions

# Butterfly flying around the screen in a looping erratic path
transform butterfly_flutter:
    xalign 0.75 yalign 0.25
    rotate 15
    block:
        linear 1.4  xalign 0.55 yalign 0.15 rotate -10
        linear 1.0  xalign 0.30 yalign 0.30 rotate 20
        linear 1.2  xalign 0.15 yalign 0.15 rotate -15
        linear 1.3  xalign 0.25 yalign 0.55 rotate 10
        linear 1.1  xalign 0.50 yalign 0.70 rotate -20
        linear 1.4  xalign 0.78 yalign 0.50 rotate 15
        linear 1.2  xalign 0.85 yalign 0.20 rotate -5
        linear 1.0  xalign 0.60 yalign 0.10 rotate 20
        linear 1.3  xalign 0.40 yalign 0.40 rotate -10
        linear 1.1  xalign 0.20 yalign 0.65 rotate 15
        linear 1.2  xalign 0.50 yalign 0.80 rotate -15
        linear 1.4  xalign 0.75 yalign 0.25 rotate 10
        repeat

# Tried a fancier zoom in, doesn't look that nice
transform pan_zoom_in:
    zoom 1.0
    xalign 0.5
    yalign 0.5
    linear 1.5 zoom 2.0 xalign 0.5 yalign 0.6


# Camera scan transform: zooms, pans across the scene, then zooms back out
transform camera_scan:
    # Start at normal size
    zoom 1.0 xalign 0.5 yalign 0.5
    # Zoom in to 1.3 on the left side
    ease 2.0 zoom 1.3 xalign 0.15 yalign 0.3
    # Scan slowly to the right
    ease 3.0 xalign 0.85 yalign 0.4
    # Scan/pan back towards the center
    ease 2.0 xalign 0.5 yalign 0.5
    # Zoom out back to 1.0
    ease 1.5 zoom 1.0


# Custom character positions, the default ones are bad
transform left_pos:
    xalign 0.2
    yalign 1.0

transform right_pos:
    xalign 0.8
    yalign 1.0

# --- Medicated Heartbeat Pulses (Subtle, lower opacity) ---

transform panic_pulse_med_slow:
    alpha 0.0 zoom 1.0
    block:
        ease 0.08 alpha 0.10 zoom 1.01
        ease 0.08 alpha 0.05 zoom 1.00
        ease 0.08 alpha 0.15 zoom 1.02
        ease 0.16 alpha 0.0 zoom 1.00
        pause 0.90
        repeat

transform panic_pulse_med_medium:
    alpha 0.0 zoom 1.0
    block:
        ease 0.06 alpha 0.15 zoom 1.015
        ease 0.06 alpha 0.08 zoom 1.00
        ease 0.07 alpha 0.22 zoom 1.025
        ease 0.15 alpha 0.0 zoom 1.00
        pause 0.53
        repeat

transform panic_pulse_med_fast:
    alpha 0.0 zoom 1.0
    block:
        ease 0.05 alpha 0.20 zoom 1.02
        ease 0.05 alpha 0.10 zoom 1.00
        ease 0.06 alpha 0.30 zoom 1.03
        ease 0.12 alpha 0.0 zoom 1.00
        pause 0.21
        repeat


# --- Unmedicated Heartbeat Pulses (Intense, higher opacity) ---

transform panic_pulse_nomed_slow:
    alpha 0.0 zoom 1.0
    block:
        ease 0.08 alpha 0.25 zoom 1.02
        ease 0.08 alpha 0.12 zoom 1.00
        ease 0.08 alpha 0.35 zoom 1.04
        ease 0.16 alpha 0.0 zoom 1.00
        pause 0.98
        repeat

transform panic_pulse_nomed_medium:
    alpha 0.0 zoom 1.0
    block:
        ease 0.06 alpha 0.40 zoom 1.03
        ease 0.06 alpha 0.20 zoom 1.00
        ease 0.06 alpha 0.55 zoom 1.05
        ease 0.14 alpha 0.0 zoom 1.00
        pause 0.53
        repeat

transform panic_pulse_nomed_fast:
    alpha 0.0 zoom 1.0
    block:
        ease 0.04 alpha 0.55 zoom 1.04
        ease 0.04 alpha 0.25 zoom 1.00
        ease 0.04 alpha 0.75 zoom 1.06
        ease 0.10 alpha 0.0 zoom 1.00
        pause 0.15
        repeat


# --- Medicated Heartbeat Shakes ---

# Slow (Subtle)
transform heartbeat_shake_med_slow:
    xoffset 0 yoffset 0
    block:
        ease 0.07  xoffset  3  yoffset -1
        ease 0.07  xoffset -2  yoffset  1
        ease 0.08  xoffset  0  yoffset  0
        ease 0.05  xoffset  2  yoffset -1
        ease 0.05  xoffset -1  yoffset  1
        ease 0.08  xoffset  0  yoffset  0
        pause 0.90
        repeat

# Medium (Subtle)
transform heartbeat_shake_med_medium:
    xoffset 0 yoffset 0
    block:
        ease 0.06  xoffset  4  yoffset -2
        ease 0.06  xoffset -3  yoffset  1
        ease 0.07  xoffset  0  yoffset  0
        ease 0.04  xoffset  3  yoffset -1
        ease 0.04  xoffset -2  yoffset  1
        ease 0.07  xoffset  0  yoffset  0
        pause 0.45
        repeat

# Fast (Subtle)
transform heartbeat_shake_med_fast:
    xoffset 0 yoffset 0
    block:
        ease 0.05  xoffset  5  yoffset -2
        ease 0.05  xoffset -4  yoffset  2
        ease 0.06  xoffset  0  yoffset  0
        ease 0.03  xoffset  4  yoffset -1
        ease 0.03  xoffset -3  yoffset  1
        ease 0.06  xoffset  0  yoffset  0
        pause 0.15
        repeat


# --- Unmedicated Heartbeat Shakes ---

# Slow (Intense)
transform heartbeat_shake_nomed_slow:
    xoffset 0 yoffset 0
    block:
        ease 0.04  xoffset  8  yoffset -4
        ease 0.04  xoffset -6  yoffset  3
        ease 0.04  xoffset  4  yoffset -2
        ease 0.06  xoffset  0  yoffset  0
        ease 0.04  xoffset  6  yoffset -3
        ease 0.04  xoffset -4  yoffset  2
        ease 0.06  xoffset  0  yoffset  0
        pause 1.0
        repeat

# Medium (Intense)
transform heartbeat_shake_nomed_medium:
    xoffset 0 yoffset 0
    block:
        ease 0.03  xoffset  12  yoffset -6
        ease 0.03  xoffset -9  yoffset  4
        ease 0.03  xoffset  6  yoffset -3
        ease 0.05  xoffset  0  yoffset  0
        ease 0.03  xoffset  8  yoffset -4
        ease 0.03  xoffset -6  yoffset  3
        ease 0.05  xoffset  0  yoffset  0
        pause 0.50
        repeat

# Fast (Intense)
transform heartbeat_shake_nomed_fast:
    xoffset 0 yoffset 0
    block:
        ease 0.02  xoffset  16  yoffset -8
        ease 0.02  xoffset -13  yoffset  6
        ease 0.02  xoffset  9  yoffset -4
        ease 0.04  xoffset  0  yoffset  0
        ease 0.02  xoffset  11  yoffset -5
        ease 0.02  xoffset -9  yoffset  4
        ease 0.04  xoffset  0  yoffset  0
        pause 0.15
        repeat

transform slow_zoom:
    zoom 1.0
    linear 20.0 zoom 1.1
    linear 20.0 zoom 1.0
    repeat
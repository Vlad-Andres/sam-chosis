image leaf_small = Transform(
    "images/leaf.png",
    zoom=0.1
)

init python:
    leaves = SnowBlossom(
        "leaf_small",
        count=30,
        border=50,
        xspeed=(-20, 20),
        yspeed=(80, 150),
        fast=True
    )
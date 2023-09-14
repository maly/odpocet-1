cislo = 9

def on_button_pressed_a():
    global cislo; cislo = 10
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global cislo
    while cislo > 1:
        basic.show_number(cislo--)
    basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)

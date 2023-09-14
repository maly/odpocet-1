let cislo = 9
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    cislo = 10
})
basic.forever(function on_forever() {
    
    while (cislo > 1) {
        basic.showNumber(cislo)
        cislo += -1
    }
    basic.showIcon(IconNames.Happy)
})

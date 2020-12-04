def on_button_pressed_a():
    music.set_built_in_speaker_enabled(True)
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

music.set_built_in_speaker_enabled(False)
basic.show_icon(IconNames.NO)

def on_forever():
    music.play_melody("C C G G A A G - ", 120)
    music.play_melody("F F E E D D C - ", 120)
basic.forever(on_forever)

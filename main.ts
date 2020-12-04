input.onButtonPressed(Button.A, function () {
    music.setBuiltInSpeakerEnabled(true)
})
music.setBuiltInSpeakerEnabled(false)
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    music.playMelody("C C G G A A G - ", 120)
    music.playMelody("F F E E D D C - ", 120)
})

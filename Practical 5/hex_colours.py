COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blueviolet": "#8a2be2",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chocolate": "#d2691e",
    "coral": "#ff7f50"
}
colour = input("Enter colour name : ").lower()
finish = False
while not finish:
    if colour in COLOUR_TO_HEX:
        print(COLOUR_TO_HEX[colour])
        colour = input("Enter colour name : ").lower()
    elif colour == "":
        print("Thank You")
        finish = True
    else:
        print("Try other colour name")
        colour = input("Enter colour name : ").lower()
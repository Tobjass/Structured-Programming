import random


def randomCombo():
    while True:
        cijfers = random.randrange(1000, 10000)
        if dubbeleCijferCheck(cijfers) == 4 and nullenCheck(cijfers) == 0:
            break
    return str(cijfers)
'''
Eerste gok voor de computer genereren: While loop blijft lopen totdat het een random 4-cijferig getal zonder dubbele 
cijfers en nullen heeft.
'''


def dubbeleCijferCheck(Input):
    cijfers = []
    for i in range(0, 4):
        if str(Input)[i] in cijfers:
            break
        else:
            cijfers.append(str(Input)[i])
    return len(cijfers)
'''
Checken of er dubbele cijfers in de input zitten. Voegt cijfer aan de lijst toe als die er nog niet in zit. Als dit wel
het geval is stopt de loop en returnt ie een te korte lijst, wat aangeeft dat er een dubbel cijfer in zit.
'''


def nullenCheck(Input):
    nullen = []
    for i in range(0, 4):
        if int(str(Input)[i]) == 0:
            nullen.append(str(Input)[i])
    return len(nullen)
'''
Checken of er een nul in de input zit. Voegt nul aan de lijst toe als die er in zit. Als er een nul in de lijst zit 
bevat de input nullen.
'''


def dubbeleCijfers(Input):
    cijfers = []
    for i in range(0, 4):
        if Input[i] in cijfers:
            return Input[i]
        else:
            cijfers.append(Input[i])
    return Input
'''
Checken welke cijfers in de input dubbel zijn. Voegt cijfer aan de lijst toe als die er nog niet in zit. Als dit wel het
geval is stopt de loop en returnt ie het cijfer wat dubbel is.
'''


def inputControleren(Input, nummer, computerGeheugen, oudeComputerInputs, niet_aanwezig):
    aanwezig = []
    goed = []

    for i in range(0, 4):
        if Input[i] == nummer[i]:
            goed.append(Input[i])
            computerGeheugen[i] = Input[i]
        elif Input[i] != nummer[i] and Input[i] in nummer:
            aanwezig.append(Input[i])
        else:
            niet_aanwezig.append(Input[i])

    oudeComputerInputs.append(Input)

    if len(goed) == 0 and len(aanwezig) == 0:
        Input = list(str(randomCombo()))
        for i in range(0, 4):
            if Input[i] == oudeComputerInputs[0][i] or Input[i] in niet_aanwezig or Input[i] in Input[:i]:
                while Input[i] == oudeComputerInputs[0][i] or Input[i] in niet_aanwezig or Input[i] in Input[:i]:
                    Input[i] = str(random.randrange(1, 10))
        return "".join(Input), computerGeheugen, oudeComputerInputs, niet_aanwezig
    elif len(goed) == 4:
        return Input, computerGeheugen, oudeComputerInputs, niet_aanwezig
    elif (len(goed) < 4 and len(goed) != 0) or len(aanwezig) != 0:
        Input = list(Input)

        if len(niet_aanwezig) <= 5 and len(goed) + len(aanwezig) != 4:
            for i in range(0, 4):
                if computerGeheugen[i] != 'X':
                    continue
                elif computerGeheugen[i] == 'X':
                    for x in range(0, 100):
                        if Input[i] not in niet_aanwezig and Input[i] not in aanwezig and Input[i] not in Input[:i] and Input[i] not in goed:
                            break
                        elif Input[i] in niet_aanwezig or Input[i] in aanwezig or Input[i] in Input[:i] or Input[i] in goed:
                            Input[i] = str(random.randrange(1, 10))

        verwisseld = ['X', 'X', 'X', 'X']
        for i in range(0, len(aanwezig)):
            for x in range(0, 4):
                oude = []
                for y in range(0, len(oudeComputerInputs)):
                    oude.append(oudeComputerInputs[y][x])
                if computerGeheugen[x] != 'X' or aanwezig[i] in oude:
                    continue
                elif computerGeheugen[x] == 'X':
                    if (Input[x] not in aanwezig and aanwezig[i] not in oude) or ((Input[x] in aanwezig and Input[x] != verwisseld[x]) and aanwezig[i] not in oude):
                        verwisseld[x] = aanwezig[i]
                        Input[x] = aanwezig[i]
                        break

        if len(niet_aanwezig) == 5 and len(dubbeleCijfers("".join(Input))) == 1:
            dubbelCijfer = dubbeleCijfers("".join(Input))
            index1 = Input.index(dubbelCijfer)
            index2 = index1 + "".join(Input)[index1+1:].index(dubbelCijfer) + 1

            for i in range(0, 4):
                oude = []
                for y in range(0, len(oudeComputerInputs)):
                    oude.append(oudeComputerInputs[y][i])
                if (i != index1 and i != index2) or Input[index1] not in oude:
                    continue
                elif Input[index1] in oude or Input[index2] in oude:
                    for x in range(0, 10):
                        x = str(x)
                        if (x not in aanwezig and x not in goed) and x not in niet_aanwezig:
                            Input[i] = x
        return "".join(Input), computerGeheugen, oudeComputerInputs, niet_aanwezig
'''
Controleren of de gok goed is. Maakt aanwezig en goed lijst aan omdat dit later in de funtie nodig is. In de for loop
daar onder wordt per cijfer van de input gekeken of ie aanwezig of goed is. Als het goed is wordt het aan die lijst
toegevoegd en in het computergeheugen gezet. Als het aanwezig is wordt het aan die lijst toegevoegd. Ook worden de niet
aanwezige cijfers en oude gokken onthouden. Daarna wordt gekeken of de gok helemaal niet klopt. Als dit het geval is
wordt er een nieuwe gok gemaakt. Er wordt gekeken naar de vorige gok, zodat er geen cijfers die eerder gebruikt zijn
in zitten. Daarna wordt gekeken of de gok helemaal goed is. Als dit het geval is wordt alle informatie gereturnt en
stopt het programma. Als de gok nog niet helemaal goed is, maar wel in de goede richting zit worden er een aantal dingen
gedaan: eerst worden er nieuwe cijfers die nog niet eerder gebruikt zijn toegevoegd. Vervolgens worden de aanwezige
cijfers op andere plekken gezet (er wordt hier naar vorige gokken gekeken). Vervolgens kan het zijn dat de gok dubbele
cijfers bevat, dat wordt in de laatste if statement goedgezet. Daarna wordt alle informatie weer gereturnt.

Gemiddeld raadt dit programma een random combinatie in 5 pogingen. 
'''

def programma():
    spelerNummer = input("Voer een getal in wat de computer zal proberen te raden:\n>> ")

    geheugen = ['X', 'X', 'X', 'X']
    oudeComputerInputs = []
    niet_aanwezig = []

    computerInput = randomCombo()

    for i in range(0, 10):
        if computerInput == spelerNummer:
            print("Computer heeft het nummer na {} keer geraden".format(i + 1))
            break
        computerInput, geheugen, oudeComputerInputs, niet_aanwezig = inputControleren(computerInput, spelerNummer, geheugen, oudeComputerInputs, niet_aanwezig)


programma()
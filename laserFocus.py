import pygame
from pygame.locals import *
import random
import json
pygame.init()

# Install FPS 
clock = pygame.time.Clock()

# Screen Sizing
displayX = 600
displayY = 600
gameDisplay = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Laser Focus")

# Class Open JSON File 
class JSON:
    def __init__(self): 
        with open("laserFocusProgress.json", "r") as file:
            soFar = json.loads(file.read())
            highestScore = soFar["highestScore"]
            totalPoints = soFar["totalPoints"]
            firstColor = soFar["firstColor"]
            secondColor = soFar["secondColor"]
            orangeColor = soFar["orangeColor"]
            yellowColor = soFar["yellowColor"]
            lightGreenColor = soFar["lightGreenColor"]
            greenColor = soFar["greenColor"]
            darkGreenColor = soFar["darkGreenColor"]
            turquoiseColor = soFar["turquoiseColor"]
            blueColor = soFar["blueColor"]
            darkBlueColor = soFar["darkBlueColor"]
            purpleColor = soFar["purpleColor"]
            pinkColor = soFar["pinkColor"]
            lightRedColor = soFar["lightRedColor"]
            file.close()
            self.soFar = soFar
            self.highestScore = highestScore
            self.totalPoints = totalPoints
            self.firstColor = firstColor
            self.secondColor = secondColor
            self.orangeColor = orangeColor
            self.yellowColor = yellowColor
            self.lightGreenColor = lightGreenColor
            self.greenColor = greenColor
            self.darkGreenColor = darkGreenColor
            self.turquoiseColor = turquoiseColor
            self.blueColor = blueColor
            self.darkBlueColor = darkBlueColor
            self.purpleColor = purpleColor
            self.pinkColor = pinkColor
            self.lightRedColor = lightRedColor

# Load Progress
gameProgress = JSON()
jsonData = gameProgress.soFar

# Class Used For Creating Font And Text
class Font:
    def __init__(self, fontType, fontSize, text, color):
        font = pygame.font.Font(fontType, fontSize)
        createText = font.render(text, True, color)
        self.createText = createText
        self.font = fontType

# Class Used For Creating Shapes
class Objects:
        def __init__(self, x, y, width, height, color):
            shape = pygame.draw.rect(gameDisplay, color, Rect(x, y, width, height))
            self.shape = shape
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color

# Mouse Hover Detection Class
class Hover:
    def __init__(self, x, y, width, height, mouseX, mouseY):
        if mouseX > x and mouseX < x + width and mouseY < y + height and mouseY > y:
            isHover = True
        else:
            isHover = False
        self.isHover = isHover

# Purchased Color
class Slash:
    def __init__(self, ownColor, slashX, slashY):
        if ownColor != True and ownColor != None:
            Objects(slashX, slashY, 90, 5, (0, 0, 0))
        self.ownColor = ownColor
        self.slashX = slashX
        self.slashY = slashY

# Build A Color Block
class Block:
    def __init__(self, borderX, borderY, mouseX, mouseY, mouseButton, firstColor, secondColor, runPage, shopY, jsonColor, colorCost, totalPoints, colorName):   
        blackHover = Objects(borderX, borderY - 5, 70, 40, (0, 0, 0))
        slash = Slash(jsonColor, borderX - 10, borderY + 13)
        if slash.ownColor == True or jsonColor == None:
            if Hover(blackHover.x, blackHover.y, blackHover.width, blackHover.height, mouseX, mouseY).isHover == True:    
                if mouseButton == True and shopY == 80:
                    with open("laserFocusProgress.json", "r+") as file:
                        jsonData["firstColor"] = firstColor
                        jsonData["secondColor"] = secondColor
                        dumpScore = json.dumps(jsonData)
                        file.truncate()
                        file.write(dumpScore)
                        file.close()
                    runPage()
        elif slash.ownColor == False:
            if Hover(blackHover.x, blackHover.y, blackHover.width, blackHover.height, mouseX, mouseY).isHover == True:
                if mouseButton == True and shopY == 80 and totalPoints >= colorCost:
                    totalPoints -= colorCost
                    with open("laserFocusProgress.json", "r+") as file:
                        if colorName == None:
                            jsonData["firstColor"] = firstColor
                            jsonData["secondColor"] = secondColor
                        else:   
                            jsonData[colorName] = True
                            jsonData["firstColor"] = firstColor
                            jsonData["secondColor"] = secondColor
                            jsonData["totalPoints"] = totalPoints
                        dumpScore = json.dumps(jsonData)
                        file.truncate()
                        file.write(dumpScore)
                        file.close()
                    runPage()
        basicColor = Objects(borderX + 5, borderY, 30, 30, firstColor)
        fadedColor = Objects(borderX + 35, borderY, 30, 30, secondColor)
        self.basicColorType = basicColor.color
        self.fadedColorType = fadedColor.color
        slash = Slash(jsonColor, slash.slashX, slash.slashY)

# The First Page Displayed When Code Is Running
def mainPage():
    # Refreshes Data Progress
    gameProgress = JSON()
    colorTypes = [gameProgress.firstColor, gameProgress.secondColor]

    # Game Name
    firstText = Font("Blox2.ttf", 50, "Laser", colorTypes[0])
    secondText = Font("blox2.ttf", 50, "Focus", gameProgress.secondColor)
    firstX = -1000
    secondX = 2000
    
    # Progress Text
    totalPoints = Font("HeadlineA.ttf", 20, f"Total Points: {gameProgress.totalPoints}", (0, 0, 0))
    highestScore = Font(totalPoints.font, 20, f"Highest Score: {gameProgress.highestScore}", (0, 0, 0))
    totalPointsY = -400
    highestScoreY = -500
    
    # Footer Text
    bottomText = Font("Blox2.ttf", 40, "Press ENTER To Begin", (255, 255, 255))
    bottomY = 1000
    
    # Laser Background Design Positions
    verticalX = 20
    horizontalY = 20
    verticalY = -2400
    horizontalX = -3600
    
    # Shop Button
    shopButtonTextColor = (0, 0, 0)
    shopButtonText = Font("HeadlineA.ttf", 20, "Change Color ->", shopButtonTextColor)
    shopButtonColor = gameProgress.secondColor
    shopButton = Objects(20, 400, 60, 200, shopButtonColor)
    pressed = False
    activateShop = False
    
    # Shop Design
    shopBackground = Objects(0, -600, 600, 600, (255, 255, 255))
    shopBackgroundY = 600
    shopText = Font("blox2.ttf", 50, "Color Shop", (0, 0, 0))
    headerY = 620
    activeColor = Font("HeadLineA.ttf", 20, "Active Color Set:", (0, 0, 0))
    exitShop = False
    howExit = Font("HeadLineA.ttf", 20, 'Press Enter To Exit Shop', (0, 0, 0))
    activatePurchase = False
    blackHoverColor = (255, 255, 255)
    blackHoverColorOrange = (255, 255, 255)

    # Colors Y Position
    activeColorsY = 630
    borderY1 = 720
    borderY2 = 820
    borderY3 = 920
    borderY4 = 1020

    # Prices
    pricesRow1 = Font("HeadLineA.ttf", 40, "50 Points", (0, 0, 0))
    pricesRow2 = Font("HeadLineA.ttf", 40, "100 Points", (0, 0, 0))
    pricesRow3 = Font("HeadLineA.ttf", 40, "200 Points", (0, 0, 0))
    rowPrices = Font("HeadLineA.ttf", 20, "Row Prices", (0, 0, 0))
    
    while True:
        # Keyboard Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and shopBackgroundY == 600:
                    gameCode()
                if event.key == pygame.K_RETURN and shopBackgroundY < 600:
                    exitShop = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                pressed = False

        # Mouse Position 
        mouse = pygame.mouse.get_pos()
        
        # Background And Lasers
        shopButtonText = Font("HeadlineA.ttf", 20, "Change Color ->", shopButtonTextColor)
        gameDisplay.fill((0, 0, 0))
        verticalPaint = Objects(verticalX, verticalY, 60, 600, gameProgress.secondColor)
        horizontalPaint = Objects(horizontalX, horizontalY, 600, 60, gameProgress.firstColor)
        if verticalY < 0:
            verticalY += 5
        else:
            shopButton = Objects(20, 450, 60, 150, shopButtonColor)
            if mouse[0] > shopButton.x and mouse[0] < shopButton.x + shopButton.width and mouse[1] < shopButton.y + shopButton.height and mouse[1] > shopButton.y:
                shopButtonColor = (0, 0, 0)
                shopButtonTextColor = (255, 255, 255)
                if pressed == True:
                    activateShop = True
            else:
                shopButtonColor = (gameProgress.secondColor)
                shopButtonTextColor = (0, 0, 0)
        if horizontalX < 0:
            horizontalX += 10
        gameDisplay.blit(pygame.transform.rotate(shopButtonText.createText, 270), (-32, verticalY + 470))

        # Displaying Text
        gameDisplay.blit(firstText.createText, (firstX, 200))
        gameDisplay.blit(secondText.createText, (secondX, 200))
        gameDisplay.blit(bottomText.createText, (115, bottomY))
        if firstX < 175:
            firstX += 5
        if secondX > 305:
            secondX -= 5
        elif bottomY > 400:
            bottomY -= 5
        gameDisplay.blit(totalPoints.createText, (20, totalPointsY))
        gameDisplay.blit(highestScore.createText, (20, highestScoreY))
        if totalPointsY < 30:
            totalPointsY += 1
        if highestScoreY < 50:
            highestScoreY += 1

        # Shop Background
        shopBackground = Objects(0, shopBackgroundY, 600, 600, (255, 255, 255))
        gameDisplay.blit(shopText.createText, (175, headerY))
        gameDisplay.blit(activeColor.createText, (20, headerY - 15))
        gameDisplay.blit(howExit.createText, (205, headerY + 55))
        
        # Color Options
        # Starter Colors
        activeColorLeft = Objects(45, activeColorsY, 30, 30, gameProgress.firstColor)
        activeColorRight = Objects(75, activeColorsY, 30, 30, gameProgress.secondColor)
        
        # Collectable Colors
        if activateShop == True:
            if shopBackgroundY > 80:
                shopBackgroundY -= 10
                activeColorsY -= 10
                headerY -= 10
                borderY1 -= 10
                borderY2 -= 10
                borderY3 -= 10
                borderY4 -= 10
            else:
                activateShop = False
        if exitShop == True:
            activateShop = False
            if shopBackgroundY < 600:
                shopBackgroundY += 10
                activeColorsY += 10
                headerY += 10
                borderY1 += 10
                borderY2 += 10
                borderY3 += 10
                borderY4 += 10
            else:
                exitShop = False

        # Layer 1
        rowColors1 = Block(40, borderY1, mouse[0], mouse[1], pressed, "#CC0000", "#FFCCCC", mainPage, shopBackground.y, None, None, gameProgress.totalPoints, None)
        rowColors2 = Block(140, borderY1, mouse[0], mouse[1], pressed, "#CC6600", "#FFE5CC", mainPage, shopBackground.y, gameProgress.orangeColor, 50, gameProgress.totalPoints, "orangeColor")
        rowColors3 = Block(240, borderY1, mouse[0], mouse[1], pressed, "#CCCC00", "#FFFFCC", mainPage, shopBackground.y, gameProgress.yellowColor, 50, gameProgress.totalPoints, "yellowColor")
        rowColors4 = Block(340, borderY1, mouse[0], mouse[1], pressed, "#66CC00", "#E5FFCC", mainPage, shopBackground.y, gameProgress.lightGreenColor, 50, gameProgress.totalPoints, "lightGreenColor")
        # Layer 2
        rowColors5 = Block(40, borderY2, mouse[0], mouse[1], pressed, "#00CC00", "#CCFFCC", mainPage, shopBackground.y, gameProgress.greenColor, 100, gameProgress.totalPoints, "greenColor")
        rowColors6 = Block(140, borderY2, mouse[0], mouse[1], pressed, "#00CC66", "#CCFFE5", mainPage, shopBackground.y, gameProgress.darkGreenColor, 100, gameProgress.totalPoints, "darkGreenColor")
        rowColors7 = Block(240, borderY2, mouse[0], mouse[1], pressed, "#00CCCC", "#CCFFFF", mainPage, shopBackground.y, gameProgress.turquoiseColor, 100, gameProgress.totalPoints, "turquoiseColor")
        rowColors8 = Block(340, borderY2, mouse[0], mouse[1], pressed, "#0066CC", "#CCE5FF", mainPage, shopBackground.y, gameProgress.blueColor, 100, gameProgress.totalPoints, "blueColor")
        # Layer 3
        rowColors9 = Block(40, borderY3, mouse[0], mouse[1], pressed, "#0000CC", "#CCCCFF", mainPage, shopBackground.y, gameProgress.darkBlueColor, 200, gameProgress.totalPoints, "darkBlueColor")
        rowColors10 = Block(140, borderY3, mouse[0], mouse[1], pressed, "#6600CC", "#E5CCFF", mainPage, shopBackground.y, gameProgress.purpleColor, 200, gameProgress.totalPoints, "purpleColor")
        rowColors11 = Block(240, borderY3, mouse[0], mouse[1], pressed, "#CC00CC", "#FFCCFF", mainPage, shopBackground.y, gameProgress.pinkColor, 200, gameProgress.totalPoints, "pinkColor")
        rowColors12 = Block(340, borderY3, mouse[0], mouse[1], pressed, "#CC0066", "#FFCCE5", mainPage, shopBackground.y, gameProgress.lightRedColor, 200, gameProgress.totalPoints, "lightRedColor")

        # Prices
        gameDisplay.blit(rowPrices.createText, (460, headerY + 55))
        gameDisplay.blit(pricesRow1.createText, (435, headerY + 95))
        gameDisplay.blit(pricesRow2.createText, (435, headerY + 195))
        gameDisplay.blit(pricesRow3.createText, (435, headerY + 295))

        # Updates Display
        pygame.display.update()

# The Page That Displays The Running Of The Game
def gameCode(): 
    # Progress
    newHighScore = 0
    gameProgress = JSON()
    colorTypes = [gameProgress.firstColor, gameProgress.secondColor]

    # Top Barrier Color
    topColor = colorTypes[1]
    disableSwap = False

    # Figure
    character = Objects(290, 570, 20, 20, colorTypes[1])
    moveRight = False
    moveLeft = False
    disableRight = False
    disableLeft = False
    allowJump = False
    disableJump = False
    limitTime = 0
    jumpComplete = True
    wallJump = False
    color = colorTypes[0]

    # Lasers
    horizontalRandomY = random.randrange(10, 591)
    horizontalLaserStarter = Objects(0, horizontalRandomY, 600, 10, colorTypes[0])
    horizontalLaser = Objects(0, horizontalRandomY - 40, 600, 60, colorTypes[0])
    laserWait = 0
    startGame = False
    laserActive = False
    verticalRandomX = random.randrange(10, 591)
    verticalLaserStarter = Objects(verticalRandomX, 0, 10, 600, colorTypes[1])
    verticalLaser = Objects(verticalRandomX - 40, 0, 60, 600, colorTypes[1])

    # Squares For Collecting
    pointRandomYLeft = random.randrange(15, 585)
    leftPoint = Objects(15, pointRandomYLeft, 10, 10, colorTypes[0])
    pointRandomYRight = random.randrange(15, 585)
    rightPoint = Objects(15, pointRandomYRight, 10, 10, colorTypes[0])
    randomColorLeft = random.randrange(0, 2)
    randomColorRight = random.randrange(0, 2)
    rightPointCollected = False
    leftPointCollected = False

    # End Of Game
    gameOver = False
    pressed = False
    quitGameText = Font("Blox2.ttf", 50, "Quit", (255, 255, 255))
    playAgainText = Font("blox2.ttf", 30, "Play Again?", (255, 255, 255))
    allowText = False
    backgroundLeftUpperX = -600
    backgroundRightLowerX = 600

    while True:
        # Background Color
        gameDisplay.fill((255, 255, 255))

        # Mouse Controls
        mouse = pygame.mouse.get_pos()

        # Barriers
        topBarrier = Objects(0, 0, 600, 10, topColor)
        leftBarrier = Objects(0, 0, 10, 600, (0, 0, 0))
        rightBarrier = Objects(590, 0, 10, 600, (0, 0, 0))
        bottomBarrier = Objects(0, 590, 600, 10, (0, 0, 0))

        # Figure
        character = Objects(character.x, character.y, 20, 20, color)

        # Progress
        newTotalPoints = Font("HeadlineA.ttf", 20, f"Total Points: {gameProgress.totalPoints}", (0, 0, 0))
        newScore = Font(newTotalPoints.font, 20, f"Score: {newHighScore}", (0, 0, 0))

        # Key Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("laserFocusProgress.json", "r+") as file:
                    if newHighScore > gameProgress.highestScore:
                        gameProgress.highestScore = newHighScore
                        jsonData["highestScore"] = newHighScore
                    jsonData["totalPoints"] = gameProgress.totalPoints
                    dumpScore = json.dumps(jsonData)
                    file.truncate()
                    file.write(dumpScore)
                    file.close()
                pygame.quit()
                quit()  
            if event.type == pygame.KEYDOWN:
                startGame = True
                if event.key == pygame.K_RIGHT:
                    moveRight = True
                if event.key == pygame.K_LEFT:
                    moveLeft = True
                if event.key == pygame.K_UP and jumpComplete == True or event.key == pygame.K_UP and wallJump == True:
                    allowJump = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moveRight = False
                if event.key == pygame.K_LEFT:
                    moveLeft = False
                if event.key == pygame.K_UP:
                    allowJump = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                pressed = False

        # Run Controls
        if moveRight == True and disableRight == False:
            character.x += 4
        if moveLeft == True and disableLeft == False:
            character.x -= 4
        if character.x + character.width >= rightBarrier.x:
            disableRight = True
        else:
            disableRight = False
        if character.x <= leftBarrier.x + leftBarrier.width:
            disableLeft = True
        else:
            disableLeft = False

        # Jump Controls
        if allowJump == True and disableJump == False:
            jumpComplete = False
            limitTime += 1
            if limitTime <= 25:
                character.y -= 6
            else:
                allowJump = False
        elif jumpComplete == False:
                if character.y + character.height <= bottomBarrier.y:
                    if character.x + character.width >= rightBarrier.x and moveRight == True or character.x <= leftBarrier.x + leftBarrier.width and moveLeft == True:  
                        character.y += 2
                        limitTime = 0
                        wallJump = True
                    else:   
                        character.y += 6
                        wallJump = False
                else:   
                    jumpComplete = True
                    limitTime = 0    
        if character.y + character.height > bottomBarrier.y:
            character.y -= 1
        if character.y <= topBarrier.y + topBarrier.height and disableSwap == False:
            disableJump = True
            if topBarrier.color == colorTypes[0]:
                topColor = colorTypes[1]
                color = colorTypes[0]
            else:
                topColor = colorTypes[0]
                color = colorTypes[1]
            disableSwap = True
        
        # Delays Color Changing
        if character.y >= 200:
            disableJump = False
            disableSwap = False

        # Begins The Laser System 
        if startGame == True and gameOver == False:   
            laserWait += 1
        if laserWait < 100 and startGame == True:   
            if character.color == colorTypes[0]:    
                verticalLaserStarter = Objects(verticalRandomX, 0, 1, 600, colorTypes[1])
                horizontalLaserStarter = Objects(0, horizontalRandomY, 600, 1, colorTypes[0])
            else:
                horizontalLaserStarter = Objects(0, horizontalRandomY, 600, 1, colorTypes[0])
                verticalLaserStarter = Objects(verticalRandomX, 0, 1, 600, colorTypes[1])
        elif laserWait < 120 and startGame == True:
            laserActive = True
            if character.color == colorTypes[0]:
                verticalLaser = Objects(verticalRandomX - 30, 0, 60, 600, colorTypes[1])
                horizontalLaser = Objects(0, horizontalRandomY - 30, 600, 60, colorTypes[0])
            else:
                horizontalLaser = Objects(0, horizontalRandomY - 30, 600, 60, colorTypes[0])
                verticalLaser = Objects(verticalRandomX - 30, 0, 60, 600, colorTypes[1])
        else:   
            if startGame == True:    
                newHighScore += 1
            laserWait = 0
            laserActive = False
            horizontalRandomY = random.randrange(10, 591)
            verticalRandomX = random.randrange(10, 591)

        # Laser To Character Collision System
        if Rect.colliderect(character.shape, horizontalLaser.shape) and laserActive == True and character.color == horizontalLaser.color or Rect.colliderect(character.shape, verticalLaser.shape) and laserActive == True and character.color == verticalLaser.color:
            gameOver = True
             
        # Little Squares Collision And Collecting System
        if leftPointCollected == False:   
            leftPoint = Objects(15, pointRandomYLeft, 10, 10, colorTypes[randomColorLeft])
        if rightPointCollected == False:    
            rightPoint = Objects(575, pointRandomYRight, 10, 10, colorTypes[randomColorRight])
        if Rect.colliderect(character.shape, leftPoint.shape) and character.color == leftPoint.color:
            leftPointCollected = True
        if Rect.colliderect(character.shape, rightPoint.shape) and character.color == rightPoint.color:
            rightPointCollected = True
        if rightPointCollected == True and leftPointCollected == True:
            gameProgress.totalPoints += 1
            pointRandomYLeft = random.randrange(15, 585)
            pointRandomYRight = random.randrange(15, 585)
            randomColorLeft = random.randrange(0, 2)
            randomColorRight = random.randrange(0, 2)
            rightPointCollected = False
            leftPointCollected = False

        # End Of Game
        if gameOver == True: 
            disableRight = True
            disableLeft = True
            disableJump = True 
            wallJump = False 
            with open("laserFocusProgress.json", "r+") as file:
                    if newHighScore > gameProgress.highestScore:
                        gameProgress.highestScore = newHighScore
                        jsonData["highestScore"] = newHighScore
                    jsonData["totalPoints"] = gameProgress.totalPoints
                    dumpScore = json.dumps(jsonData)
                    file.truncate()
                    file.write(dumpScore)
                    file.close()
            backgroundLeftUpper = Objects(backgroundLeftUpperX, 0, 600, 300, (0, 0, 0))
            backgroundRightLower = Objects(backgroundRightLowerX, 300, 600, 300, (0, 0, 0))
            if backgroundLeftUpperX < 0 and backgroundRightLowerX > 0:
                backgroundLeftUpperX += 10
                backgroundRightLowerX -= 10
            else:
                mainPage()
        
        gameDisplay.blit(newTotalPoints.createText, (20, 20))
        gameDisplay.blit(newScore.createText, (20, 40))
        
        # Total FPS
        clock.tick(80)

        # Updates The Game Screen
        pygame.display.update()

mainPage()
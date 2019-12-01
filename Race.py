import random, time, os

class Race:

    def __init__(self, length):
        self.trackLength = length
        self.raceRunning = True
        self.cars = {
            'bodies': [],
            'names': [],
        }

    def killGame(self):
        self.raceRunning = False

    def addCar(self, name):
        self.cars['bodies'].append('⛟')
        self.cars['names'].append(name)

    def start(self):
        winMsg = ''
        while self.raceRunning == True:
            selectedCar = self.cars['names'].index(random.choice(self.cars['names']))
            self.cars['bodies'][selectedCar] = ('=' * random.randint(1, 3)) + self.cars['bodies'][selectedCar]
            os.system('clear')

            for car in self.cars['names']:
                carInd = self.cars['names'].index(car)
                nameWhiteSpace = 15 - len(self.cars['names'][carInd])
                finishLineDist = (self.trackLength - len(self.cars['bodies'][carInd]) ) - 1
                finishLine = (' ' * finishLineDist) + '|'
                print(self.cars['names'][carInd] + (' ' * nameWhiteSpace) + self.cars['bodies'][carInd] + finishLine + '\n')

                if len(self.cars['bodies'][carInd]) >= self.trackLength:
                    winMsg = str(self.cars['names'][carInd]) + ' Won'
                    self.killGame()

            print(winMsg)
            time.sleep(0.1)




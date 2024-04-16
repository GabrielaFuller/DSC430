from time import time_ns
from statistics import mean

class WarAndPeacePseudoRandomNumberGenerator():
    # Define the file path
    filepath = "war-and-peace.txt"

    def __init__(self, seedValue=None):
        self.seedValue = seedValue
        self.file = self.openFile()  # Open the text file

    def getRandomValue(self):
        if self.seedValue is None:
            # Generate a seed value based on time (last 5 digits of nanoseconds)
            x = time_ns()
            sax = str(x)
            x = int(sax[-5:])  # Extract last 5 digits
            return self.doSomeLCGMath(x)
        return self.doSomeLCGMath(self.seedValue)

    def doSomeLCGMath(self, seed):
        # Linear Congruential Generator math
        a = 1
        c = 3123
        m = 999999
        return (a * seed + c) % m

    def random(self):
        value = self.getRandomValue()
        binaryString = ""

        while len(binaryString) < 16:
            a = self.getCharacter(value)
            i = value + self.getRandomValue()
            b = self.getCharacter(i)
            bit = self.judge(a, b)
            
            if bit is None:
                value = value + self.getRandomValue()
                continue
            value = value + self.getRandomValue()
            binaryString += bit

        return self.calculateNumber(binaryString)

    def calculateNumber(self, bitString):
        # Convert a bit string to a number in [0, 1)
        sum = 0.0
        divisor = 2
        for i in range(len(bitString)):
            sum += int(bitString[i]) * (1 / divisor)
            divisor = divisor * 2
        return sum

    def judge(self, a, b):
        # Determine if the character comparison results in a 0 or 1
        if a > b:
            return "1"
        if a < b:
            return "0"
        else:
            return None

    def getCharacter(self, value):
        # Extract a character from the text file
        a = " "
        b = None

        while a.isspace():  # Avoid returning whitespace
            self.file.seek(value)
            a = self.file.read(1)
            value += 1
            try:
                b = a.decode("ascii")  # Handle non-ASCII characters differently
            except UnicodeError:
                a = " "

        return b

    def openFile(self):
        # Open the text file
        return open(self.filepath, "rb")

    def closeFile(self):
        # Close the text file
        self.file.close()

def main():
    prng = WarAndPeacePseudoRandomNumberGenerator()
    list1 = []

    prng2 = WarAndPeacePseudoRandomNumberGenerator(12345)
    a = prng2.random()
    b = prng2.random()
    prng2.closeFile()  # Close the file explicitly here

    for i in range(10000):
        r = prng.random()
        list1.append(r)

    prng.closeFile()  # Close the file explicitly
    median = mean(list1)
    minimum = min(list1)
    maximum = max(list1)

    print("Median: {} ".format(median))
    print("Minimum: {} ".format(minimum))
    print("Maximum: {} ".format(maximum))
    print("With seed 12345: {} {}".format(a, b))

if __name__ == '__main__':
    main()

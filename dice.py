import hashlib
import csv
import os

class SeedPairAndNonce:
    def __init__(self, serverSeed: str, clientSeed: str, nonce: int):
        self.serverSeed = serverSeed
        self.clientSeed = clientSeed
        self.nonce = nonce

def generateBytes(seed: SeedPairAndNonce, cursor: int) -> bytes:
    data = f"{seed.serverSeed}:{seed.clientSeed}:{seed.nonce}:{cursor}"
    return hashlib.sha256(data.encode()).digest()

def generateFloat(seed: SeedPairAndNonce) -> float:
    buffer = generateBytes(seed, 0)
    floatValue = 0
    for i in range(4):
        floatValue += buffer[i] / (256 ** (i + 1))
    return floatValue

def generateDiceroll(seed: SeedPairAndNonce) -> float:
    randomFloat = generateFloat(seed)
    return round(randomFloat * 10000) / 100

def generateDiceCSV(serverSeed: str, clientSeed: str, nonceCount: int, outputFile: str):
    try:
        with open(outputFile, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['nonce', 'roll','', 'Sampled Unhashed Server Seed: '+ serverSeed, 'Sampled Client Seed: ' + clientSeed])
            for nonce in range(nonceCount):
                seed = SeedPairAndNonce(serverSeed, clientSeed, nonce)
                roll = generateDiceroll(seed)
                writer.writerow([nonce, roll])
    except PermissionError:
        print("Cannot overwrite the output file, as it is in use. Writing to a new file.")
        base_filename, ext = os.path.splitext(outputFile)
        new_filename = f"{base_filename}_new{ext}"
        with open(new_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['nonce', 'roll','', 'Sampled Unhashed Server Seed: '+ serverSeed, 'Sampled Client Seed: ' + clientSeed])
            for nonce in range(nonceCount):
                seed = SeedPairAndNonce(serverSeed, clientSeed, nonce)
                roll = generateDiceroll(seed)
                writer.writerow([nonce, roll])
        print(f"Results written to {new_filename}")

serverSeed = input("Input unhashed server seed: ")
clientSeed = input("Input client seed: ")
nonceCount = int(input("Enter last nonce to count...: "))
outputFile = "goateddicerolls.csv"

generateDiceCSV(serverSeed, clientSeed, nonceCount, outputFile)

print(f"Generated {nonceCount} dice rolls to {outputFile}, meow.")
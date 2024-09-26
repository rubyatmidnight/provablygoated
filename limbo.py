import hashlib
import math
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

def limboMultiplier(seed: SeedPairAndNonce, houseEdge: float) -> float:
    floatValue = 1 - generateFloat(seed)
    float_with_house_edge = (1e8) / (floatValue * 1e8) * (1 - houseEdge/100)
    return max(1, math.floor(float_with_house_edge * 100) / 100.0)

def generateLimbocsv(serverSeed: str, clientSeed: str, nonceCount: int, houseEdge: float, outputFile: str):
    try:
        with open(outputFile, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['nonce', 'multiplier','', 'Sampled Unhashed Server Seed: '+ serverSeed, 'Sampled Client Seed: ' + clientSeed])
            for nonce in range(nonceCount):
                seed = SeedPairAndNonce(serverSeed, clientSeed, nonce)
                multiplier = limboMultiplier(seed, houseEdge)
                writer.writerow([nonce, multiplier])
    except PermissionError:
        print("Cannot overwrite the output file, as it is in use. Writing to a new file.")
        base_filename, ext = os.path.splitext(outputFile)
        new_filename = f"{base_filename}_new{ext}"
        with open(new_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['nonce', 'multiplier','', 'Sampled Unhashed Server Seed: '+ serverSeed, 'Sampled Client Seed: ' + clientSeed])
            for nonce in range(nonceCount):
                seed = SeedPairAndNonce(serverSeed, clientSeed, nonce)
                multiplier = limboMultiplier(seed, houseEdge)
                writer.writerow([nonce, multiplier])
        print(f"Results written to {new_filename}")


serverSeed = input("Input unhashed server seed: ")
clientSeed = input("Input client seed: ")
nonceCount = int(input("Enter last nonce to count...: "))
houseEdge = 2
outputFile = "goatedlimborolls.csv"

generateLimbocsv(serverSeed, clientSeed, nonceCount, houseEdge, outputFile)

print(f"Generated {nonceCount} Limbo rolls to {outputFile}, meow.")
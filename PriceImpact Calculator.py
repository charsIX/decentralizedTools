tvl = int(input("Total $ TVL: "))
tokenXValue = int(input("Token X value: "))
tokenYValue = int(input("Token Y value: "))
tokenXWeight = int(input("Token X weight: "))/100
tokenYWeight = 1-tokenXWeight
resX = tvl*tokenXWeight/tokenXValue
resY = tvl*tokenYWeight/tokenYValue
k = resX*resY #token X reserve * token Y reserve = k, the pool golden rule
print("....")

print(f"Token X value: {tokenXValue}")
print(f"Token Y value: {tokenYValue}")
print(f"Token X weight: {tokenXWeight}")
print(f"Token Y weight: {tokenYWeight}")
print(f"{resX} token X")
print(f"{resY} token Y")
print(f"K: {k}")
print("...")

deltaXIn = int(input("Token X swap amount (in tokenX): "))*tokenXValue
receivedTokenYNoPriceImpact = deltaXIn/tokenYValue
newResX = resX + deltaXIn
newResY = k/newResX
receivedTokenY = resY-newResY
priceImpact = 100-((receivedTokenY/receivedTokenYNoPriceImpact)*100)
liqProvFee = deltaXIn*0.003
print(f"newResX after depositing token X {newResX}")
print(f"newResY after depositing token Y {newResY}")
print(f"Expected token Y without Price Impact: {receivedTokenYNoPriceImpact}")
print(f"Received token Y: {receivedTokenY}")
print(f"Price Impact: {priceImpact}%")
print(f"Liquidity provider fee {liqProvFee}")
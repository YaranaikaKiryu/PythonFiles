import math

D = input("Enter the raw data: ")
D = [int(x) for x in D.split(",")]

NC = int(input("Enter the number of classes: "))
MIV = min(D)
MAV = max(D)

DR = MAV - MIV
CW = math.ceil(DR / NC)
LCL = [MIV + i * CW for i in range(NC)]

UCL = []
for i in range(NC):
    if i < NC - 1:
        UCL.append(min(LCL[i] + CW - 1, MAV - 1))
    else:
        UCL.append(MAV + 1)

midpoint = [(LCL[i] + UCL[i]) / 2 for i in range(NC)]

frequency = [0] * NC
for DP in D:
    for i in range(NC):
        if LCL[i] <= DP <= UCL[i]:
            frequency[i] += 1
            break

cumulativefrequency = [sum(frequency[:i+1]) for i in range(NC)]

n = len(D)
relativefrequency = [f / n for f in frequency]
sumrelativefrequency = sum(relativefrequency)

classboundaries = []
for i in range(NC):
    if i == 0:
        lowerboundary = LCL[i] - 0.5
    else:
        lowerboundary = UCL[i-1] + 0.5
    if i < NC - 1:
        upperboundary = UCL[i] + 0.5
    else:
        upperboundary = UCL[i] + 0.5
    classboundaries.append((lowerboundary, upperboundary))
    

frequencytimesmidpoint = [frequency[i] * midpoint[i] for i in range(NC)]
sumfrequencytimesmidpoint = sum(frequencytimesmidpoint)

print("Class        Frequency    Cumulative Frequency   Relative Frequency           Midpoint           Class Boundaries      Frequency * Midpoint")
print("-" * 140)
for i in range(NC):
    print(f"{LCL[i]} - {UCL[i]:<10}  {frequency[i]:<13} {cumulativefrequency[i]:<20} {relativefrequency[i]:.3f}                    {midpoint[i]:<10.1f}        {classboundaries[i][0]:<3} - {classboundaries[i][1]:<5}               {frequencytimesmidpoint[i]}")
print("-" * 140)
print(f"{'':<13} ∑f = {sum(frequency)}                        ∑f/n = {sumrelativefrequency:.1f}                                                             ∑f*x = {sumfrequencytimesmidpoint}")
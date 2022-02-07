# Create a Tmp Calculator for PV and FV


#


def CalculatorFV(N, Rate, PMT, PV):
    FV = 0.0
    TotalRate = 0.0
    TotalRate = 1 + Rate / 100
    
    # Calculator Present Value first
    FV = TotalRate ** N * PV

    # Calculator PMT based on pay-times(N)
    for n in range(0, N):
        FV = FV + PMT * (TotalRate ** n)
    return FV

def CalculatorPV(N, Rate, PMT, FV):
    PV = 0.0
    TotalRate = 0.0
    TotalRate = 1 + Rate / 100

    # Calculate Future Value first
    PV = FV / TotalRate ** N
    # Calculat PMT based on N
    for n2 in range(1, N + 1): ## KEY: the stop point is not N, but N + 1
        PV = PV + PMT / (TotalRate ** n2)
    return PV

### Verifier: TEST GOOD
#print(CalculatorFV(15, 7.0, -150.0, 0.0))
#print(CalculatorPV(2, 9.0, 0.0, -323.97))
#print(CalculatorPV(4, 9.0, 100.0, 0.0))
#print(CalculatorPV(int(4), float(9), float(100), float(0)))

while True:
    print("--------------------------------------------------------------------------------")
    print("================================================================================")
            
       
    print("Options: ")
    print("     Calculate PV: 1")
    print("     Calculate FV: 2")

    Option = input()

    if Option == 1:
        print("Inputs: ")
        print("N:")
        N = input()
        print("Rate:")
        Rate = input()
        print("PMT:")
        PMT = input()
        print("FV:")
        FV = input()

        # verify input in case of crash
        print("Present Value is", CalculatorPV(int(N), float(Rate), float(PMT), float(FV)))
    else:
        print("Inputs: ")
        print("N:")
        N = input()
        print("Rate:")
        Rate = input()
        print("PMT:")
        PMT = input()
        print("PV:")
        PV = input()
        print("Future Value is", CalculatorFV(int(N), float(Rate), float(PMT), float(PV)))
    

        
import numpy as np
import math 
import matplotlib.pyplot as plt

# Setup constants
lte_C = 0
lte_T = 0
b1 = 0
ln1 = 0.0
lm1 = 0.0
BLOCK_NEW_CALLS1 = []
BLOCK_HANDOFF_CALLS1 = []

fiveG_C = 0
fiveG_T = 0
b2 = 0
ln2 = 0.0
lm2 = 0.0
BLOCK_NEW_CALLS2 = []
BLOCK_HANDOFF_CALLS2 = []

def reset():
    # set constant values
    global lte_C, lte_T, b1, ln1, lm1, fiveG_C, fiveG_T, b2, ln2, lm2
    global BLOCK_NEW_CALLS1, BLOCK_HANDOFF_CALLS1, BLOCK_NEW_CALLS2, BLOCK_HANDOFF_CALLS2

    lte_C = 25
    lte_T = 10
    b1 = 1
    ln1 = 10
    lm1 = 10
    BLOCK_NEW_CALLS1 = []
    BLOCK_HANDOFF_CALLS1 = []

    fiveG_C = 20
    fiveG_T = 10
    b2 = 1
    ln2 = 10
    lm2 = 10
    BLOCK_NEW_CALLS2 = []
    BLOCK_HANDOFF_CALLS2 = []
    

def main():
    ST = 0
    SB = 0
    SD = 0
    # LTE NETWORK
    P = np.zeros([lte_T+1, lte_C+1])
    for m1 in range(0,lte_T+1):
        for n1 in range (0,lte_C+1):
            if ((b1*(m1+n1)<=lte_C) & (b1*m1<=lte_T)):
                P[m1][n1] = ((math.pow(lm1,m1))*(math.pow(ln1,n1)))/(math.factorial(m1)*math.factorial(n1))
                ST = ST + P[m1][n1]
                # Probability of blocking states
                if (b1 + (b1*(m1+n1)) > lte_C) | ((b1 + (b1*m1)) > lte_T):
                    SB = SB + P[m1][n1]
                # Probability of dropping states 
                if (b1 + (b1*(m1+n1))) > lte_C:
                    SD = SD + P[m1][n1] 
    BLOCK_NEW_CALLS1.append(SB*100/ST)
    BLOCK_HANDOFF_CALLS1.append(SD*100/ST)

    # DEBUG
    # print("SB: "+repr(SB))
    # print("SD: "+repr(SD))
    # print("ST: "+repr(ST))
    # print("Block new call probability : "+repr(BLOCK_NEW_CALLS1)+ " %")
    # print("Drop handoff call probability: "+repr(BLOCK_HANDOFF_CALLS1)+ " %")
    # print(P)

    ST = 0
    SB = 0
    SD = 0
    # 5G NETWORK
    P = np.zeros([fiveG_T+1, fiveG_C+1])
    for m2 in range(0,fiveG_T+1):
        for n2 in range (0,fiveG_C+1):
            if ((b2*(m2+n2)<=fiveG_C) & (b2*m2<=fiveG_T)):
                P[m2][n2] = ((math.pow(lm2,m2))*(math.pow(ln2,n2)))/(math.factorial(m2)*math.factorial(n2))
                ST = ST + P[m2][n2]
                # Probability of blocking states
                if (b2 + (b2*(m2+n2)) > fiveG_C) | ((b2 + (b2*m2)) > fiveG_T):
                    SB = SB + P[m2][n2]
                # Probability of dropping states 
                if (b2 + (b2*(m2+n2))) > fiveG_C:
                    SD = SD + P[m2][n2] 
    BLOCK_NEW_CALLS2.append(SB*100/ST)
    BLOCK_HANDOFF_CALLS2.append(SD*100/ST)
    
    # DEBUG
    # print("SB: "+repr(SB))
    # print("SD: "+repr(SD))
    # print("ST: "+repr(ST))
    # print("Block new call probability : "+repr(BLOCK_NEW_CALLS2)+ " %")
    # print("Drop handoff call probability: "+repr(BLOCK_HANDOFF_CALLS2)+ " %")
    # print(P)
    # print("__________________________________________________")



if __name__ == "__main__":
    # Enable 'qx = True' to print out graphs for that question
    q6 = True
    q7 = True
    q8 = True
    q9 = True
    q10 = True
    # Question 6 
    if q6:
        reset()
        ln1=0
        lm1=0
        ln2=0
        lm2=0
        LN = []
        for i in range(0,1000):
            main()
            LN.append(ln1)
            ln1= ln1+0.1
            lm1= lm1+0.1
            ln2= ln2+0.1
            lm2= lm2+0.1

        plt.figure()
        plt.plot(LN,BLOCK_NEW_CALLS1,label='New Calls')
        plt.plot(LN,BLOCK_HANDOFF_CALLS1,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Call Arrival Ratio (Arrivals/Departures)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Call Arrival Rate on \nBlocking Probability for LTE network")
        plt.show()
        plt.savefig("images/6_LTE.png")

        plt.figure()
        plt.plot(LN,BLOCK_NEW_CALLS2,label='New Calls')
        plt.plot(LN,BLOCK_HANDOFF_CALLS2,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Call Arrival Ratio (Arrivals/Departures)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Call Arrival Rate on \nBlocking Probability for 5G network")
        plt.show()
        plt.savefig("images/6_fiveG.png")

    # Question 7
    if q7:
        reset()
        lte_C = 0
        lte_T = 0
        fiveG_C = 0
        fiveG_T = 0
        C = []
        for i in range(0,40):
            main()
            C.append(lte_C)
            lte_C+=1
            lte_T = round(lte_C*0.6)
            fiveG_C+=1
            fiveG_T = round(fiveG_C*0.6)

        plt.figure()
        plt.plot(C,BLOCK_NEW_CALLS1,label='New Calls')
        plt.plot(C,BLOCK_HANDOFF_CALLS1,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Network Capacity')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Network Capacity on \nBlocking Probability for LTE network")
        plt.show()
        plt.savefig("images/7_LTE.png")

        plt.figure()
        plt.plot(C,BLOCK_NEW_CALLS2,label='New Calls')
        plt.plot(C,BLOCK_HANDOFF_CALLS2,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Network Capacity')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Network Capacity on \nBlocking Probability for 5G network")
        plt.show()
        plt.savefig("images/7_fiveG.png")

    # Question 8
    if q8:
        reset()
        lte_T = 0
        fiveG_T = 0
        T1 = []
        T2 = []
        t1 = 0
        t2 = 0
        for i in range(0,21):
            main()
            T1.append(100*lte_T/lte_C)
            T2.append(100*fiveG_T/fiveG_C)
            t1 = t1+0.05*lte_C
            lte_T = round(t1)
            t2 = t2+0.05*fiveG_C
            fiveG_T = round(t2)

        plt.figure()
        plt.plot(T1,BLOCK_NEW_CALLS1,label='New Calls')
        plt.plot(T1,BLOCK_HANDOFF_CALLS1,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Threshold (% of Maximum)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Threshold on \nBlocking Probability for LTE network")
        plt.show()
        plt.savefig("images/8_LTE.png")

        plt.figure()
        plt.plot(T2,BLOCK_NEW_CALLS2,label='New Calls')
        plt.plot(T2,BLOCK_HANDOFF_CALLS2,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Threshold (% of Maximum)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Threshold on \nBlocking Probability for 5G network")
        plt.show()
        plt.savefig("images/8_fiveG.png")

    # Question 9
    if q9:
        reset()
        b1 = 0
        b2 = 0
        B = []
        for i in range(0,1000):
            main()
            B.append(b1)
            b1= b1+0.01
            b2= b2+0.01

        plt.figure()
        plt.plot(B,BLOCK_NEW_CALLS1,label='New Calls')
        plt.plot(B,BLOCK_HANDOFF_CALLS1,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Bandwidth per Call (bbu)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Call Bandwidth on \nBlocking Probability for LTE network")
        plt.show()
        plt.savefig("images/9_LTE.png")

        plt.figure()
        plt.plot(B,BLOCK_NEW_CALLS2,label='New Calls')
        plt.plot(B,BLOCK_HANDOFF_CALLS2,label='Handoff Calls')
        plt.legend()
        plt.xlabel('Bandwidth per Call (bbu)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Call Bandwidth on \nBlocking Probability for 5G network")
        plt.show()
        plt.savefig("images/9_fiveG.png")

# Question 10
    if q10:
        reset()
        ln1=100
        lm1=100
        ln2=100
        lm2=100
        LN = []
        for i in range(0,1000):
            main()
            LN.append(ln1)
            ln1= ln1-0.1
            lm1= lm1-0.1
            ln2= ln2-0.1
            lm2= lm2-0.1

        plt.figure()
        plt.plot(LN,BLOCK_NEW_CALLS1,label='New Calls')
        plt.plot(LN,BLOCK_HANDOFF_CALLS1,label='Handoff Calls')
        plt.legend()
        plt.gca().invert_xaxis()
        plt.xlabel('Call Arrival Ratio (Arrivals/Departures)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Call Departure Rate on \nBlocking Probability for LTE network")
        plt.show()
        plt.savefig("images/10_LTE.png")

        plt.figure()
        plt.plot(LN,BLOCK_NEW_CALLS2,label='New Calls')
        plt.plot(LN,BLOCK_HANDOFF_CALLS2,label='Handoff Calls')
        plt.legend()
        plt.gca().invert_xaxis()
        plt.xlabel('Call Arrival Ratio (Arrivals/Departures)')
        plt.ylabel('Blocking Probabilty (%)')
        plt.title("Effect of Increasing Call Departure Rate on \nBlocking Probability for 5G network")
        plt.show()
        plt.savefig("images/10_fiveG.png")
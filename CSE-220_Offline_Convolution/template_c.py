import numpy as np
import matplotlib.pyplot as plt

# Todo: Define DiscreteSignal class
from signal_lti import DiscreteSignal,LTISystem
        
class SuperDiscreteSignal:
    def __init__(self):
        self.components = []

    def add(self, DiscreteSignal: DiscreteSignal, coefficient=1.0):
        self.components.append((coefficient, DiscreteSignal))
        
# Todo: Define LTI class

if __name__ == "__main__":
    INF = 10

    # Component DiscreteSignals
    x1 = DiscreteSignal(-INF,INF)
    x1.set_value_at_time(0, 1)

    x2 = DiscreteSignal(-INF,INF)
    x2.set_value_at_time(2, 1)

    # Todo: Create SuperDiscreteSignal: x(n) = 2*x1(n) - x2(n)
    supersignal=SuperDiscreteSignal()
    supersignal.add(x1,2.0)
    supersignal.add(x2)
    # Impulse response
    h = DiscreteSignal(-INF,INF)
    h.set_value_at_time(0, 1)
    h.set_value_at_time(1, 0.5)

    system = LTISystem(h)
    y_final=DiscreteSignal(-INF,INF)
    for coeff,component in supersignal.components:
        y_final=y_final.add(system.output(component.multiply(coeff)))
    print("Time")
    for i in range(len(y_final)):
        print(y_final.n[i],end=" ")
    print("Y Value")
    for i in range(len(y_final)):
        print(y_final.values[i],end=" ")

    fig,axes=plt.subplots(2,1)
    axes[0].stem(h.n,h.values)
    axes[0].set_title("Impulse graph")
    axes[0].set_xlabel("n")
    axes[0].set_ylabel("h")
    axes[1].stem(y_final.n,y_final.values)
    plt.show()
    # Todo: Output using superposition

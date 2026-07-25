import numpy as np
import matplotlib.pyplot as plt

# Todo: Define DiscreteSignal class

# Todo: Define LTI class

from signal_lti import DiscreteSignal,LTISystem

if __name__ == "__main__":
    INF = 10

    x = DiscreteSignal(-INF,INF)
    x.set_value_at_time(0, 1)
    x.set_value_at_time(2, -1)
    x.plot("Input x(n)")

    h1 = DiscreteSignal(-INF,INF)
    h1.set_value_at_time(0, 1)

    h2 = DiscreteSignal(-INF,INF)
    h2.set_value_at_time(1, 0.5)

    h3 = DiscreteSignal(-INF,INF)
    h3.set_value_at_time(0, 1)
    h3.set_value_at_time(1, 1)

    sys1 = LTISystem(h1)
    sys2 = LTISystem(h2)
    sys3 = LTISystem(h3)
    
    # Todo: Determine output block by block
    x1=sys1.output(x)
    x2=sys2.output(x)
    x_comb=x1.add(x2)
    y_final_1=sys3.output(x_comb)
    y_final_1.plot("Output via block-by-block system")

    # Todo: Determine h_combined
    h12=h1.add(h2)
    h_combined=sys3.output(h12)
    sys_combined = LTISystem(h_combined)

    y_final_2 = sys_combined.output(x)
    y_final_2.plot("Output via combined impulse response")

    print("Outputs are equal:",
          np.allclose(y_final_1.x_n, y_final_2.x_n))

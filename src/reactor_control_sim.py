"""
Industrial Batch Reactor Closed-Loop Temperature Control Simulation
Author: J Shreyas Aradhya
"""

import math

class PIDController:
    def __init__(self, Kp=2.5, Ki=0.08, Kd=1.2, setpoint=80.0, output_limits=(-100.0, 100.0)):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.min_out, self.max_out = output_limits
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, current_val, dt):
        error = self.setpoint - current_val
        
        # Proportional term
        P = self.Kp * error
        
        # Integral term with anti-windup clamping
        self.integral += error * dt
        I = self.Ki * self.integral
        
        # Derivative term
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        D = self.Kd * derivative
        
        self.prev_error = error
        raw_output = P + I + D
        
        # Clamp output
        clamped = max(self.min_out, min(self.max_out, raw_output))
        # Anti-windup back-calculation
        if raw_output != clamped:
            self.integral -= error * dt
            
        return clamped

def simulate_batch_reactor():
    print("Simulating Industrial Batch Reactor Temperature Response...")
    dt = 1.0 # 1 second time step
    sim_time = 300 # 5 minutes
    
    T_ambient = 25.0
    T_reactor = 25.0
    T_setpoint = 85.0
    
    pid = PIDController(Kp=3.0, Ki=0.05, Kd=1.5, setpoint=T_setpoint)
    
    print(f"{'Time (s)':<10} {'T_Reactor (°C)':<16} {'Control Effort (%)':<20} {'Status':<15}")
    print("-" * 65)
    
    for t in range(0, sim_time + 1, 10):
        control_u = pid.compute(T_reactor, dt=10)
        
        # Simplified first-order thermal model with heat exchange:
        # dT/dt = alpha * (T_ambient - T_reactor) + beta * control_u
        alpha = 0.005
        beta = 0.035
        dT = (-alpha * (T_reactor - T_ambient) + beta * control_u) * 10
        T_reactor += dT
        
        status = "HEATING" if control_u > 0 else "COOLING"
        if abs(T_reactor - T_setpoint) < 0.5:
            status = "STABILIZED"
            
        print(f"{t:<10} {T_reactor:<16.2f} {control_u:<20.2f} {status:<15}")

if __name__ == '__main__':
    simulate_batch_reactor()

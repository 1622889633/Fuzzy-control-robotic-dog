import time

class FuzzyPID:
    ''' PID controller with fuzzy logic for dynamic gain adjustment '''
    def __init__(self, P=0.0, I=0.0, D=0.0):
        self.setPoint = 0.0
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.last_error = 0.0
        self.P_error = 0.0
        self.I_error = 0.0
        self.D_error = 0.0
        self.I_saturation = 10.0
        self.output = 0.0

        # Fuzzy membership functions setup
        self.error_categories = {'small': 0.1, 'medium': 0.3, 'large': 0.5}
        self.delta_categories = {'small': 0.1, 'medium': 0.2, 'large': 0.4}

    def compute_fuzzy_control(self, error, delta_error):
        # Simple fuzzy logic to adjust PID gains
        # Adjust Kp
        if abs(error) < 5:
            self.Kp = self.error_categories['small'] * 0.5
        elif abs(error) < 10:
            self.Kp = self.error_categories['medium'] * 0.75
        else:
            self.Kp = self.error_categories['large']

        # Adjust Ki
        if abs(delta_error) < 0.1:
            self.Ki = self.delta_categories['small'] * 0.02
        elif abs(delta_error) < 0.2:
            self.Ki = self.delta_categories['medium'] * 0.05
        else:
            self.Ki = self.delta_categories['large']

        # Adjust Kd
        self.Kd = self.delta_categories['small'] if abs(delta_error) < 0.1 else self.delta_categories['medium']

    def PID_compute(self, feedback_val):
        error = self.setPoint - feedback_val
        delta_error = error - self.last_error

        # Update PID gains based on fuzzy logic
        self.compute_fuzzy_control(error, delta_error)

        self.P_error = self.Kp * error
        self.I_error += error 
        self.D_error = self.Kd * delta_error

        # Anti-windup check for integral term
        if self.I_error < -self.I_saturation:
            self.I_error = -self.I_saturation
        elif self.I_error > self.I_saturation:
            self.I_error = self.I_saturation

        self.output = self.P_error + (self.Ki * self.I_error) + self.D_error
        self.last_error = error
        return self.output

    def setSetpoint(self, set_point):
        self.setPoint = set_point

    def setI_saturation(self, saturation_val):
        self.I_saturation = saturation_val



# coding:utf-8
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyController:
    def __init__(self):
        error = np.arange(-10, 11, 1)
        delta_error = np.arange(-10, 11, 1)
        output = np.arange(-50, 51, 1)


        error_low = fuzz.trimf(error, [-10, -10, 0])
        error_med = fuzz.trimf(error, [-10, 0, 10])
        error_high = fuzz.trimf(error, [0, 10, 10])

        delta_error_low = fuzz.trimf(delta_error, [-10, -10, 0])
        delta_error_med = fuzz.trimf(delta_error, [-10, 0, 10])
        delta_error_high = fuzz.trimf(delta_error, [0, 10, 10])

        output_negative = fuzz.trimf(output, [-50, -25, 0])
        output_zero = fuzz.trimf(output, [-25, 0, 25])
        output_positive = fuzz.trimf(output, [0, 25, 50])

        error_ctrl = ctrl.Antecedent(error, 'error')
        delta_error_ctrl = ctrl.Antecedent(delta_error, 'delta_error')
        output_ctrl = ctrl.Consequent(output, 'output')

        error_ctrl['low'] = error_low
        error_ctrl['medium'] = error_med
        error_ctrl['high'] = error_high

        delta_error_ctrl['low'] = delta_error_low
        delta_error_ctrl['medium'] = delta_error_med
        delta_error_ctrl['high'] = delta_error_high

        output_ctrl['negative'] = output_negative
        output_ctrl['zero'] = output_zero
        output_ctrl['positive'] = output_positive

        rule1 = ctrl.Rule(error_ctrl['low'] & delta_error_ctrl['medium'], output_ctrl['negative'])
        rule2 = ctrl.Rule(error_ctrl['medium'], output_ctrl['zero'])
        rule3 = ctrl.Rule(error_ctrl['high'] & delta_error_ctrl['medium'], output_ctrl['positive'])

        self.system = ctrl.ControlSystem([rule1, rule2, rule3])
        self.simulation = ctrl.ControlSystemSimulation(self.system)

    def compute(self, current_error, delta_error):
        self.simulation.input['error'] = current_error
        self.simulation.input['delta_error'] = delta_error
        self.simulation.compute()
        return self.simulation.output['output']

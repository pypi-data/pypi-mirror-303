import numpy as np
import math
import warnings
import sys
from scipy.optimize import minimize, Bounds


class util_itc:

    """
    Takes intertemporal choice data for n >= 3 decisions and returns estimated parameters k, inverse temperature, and an extra parameter where relevant for the model.

    Args:
    modeltype: string describing the model used to fit data: 'E' for exponential, 'H' for hyperbolic, 'GH' for generalized hyperbolic, or 'Q' for quasi-hyperbolic.
    choice: array-like of size n containing only the values 1 and 0, where 1 represents option 1 in the choice data and 0 represents option 2.
    amt1: array-like of size n containing nonnegative numbers, where each value represents a payoff from option 1
    delay1: array-like of size n containing nonnegative numbers, where each value represents a delay before receiving a payoff from option 1
    amt2: array-like of size n containing nonnegative numbers, where each value represents a payoff from option 2
    delay2: array-like of size n containing nonnegative numbers, where each value represents a delay before receiving a payoff from option 2

    Validates inputs, then runs the fit method to fit intertemporal choice data to a model of the type given.
    Stores parameters in instance variable named output, formatted as: [[est. k, est. inverse temperature, est. extra parameter (s for GH, b for Q)], "model", number of choices]
    """

    def __init__(self, modeltype, choice, amt1, delay1, amt2, delay2):

        # Validates inputs
        self.modeltype, self.choice, self.amt1, self.delay1, self.amt2, self.delay2 = self.__itc_input_checker(modeltype, choice, amt1, delay1, amt2, delay2)
        
        # Checks for one-sided choice data
        if np.all(self.choice == 1) or np.all(self.choice == 0):
            warnings.warn('All input data is one-sided')

        # Fits data using given model
        self.params = self.fit()

        # Stores fitted results in list "output"
        # Format: [[est. k, est. inverse temperature, est. extra parameter (s for GH, b for Q)], "model", number of choices]
        self.output = []
        self.output.append(self.params)
        self.output.append(self.modeltype)
        self.output.append(len(choice))

    
    def fit(self):

        """
        Uses scipy.optimize.minimize to fit intertemporal choice data to a model specified during object initialization.
        """

        estimated_k = []
        estimated_it = []
        average_likelihoods = []

        best_params = []

        if self.modeltype == 'GH':

            lower_k, upper_k = self.__bounds_h(self.amt1, self.delay1, self.amt2, self.delay2)

            if lower_k > 0:
                lower_k_log = math.log(lower_k)
            else:
                lower_k_log = math.log(0.00001)

            upper_k_log = math.log(upper_k)

            bounds = Bounds([lower_k_log, -1, -1], [upper_k_log, 2, 2])

            estimated_s = []

            simple_hyperbolic = util_itc('H', self.choice, self.amt1, self.delay1, self.amt2, self.delay2)
            initial_k = simple_hyperbolic.fit()[0]
            initial_it = simple_hyperbolic.fit()[1]

            for i in np.linspace(0, 1, 5)[1:-1]:
                init = np.array([initial_k, initial_it, i])
                result = minimize(self.fun, init, method='SLSQP', bounds=bounds)
                estimated_k.append(math.exp(result.x[0]))
                estimated_it.append(math.exp(result.x[1]))
                estimated_s.append(math.exp(result.x[2]))
                average_likelihoods.append(-result.fun)

            best_index = average_likelihoods.index(max(average_likelihoods))
            best_k = estimated_k[best_index]
            best_it = estimated_it[best_index]
            best_s = estimated_s[best_index]

            best_params.append(best_k)
            best_params.append(best_it)
            best_params.append(best_s)

        elif self.modeltype == 'Q':

            lower_k, upper_k = self.__bounds_e(self.amt1, self.delay1, self.amt2, self.delay2)
            lower_k_log = math.log(lower_k)
            upper_k_log = math.log(upper_k)

            bounds = Bounds([lower_k_log, -1, 0], [upper_k_log, 2, 1])

            estimated_b = []

            for i in np.linspace(lower_k_log, upper_k_log, 5)[1:-1]:
                for j in np.linspace(0, 1, 5)[1:-1]:
                    init = np.array([i, 1, j])
                    result = minimize(self.fun, init, method='SLSQP', bounds=bounds)
                    estimated_k.append(math.exp(result.x[0]))
                    estimated_it.append(math.exp(result.x[1]))
                    estimated_b.append(result.x[2])
                    average_likelihoods.append(-result.fun)

            best_index = average_likelihoods.index(max(average_likelihoods))
            best_k = estimated_k[best_index]
            best_it = estimated_it[best_index]
            best_b = estimated_b[best_index]

            best_params.append(best_k)
            best_params.append(best_it)
            best_params.append(best_b)

        else: 

            if self.modeltype == 'E':
                lower_k, upper_k = self.__bounds_e(self.amt1, self.delay1, self.amt2, self.delay2)
            else:
                lower_k, upper_k = self.__bounds_h(self.amt1, self.delay1, self.amt2, self.delay2)

            if lower_k > 0:
                lower_k_log = math.log(lower_k)
            else:
                lower_k_log = math.log(0.00001)

            upper_k_log = math.log(upper_k)

            bounds = Bounds([lower_k_log, -1], [upper_k_log, 2])

            for i in np.linspace(lower_k_log, upper_k_log, 5)[1:-1]:
                for j in np.linspace(0, 3, 5)[1:-1]:
                    init = np.array([i, j])
                    result = minimize(self.fun, init, method='SLSQP', bounds=bounds)
                    estimated_k.append(math.exp(result.x[0]))
                    estimated_it.append(math.exp(result.x[1]))
                    average_likelihoods.append(-result.fun)

            best_index = average_likelihoods.index(max(average_likelihoods))
            best_k = estimated_k[best_index]
            best_it = estimated_it[best_index]

            best_params.append(best_k)
            best_params.append(best_it)

        return best_params


    def fun(self, params):

        """
        Defines the objective function to be minimized, calculating utility differences based on model type and given parameters.

        Args:
        params: a size 2 or 3 list containing initial parameter starting points for k, inverse temperature, and an optional second parameter s or b.

        Returns:
        float: negative average log likelihood of choices
        """

        k = math.exp(params[0])
        inverse_temp = math.exp(params[1])

        if self.modeltype == 'E':
            util1 = self.__exponential(self.amt1, k, self.delay1)
            util2 = self.__exponential(self.amt2, k, self.delay2)

        if self.modeltype == 'H':
            util1 = self.__hyperbolic(self.amt1, k, self.delay1)
            util2 = self.__hyperbolic(self.amt2, k, self.delay2)
        
        if self.modeltype == 'GH':
            s = math.exp(params[2])
            util1 = self.__generalized_hyperbolic(self.amt1, k, self.delay1, s)
            util2 = self.__generalized_hyperbolic(self.amt2, k, self.delay2, s)

        if self.modeltype == 'Q':
            b = params[2]
            util1 = self.__quasi_hyperbolic(self.amt1, k, self.delay1, b)
            util2 = self.__quasi_hyperbolic(self.amt2, k, self.delay2, b)

        dv = util2 - util1
        
        dv_choice = -np.where(self.choice == 1, dv, -dv)
        reg = np.divide(dv_choice, inverse_temp)
        logp = np.array([-np.log(1 + np.exp(reg[i])) if reg[i] < 709 else -reg[i] for i in range(len(reg))])

        return -np.average(logp)


    # Utility calculation functions

    @staticmethod
    def __exponential(a, k, d):

        """
        Calculates utility given an amount, k value, and delay using the exponential model type.

        Args:
        a: numpy array containing nonnegative numbers, where each value represents a payoff amount
        k: numerical value indicating k parameter in exponential model
        d: numpy array containing nonnegative numbers, where each value represents a delay before receiving a payoff

        Returns:
        numpy array: utility values of each amount and delay combination given the parameter k
        """

        return np.multiply(a, np.exp(np.multiply(-k, d)))
    

    @staticmethod
    def __hyperbolic(a, k, d):

        """
        Calculates utility given an amount, k value, and delay using the hyperbolic model type.

        Args:
        a: numpy array containing nonnegative numbers, where each value represents a payoff amount
        k: numerical value indicating k parameter in hyperbolic model
        d: numpy array containing nonnegative numbers, where each value represents a delay before receiving a payoff

        Returns:
        numpy array: utility values of each amount and delay combination given the parameter k
        """
        
        return np.multiply(a, np.divide(1, np.add(1, np.multiply(k, d))))
    

    @staticmethod
    def __generalized_hyperbolic(a, k, d, s):

        """
        Calculates utility given an amount, k value, and delay using the generalized hyperbolic model type.

        Args:
        a: numpy array containing nonnegative numbers, where each value represents a payoff amount
        k: numerical value indicating k parameter in generalized hyperbolic model
        d: numpy array containing nonnegative numbers, where each value represents a delay before receiving a payoff
        s: numerical value indicating s parameter in generalized hyperbolic model

        Returns:
        numpy array: utility values of each amount and delay combination given the parameters k and s
        """

        return np.multiply(a, np.divide(1, np.power(np.add(1, np.multiply(k, d)), s)))
    

    @staticmethod
    def __quasi_hyperbolic(a, k, d, b):

        """
        Calculates utility given an amount, k value, and delay using the quasi-hyperbolic model type.

        Args:
        a: numpy array containing nonnegative numbers, where each value represents a payoff amount
        k: numerical value indicating k parameter in quasi-hyperbolic model
        d: numpy array containing nonnegative numbers, where each value represents a delay before receiving a payoff
        b: numerical value indicating b parameter in quasi-hyperbolic model

        Returns:
        numpy array: utility values of each amount and delay combination given the parameters k and b
        """

        return np.multiply(a, np.multiply(b, np.exp(np.multiply(-k, d))))
    

    # Bounds calculation functions. E and Q models share __bounds_e; H and GH share __bounds_h
    # Sets lower and upper bounds (for use in minimize) to the min and max indifference k values from given data

    @staticmethod
    def __bounds_e(amt1, delay1, amt2, delay2):

        """
        Finds appropriate bounds for optimization using the given data by finding minimum and maximum indifference values for parameters. 
        Used in exponential and quasi-hyperbolic models.
        """

        indifference_ks = np.divide(np.subtract(np.log(amt2), np.log(amt1)), np.subtract(delay2, delay1))
        return min(indifference_ks), max(indifference_ks)
    

    @staticmethod
    def __bounds_h(amt1, delay1, amt2, delay2):

        """
        Finds appropriate bounds for optimization using the given data by finding minimum and maximum indifference values for parameters. 
        Used in hyperbolic and generalized hyperbolic models.
        """

        indifference_ks = np.divide(np.subtract(amt2, amt1), np.subtract(np.multiply(amt1, delay2), np.multiply(amt2, delay1)))
        return min(indifference_ks), max(indifference_ks)


    @staticmethod
    def __itc_input_checker(modeltype, choice, amt1, delay1, amt2, delay2):

        """
        Validates input data passed from the constructor and formats all array-like object into numpy arrays.
        """

        modeltypes = ['E', 'H', 'GH', 'Q']

        assert (type(modeltype) == str and modeltype.upper() in modeltypes), f'{modeltype} should be a string from the list "E" (exponential), "H" (hyperbolic), "GH" (generalized hyperbolic), and "Q" (quasi hyperbolic)'
        modeltype = modeltype.upper()

        arraylike_inputs = [choice, amt1, delay1, amt2, delay2]
        arraylike_labels = ['choice', 'amt1', 'delay1', 'amt2', 'delay2']

        for i in range(len(arraylike_inputs)):

            if not isinstance(arraylike_inputs[i], np.ndarray):
                try:
                    arraylike_inputs[i] = np.array(arraylike_inputs[i])
                except Exception as e:
                    raise RuntimeError(f'{arraylike_labels[i]} should be an array-like; error converting to numpy array: {e}')
            
            try:
                arraylike_inputs[i] = arraylike_inputs[i].astype(float)
            except Exception as e:
                raise RuntimeError(f'{arraylike_labels[i]} should only contain numerical values, error casting to float: {e}')
            
            assert (type(arraylike_inputs[i]) == np.ndarray and arraylike_inputs[i].ndim == 1), f'{arraylike_labels[i]} should be a vector'
            assert (arraylike_inputs[i].size > 2), f'{arraylike_labels[i]} should have at least 3 elements'

            if i == 0:
                assert (np.all((arraylike_inputs[i] == 0) | (arraylike_inputs[i] == 1))), f'all elements in {arraylike_labels[i]} should be 1 or 0'
            else:
                assert (np.all(arraylike_inputs[i] >= 0)), f'{arraylike_labels[i]} should be nonnegative numbers only'

        assert (arraylike_inputs[0].size == arraylike_inputs[1].size == arraylike_inputs[2].size == arraylike_inputs[3].size == arraylike_inputs[4].size), 'all vectors should have equal size'

        return modeltype, arraylike_inputs[0], arraylike_inputs[1], arraylike_inputs[2], arraylike_inputs[3], arraylike_inputs[4]

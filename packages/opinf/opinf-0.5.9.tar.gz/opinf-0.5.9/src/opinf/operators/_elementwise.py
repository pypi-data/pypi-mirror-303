# operators/_elementwise.py
"""Operators for Hadamard (element-wise) products."""

from ._base import OperatorTemplate


class ElementwiseQuadraticOperator(OperatorTemplate):
    def __init__(self, state_dimension=None):
        self.__r = None

    @property
    def state_dimension(self):
        return self.__r

    def apply(self, state, input_=None):
        if self.__r is None:
            self.__r = state.shape[0]
        return state**2

    def jacobian(self, state, input_=None):
        pass

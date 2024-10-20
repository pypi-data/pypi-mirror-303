from ..extension import Extension


class BackwardOutputExtension(Extension):

    def __init__(self):
        self._name = 'output_grad'

    def _default(self, module, grad_input, grad_output):
        return grad_output[0]

    def _Linear(self, module, grad_input, grad_output):
        return grad_output[0]

    def _Conv2d(self, module, grad_input, grad_output):
        return grad_output[0]



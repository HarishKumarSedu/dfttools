# global context

class global_context():
    def __init__(self):
        # List of output instructions
        self.output = []
        self.instructions = {}
        self.dut_descr = None

g = global_context()

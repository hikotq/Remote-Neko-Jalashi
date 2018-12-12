class Controller(object):
    def __init__(self, servo):
        self.servo = servo
        
    def execute_prog(self, prog):
        for inst in prog:
            self.execute(inst)

    def execute(self, inst):
        if isinstance(inst, Horizon):
            self.servo.horizon(inst.pulse)
        elif isinstance(inst, Vertical):
            self.servo.vertical(inst.pulse)
        else:
            self.servo.to_default()

class Controller(object):
    def __init__(self, servo):
        self.servo = servo
        
    def execute_prog(self, prog):
        for inst in prog:
            self.execute(inst)

    def execute(self, inst):
        if isinstance(inst, Rotate):
            self.servo.rotate(vertical=inst.vertical, horizon=inst.vertical)
        else:
            self.servo.to_default()

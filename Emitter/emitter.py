from collections.abc import Iterable

class emitter():

    def __init__(self, program, filename):

        self.filename = filename

        instructions = self.flatten(program)

        self.emit_code(instructions)


    def emit_code(self, program):
        with open(f'{self.filename}.wpk', 'a') as f:

            for operation in program:
                #print(operation)
                f.write(operation + "\n")
        return 1

    def flatten(self, xs):
        for x in xs:
            if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
                yield from self.flatten(x)
            else:
                yield x
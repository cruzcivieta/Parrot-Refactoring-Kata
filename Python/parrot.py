class Parrot:
    @staticmethod
    def european_parrot():
        return EuropeanParrot()

    @staticmethod
    def african_parrot(number_of_coconuts):
        return AfricanParrot(number_of_coconuts)

    @staticmethod
    def norwegian_blue_parrot(voltage):
        return NorwegianBlueParrot(voltage)

    @staticmethod
    def nailed_parrot():
        return NailedParrot()

    def _base_speed(self):
        return 12.0


class EuropeanParrot(Parrot):
    def speed(self):
        return self._base_speed()


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts):
        self.number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self.number_of_coconuts)

    def _load_factor(self):
        return 9.0


class NorwegianBlueParrot(Parrot):
    def __init__(self, voltage):
        self.voltage = voltage

    def speed(self):
        return self._compute_base_speed_for_voltage(self.voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])


class NailedParrot:
    def speed(self):
        return 0

class RechargeEnergyMixin:

    def recharge_energy(self, amount: int):
        energy_to_recharge = 100 - self.energy
        self.energy += energy_to_recharge
        self.save()
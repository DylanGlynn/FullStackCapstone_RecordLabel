from django.db import models


class PerformerInstrument(models.Model):
    performer = models.ForeignKey('Performer', on_delete=models.CASCADE)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)

    @property
    def instrument_name(self):
        ''' Get instrument name. '''
        return f'{self.instrument.name}'
    
    @property
    def performer_name(self):
        ''' Get a performer's name. '''
        return f'{self.performer.first_name} {self.performer.last_name}'

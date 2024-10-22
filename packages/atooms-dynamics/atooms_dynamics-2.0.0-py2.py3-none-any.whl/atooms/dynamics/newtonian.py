"""Molecular dynamics fortran backend for atooms"""

import os
import math
import numpy
import logging
import f2py_jit
from atooms.system import Thermostat
from .base import _Dynamics

__all__ = ['VelocityVerlet', 'NosePoincare', 'EventDriven', 'Berendsen']

_log = logging.getLogger(__name__)
_f90_kernel_soft = os.path.join(os.path.dirname(__file__), 'kernels_soft.f90')
_f90_kernel_hard = os.path.join(os.path.dirname(__file__), 'kernels_hard.f90')


class VelocityVerlet(_Dynamics):

    def __init__(self, system, timestep=0.001):
        _Dynamics.__init__(self, system)

        # Molecular dynamics specific stuff
        self.conserved_energy = 0.0
        self.timestep = timestep

        # We compute the initial potential energy
        self.system.compute_interaction('forces')
        self._reference_energy = None
        self._uid = f2py_jit.build_module(_f90_kernel_soft)

    def __str__(self):
        return """
backend: newtonian dynamics
algorithm: {}
timestep: {}
""".format(self.__class__, self.timestep)

    def run(self, steps):
        # Dump the arrays before we start. This can be done at each
        # run() call because we ask for views, and this does not incur
        # into overhead.
        _box = self.system.view('cell.side', dtype='float64')
        _pos = self.system.view('particle.position', dtype='float64', order='F')
        _vel = self.system.view('particle.velocity', dtype='float64', order='F')
        _ids = self.system.view('particle.species', dtype='int32')
        _rad = self.system.view('particle.radius', dtype='float64')
        _pos_unf = self.system.view('particle.position_unfolded', order='F')
        # Masses have to be replicated along the spatial dimensions to keep the vector syntax
        # The None indexing syntax adds a new dimension to the array
        _mas = self.system.view('particle.mass', dtype='float64')
        _mas = numpy.repeat(_mas[:, numpy.newaxis], len(_box), axis=1)
        _mas = numpy.transpose(_mas, (1, 0))
        if self._reference_energy is None:
            self._reference_energy = self.system.total_energy()

        # Main loop
        f90 = f2py_jit.import_module(self._uid)
        for _ in range(steps):
            f90.methods.evolve_velocity_verlet(1, self.timestep,
                                               self.system.interaction.forces,
                                               _box, _pos, _pos_unf,
                                               _vel, _ids, _mas)
            self.system.compute_interaction('forces')
            f90.methods.evolve_velocity_verlet(2, self.timestep,
                                               self.system.interaction.forces,
                                               _box, _pos, _pos_unf,
                                               _vel, _ids, _mas)

        self.conserved_energy = self.system.total_energy(cache=True) - self._reference_energy


class NosePoincare(_Dynamics):

    def __init__(self, system, timestep=0.001, temperature=-1.0, mass=-1.0):
        _Dynamics.__init__(self, system)

        # Molecular dynamics specific stuff
        self.conserved_energy = 0.0
        self.timestep = timestep

        # Thermostat
        if system.thermostat is None:
            assert temperature > 0.0
            if mass < 0.0: mass = 5.0
            system.thermostat = Thermostat(temperature, mass=mass)
        else:
            if temperature > 0.0:
                system.thermostat.temperature = temperature
            if mass > 0.0:
                system.thermostat.mass = mass

        # We compute the initial potential energy
        self.system.compute_interaction('forces')
        self._reference_energy = None
        self._uid = f2py_jit.build_module(_f90_kernel_soft)

    def __str__(self):
        return """
backend: newtonian dynamics
algorithm: nose-poincare
timestep: {}
temperature: {}
""".format(self.timestep, self.system.thermostat.temperature)

    def run(self, steps):
        # Dump the arrays before we start. This can be done at each
        # run() call because we ask for views, and this does not incur
        # into overhead.
        _box = self.system.view('cell.side', dtype='float64')
        _pos = self.system.view('particle.position', dtype='float64', order='F')
        _vel = self.system.view('particle.velocity', dtype='float64', order='F')
        _ids = self.system.view('particle.species', dtype='int32')
        _rad = self.system.view('particle.radius', dtype='float64')
        _pos_unf = self.system.view('particle.position_unfolded', order='F')
        # Masses have to be replicated along the spatial dimensions to keep the vector syntax
        # The None indexing syntax adds a new dimension to the array
        _mas = self.system.view('particle.mass', dtype='float64')
        _mas = numpy.repeat(_mas[:, numpy.newaxis], len(_box), axis=1)
        _mas = numpy.transpose(_mas, (1, 0))
        # Make sure the thermostat coordinates are 0-dim arrays
        # TODO: this calls for coords/moms to be added to Thermostat
        thermostat = self.system.thermostat
        # Reference energy
        ndim = self.system.number_of_dimensions
        ndf = ndim * (len(self.system.particle) - 1)
        if self._reference_energy is None:
            thermostat = self.system.thermostat
            # TODO: this calls for a NosePoincareThermostat.energy method?
            self._reference_energy = self.system.total_energy() + \
                thermostat.momentum**2 / (2*thermostat.mass) + \
                ndf * thermostat.temperature * math.log(thermostat.coordinate)

        # Main loop
        f90 = f2py_jit.import_module(self._uid)
        for _ in range(steps):
            f90.methods.evolve_nose_poincare(1, self.timestep,
                                             self.system.interaction.forces,
                                             0.0, 0.0,
                                             thermostat.temperature,
                                             thermostat.coordinate,
                                             thermostat.momentum,
                                             thermostat.mass,
                                             self._reference_energy,
                                             _box, _pos, _pos_unf,
                                             _vel, _ids, _mas)
            epot_old = self.system.interaction.energy
            self.system.compute_interaction('forces')
            epot_new = self.system.interaction.energy
            f90.methods.evolve_nose_poincare(2, self.timestep,
                                             self.system.interaction.forces,
                                             epot_old, epot_new,
                                             thermostat.temperature,
                                             thermostat.coordinate,
                                             thermostat.momentum,
                                             thermostat.mass,
                                             self._reference_energy,
                                             _box, _pos, _pos_unf,
                                             _vel, _ids, _mas)

        energy = self.system.total_energy(cache=True) + \
            thermostat.momentum**2 / (2*thermostat.mass) + \
            ndf * thermostat.temperature * math.log(thermostat.coordinate)
        self.conserved_energy = thermostat.coordinate * (energy - self._reference_energy)


class EventDrivenAllenTildesley(_Dynamics):

    def __init__(self, system, timestep=0.001):
        _Dynamics.__init__(self, system)
        if self.system.interaction is None:
            from atooms.system.interaction import InteractionBase
            self.system.interaction = InteractionBase()
        self.timestep = timestep
        self._init = False
        self._uid = f2py_jit.build_module(_f90_kernel_hard)
        # TODO: Inlining with 0.6.0 gives a seg fault
        # f90 = f2py_jit.jit(f2py_jit.inline(_f90_kernel_hard))  #, extra_args='--opt="-fbounds-check"')

    def __str__(self):
        txt = """
backend: netwonian dynamics
algorithm: event-driven
method: allen-tildesley
timestep: {}
""".format(self.timestep)
        return txt

    def run(self, steps):

        # Dump variables
        box = self.system.view('cell.side')
        pos = self.system.view('particle.position', order='F')
        unf = self.system.view('particle.position_unfolded', order='F')
        vel = self.system.view('particle.velocity', order='F')
        ids = self.system.view('particle.species', dtype='int32')
        rad = self.system.view('particle.radius')
        
        f90 = f2py_jit.import_module(self._uid)
        if not self._init:
            self._coltime = numpy.ndarray(len(self.system.particle))
            self._partner = numpy.ndarray(len(self.system.particle), dtype='int32')
            f90.methods.run(pos, unf, vel, rad*2, box[0],
                            self.timestep, 0, self._coltime, self._partner)
            self._init = True

        # Main loop
        virial = f90.methods.run(pos, unf, vel, rad*2, box[0], self.timestep, steps, self._coltime, self._partner)
        self.system.interaction.virial = virial * self.system.number_of_dimensions


EventDriven = EventDrivenAllenTildesley


class Berendsen(_Dynamics):

    def __init__(self, system, timestep=0.001):
        _Dynamics.__init__(self, system)
        self.timestep = timestep
        self.system.compute_interaction('forces')
        self._T, self._tau_T = -1.0, 1.0
        self._P, self._tau_P = -1.0, 1.0
        if system.thermostat is not None:
            self._T = system.thermostat.temperature
            self._tau_T = system.thermostat.relaxation_time
        if system.barostat is not None:
            self._P = system.barostat.pressure
            self._tau_P = system.barostat.relaxation_time
        self._uid = f2py_jit.build_module(_f90_kernel_soft)

    def run(self, steps):
        # Get variables
        box = self.system.view('cell.side', dtype='float64')
        pos = self.system.view('particle.position', dtype='float64', order='F')
        vel = self.system.view('particle.velocity', dtype='float64', order='F')
        ids = self.system.view('particle.species', dtype='int32')
        rad = self.system.view('particle.radius', dtype='float64')
        pos_unf = self.system.view('particle.position_unfolded', order='F')
        # Masses have to be replicated along the spatial dimensions to keep the vector syntax
        # The None indexing syntax adds a new dimension to the array
        mas = self.system.view('particle.mass', dtype='float64')
        mas = numpy.repeat(mas[:, numpy.newaxis], len(box), axis=1)
        mas = numpy.transpose(mas, (1, 0))

        # Main loop
        f90 = f2py_jit.import_module(self._uid)
        for _ in range(steps):
            f90.methods.evolve_velocity_verlet(1, self.timestep,
                                               self.system.interaction.forces,
                                               box, pos, pos_unf, vel,
                                               ids, mas)
            self.system.compute_interaction('forces')
            f90.methods.evolve_velocity_verlet(2, self.timestep,
                                               self.system.interaction.forces,
                                               box, pos, pos_unf, vel,
                                               ids, mas)
            virial = self.system.virial(cache=True, per_particle=False)
            f90.methods.rescale_berendsen(self._T, self._tau_T,
                                          self._P, self._tau_P, box,
                                          pos, vel, mas, virial)

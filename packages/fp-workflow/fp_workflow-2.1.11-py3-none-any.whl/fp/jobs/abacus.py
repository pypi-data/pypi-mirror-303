#region: Modules.
from fp.inputs.input_main import *
from fp.io.strings import *
from fp.flows.run import *
from pkg_resources import resource_filename
import glob 
from ase.data import atomic_masses, atomic_numbers
#endregion

#region: Variables.
#endregion

#region: Functions.
#endregion

#region: Classes.
class AbacusJob:
    def __init__(
        self,
        input: Input,
    ):
        self.input: Input = input

        self.stru_abacus = \
f'''
'''
        self.input_abacus = \
f'''
'''
        self.kpt_abacus = \
f'''
'''
        
        self.job_abacus = \
f'''#!/bin/bash
{self.input.scheduler.get_sched_header(self.input.abacus.job_desc)}

{self.input.scheduler.get_sched_mpi_prefix(self.input.abacus.job_desc)}abacus &> abacus.out
'''
        
        self.jobs = [
            'job_abacus.sh',
        ]

    def create_pseudos_dir(self):
        os.system('mkdir -p ./abacus_pseudos')
        data_dir = resource_filename('fp', '') + '/data/pseudos/abacus'

        # Copy the pseudopotentials. 
        for symbol in self.input.atoms.atoms.get_chemical_symbols():
            pseudo_filepath = glob.glob(f'{data_dir}/{symbol}*')[0]
            os.system(f'cp {pseudo_filepath} ./abacus_pseudos/')

    def create_orbitals_dir(self):
        os.system('mkdir -p ./abacus_orbitals')
        data_dir = resource_filename('fp', '') + '/data/orbitals/abacus'

        # Copy the pseudopotentials. 
        for symbol in self.input.atoms.atoms.get_chemical_symbols():
            pseudo_filepath = glob.glob(f'{data_dir}/{symbol}*')[0]
            os.system(f'cp {pseudo_filepath} ./abacus_orbitals/') 

    def get_stru(self):
        output = ''
        
        # Atomic species. 
        output += 'ATOMIC_SPECIES\n'
        for symbol in self.input.atoms.atoms.get_chemical_symbols():
            pseudo_filename = glob.glob(f'./abacus_pseudos/{symbol}*')[0].split('/')[-1]
            output += f'{symbol} {atomic_masses[atomic_numbers[symbol]]} {pseudo_filename}\n'

        # Orbitals.
        output += 'NUMERICAL_ORBITAL\n'
        for symbol in self.input.atoms.atoms.get_chemical_symbols():
            orbital_filename = glob.glob(f'./abacus_orbitals/{symbol}*')[0].split('/')[-1]
            output += f'{orbital_filename}\n'

        # Lattice vectors. 

        # Atomic positions. 

        self.stru_abacus = output

    def get_input(self):
        output = ''
        output += 'INPUT_PARAMETERS\n'
        output += 'suffix struct\n'
        output += 'ntype {}\n'
        output += 'pseudo_dir ./abacus_pseudos\n'
        output += 'orbital_dir ./abacus_orbitals\n'
        output += f'ecutwfc {self.input.abacus.ecut:15.10f} # In Rydberg\n'
        output += f'scf_thr 1e-4 # In Rydberg\n'
        output += f'basis_type {self.input.abacus.basis_type}\n'
        output += f'calculation {self.input.abacus.calculation}\n'
        output += f'{self.input.abacus.extra_args if self.input.abacus.extra_args is not None else ""}'

        self.input_abacus = output

    def get_kpt(self):
        output = ''
        output += 'K_POINTS\n'
        output += '0\n'
        output += 'Gamma\n'
        output += f'{self.input.abacus.kdim[0]} {self.input.abacus.kdim[1]} {self.input.abacus.kdim[2]} 0 0 0\n'
    
        self.kpt_abacus = output

    def create(self):
        self.create_pseudos_dir()
        self.create_orbitals_dir()
        self.get_stru()
        self.get_input()
        self.get_kpt()

        write_str_2_f('STRU', self.stru_abacus)
        write_str_2_f('INPUT', self.input_abacus)
        write_str_2_f('KPT', self.kpt_abacus)
        write_str_2_f('./job_abacus.sh', self.job_abacus)

    def run(self, total_time):
        total_time = run_and_wait_command('./job_abacus.sh', self.input, total_time)

        return total_time

    def save(self, folder):
        inodes = [
            'STRU',
            'INPUT',
            'KPT',
            'OUT.struct',
        ] 

        for inode in inodes:
            os.system(f'cp -r ./{inode} {folder}')

    def remove(self):
        os.system('rm -rf STRU INPUT KPT')
        os.system('rm -rf abacus.out OUT.struct')

#endregion

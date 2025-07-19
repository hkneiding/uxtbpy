import warnings
from string import digits


element_identifiers = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
                       'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
                       'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
                       'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
                       'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
                       'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
                       'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
                       'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
                       'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb',
                       'Bi', 'Po', 'At', 'Rn']


class XtbOutputParser:

    """Class for parsing xTB output."""

    def __init__(self):
        
        """Constructor."""

        self.lines = None
        self.n_atoms = None

    def parse(self, data: str):
        
        """Parses a given xTB output line by line to extract different properties.

        Arguments:
            data (str): The xTB output.

        Returns:
            dict: A dictionary containing the different outputs.
        """

        self.lines = data.split('\n')
        
        xtb_output_data = {}
        
        for i, line in enumerate(self.lines):
            if 'Mol. C6AA /au·bohr⁶' in line:
                self.n_atoms = int(self.lines[i - 2].split()[0])
                break

        if self.n_atoms is None:
            warnings.warn('Failed to retrieve number of atoms. Check input file.')
            return xtb_output_data

        # go through lines to find targets
        for i in range(len(self.lines)):

            if  'HOMO-LUMO GAP' in self.lines[i]:
                xtb_output_data['homo_lumo_gap'] = self._extract_homo_lumo_gap(i)

            if  '(HOMO)' in self.lines[i]:
                xtb_output_data['homo_energy'] = self._extract_homo(i)

            if  '(LUMO)' in self.lines[i]:
                xtb_output_data['lumo_energy'] = self._extract_lumo(i)

            if  'TOTAL ENERGY' in self.lines[i]:
                xtb_output_data['energy'] = self._extract_energy(i)

            if  'TOTAL ENTHALPY' in self.lines[i]:
                xtb_output_data['enthalpy_energy'] = self._extract_enthalpy_energy(i)

            if  'TOTAL FREE ENERGY' in self.lines[i]:
                xtb_output_data['free_energy'] = self._extract_free_energy(i)

            if 'partition function' in self.lines[i]:
                xtb_output_data['enthalpy'] = self._extract_enthalpy(i + 6)
                xtb_output_data['heat_capacity'] = self._extract_heat_capacity(i + 6)
                xtb_output_data['entropy'] = self._extract_entropy(i + 6)

            if 'zero point energy' in self.lines[i]:
                xtb_output_data['zpve'] = self._extract_zpve(i)

            if 'molecular dipole' in self.lines[i]: 
                xtb_output_data['dipole_moment'] = self._extract_dipole_moment(i + 3)

            if 'molecular mass/u' in self.lines[i]:
                xtb_output_data['molecular_mass'] = self._extract_molecular_mass(i)
            
            if 'final structure' in self.lines[i]:
                xtb_output_data['atomic_numbers'] = self._extract_atomic_numbers(i + 4)
                xtb_output_data['optimised_atomic_positions'] = self._extract_optimised_atomic_positions(i + 4)
                xtb_output_data['optimised_xyz'] = self._extract_optimised_xyz(i + 4)

            if 'projected vibrational frequencies' in self.lines[i]:
                xtb_output_data['vibrational_frequencies'] = self._extract_vibrational_frequencies(i + 1)

            if 'reduced masses' in self.lines[i]:
                xtb_output_data['reduced_masses'] = self._extract_reduced_masses(i + 1)

            if 'IR intensities' in self.lines[i]:
                xtb_output_data['ir_intensities'] = self._extract_ir_intensities(i + 1)

            if 'Raman intensities' in self.lines[i]:
                xtb_output_data['raman_intensities'] = self._extract_raman_intensities(i + 1)

            if 'Mol. α(0) /au' in self.lines[i]:
                xtb_output_data['polarisability'] = self._extract_polarisability(i)

            if 'Wiberg/Mayer (AO) data.' in self.lines[i]:
                xtb_output_data['wiberg_index_matrix'] = self._extract_wiberg_index_matrix(i + 6)

        return xtb_output_data

    def _extract_homo_lumo_gap(self, start_index: int):
        
        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_dipole_moment(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])

    def _extract_enthalpy_energy(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_energy(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_free_energy(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])

    def _extract_enthalpy(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[1])

    def _extract_heat_capacity(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[2])
    
    def _extract_entropy(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_zpve(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])

    def _extract_homo(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[-2])

    def _extract_lumo(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[-2])

    def _extract_molecular_mass(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_polarisability(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])

    def _extract_atomic_numbers(self, start_index: int):

        atomic_numbers = []

        while self.lines[start_index].strip() != '':

            line_split = self.lines[start_index].split()
            atomic_numbers.append(element_identifiers.index(line_split[0]) + 1)
            start_index += 1
        
        return atomic_numbers

    def _extract_optimised_atomic_positions(self, start_index: int):

        optimised_atomic_positions = []

        while self.lines[start_index].strip() != '':

            line_split = self.lines[start_index].split()
            optimised_atomic_positions.append([float(line_split[1]),
                                               float(line_split[2]),
                                               float(line_split[3])])
            start_index += 1
        
        return optimised_atomic_positions

    def _extract_optimised_xyz(self, start_index: int):

        optimised_xyz_lines = []

        while self.lines[start_index].strip() != '':

            optimised_xyz_lines.append(' '.join(self.lines[start_index].split()))
            start_index += 1

        return '\n\n'.join([
            str(len(optimised_xyz_lines)), '\n'.join(optimised_xyz_lines)
        ])

    def _extract_vibrational_frequencies(self, start_index: int):

        vibrational_frequencies = []
        while 'eigval' in self.lines[start_index]:

            line_split = self.lines[start_index].split()
            for i in range(2, len(line_split)):
                vibrational_frequencies.append(float(line_split[i]))
            
            start_index += 1
        
        return vibrational_frequencies
    
    def _extract_reduced_masses(self, start_index: int):

        reduced_masses = []

        allowed = set(digits).union(':. ')

        while all(_ in allowed for _ in self.lines[start_index]):

            line_split = self.lines[start_index].replace(':', '').split()
            for i in range(1, len(line_split), 2):
                reduced_masses.append(float(line_split[i]))
            
            start_index += 1

        return reduced_masses

    def _extract_ir_intensities(self, start_index: int):

        ir_intensities = []

        allowed = set(digits).union(':. ')

        while all(_ in allowed for _ in self.lines[start_index]):

            line_split = self.lines[start_index].replace(':', '').split()
            for i in range(1, len(line_split), 2):
                ir_intensities.append(float(line_split[i]))
            
            start_index += 1

        return ir_intensities
    
    def _extract_raman_intensities(self, start_index: int):

        raman_intensities = []

        allowed = set(digits).union(':. ')

        while all(_ in allowed for _ in self.lines[start_index]):

            line_split = self.lines[start_index].replace(':', '').split()
            for i in range(1, len(line_split), 2):
                raman_intensities.append(float(line_split[i]))
            
            start_index += 1

        return raman_intensities

    def _extract_wiberg_index_matrix(self, start_index: int):

        # set up Wiberg matrix
        wiberg_index_matrix = [
            [0 for _ in range(self.n_atoms)] for __ in range(self.n_atoms)
        ]

        while '-------' not in self.lines[start_index]:
            
            line_split = self.lines[start_index].split()
            i_index = int(line_split[0]) - 1

            for i in range(5, len(line_split), 3):
                
                j_index = int(line_split[i]) - 1

                wiberg_index_matrix[i_index][j_index] = float(line_split[i + 2])

            while '--' not in self.lines[start_index + 1]:

                start_index += 1
                line_split = self.lines[start_index].split()
                # break if next line corresponds to the next atom which has no
                # associated Wiberg bond indices
                if len(line_split) % 3 != 0:
                    break

                for i in range(0, len(line_split), 3):

                    j_index = int(line_split[i]) - 1

                    wiberg_index_matrix[i_index][j_index] = float(line_split[i + 2])

            start_index += 1

        return wiberg_index_matrix

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

    """Class for parsing xTB output"""

    def __init__(self):
        
        """Constructor"""

        self.lines = None

    def parse(self, data: str):
        
        """Parses a given xTB output line by line to extract different properties.

        Arguments:
            data (str): The xTB output.

        Returns:
            dict: A dictionary containing the different outputs.
        """

        self.lines = data.split('\n')

        # output variable
        xtb_output_data = {}

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

            if 'molecular dipole:' in self.lines[i]:
                xtb_output_data['dipole_moment'] = self._extract_dipole_moment(i + 3)

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
                xtb_output_data['optimised_structure'] = self._extract_optimised_structure(i + 4)

            if 'projected vibrational frequencies' in self.lines[i]:
                xtb_output_data['vibrational_frequencies'] = self._extract_vibrational_frequencies(i + 1)

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
        return float(line_split[3])

    def _extract_lumo(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[2])

    def _extract_dipole_moment(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])

    def _extract_molecular_mass(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_atomic_numbers(self, start_index: int):

        atomic_numbers = []

        while self.lines[start_index].strip() != '':

            line_split = self.lines[start_index].split()
            atomic_numbers.append(element_identifiers.index(line_split[0]) + 1)
            start_index += 1
        
        return atomic_numbers

    def _extract_optimised_structure(self, start_index: int):

        optimised_structure = []

        while self.lines[start_index].strip() != '':

            line_split = self.lines[start_index].split()
            optimised_structure.append([float(line_split[1]),
                                        float(line_split[2]),
                                        float(line_split[3])])
            start_index += 1
        
        return optimised_structure

    def _extract_vibrational_frequencies(self, start_index: int):

        vibrational_frequencies = []
        while 'eigval' in self.lines[start_index]:

            line_split = self.lines[start_index].split()
            print(line_split)
            for i in range(2, len(line_split)):
                vibrational_frequencies.append(float(line_split[i]))
            
            start_index += 1
        
        return vibrational_frequencies
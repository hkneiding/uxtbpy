class XtbOutputParser:

    """Class for parsing xtb output"""

    def __init__(self, output):
        
        self.output = output
        self.lines = output.split('\n')

    def parse(self):
        
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
                xtb_output_data['enthalpy'] = self._extract_enthalpy(i)

            if  'TOTAL FREE ENERGY' in self.lines[i]:
                xtb_output_data['free_energy'] = self._extract_free_energy(i)

            if 'molecular dipole:' in self.lines[i]:
                xtb_output_data['dipole_moment'] = self._extract_dipole_moment(i + 3)

            if 'partition function' in self.lines[i]:
                xtb_output_data['heat_capacity'] = self._extract_heat_capacity(i + 6)

            if 'partition function' in self.lines[i]:
                xtb_output_data['entropy'] = self._extract_entropy(i + 6)

            if 'zero point energy' in self.lines[i]:
                xtb_output_data['zpve'] = self._extract_zpve(i)

        return xtb_output_data

    def _extract_homo_lumo_gap(self, start_index: int):
        
        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_dipole_moment(self, start_index: int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])

    def _extract_enthalpy(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_energy(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_free_energy(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])
    
    def _extract_heat_capacity(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[2])
    
    def _extract_entropy(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_zpve(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[4])

    def _extract_homo(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[3])

    def _extract_lumo(self, start_index:int):

        line_split = self.lines[start_index].split()
        return float(line_split[2])
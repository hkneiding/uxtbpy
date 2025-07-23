class StdaOutputParser:
    """Class for parsing sTDA output."""

    def __init__(self):
        """Constructor."""

        self.lines = None

    def parse(self, data: str):
        """Parses a given sTDA output line by line to extract different properties.

        Arguments:
            data (str): The sTDA output.

        Returns:
            dict: A dictionary containing the different outputs.
        """

        self.lines = data.split("\n")

        stda_output_data: dict = {}

        # go through lines to find targets
        for i in range(len(self.lines)):

            if (
                "excitation energies, transition moments and TDA amplitudes"
                in self.lines[i]
            ):
                excitation_wavelenghts, excitation_oscillator_strengths = (
                    self._extract_excitations(i + 2)
                )
                stda_output_data["excitation_wavelenghts"] = excitation_wavelenghts
                stda_output_data["excitation_oscillator_strengths"] = (
                    excitation_oscillator_strengths
                )

            if "alpha tensor" in self.lines[i]:
                stda_output_data["polarizability_tensor"] = (
                    self._extract_polarizability_tensor(i + 4)
                )

            if "SOS specific optical rotation" in self.lines[i]:
                (
                    specific_optical_rotation_wavelengths,
                    specific_optical_rotation_angles,
                ) = self._extract_specific_optical_rotations(i + 3)
                stda_output_data["specific_optical_rotation_wavelengths"] = (
                    specific_optical_rotation_wavelengths
                )
                stda_output_data["specific_optical_rotation_angles"] = (
                    specific_optical_rotation_angles
                )

        return stda_output_data

    def _extract_excitations(self, start_index: int):

        excitation_wavelengths = []
        excitation_oscillartor_stengths = []

        while self.lines[start_index].strip() != "":

            line_split = self.lines[start_index].strip().split()
            excitation_wavelengths.append(float(line_split[2]))
            excitation_oscillartor_stengths.append(float(line_split[3]))

            start_index += 1

        return excitation_wavelengths, excitation_oscillartor_stengths

    def _extract_polarizability_tensor(self, start_index: int):

        polarizability_tensor = [[0.0 for _ in range(3)] for __ in range(3)]

        for i in range(3):
            for j in range(0, i + 1, 1):

                line_split = self.lines[start_index + i].strip().split()
                polarizability_tensor[i][j] = float(line_split[j + 1])
                polarizability_tensor[j][i] = float(line_split[j + 1])

        return polarizability_tensor

    def _extract_specific_optical_rotations(self, start_index: int):

        specific_optical_rotation_wavelengths = []
        specific_optical_rotation_angles = []

        while self.lines[start_index].strip() != "":

            line_split = self.lines[start_index].strip().split()
            specific_optical_rotation_wavelengths.append(float(line_split[0]))
            specific_optical_rotation_angles.append(float(line_split[2]))

            start_index += 1

        return specific_optical_rotation_wavelengths, specific_optical_rotation_angles

import unittest
from qtpyvcp_conversational_gcode.ops.face_ops import FaceOps


class TestFacing(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.sut = FaceOps()
        cls.sut.tool_number = 4
        cls.sut.spindle_rpm = 1200
        cls.sut.spindle_dir = 'cw'
        cls.sut.wcs = 'G55'
        cls.sut.coolant = ''
        cls.sut.retract = 0.02
        cls.sut.z_start = 1
        cls.sut.z_end = 0.5
        cls.sut.z_feed = 4.8
        cls.sut.z_clear = 1.2
        cls.sut.x_start = 1
        cls.sut.y_start = 1
        cls.sut.x_end = 6
        cls.sut.y_end = -2
        cls.sut.tool_diameter = 2
        cls.sut.step_over = 1
        cls.sut.step_down = 0.125
        cls.sut.xy_feed = 60
        cls.sut.units = 'in'

    def test_should_face_in_one_pass_when_possible(self):
        expected_gcode = [
            'G20',
            'T4 M6 G43',
            'S1200.0000',
            'M3',
            'G55',
            'F60.0000',
            'G0 X-0.1450 Y1.0000',
            'G0 Z1.0200',
            'G18 G2 X0.0000 Z0.8750 I0.1450',
            'G1 X6.0000',
            'G18 G2 X6.1450 Z1.0200 K0.1450',
            'G0 Z1.2000',
        ]

        self.sut.y_end = 0
        self.sut.z_end = 0.875
        self.assertEqual(expected_gcode, self.sut.face())

    def test_should_face_with_multiple_step_overs(self):
        expected_gcode = [
            'G20',
            'T4 M6 G43',
            'S1200.0000',
            'M3',
            'G55',
            'F60.0000',
            'G0 X-0.1450 Y1.0000',
            'G0 Z1.0200',
            'G18 G2 X0.0000 Z0.8750 I0.1450',
            'G1 X6.0000',
            'G17 G2 Y0.0000 J-0.5000',
            'G1 X1.0000',
            'G18 G3 X0.8550 Z1.0200 K0.1450',
            'G0 Z1.2000',
        ]

        self.sut.y_end = -1
        self.sut.z_end = 0.875
        self.assertEqual(expected_gcode, self.sut.face())

    def test_should_face_with_odd_number_of_steps_overs(self):
        expected_gcode = [
            'G20',
            'T4 M6 G43',
            'S1200.0000',
            'M3',
            'G55',
            'F60.0000',
            'G0 X-0.1450 Y1.0000',
            'G0 Z1.0200',
            'G18 G2 X0.0000 Z0.8750 I0.1450',
            'G1 X6.0000',
            'G17 G2 Y0.0000 J-0.5000',
            'G1 X1.0000',
            'G17 G3 Y-1.0000 J-0.5000',
            'G1 X6.0000',
            'G18 G2 X6.1450 Z1.0200 K0.1450',
            'G0 Z1.2000',
        ]

        self.sut.y_end = -2
        self.sut.z_end = 0.875
        self.assertEqual(expected_gcode, self.sut.face())

    def test_should_face_with_multiple_step_downs(self):
        expected_gcode = [
            'G20',
            'T4 M6 G43',
            'S1200.0000',
            'M3',
            'G55',
            'F60.0000',
            'G0 X-0.1450 Y1.0000',
            'G0 Z1.0200',
            'G18 G2 X0.0000 Z0.8750 I0.1450',
            'G1 X6.0000',
            'G18 G2 X6.1450 Z1.0200 K0.1450',
            'G0 Z1.2000',
            'G0 X-0.1450 Y1.0000',
            'G0 Z0.8950',
            'G18 G2 X0.0000 Z0.7500 I0.1450',
            'G1 X6.0000',
            'G18 G2 X6.1450 Z0.8950 K0.1450',
            'G0 Z1.2000',
        ]

        self.sut.y_end = 0
        self.sut.z_end = 0.750
        self.assertEqual(expected_gcode, self.sut.face())

    def test_should_face_with_multiple_step_downs_and_step_overs(self):
        expected_gcode = [
            'G20',
            'T4 M6 G43',
            'S1200.0000',
            'M3',
            'G55',
            'F60.0000',
            'G0 X-0.1450 Y1.0000',
            'G0 Z1.0200',
            'G18 G2 X0.0000 Z0.8750 I0.1450',
            'G1 X6.0000',
            'G17 G2 Y0.0000 J-0.5000',
            'G1 X1.0000',
            'G17 G3 Y-1.0000 J-0.5000',
            'G1 X6.0000',
            'G18 G2 X6.1450 Z1.0200 K0.1450',
            'G0 Z1.2000',
            'G0 X-0.1450 Y1.0000',
            'G0 Z0.8950',
            'G18 G2 X0.0000 Z0.7500 I0.1450',
            'G1 X6.0000',
            'G17 G2 Y0.0000 J-0.5000',
            'G1 X1.0000',
            'G17 G3 Y-1.0000 J-0.5000',
            'G1 X6.0000',
            'G18 G2 X6.1450 Z0.8950 K0.1450',
            'G0 Z1.2000',
        ]

        self.sut.y_end = -2
        self.sut.z_end = 0.750
        self.assertEqual(expected_gcode, self.sut.face())

    def test_should_adjust_the_step_over_to_use_even_step_over(self):
        expected_gcode = [
            'G20',
            'T4 M6 G43',
            'S1200.0000',
            'M3',
            'G55',
            'F60.0000',
            'G0 X-0.1450 Y0.5000',
            'G0 Z1.0200',
            'G18 G2 X0.0000 Z0.8750 I0.1450',
            'G1 X6.0000',
            'G17 G2 Y-1.0000 J-0.7500',
            'G1 X1.0000',
            'G18 G3 X0.8550 Z1.0200 K0.1450',
            'G0 Z1.2000',
        ]

        self.sut.step_over = 2
        self.sut.y_end = -2
        self.sut.z_end = 0.875
        self.assertEqual(expected_gcode, self.sut.face())

    def test_should_adjust_the_step_down_to_use_even_step_down(self):
        expected_gcode = [
            'G20',
            'T4 M6 G43',
            'S1200.0000',
            'M3',
            'G55',
            'F60.0000',
            'G0 X-1.5200 Y1.0000',
            'G0 Z1.0200',
            'G18 G2 X0.0000 Z-0.5000 I1.5200',
            'G1 X6.0000',
            'G18 G2 X7.5200 Z1.0200 K1.5200',
            'G0 Z1.2000',
            'G0 X-1.5200 Y1.0000',
            'G0 Z-0.4800',
            'G18 G2 X0.0000 Z-2.0000 I1.5200',
            'G1 X6.0000',
            'G18 G2 X7.5200 Z-0.4800 K1.5200',
            'G0 Z1.2000',
        ]

        self.sut.y_end = 0
        self.sut.step_down = 2
        self.sut.z_end = -2
        self.assertEqual(expected_gcode, self.sut.face())

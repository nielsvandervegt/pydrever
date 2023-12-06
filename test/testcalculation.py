import sys
import os

sys.path.append(os.getcwd() + "\src")
sys.path.append(os.getcwd() + "\src\dikerneldll")

from dikerneloutput import CalculationMethod
from toplayertypes import TopLayerType

from dikernelinput import (
    DikernelInput,
    DikeSchematization,
    HydraulicInput,
)
from dikerneloutputlocations import (
    GrassWaveImpactOutputLocation,
    GrassOvertoppingOutputLocation,
    AsphaltOutputLocation,
    NordicStoneOutputLocation,
)
from dikernelcalculationsettings import (
    AsphalCalculationSettings,
    NaturalStoneCalculationSettings,
    GrassWaveImpactCalculationSettings,
    GrassWaveOvertoppingCalculationSettings,
    AsphaltTopLayerSettings,
    GrasCoverOvertoppingTopLayerSettings,
    GrassCoverWaveImpactTopLayerSettings,
)

from dikernel import Dikernel


class TestCalculationInputFactory:
    @staticmethod
    def GetCalculationInput() -> DikernelInput:
        input = DikernelInput()
        input.DikeOrientation = 0.0
        input.HydraulicInput = TestCalculationInputFactory.GetHydraulicBoundaries()
        input.DikeSchematization = TestCalculationInputFactory.GetDikeProfile()
        input.OutputLocations = TestCalculationInputFactory.GetOutputLocations()
        input.Settings = TestCalculationInputFactory.GetCalculationSettings()
        return input

    @staticmethod
    def GetHydraulicBoundaries() -> HydraulicInput:
        timeSteps = [
            0.0,
            2269.440000000016,
            4538.879999999999,
            6808.320000000018,
            9077.760000000031,
            11347.200000000015,
            13616.64,
            15180.292682926836,
            16371.902439024394,
            17563.51219512195,
            18755.12195121951,
            19946.731707317074,
            21138.341463414636,
            22329.951219512193,
            23521.560975609762,
            24713.170731707323,
            25904.780487804877,
            27096.390243902435,
            28287.999999999993,
            29479.60975609755,
            30671.219512195123,
            31862.829268292684,
            33054.43902439024,
            34246.04878048779,
            35437.65853658537,
            36629.26829268294,
            37820.87804878049,
            39012.487804878045,
            40204.0975609756,
            41395.70731707315,
            42587.31707317072,
            43778.92682926828,
            44970.53658536586,
            46162.14634146341,
            47353.75609756097,
            48545.36585365854,
            49736.9756097561,
            50928.58536585365,
            52120.195121951205,
            53311.804878048766,
            54503.41463414634,
            55695.0243902439,
            56883.317073170736,
            58078.243902439026,
            59269.85365853659,
            60461.46341463415,
            61653.0731707317,
            62844.68292682927,
            64036.29268292684,
            65227.9024390244,
            66419.51219512196,
            67611.12195121952,
            68802.73170731709,
            69994.34146341465,
            71185.95121951221,
            72377.56097560977,
            73569.17073170732,
            74760.78048780488,
            75952.39024390244,
            77144.0,
            78335.60975609756,
            79527.21951219512,
            80718.82926829268,
            81910.43902439025,
            83102.0487804878,
            84293.65853658537,
            85485.26829268293,
            86676.87804878049,
            87868.48780487805,
            89060.09756097561,
            90251.70731707317,
            91441.65853658537,
            92634.9268292683,
            93826.53658536586,
            95018.14634146342,
            96209.75609756098,
            97401.36585365854,
            98592.9756097561,
            99784.58536585367,
            100976.19512195123,
            102167.80487804877,
            103359.41463414633,
            104551.0243902439,
            105742.63414634146,
            106934.24390243902,
            108125.85365853658,
            109317.46341463414,
            110509.0731707317,
            111700.68292682926,
            112892.29268292683,
            114083.90243902439,
            115275.51219512195,
            116467.12195121951,
            117658.73170731707,
            118850.34146341463,
            120041.9512195122,
            121233.56097560977,
            122425.17073170733,
            123616.78048780489,
            124808.39024390245,
            126000.0,
        ]
        waterLevels = [
            0.50,
            0.50,
            0.51,
            0.52,
            0.54,
            0.56,
            0.59,
            0.62,
            0.66,
            0.70,
            0.75,
            0.80,
            0.85,
            0.91,
            0.97,
            1.04,
            1.10,
            1.17,
            1.25,
            1.32,
            1.40,
            1.48,
            1.56,
            1.64,
            1.72,
            1.80,
            1.88,
            1.96,
            2.04,
            2.12,
            2.20,
            2.28,
            2.35,
            2.43,
            2.50,
            2.56,
            2.63,
            2.69,
            2.75,
            2.80,
            2.85,
            2.90,
            2.94,
            2.98,
            3.01,
            3.04,
            3.06,
            3.08,
            3.09,
            3.10,
            3.10,
            3.10,
            3.09,
            3.08,
            3.06,
            3.04,
            3.01,
            2.98,
            2.94,
            2.90,
            2.85,
            2.80,
            2.75,
            2.69,
            2.63,
            2.56,
            2.50,
            2.43,
            2.35,
            2.28,
            2.20,
            2.12,
            2.04,
            1.96,
            1.88,
            1.80,
            1.72,
            1.64,
            1.56,
            1.48,
            1.40,
            1.32,
            1.25,
            1.17,
            1.10,
            1.04,
            0.97,
            0.91,
            0.85,
            0.80,
            0.75,
            0.70,
            0.66,
            0.62,
            0.59,
            0.56,
            0.54,
            0.52,
            0.51,
            0.50,
        ]
        waveHeights = [
            0.80,
            0.80,
            0.80,
            0.81,
            0.82,
            0.82,
            0.84,
            0.85,
            0.86,
            0.88,
            0.90,
            0.91,
            0.94,
            0.96,
            0.98,
            1.01,
            1.03,
            1.06,
            1.09,
            1.12,
            1.15,
            1.18,
            1.21,
            1.24,
            1.27,
            1.30,
            1.33,
            1.36,
            1.39,
            1.42,
            1.45,
            1.48,
            1.51,
            1.54,
            1.57,
            1.59,
            1.62,
            1.64,
            1.66,
            1.69,
            1.70,
            1.72,
            1.74,
            1.75,
            1.76,
            1.78,
            1.78,
            1.79,
            1.80,
            1.80,
            1.80,
            1.80,
            1.80,
            1.79,
            1.78,
            1.78,
            1.76,
            1.75,
            1.74,
            1.72,
            1.70,
            1.69,
            1.66,
            1.64,
            1.62,
            1.59,
            1.57,
            1.54,
            1.51,
            1.48,
            1.45,
            1.42,
            1.39,
            1.36,
            1.33,
            1.30,
            1.27,
            1.24,
            1.21,
            1.18,
            1.15,
            1.12,
            1.09,
            1.06,
            1.03,
            1.01,
            0.98,
            0.96,
            0.94,
            0.91,
            0.90,
            0.88,
            0.86,
            0.85,
            0.84,
            0.82,
            0.82,
            0.81,
            0.80,
            0.80,
        ]
        wavePeriods = [
            7,
            7.06,
            7.12,
            7.18,
            7.24,
            7.3,
            7.36,
            7.42,
            7.48,
            7.54,
            7.6,
            7.66,
            7.72,
            7.78,
            7.84,
            7.9,
            7.96,
            8.02,
            8.08,
            8.14,
            8.2,
            8.26,
            8.32,
            8.38,
            8.44,
            8.5,
            8.56,
            8.62,
            8.68,
            8.74,
            8.8,
            8.86,
            8.92,
            8.98,
            9.04,
            9.1,
            9.16,
            9.22,
            9.28,
            9.34,
            9.4,
            9.46,
            9.52,
            9.58,
            9.64,
            9.7,
            9.76,
            9.82,
            9.88,
            9.94,
            10,
            10.06,
            10.12,
            10.18,
            10.24,
            10.3,
            10.36,
            10.42,
            10.48,
            10.54,
            10.6,
            10.66,
            10.72,
            10.78,
            10.84,
            10.9,
            10.96,
            11.02,
            11.08,
            11.14,
            11.2,
            11.26,
            11.32,
            11.38,
            11.44,
            11.5,
            11.56,
            11.62,
            11.68,
            11.74,
            11.8,
            11.86,
            11.92,
            11.98,
            12.04,
            12.1,
            12.16,
            12.22,
            12.28,
            12.34,
            12.4,
            12.46,
            12.52,
            12.58,
            12.64,
            12.7,
            12.76,
            12.82,
            12.88,
            12.94,
        ]
        waveAngles = [
            -20,
            -19.5,
            -19,
            -18.5,
            -18,
            -17.5,
            -17,
            -16.5,
            -16,
            -15.5,
            -15,
            -14.5,
            -14,
            -13.5,
            -13,
            -12.5,
            -12,
            -11.5,
            -11,
            -10.5,
            -10,
            -9.5,
            -9,
            -8.5,
            -8,
            -7.5,
            -7,
            -6.5,
            -6,
            -5.5,
            -5,
            -4.5,
            -4,
            -3.5,
            -3,
            -2.5,
            -2,
            -1.5,
            -1,
            -0.5,
            0,
            0.5,
            1,
            1.5,
            2,
            2.5,
            3,
            3.5,
            4,
            4.5,
            5,
            5.5,
            6,
            6.5,
            7,
            7.5,
            8,
            8.5,
            9,
            9.5,
            10,
            10.5,
            11,
            11.5,
            12,
            12.5,
            13,
            13.5,
            14,
            14.5,
            15,
            15.5,
            16,
            16.5,
            17,
            17.5,
            18,
            18.5,
            19,
            19.5,
            20,
            20.5,
            21,
            21.5,
            22,
            22.5,
            23,
            23.5,
            24,
            24.5,
            25,
            25.5,
            26,
            26.5,
            27,
            27.5,
            28,
            28.5,
            29,
            29.5,
        ]
        return HydraulicInput(timeSteps, waterLevels, waveHeights, wavePeriods, waveAngles)

    @staticmethod
    def GetDikeProfile() -> DikeSchematization:
        schematization = DikeSchematization()
        schematization.XPositions = [0.0, 25.0, 35.0, 41.0, 45, 50, 60, 70]
        schematization.ZPositions = [-3, 0.0, 1.5, 1.7, 3.0, 3.1, 0, -1]
        schematization.Roughnesses = [1, 1, 0.75, 0.5, 0.8, 0.8, 0.8]
        schematization.OuterToe = 25.0
        schematization.OuterCrest = 45.0
        schematization.CrestOuterBerm = 35.0
        schematization.NotchOuterBerm = 41.0
        schematization.InnerCrest = 50.0
        schematization.InnerToe = 60.0
        return schematization

    @staticmethod
    def GetOutputLocations():
        return [
            NordicStoneOutputLocation(25.01, 0, 0.28, 2.45),
            NordicStoneOutputLocation(25.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(26.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(26.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(27.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(27.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(28.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(28.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(29.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(29.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(30.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(30.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(31.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(31.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(32.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(32.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(33.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(33.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(34.0, 0, 0.28, 2.45),
            NordicStoneOutputLocation(34.5, 0, 0.28, 2.45),
            NordicStoneOutputLocation(34.9, 0, 0.28, 2.45),
            AsphaltOutputLocation(35.1, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(35.5, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(36.0, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(36.5, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(37.0, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(37.5, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(38.0, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(38.5, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(39.0, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(39.5, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(40.0, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(40.5, 0.0, 0.9, 64.0, 0.146, 5712.0),
            AsphaltOutputLocation(40.9, 0.0, 0.9, 64.0, 0.146, 5712.0),
            GrassWaveImpactOutputLocation(41.1, 0.0, TopLayerType.GrassClosedSod),
            GrassWaveImpactOutputLocation(41.5, 0.0, TopLayerType.GrassClosedSod),
            GrassWaveImpactOutputLocation(42.0, 0.0, TopLayerType.GrassClosedSod),
            GrassWaveImpactOutputLocation(42.5, 0.0, TopLayerType.GrassClosedSod),
            GrassWaveImpactOutputLocation(43.0, 0.0, TopLayerType.GrassClosedSod),
            GrassWaveImpactOutputLocation(43.5, 0.0, TopLayerType.GrassClosedSod),
            GrassWaveImpactOutputLocation(44.0, 0.0, TopLayerType.GrassOpenSod),
            GrassWaveImpactOutputLocation(44.5, 0.0, TopLayerType.GrassOpenSod),
            GrassWaveImpactOutputLocation(44.99, 0.0, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(45.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(45.5, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(46.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(46.5, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(47.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(47.5, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(48.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(48.5, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(49.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(49.5, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(49.99, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(45.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(52.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(54.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(56.0, 0.02, TopLayerType.GrassClosedSod),
            GrassOvertoppingOutputLocation(58.0, 0.02, TopLayerType.GrassClosedSod),
        ]

    @staticmethod
    def GetCalculationSettings():
        grasCoverTopLayer1 = GrassCoverWaveImpactTopLayerSettings(TopLayerType.GrassClosedSod)
        grasCoverTopLayer1.StanceTimeLineA = 1
        grasCoverTopLayer1.StanceTimeLineB = -0.000009722
        grasCoverTopLayer1.StanceTimeLineC = 0.25
        grasCoverTopLayer2 = GrassCoverWaveImpactTopLayerSettings(TopLayerType.GrassOpenSod)
        grasCoverTopLayer2.StanceTimeLineA = 0.8
        grasCoverTopLayer2.StanceTimeLineB = -0.00001944
        grasCoverTopLayer2.StanceTimeLineC = 0.25

        return [
            AsphalCalculationSettings([AsphaltTopLayerSettings()]),
            NaturalStoneCalculationSettings(),
            GrassWaveImpactCalculationSettings([grasCoverTopLayer1, grasCoverTopLayer2]),
            GrassWaveOvertoppingCalculationSettings(
                [GrasCoverOvertoppingTopLayerSettings(TopLayerType.GrassClosedSod)]
            ),
        ]


input = TestCalculationInputFactory.GetCalculationInput()
dikernel = Dikernel(input)

print("Starting validation")
validationresult = dikernel.validate()
print("   Validation was: " + "succesfull" if validationresult else "unsuccessfull")

print("Starting calculation")
runresult = dikernel.run()
print("   Run was: " + "succesfull" if runresult else "unsuccessfull")

output = dikernel.Output
print("   number of output locations: " + str(len(output)))
print("   Number of failed locations: " + str(len([l for l in output if l.Failed])))
stones = [o for o in output if o.CalculationType == CalculationMethod.NaturalStone]
print("   Number of natural stone output locations: " + str(len(stones)))
for stone in stones:
    print("      X: " + str(stone.XPosition) + ", Damage lvel = " + str(stone.DamageDevelopment[-1]))

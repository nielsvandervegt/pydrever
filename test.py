import numpy as np

from pydrever.data import DikeSchematization

x_positions = [0.0, 18.0, 20.0, 26.0]
z_positions = [-3.0, 3.0, 3.0, 0.0]
roughnesses = [1, 1, 0.8, 0.8]
dike_schematization = DikeSchematization(
    dike_orientation=90.0, 
    x_positions=x_positions, 
    z_positions=z_positions, 
    roughnesses=roughnesses, 
    x_outer_toe=0.0, 
    x_outer_crest=18.0,
    x_inner_crest=20.0,
    x_inner_toe=26.0,
)
# dike_schematization.foreshore_min_z = -5
# dike_schematization.foreshore_slope = 1/100

from pydrever.data import HydrodynamicConditions

time_steps = [0.0, 25000.0, 50000.0, 75000.0, 100000.0, 126000.0]
water_levels = [1.2, 1.9, 2.8, 2.7, 2.0]
wave_heights = [0.5, 0.9, 1.2, 1.1, 0.8]
wave_periods = [6.0, 6.0, 6.0, 6.0, 6.0]
wave_directions = [60.0, 70.0, 80.0, 90.0, 100.0]

hydrodynamic_conditions = HydrodynamicConditions(
    time_steps=time_steps, 
    water_levels=water_levels, 
    wave_heights=wave_heights, 
    wave_periods=wave_periods, 
    wave_directions=wave_directions
)

from pydrever.data import (
    DikernelInput,
    TopLayerType,
    GrassWaveImpactLayerSpecification,
    AsphaltLayerSpecification,
    NordicStoneLayerSpecification,
)

input = DikernelInput(dike_schematization=dike_schematization, hydrodynamic_input=hydrodynamic_conditions)
input.start_time = 0.0
output_time_steps = np.arange(0.0, 126000, 1000)
output_time_steps = np.union1d(time_steps, output_time_steps)
input.output_time_steps = output_time_steps


input.add_output_location(
        x_location=16.0,
        top_layer_specification=NordicStoneLayerSpecification(
            top_layer_thickness=0.35,
            relative_density=1.65)
            )

input.add_output_location(
        x_location=16.0,
        top_layer_specification=AsphaltLayerSpecification(
            top_layer_type = TopLayerType.Asphalt,
            flexural_strength=0.9, 
            soil_elasticity=64.0, 
            upper_layer_thickness=0.146, 
            upper_layer_elasticity_modulus=5712.0,
            stiffness_ratio_nu = 0.35,
            fatigue_asphalt_alpha = 0.5,
            fatigue_asphalt_beta = 5.4)
)

input.add_output_location(
        x_location=16.0, 
        top_layer_specification=GrassWaveImpactLayerSpecification(
            top_layer_type=TopLayerType.GrassClosedSod)
            )

input.add_output_location(
        x_location=16.0, 
        top_layer_specification=GrassWaveImpactLayerSpecification(
            top_layer_type=TopLayerType.GrassOpenSod)
            )

from pydrever.calculation import Dikernel

dikernel = Dikernel(input)
run_result = dikernel.run()

print("Run was: " + "succesfull" if run_result else "unsuccessfull")
if not run_result:
    for message in dikernel.errors:
        print("   %s" % message)
    quit()

output = dikernel.output

print(1)
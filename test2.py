import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from pydrever.data import DikeSchematization

x_positions = [0.0, 25.0, 35.0, 41.0, 45, 50, 60, 70]
z_positions = [-3, 0.0, 1.5, 1.7, 3.0, 3.1, 0, -1]
roughnesses = [1, 1, 1, 0.75, 0.5, 0.8, 0.8, 0.8]
schematization = DikeSchematization(
    dike_orientation=0.0, 
    x_positions=x_positions, 
    z_positions=z_positions, 
    roughnesses=roughnesses, 
    x_outer_toe=25.0, 
    x_outer_crest=45.0
)
schematization.x_crest_outer_berm = 35.0
schematization.x_notch_outer_berm = 41.0
schematization.x_inner_crest = 50.0
schematization.x_inner_toe = 60.0

from pydrever.data import HydrodynamicConditions

hydrodynamic_conditions = HydrodynamicConditions(
    time_steps=[0, 3600], 
    water_levels=[1.0], 
    wave_heights=[2.0], 
    wave_periods=[7.0], 
    wave_directions=[0.0]
)

from pydrever.data import (
    RevetmentZoneSpecification,
    HorizontalRevetmentZoneDefinition,
    TopLayerType,
    GrassWaveImpactLayerSpecification,
    GrassWaveRunupBattjesGroenendijkLayerSpecification,
    GrassWaveRunupRayleighLayerSpecification,
    GrassWaveOvertoppingRayleighAnalyticalLayerSpecification,
    GrassWaveOvertoppingRayleighDiscreteLayerSpecification,
    AsphaltLayerSpecification,
    NordicStoneLayerSpecification,
)

# asphalt_layer = AsphaltLayerSpecification(
#     top_layer_type = TopLayerType.Asphalt,
#     flexural_strength=0.9, 
#     soil_elasticity=64.0, 
#     upper_layer_thickness=0.146, 
#     upper_layer_elasticity_modulus=5712.0,
#     stiffness_ratio_nu = 0.35,
#     fatigue_asphalt_alpha = 0.5,
#     fatigue_asphalt_beta = 5.4,
# )
# nordic_stone_layer = NordicStoneLayerSpecification(
#     top_layer_thickness=0.28, 
#     relative_density=2.45)
grass_wave_impact_layer = GrassWaveImpactLayerSpecification(
    top_layer_type=TopLayerType.GrassOpenSod)
# grass_wave_runup_layer_bg = GrassWaveRunupBattjesGroenendijkLayerSpecification(
#     outer_slope=0.3, 
#     top_layer_type=TopLayerType.GrassClosedSod)
grass_wave_runup_layer = GrassWaveRunupRayleighLayerSpecification(
    outer_slope=0.3, 
    top_layer_type=TopLayerType.GrassClosedSod)
grass_overtopping_layer_closed = GrassWaveOvertoppingRayleighAnalyticalLayerSpecification(top_layer_type=TopLayerType.GrassClosedSod)
grass_overtopping_layer_open = GrassWaveOvertoppingRayleighDiscreteLayerSpecification(top_layer_type=TopLayerType.GrassOpenSod)

revetment_zones = [
    # RevetmentZoneSpecification(
    #     zone_definition=HorizontalRevetmentZoneDefinition(x_min=25.01, x_max=34.9, dx_max=0.5), 
    #     top_layer_specification=nordic_stone_layer),
    # RevetmentZoneSpecification(
    #     zone_definition=HorizontalRevetmentZoneDefinition(x_min=35.1, x_max=40.9, dx_max=0.5), 
    #     top_layer_specification=asphalt_layer),
    RevetmentZoneSpecification(
        zone_definition=HorizontalRevetmentZoneDefinition(x_min=41.1, x_max=44.9, dx_max=0.5), 
        top_layer_specification=grass_wave_impact_layer),
    RevetmentZoneSpecification(
        zone_definition=HorizontalRevetmentZoneDefinition(x_min=41.1, x_max=44.9, dx_max=0.5), 
        top_layer_specification=grass_wave_runup_layer),
    # RevetmentZoneSpecification(
    #     zone_definition=HorizontalRevetmentZoneDefinition(x_min=41.1, x_max=44.9, dx_max=0.5), 
    #     top_layer_specification=grass_wave_runup_layer_bg),
    RevetmentZoneSpecification(
        zone_definition=HorizontalRevetmentZoneDefinition(x_min=45.0, x_max=49.99, dx_max=0.5), 
        top_layer_specification=grass_overtopping_layer_closed),
    RevetmentZoneSpecification(
        zone_definition=HorizontalRevetmentZoneDefinition(x_min=52.0, x_max=58, dx_max=2.0), 
        top_layer_specification=grass_overtopping_layer_open),
]

from pydrever.data import DikernelInput

input = DikernelInput(dike_schematization=schematization, hydrodynamic_input=hydrodynamic_conditions)
input.output_revetment_zones = revetment_zones
# input.settings = calculation_settings

from pydrever.calculation import Dikernel

dikernel = Dikernel(input)

run_result = dikernel.run()

print("Run was: " + "succesfull" if run_result else "unsuccessfull")
if not run_result:
    for message in dikernel.errors:
        print("   %s" % message)
    quit()

dikernel.output

print(1)
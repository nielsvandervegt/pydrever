"""
 Copyright (C) Stichting Deltares 2023-2024. All rights reserved.
 
 This file is part of the dikernel-python toolbox.
 
 This program is free software; you can redistribute it and/or modify it under the terms of
 the GNU Lesser General Public License as published by the Free Software Foundation; either
 version 3 of the License, or (at your option) any later version.
 
 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 See the GNU Lesser General Public License for more details.
 
 You should have received a copy of the GNU Lesser General Public License along with this
 program; if not, see <https://www.gnu.org/licenses/>.
 
 All names, logos, and references to "Deltares" are registered trademarks of Stichting
 Deltares and remain full property of Stichting Deltares at all times. All rights reserved.
"""

import copy, numpy
from pydrever.data import (
    DikernelInput,
    HydrodynamicConditions,
    OutputLocationSpecification,
)
import pydrever.calculation._hydrodynamicsinterpolation as interpolation


def get_run_input(input: DikernelInput) -> DikernelInput:
    """
    Returns manipulated input that incorporates the desired output time steps and start time of the calculation in the hydrodynamic input.

    Args:
        input (DikernelInput): The input object to copy all input from.

    Returns:
        DikernelInput: A manipulated input object that can be used to calculate.
    """
    time_steps = input.hydrodynamic_input.time_steps
    run_time_steps = get_run_time_steps(input)
    run_hydrodynamics = HydrodynamicConditions(
        time_steps=run_time_steps,
        water_levels=interpolation.interpolate_time_series(
            time_steps, input.hydrodynamic_input.water_levels, run_time_steps
        ),
        wave_heights=interpolation.interpolate_time_series(
            time_steps, input.hydrodynamic_input.wave_heights, run_time_steps
        ),
        wave_periods=interpolation.interpolate_time_series(
            time_steps, input.hydrodynamic_input.wave_periods, run_time_steps
        ),
        wave_directions=interpolation.interpolate_time_series(
            time_steps,
            input.hydrodynamic_input.wave_directions,
            run_time_steps,
        ),
    )
    run_input = DikernelInput(run_hydrodynamics, input.dike_schematization)
    run_input.output_locations = copy.deepcopy(input.output_locations)
    run_input.output_revetment_zones = copy.deepcopy(input.output_revetment_zones)
    run_input.settings = copy.deepcopy(input.settings)
    return run_input


def get_run_time_steps(input: DikernelInput) -> list[float]:
    """
    This method combines all time steps and required output time steps to for
    a list of time steps that needs to be used during calculation.

    It combines the specified time steps for hydrodynamic conditions and the
    specified output time steps and then takes all time steps between the
    optional start and stop times (including the start and stop times).

    Args:
        input (DikernelInput): The input object to subtract the run time steps from.

    Returns:
        list[float]: A list with the time steps needed to run calculations.
    """
    run_time_steps = input.hydrodynamic_input.time_steps
    if input.output_time_steps is not None:
        run_time_steps = numpy.union1d(run_time_steps, input.output_time_steps).tolist()

    if input.start_time is not None:
        run_time_steps = list(
            time_step
            for time_step in numpy.union1d(run_time_steps, [input.start_time])
            if time_step >= input.start_time
        )

    if input.stop_time is not None:
        run_time_steps = list(
            time_step
            for time_step in numpy.union1d(run_time_steps, [input.stop_time])
            if time_step <= input.start_time
        )
    return run_time_steps


def get_output_locations_from_input(
    input: DikernelInput,
) -> list[OutputLocationSpecification]:
    """
    This method gathers all desired calculation locations from both the specified zones as well as the manually specified locations.

    Args:
        input (DikernelInput): The input object to retrieve the output locations from

    Returns:
        list[OutputLocationSpecification]: A list of output locations specified in the input object and generated by the specified revetment zones.
    """
    locations = input.output_locations if input.output_locations is not None else []
    if input.output_revetment_zones is not None:
        for zone in input.output_revetment_zones:
            locations = locations + zone.get_output_locations(input.dike_schematization)

    return sorted(locations, key=lambda l: l.x_position)

from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height,pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction


def test_water_column_height():
    """
    Tests outputs of water_column_height with known values
    """
    
    assert water_column_height(0,0) == 0
    assert water_column_height(0,10) == approx(7.5)
    assert water_column_height(25,0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9)
    
def test_preaseure_gain_from_water_height():
    """
    Tests outputs of gain_from_water_height with known values
    """
    
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)
    
def test_preassure_loss_from_pipe():
    """
    Tests outputs of preassure_loss_from_pipe with known values
    """    
    #loss = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)
    
def test_pressure_loss_from_fittings():
    """
    Tests outputs of pressure_loss_from_fittings with known values
    """
    
    #pressure_loss_from_fittings(fluid_velocity,quantity_fittings)

    
    assert pressure_loss_from_fittings(0,3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65,0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65,2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75,2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75,5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    """
    Tests outputs of reynolds_number with known values
    """
    assert reynolds_number(0.048692, 0) == approx(0,abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069,abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922,abs=1)
    assert reynolds_number(0.28687, 1.65) == approx(471729,abs=1)
    assert reynolds_number(0.28687, 1.75) == approx(500318,abs=1)
    
def test_pressure_loss_from_pipe_reduction():
    """
    Tests outputs of pressure_loss_from_pipe_reduction with known values
    """
    
    assert pressure_loss_from_pipe_reduction(0.28687 , 0, 1, 0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687 , 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687 , 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

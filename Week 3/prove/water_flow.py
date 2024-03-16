
def water_column_height(tower_height, tank_height):
    """ 
    Calculates and returns the height of a column of water from a tower height and a tank wall height using the fillowing formula

    height_of_colunm = height_of_tower + (3 * wall_height_of_tank (on top of tower)) / 4 
    
    """
    height_of_colunm = float(tower_height + (3 * tank_height) / 4)
    return height_of_colunm

def pressure_gain_from_water_height(height):
    """
    calculates and returns the pressure caused by earth's gravity pulling on the water in the tank.
    
    preasure in kilopascals = (998.2 kg/m^3 * 9.80665 m/s^2 * height) / 1000 
    """
    preasure_in_kilopascals = float((998.2 * 9.80665 * height) / 1000)
    
    return preasure_in_kilopascals

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    Calculates and returns the water preassure lost because of friction between walls of a pipe and the water.
    
    preasure_lost = (-1 * friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)
   
    
    """
    preasure_lost = (-1 * friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return preasure_lost

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculates the loss because of fitting angles such as 45 and 90 degree bends in pipe. 
    
    """
    pressure_loss = (-0.04 * 998.2 * fluid_velocity ** 2 * quantity_fittings) / 2000
    
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates and returns the Reynolds number for a pipe with water flowing through it.
    """
    
    reynolds_number_result = (998.2 * hydraulic_diameter * fluid_velocity ) / 0.0010016 
    
    return reynolds_number_result

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter.
    """
    konstant = (0.1 + 50/reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    
    lost_pressure = (-konstant * 998.2 * (fluid_velocity ** 2)) / 2000
    
    return lost_pressure
    
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()

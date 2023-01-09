import mdtraj as md

# Load the topology and coordinates for the system
topology = md.load("system.pdb").topology
coordinates = md.load("system.dcd", top=topology).xyz

# Set up the simulation parameters
temperature = 300.0  # simulation temperature in Kelvin
friction = 1.0 / ps  # friction coefficient in ps^-1
timestep = 0.002  # timestep in ps

# Set up the integrator
integrator = md.integrate.LangevinIntegrator(temperature, friction, timestep)

# Set up the simulation
simulation = md.Simulation(topology, coordinates, integrator)

# Run the simulation for 1000 steps
simulation.run(1000)

# Save the final coordinates
coordinates = simulation.context.getState(getPositions=True).getPositions()
md.save("final.dcd", simulation.topology, coordinates)

import pybel

# Load the ligand and receptor molecules
ligand = pybel.readfile("mol2", "ligand.mol2").next()
receptor = pybel.readfile("pdb", "receptor.pdb").next()

# Set up the docking input
docking_input = pybel.Docking()
docking_input.ligand = ligand
docking_input.receptor = receptor

# Run the docking simulation
result = docking_input.run()

# Print the docking energy
print(result.energy)

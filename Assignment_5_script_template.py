#################### Task 1 ############################
    # Request for reservoir dimensions and discretization parameters

Lx = float(input("Enter the length of the reservoir in the x-direction: "))
Ly = float(input("Enter the length of the reservoir in the y-direction: "))
Lz = float(input("Enter the length of the reservoir in the z-direction: "))

nx = int(input("Enter the number of gridblocks in the x-direction: "))
ny = int(input("Enter the number of gridblocks in the y-direction: "))
nz = int(input("Enter the number of gridblocks in the z-direction: "))


#################### Task 2 ############################
    # Request for the cut-off value
cut_off = float(input("Enter the permeability cut-off value: "))


#################### Task 3 ############################
    # Initialize counters

n_active = 0
n_inactive = 0


#################### Task 4 ############################
    # Loop through all blocks (nested loop)
for k in range(1, nz+1):
    n_active_layer = 0
    for j in range(1, ny+1):
        for i in range(1, nx+1):
            # Request for the permeability value
            permeability = float(input(f"Enter permeability value for gridblock ({i}, {j}, {k}): "))

            # Classify the gridblock as intended
            if permeability >= cut_off:
                n_active += 1 # Increment n_active counter
                n_active_layer += 1
            else:
                n_inactive += 1 # Increment n_active counter

    # Print layer count
    print(f"Layer {k} has {n_active_layer} active gridblocks")


#################### Task 5 ############################
    # Print overall counts
# print 'active'
print(f"The entire reservoir has {n_active} active gridblocks")
#print 'inactive'
print(f"The entire reservoir has {n_inactive} inactive gridblocks")

print(f"The percentage of active gridblocks is {(n_active / (nx * ny * nz)) * 100:.2f}%")

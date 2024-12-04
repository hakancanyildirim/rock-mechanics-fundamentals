import matplotlib.pyplot as plt

def shear_strength_vs_normal_stress(sigma1, tau1, sigma2, tau2):
    
    # plotting the points 
    plt.plot(sigma1, tau1, label="Peak Shear Strength")
    plt.plot(sigma2, tau2, label="Residual Shear Strength")

    # naming the x axis
    plt.xlabel('Normal Stress σ (MPa)')
    # naming the y axis
    plt.ylabel('Shear Strength τ (MPa)')

    # giving a title to my graph
    plt.title('Normal Stress vs Shear Stress')

    plt.legend()
    # function to show the plot
    plt.show()

#direct_shear_graph([1,2,3], [2,4,1], [2,4,1], [1,2,3])

def normal_stress_vs_normal_displacement(stresses, displacements):
    plt.plot(stresses, displacements)
    plt.xlabel('Normal Stress σ (MPa)')
    plt.ylabel('Normal Displacement')
    plt.title('Normal Stress σ vs Normal Displacement')
    plt.show()

def shear_stress_vs_shear_displacement(stresses, displacements):
    plt.plot(displacements, stresses)
    plt.xlabel('Shear Displacement')
    plt.ylabel('Shear Stress τ (MPa)')
    plt.title('Shear Stress τ vs Shear Displacement')
    plt.show()
    
import matplotlib.pyplot as plt

def shear_strength_vs_normal_stress(sigma1, tau1, sigma2, tau2):
    plt.plot(sigma1, tau1, label="Peak Shear Strength")
    plt.plot(sigma2, tau2, label="Residual Shear Strength")
    plt.xlabel('Normal Stress σ (MPa)')
    plt.ylabel('Shear Strength τ (MPa)')
    plt.title('Normal Stress vs Shear Stress')
    plt.legend()
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

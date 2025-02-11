import numpy as np
import pandas as pd

def dh_transform(alpha, a, d, theta):
    alpha_rad = np.radians(alpha)
    theta_rad = np.radians(theta)
    return np.array([
        [np.cos(theta_rad), -np.sin(theta_rad)*np.cos(alpha_rad),  np.sin(theta_rad)*np.sin(alpha_rad), a * np.cos(theta_rad)],
        [np.sin(theta_rad),  np.cos(theta_rad)*np.cos(alpha_rad), -np.cos(theta_rad)*np.sin(alpha_rad), a * np.sin(theta_rad)],
        [0,                 np.sin(alpha_rad),                   np.cos(alpha_rad),                  d],
        [0,                 0,                                   0,                                  1]
    ])

dh_params = [
    [-90, 0,      0, 0],
    [180, 260,    0, 0],
    [0,   290.688,0, 0],
    [90,  0,      0, 0],
    [0,   0,      78, 0]
]

def compute_fk(joint_angles):
    T_final = np.eye(4)
    for i in range(len(joint_angles)):
        theta = joint_angles[i] + dh_params[i][3]
        T_final = T_final @ dh_transform(dh_params[i][0], dh_params[i][1], dh_params[i][2], theta)
    return T_final[:3, 3]

test_angles = [
    [0,   -45, -90, 135, 0],
    [30,  -90, -135,135, 0],
    [-45, -30, -45, 90,  0],
    [-25, -70, -70, 110, 0]
]

results = [compute_fk(angles) for angles in test_angles]

df_results = pd.DataFrame(results, 
                          columns=["X (mm)", "Y (mm)", "Z (mm)"],
                          index=["Test 1", "Test 2", "Test 3", "Test 4 (Validation)"])

df_results = df_results.round(3)

print(df_results)

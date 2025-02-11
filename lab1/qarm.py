import numpy as np

def homogeneous_transform(R, t):
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T

# Parameters [mm]
p_C_A = np.array([515, 90, 990])
p_S_C = np.array([0, 0, -4.3])

p_D_B = np.array([480, 10, 990])
p_Q_D = np.array([0, 0, -4.3])

# Transformation Matrices
T_S_C = homogeneous_transform(np.eye(3), p_S_C)

print("T_S_C\n", T_S_C)

R_C_A = np.array([
    [0,  1,  0],
    [1,  0,  0],
    [0,  0, -1]
])
T_C_A = homogeneous_transform(R_C_A, p_C_A)

print("T_C_A\n", T_C_A)

T_Q_D = homogeneous_transform(np.eye(3), p_Q_D)

print("T_Q_D\n", T_Q_D)

R_D_B = np.array([
    [ 0, -1,  0],
    [-1,  0,  0],
    [ 0,  0, -1]
])
T_D_B = homogeneous_transform(R_D_B, p_D_B)

print("T_D_B\n", T_D_B)

def transform_point(T, p):
    p_hom = np.append(p, 1)
    p_transformed = T @ p_hom
    return p_transformed[:3]

# For Robot A
p_O_S = np.array([100, 200, 50])
p_O_C = transform_point(T_S_C, p_O_S)
p_O_A = transform_point(T_C_A, p_O_C)

# For Robot B
p_O_Q = np.array([150, 250, 60])
p_O_D = transform_point(T_Q_D, p_O_Q)
p_O_B = transform_point(T_D_B, p_O_D)


print("\nRobot A")
print("Object position in Sensor frame (S):", p_O_S)
print("Object position in Camera frame (C):", p_O_C)
print("Object position in Robot A frame (A):", p_O_A)

print("\nRobot B")
print("Object position in Sensor frame (Q):", p_O_Q)
print("Object position in Camera frame (D):", p_O_D)
print("Object position in Robot B frame (B):", p_O_B)

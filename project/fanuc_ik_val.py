import numpy as np

def inverse_kinematics(xe, ye, ze, a):
    a = np.radians(a)
    l1 = 260
    l2 = np.sqrt(290**2 + 20**2)
    l3 = 78

    theta1 = np.arctan2(ye, xe)
    
    z = ze + l3
    c = np.sqrt(xe**2 + ye**2 + z**2)
    alpha = np.arccos((l1**2 + l2**2 - c**2) / (2 * l1 * l2))
    beta = np.arccos((l1**2 + c**2 - l2**2) / (2 * l1 * c))
    gamma = np.arcsin(z / c)
    
    theta2 = -(beta + gamma)
    
    theta3 =  alpha - np.pi
    theta4 =  np.pi/2 - (alpha - (np.pi/2 - (beta + gamma)))
    
    theta5 = np.pi + theta1 - a
    
    return np.degrees(theta1), np.degrees(theta2), np.degrees(theta3), np.degrees(theta4), np.degrees(theta5)

# Test cases
test_cases = [
    (435, -105, -80, 45),
    (435, -105, -120, 45),
    (430, 100, -80, 90),
    (430, 100, -120, 90)
]

print("Testing Fanuc Inverse Kinematics")
for i, (xe, ye, ze, alpha) in enumerate(test_cases):
    angles = inverse_kinematics(xe, ye, ze, alpha)
    print(f"Test case {i+1}: (xe, ye, ze, alpha) = ({xe}, {ye}, {ze}, {alpha})")
    print(f"Computed joint angles: {angles}\n")
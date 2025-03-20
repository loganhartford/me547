clear;
clc;

% Input

xe = 540;
ye = -50;
ze = 175;


% INitialize robot params

d_arm = 360;
d_base = 140;
l_eff = sqrt(350^2 + 50^2);


%Theta 1
t11 = atan2(ye,xe);

t12 = t11 + pi;


% Theta 3. Had to make second value for calc. of Theta 2 for some reason
% with x and y flipped
A_val = ((ze - d_base)^2 + xe^2 + ye^2 - d_arm^2 - l_eff^2)/(2*d_arm*l_eff);

t31 = atan2(A_val,sqrt(1 - A_val^2));
t31i = atan2(sqrt(1 - A_val^2),A_val);


t32 = atan2(-A_val,sqrt(1 - A_val^2));
t32i = atan2(-sqrt(1 - A_val^2),A_val);


% Theta 2 last, as it depends on Theta 3
t21 = atan2(ze - d_base , sqrt(xe^2 + ye^2)) + atan2(d_arm*sin(t31) , d_arm*cos(t31)+l_eff);

t22 = -atan2(ze - d_base , sqrt(xe^2 + ye^2)) + atan2(d_arm*sin(t32i) , d_arm*cos(t32i)+l_eff);


 t = [t11 t12 t21 t22 t31 t32];
 disp(t);








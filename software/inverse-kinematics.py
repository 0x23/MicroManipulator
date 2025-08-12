import numpy as np
# I've never worked with closed-chain robots so this is going to be a bit ugly notation-wise, but here is my shot at this.
 
# We approximate flex points as ball joints
# L: approximate length of arm between ball joints (meters)

# Consider a 3DoF [x,y,z] translation (relative to the origin) of the end-effector with no rotational component: [x1,y1,z1]
# We wish to find the three prismatic joint deltas [p1, p2, p3] to achieve this position.

# the positional delta of each ball joint (closest to the end-effector) is trivially equal to [x1,y1,z1]
# The ball joint at the other end of the linkage is coincident with its corresponding prismatic joint.

# Let's consider the z-axis first. Here we use a coordinate system where the origin is at the position of the ball joint on the z-linkage closest to the end-effector.
# The z-linkage is a linkage with length L. Initially (at the robot's home-position), it is between the points [0,0,-L] and [0,0,0].
# Generally, the linkage is between the points [0,0,-L+p3] and [x1,y1,z1]
# The length of this linkage is given by:
 # lenZ = sqrt((x1-0)^2 + (y1-0)^2 + (z1+L-p3)^2) = L
 # Solving for p3:
 # (z1 +L -p3)^2  = L^2 -x1^2 -y1^2
 # z1 +L -p3 = +-sqrt(L^2 -x1^2 -y1^2)
 # p3 = z1 +L +-sqrt(L^2 -x1^2 -y1^2)
# Asserting that p3 and z1 are small, and L is not small, the solution must contain the negative root 
 # p3 = z1 +L -sqrt(L^2 -x1^2 -y1^2)

# By symmetry:

def jointX(x1,y1,z1,L):
    return(x1+L-np.sqrt(L**2 -y1**2 -z1**2))

def jointY(x1,y1,z1,L):
    return(y1+L-np.sqrt(L**2 -x1**2 -z1**2))
    
def jointZ(x1,y1,z1,L):
    return(z1+L-np.sqrt(L**2 -x1**2 -y1**2))
    
xyzL=[0,0.005,-0.005]
x1=xyzL[0]
y1=xyzL[1]
z1=xyzL[2]
L=0.045

print("joint positions:")
p1=jointX(x1,y1,z1,L)
p2=jointY(x1,y1,z1,L)
p3=jointZ(x1,y1,z1,L)

print(p1, p2, p3)

print("\nThe following should be equal to L:")
a1=[-L+p1,0,0]
b1=[x1,y1,z1]

a2=[0,-L+p2,0]
b2=[x1,y1,z1]

a3=[0,0,-L+p3]
b3=[x1,y1,z1]

def dist(a,b):
    return np.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2+(b[2]-a[2])**2)
    
print(dist(a1,b1))
print(dist(a2,b2))
print(dist(a3,b3))

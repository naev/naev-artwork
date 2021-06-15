#!/usr/bin/env python3

# Generates polygons from stl files


# If you added a ship blend:
# Go to bottom of the file, and replace 
#'../naev-atwork_back/naev-artwork/3D/ships/' and
# './ship_polygon_3d/' by the right paths in naev repo.
# If the ship is big, go in the function "polygonify_all_ships"
# and add the name of your blend in the dictionary params,
# along with (sx,np).
# If your ship is small (fighter, yacht...), use (8,30)
# Rem : in this case, it's not useful to add it to the dict.
# If your ship is medium (destroyer, courrier...), use (10,40)
# If your ship is big (cruiser, bulk...), use (12,50)
# Special case of medium/big ships with a simple shape: 
# you may use (10,30) or (12,30)

# First parameter should be increased when the ship is long
# Second parameter should be increased when the shape of the ship is complex

# Then,run the script from shell 
# (or any other interface that prints warnings).
# If the script refines the polygon a lot (more than 10-15 times), there
# is maybe something wrong. To see what parameters to use,
# request help on discord.

# Principle of the algorithm :

# 1 ) The .blend is transformet into a STL file

# 2 ) The STL is transformed into a set of points in PointsFromSTL.
# a/ Each point of the STL is rotated and projected to create the 2D shape
#    for different angles.
# b/ For each angular value, a set of points is created in all the rectangle
#    containing the points of the projected STL. Each of these points is 
#    activated only if it is inside a triangle of the STL.

# 3 ) The set of points is transformed into a polygon in polygonFromPng.
# See the script polygon_from_sprite to see what's happening there


import numpy as np
from stl import mesh
import math
import matplotlib.pyplot as plt
#import polygon_from_sprite
from polygon_from_sprite import *
import os
import subprocess

# Create the projections of the ship from the STL data
def pointsFromSTL( adress, sx, size, center, alpha ) :
    # Extract the mesh and the points

    shipMesh = mesh.Mesh.from_file(adress)
    v0 = np.transpose(shipMesh.v0) # TODO : take the center into account
    v1 = np.transpose(shipMesh.v1)
    v2 = np.transpose(shipMesh.v2)
    
    # Compute x and y max and min
    xM = max( [np.amax(v0[0,:]), np.amax(v1[0,:]), np.amax(v2[0,:])] )
    xm = min( [np.amin(v0[0,:]), np.amin(v1[0,:]), np.amin(v2[0,:])] )
    yM = max( [np.amax(v0[1,:]), np.amax(v1[1,:]), np.amax(v2[1,:])] )
    ym = min( [np.amin(v0[1,:]), np.amin(v1[1,:]), np.amin(v2[1,:])] )
    
    # Rescale the data
    leng   = max(xM-xm,yM-ym)
    factor = size/leng
    
    v0 = factor*v0
    v1 = factor*v1
    v2 = factor*v2
    
    # Rotate the stuff for any angle
    dtheta = 2*math.pi/sx**2
    
    xlist = []
    ylist = []
    
    for it in range(sx**2):
        # Rotate the points
        theta = it*dtheta + math.pi/2
        rot = np.matrix([[math.cos(theta), -math.sin(theta), 0],\
                         [math.sin(theta), math.cos(theta), 0],\
                         [0, 0, 1]])
        vt0 = rot * v0
        vt1 = rot * v1
        vt2 = rot * v2
        
        # Projection for the view
        proj = np.matrix([[1, 0, 0],\
                          [0, 1, math.tan(alpha)],\
                          [0, 0, 0]])
        vt0 = proj * vt0
        vt1 = proj * vt1
        vt2 = proj * vt2
        
        x0 = vt0[0,:] # Extract x and y coordiantes
        x1 = vt1[0,:]
        x2 = vt2[0,:]
        y0 = vt0[1,:]
        y1 = vt1[1,:]
        y2 = vt2[1,:]

        xmax = max( [np.amax(x0), np.amax(x1), np.amax(x2)] )
        xmin = min( [np.amin(x0), np.amin(x1), np.amin(x2)] )
        ymax = max( [np.amax(y0), np.amax(y1), np.amax(y2)] )
        ymin = min( [np.amin(y0), np.amin(y1), np.amin(y2)] )

        # Now we create a grid of points that are inside the ship.
        # We need this regular grid because its the only way to have a
        # non-convex polygon generation algo that is guaranteed to work.
        xgrid = []
        ygrid = []
        fullDots = np.zeros( ( int(xmax)-int(xmin)+1 , int(ymax)-int(ymin)+1 ) )
        
        for ai, i in enumerate( range(int(xmin),int(xmax)+1) ):
            for aj, j in enumerate( range(int(ymin),int(ymax)+1) ):
                # Test if there is a triangle for which the point (i,j) is inside
                # Here, we do vector operations to speed up computations
                D1 = np.multiply(x1-i,y2-j) - np.multiply(x2-i,y1-j);
                D2 = np.multiply(x2-i,y0-j) - np.multiply(x0-i,y2-j);
                D3 = np.multiply(x0-i,y1-j) - np.multiply(x1-i,y0-j);
                D0 = D1+D2+D3;
                
                j1 = np.where(np.multiply(D0,D1) > 0)[1];
                j2 = np.where(np.multiply(D0,D2) > 0)[1];
                j3 = np.where(np.multiply(D0,D3) > 0)[1];
                j4 = np.intersect1d( np.intersect1d(j1,j2) , j3);
                
                # Hell, there are flat triangles. As a consequence, > cannot
                # be replaced by >= in np.where
                
                if len(j4) >= 1: # point is in a triangle
                    fullDots[ai,aj] = 1

        # Second loop to remove points that are inside the domain
        # (to speedup polygon generation)
        for ai, i in enumerate( range(int(xmin),int(xmax)+1) ):
            for aj, j in enumerate( range(int(ymin),int(ymax)+1) ):
                if fullDots[ai,aj] == 1:
                    if (i == int(xmin) or i == int(xmax) or \
                       j == int(ymin) or j == int(ymax)):
                           # We're on the boundary : activate the point
                           xgrid.append(i)
                           ygrid.append(j)
                    elif (fullDots[ai-1,aj] == 1 and fullDots[ai,aj-1] == 1\
                       and fullDots[ai+1,aj] == 1 and fullDots[ai,aj+1] == 1) :
                           # This point is inside the shape. Don't activate it
                           pass
                    else:
                        xgrid.append(i)
                        ygrid.append(j)
                    
        xlist.append(xgrid)
        ylist.append(ygrid)
        
        #plt.scatter(xgrid,ygrid)
        #plt.scatter(x0.tolist()[0],y0.tolist()[0])
        #break
        
        # A nice progress bar
        progress = str( int(100 * (it / sx**2)) )
        nbars = int(50 * it / sx**2)
        bar = '=' * nbars + ' ' * (50 - nbars)
        print('\rTransforming STL... [%s] %s%%' % (bar, progress), end = '\r')

    bar = '=' * 50
    progress = 100
    print('\rTransforming STL... [%s] %s%%' % (bar, progress), end = '\n')
                    
    return (xlist,ylist,factor)


# Computes a polygon from STL
def polygonFromSTL(adress,sx,scale,center,alpha,minlen,maxlen):
    points  = pointsFromSTL(adress,sx,scale,center,alpha)
    xlist  = points[0]
    ylist  = points[1]
    factor = points[2]
    polygon = polygonFromPoints((xlist,ylist),minlen,maxlen)
    
    # Rescale by dividing by factor
    xlist = polygon[1]
    ylist = polygon[2]
    xlist = [np.array(i)/factor for i in xlist]
    ylist = [np.array(i)/factor for i in ylist]
    
    xpoint = points[0]
    ypoint = points[1]
    xpoint = [np.array(i)/factor for i in xpoint]
    ypoint = [np.array(i)/factor for i in ypoint]
    
    return ( (xpoint,ypoint), (polygon[0],xlist,ylist) )

# Computes a polygon from Blender
def polygonFromBlend(adress,sx,scale,center,alpha,minlen,maxlen):
    # Export from Blender to STL
    ret = subprocess.run([os.environ.get('BLENDER', 'blender'), address, '--background', '--python', 'blend_to_stl.py'])
    if ret.returncode != 0:
        print("Warning: STL export failed.\
              probably the required blender file does not exist")
    
    stlAdress = (os.path.basename(adress) + ".stl")
    
    # Generate the polygon
    out = polygonFromSTL(stlAdress,sx,scale,center,alpha,minlen,maxlen)
    
    # Remove the intermediate stl file
    os.remove(stlAdress)
    
    return out
    

# Generates polygon for all ships via stl
def polygonify_all_ships_stl(blendPath, polyPath, overwrite):
    
    # Default parameters
    default_params = (8,30)
    
    # First define the parameters for special files
    params = {
               "archimedes.blend" : (12,50),
               "arx.blend" : (12,50),
               "divinity.blend" : (12,30),
               "dogma.blend" : (12,30),
               "goddard.blend" : (12,50),
               "goddard_dvaered.blend" : (12,50),
               "hawking.blend" : (12,50),
               "hawking_empire.blend" : (12,50),
               "ira.blend" : (12,50),
               "kahan.blend" : (10,40),
               "kestrel.blend" : (10,40),
               "kestrel_pirate.blend" : (10,40),
               "mule.blend" : (10,40),
               "nyx.blend" : (10,40),
               "pacifier.blend" : (10,40),
               "pacifier_empire.blend" : (10,40),
               "peacemaker.blend" : (12,50),
               "phalanx.blend" : (10,40),
               "phalanx_pirate.blend" : (10,40),
               "phalanx_dvaered.blend" : (10,40),
               "preacher.blend" : (10,40),
               "quicksilver.blend" : (10,40),
               "rhino.blend" : (10,40),
               "rhino_pirate.blend" : (10,40),
               "taciturnity.blend" : (10,40),
               "vigilance.blend" : (10,40),
               "vigilance_dvaered.blend" : (10,40),
               "watson.blend" : (12,50),
              }
    
    for fileName in os.listdir(blendPath):
        if (fileName.endswith(".blend")):
            
            # Remove the .png
            name = os.path.splitext(fileName)[0]
            
            polyAdress = (polyPath+name+".xml")
            
            # Test if the file already exists
            if ( not overwrite and os.path.exists(polyAdress) ) :
                continue
                
            # Manage parameters
            sx   = default_params[0]
            np   = default_params[1]
            if fileName in params:
                mNm = params[fileName]
                sx   = mNm[0]
                np   = mNm[1]

            blendAdress  = (blendPath+fileName)
     
            print("Generation of " + polyAdress + ". Parameters are : ("\
                   + str(sx) + ", " + str(np) + ")")
            
            pntNplg = polygonFromBlend(blendAdress,sx,np,[0,0,0],math.pi/4,3,6)
            
            polygon = pntNplg[1]
            generateXML(polygon,polyAdress)


if __name__ == "__main__":
    
    polygonify_all_ships_stl("../naev-atwork_back/naev-artwork/3D/ships/", "./ship_polygon_3d/", 0)
    
#    pntNplg = polygonFromBlend(\
#        "../naev-atwork_back/naev-artwork/3D/ships/watson.blend",\
#        12,50,[0,0,0],math.pi/4,3,6)
#    
#    points  = pntNplg[0]
#    polygon = pntNplg[1]
#    poly    = polygon[0]
#    
#    plt.scatter(points[0][0],points[1][0])
#    plt.scatter(polygon[1][0],polygon[2][0])

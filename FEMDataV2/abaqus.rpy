# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by Till on Thu Feb 28 16:08:29 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=106.783340454102, 
    height=128.435180664063)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/A320_V2.cae')
#: The model database "D:\Documents\Studium\AA_Courses\Semester_6\SVV\A15_SVV_Structures\FEMDataV2\A320_V2.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['A320-19'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb')
#: Model: D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          66
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['A320-19'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4621.27, 
    farPlane=7642.33, width=2698.82, height=1204.98, viewOffsetX=-80.9645, 
    viewOffsetY=221.875)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4773.65, 
    farPlane=7625.12, width=2787.81, height=1244.71, viewOffsetX=-74.3415, 
    viewOffsetY=-55.9004)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5197.91, 
    farPlane=7053.93, width=3035.58, height=1355.34, cameraPosition=(2819.56, 
    5074.4, 2975.61), cameraUpVector=(-0.525001, 0.234818, -0.818067), 
    cameraTarget=(1517.41, -94.4528, -200.696), viewOffsetX=-80.9487, 
    viewOffsetY=-60.8686)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5322.55, 
    farPlane=6929.28, width=1968.33, height=878.827, viewOffsetX=-82.8898, 
    viewOffsetY=-62.3282)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5314.62, 
    farPlane=6937.22, width=1965.4, height=877.518, viewOffsetX=-304.201, 
    viewOffsetY=103.285)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4989.89, 
    farPlane=7185.01, width=1845.31, height=823.901, cameraPosition=(4077.32, 
    4301.79, 3218.45), cameraUpVector=(-0.402472, 0.398671, -0.824062), 
    cameraTarget=(1481.63, -183.798, -193.8), viewOffsetX=-285.614, 
    viewOffsetY=96.9741)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5022.46, 
    farPlane=7189.34, width=1857.35, height=829.279, cameraPosition=(3979.93, 
    3527.73, 4105.73), cameraUpVector=(-0.360087, 0.559212, -0.746739), 
    cameraTarget=(1485.64, -155.911, -219.876), viewOffsetX=-287.478, 
    viewOffsetY=97.607)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5021.69, 
    farPlane=7190.11, width=1857.07, height=829.151, viewOffsetX=-478.093, 
    viewOffsetY=153.448)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5021.68, 
    farPlane=7190.11, width=1857.07, height=829.151, viewOffsetX=-554.851, 
    viewOffsetY=208.063)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5754.84, 
    farPlane=6941.62, width=2128.2, height=950.208, cameraPosition=(1248.66, 
    4970.99, 3810.5), cameraUpVector=(-0.0510611, 0.283735, -0.957542), 
    cameraTarget=(1563.91, -30.4982, 151.633), viewOffsetX=-635.859, 
    viewOffsetY=238.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5718.42, 
    farPlane=6978.05, width=2114.73, height=944.195, viewOffsetX=-791.146, 
    viewOffsetY=276.508)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5795.97, 
    farPlane=6900.5, width=1588.31, height=709.153, viewOffsetX=-801.875, 
    viewOffsetY=280.258)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5793.07, 
    farPlane=6903.4, width=1587.51, height=708.8, viewOffsetX=-932.708, 
    viewOffsetY=336.355)
#: 
#: Node: A320-1.4973
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.23500e+002,  8.75000e+001, -9.65556e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.24643e+002,  9.37531e+001, -9.65288e+001,      -      
#: Deformed coordinates (scaled):     5.24643e+002,  9.37531e+001, -9.65288e+001,      -      
#: Displacement (unscaled):           1.14344e+000,  6.25309e+000,  2.68052e-002,  6.35683e+000
#: 
#: Node: A320-1.4939
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.72900e+002,  8.75000e+001, -9.65556e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.74010e+002,  9.31539e+001, -9.65602e+001,      -      
#: Deformed coordinates (scaled):     5.74010e+002,  9.31539e+001, -9.65602e+001,      -      
#: Displacement (unscaled):           1.11016e+000,  5.65386e+000, -4.66823e-003,  5.76182e+000
#: 
#: Node: A320-1.4922
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.97600e+002,  8.75000e+001, -9.65556e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.98688e+002,  9.28478e+001, -9.65713e+001,      -      
#: Deformed coordinates (scaled):     5.98688e+002,  9.28478e+001, -9.65713e+001,      -      
#: Displacement (unscaled):           1.08775e+000,  5.34776e+000, -1.57045e-002,  5.45728e+000
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, Mises (Not averaged): 0.0770712
#: 
#: Element: A320-1.4725
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 656, 4902, 4919, 657
#:   S, Mises (Not averaged): 0.0786058
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, Mises (Not averaged): 0.0770712
session.viewports['Viewport: 1'].view.setValues(nearPlane=5965.65, 
    farPlane=6730.82, width=348.067, height=155.407, viewOffsetX=-921.269, 
    viewOffsetY=291.66)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, S11 (Not averaged): -0.0798628
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, S22 (Not averaged): -0.00611587
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, S11 (Not averaged): -0.0798628
#: 
#: Element: A320-1.4728
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4904, 4905, 4922, 4921
#:   S, S11 (Not averaged): -0.0750193
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, S11 (Not averaged): -0.0798628
#: 
#: Node: A320-1.4903
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.22300e+002,  1.00000e+002, -4.82778e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   6.23519e+002,  1.04876e+002, -4.82464e+001,      -      
#: Deformed coordinates (scaled):     6.23519e+002,  1.04876e+002, -4.82464e+001,      -      
#: Displacement (unscaled):           1.21948e+000,  4.87551e+000,  3.13750e-002,  5.02581e+000
#: 
#: Node: A320-1.4920
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.97600e+002,  1.00000e+002, -4.82778e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.98846e+002,  1.05183e+002, -4.82399e+001,      -      
#: Deformed coordinates (scaled):     5.98846e+002,  1.05183e+002, -4.82399e+001,      -      
#: Displacement (unscaled):           1.24598e+000,  5.18280e+000,  3.79263e-002,  5.33060e+000
#: 
#: Element: A320-1.4727
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4903, 4904, 4921, 4920
#:   S, S11 (Not averaged): -0.078638
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, S11 (Not averaged): -0.0798628
session.viewports['Viewport: 1'].view.setValues(nearPlane=5896.87, 
    farPlane=6799.6, width=844.956, height=377.26, viewOffsetX=-910.647, 
    viewOffsetY=288.297)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5907.86, 
    farPlane=7113.94, width=846.532, height=377.963, cameraPosition=(594.161, 
    -4798.9, 4176.56), cameraUpVector=(0.063443, 0.900052, 0.43114), 
    cameraTarget=(1515.78, -478.581, -180.85), viewOffsetX=-912.344, 
    viewOffsetY=288.834)
#: 
#: Element: A320-1.6239
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6215, 6216, 6233, 6232
#:   S, S11 (Not averaged): 0.071576
#: 
#: Element: A320-1.6240
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6216, 6217, 6234, 6233
#:   S, S11 (Not averaged): 0.0700574
#: 
#: Element: A320-1.6242
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6218, 268, 267, 6235
#:   S, S11 (Not averaged): 0.0629214
#: 
#: Element: A320-1.6235
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6211, 6212, 6229, 6228
#:   S, S11 (Not averaged): 0.0665542
session.viewports['Viewport: 1'].view.setValues(nearPlane=5907.67, 
    farPlane=7114.13, width=846.505, height=377.951, viewOffsetX=-912.315, 
    viewOffsetY=288.825)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5746.57, 
    farPlane=6867.65, width=823.422, height=367.645, cameraPosition=(2384.11, 
    4.27377, 6074.91), cameraUpVector=(-0.425299, 0.86743, -0.258237), 
    cameraTarget=(1647.93, 194.439, -83.2886), viewOffsetX=-887.437, 
    viewOffsetY=280.949)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5749.78, 
    farPlane=6864.44, width=823.882, height=367.85, viewOffsetX=-858.822, 
    viewOffsetY=297.626)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5217.01, 
    farPlane=7064.63, width=747.542, height=333.765, cameraPosition=(4006.06, 
    3300.36, 4322.16), cameraUpVector=(-0.281538, 0.585739, -0.760031), 
    cameraTarget=(1597.02, -196.787, -202.004), viewOffsetX=-779.244, 
    viewOffsetY=270.048)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5178.24, 
    farPlane=7103.4, width=1086.95, height=485.304, viewOffsetX=-773.453, 
    viewOffsetY=268.041)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5862.95, 
    farPlane=7147.45, width=1230.67, height=549.477, cameraPosition=(674.504, 
    3728.91, 5155.55), cameraUpVector=(0.22809, 0.524757, -0.820125), 
    cameraTarget=(1577.69, -153.742, 400.461), viewOffsetX=-875.725, 
    viewOffsetY=303.483)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5806.19, 
    farPlane=7254.58, width=1218.76, height=544.157, cameraPosition=(444.957, 
    3341.41, 5397.12), cameraUpVector=(0.136746, 0.599111, -0.788902), 
    cameraTarget=(1610.62, -97.6763, 365.671), viewOffsetX=-867.247, 
    viewOffsetY=300.545)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5887.8, 
    farPlane=6894.65, width=1235.89, height=551.806, cameraPosition=(1933.02, 
    3724.26, 5027.57), cameraUpVector=(-0.112603, 0.544758, -0.830999), 
    cameraTarget=(1758.68, -37.6551, 96.1268), viewOffsetX=-879.437, 
    viewOffsetY=304.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5885.48, 
    farPlane=6896.97, width=1235.4, height=551.588, viewOffsetX=-1042.99, 
    viewOffsetY=300.521)
#: 
#: Element: A320-1.6235
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6211, 6212, 6229, 6228
#:   S, S12 (Not averaged): -0.00123116
session.viewports['Viewport: 1'].view.setValues(nearPlane=5784.03, 
    farPlane=6998.41, width=1917.32, height=856.052, viewOffsetX=-1025.01, 
    viewOffsetY=295.341)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5788.58, 
    farPlane=6993.87, width=1918.83, height=856.726, viewOffsetX=-991.277, 
    viewOffsetY=280.183)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5085.51, 
    farPlane=7189.79, width=1685.77, height=752.67, cameraPosition=(3983.05, 
    1231.22, 5285.22), cameraUpVector=(-0.155226, 0.829754, -0.536109), 
    cameraTarget=(1729.97, -299.675, -289.856), viewOffsetX=-870.878, 
    viewOffsetY=246.152)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5338.58, 
    farPlane=7055.36, width=1769.66, height=790.125, cameraPosition=(3319.85, 
    3685.54, 4460.36), cameraUpVector=(-0.308724, 0.531243, -0.788968), 
    cameraTarget=(1807.65, -166.449, -163.163), viewOffsetX=-914.216, 
    viewOffsetY=258.401)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5680.69, 
    farPlane=7257.04, width=1883.07, height=840.759, cameraPosition=(155.678, 
    -3677.57, 5084.42), cameraUpVector=(0.734543, 0.669341, 0.111481), 
    cameraTarget=(1242.46, -875.95, -344.335), viewOffsetX=-972.802, 
    viewOffsetY=274.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5664.91, 
    farPlane=7272.83, width=1877.84, height=838.425, viewOffsetX=-784.82, 
    viewOffsetY=201.399)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5664.88, 
    farPlane=7272.87, width=1877.83, height=838.42, viewOffsetX=-991.376, 
    viewOffsetY=230.266)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5495.25, 
    farPlane=6891.57, width=1821.6, height=813.316, cameraPosition=(2555.43, 
    -5810.21, 1765.98), cameraUpVector=(0.382178, 0.712255, 0.588755), 
    cameraTarget=(1624.39, -255.094, -836.992), viewOffsetX=-961.691, 
    viewOffsetY=223.371)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxAutoCompute=OFF, maxValue=0.15, minAutoCompute=OFF, minValue=-0.15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4726.13, 
    farPlane=7121.16, width=1566.65, height=699.484, cameraPosition=(4604.65, 
    -236.544, 4881.99), cameraUpVector=(0.216047, 0.770771, -0.599363), 
    cameraTarget=(1515.42, -844.924, -464.801), viewOffsetX=-827.093, 
    viewOffsetY=192.108)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5247.21, 
    farPlane=6787.25, width=1739.38, height=776.606, cameraPosition=(3079.67, 
    2715.93, 4986.11), cameraUpVector=(-0.159833, 0.643351, -0.748701), 
    cameraTarget=(1945.34, -432.052, -239.325), viewOffsetX=-918.284, 
    viewOffsetY=213.289)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5113.81, 
    farPlane=6808.71, width=1695.16, height=756.862, cameraPosition=(3362.73, 
    3376.77, 4398.74), cameraUpVector=(-0.166798, 0.523039, -0.835828), 
    cameraTarget=(1923.74, -508.72, -220.123), viewOffsetX=-894.938, 
    viewOffsetY=207.866)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5118.76, 
    farPlane=6803.75, width=1696.8, height=757.594, viewOffsetX=-895.804, 
    viewOffsetY=208.067)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5118.77, 
    farPlane=6803.74, width=1696.8, height=757.595, viewOffsetX=-876.575, 
    viewOffsetY=208.067)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5118.77, 
    farPlane=6803.74, width=1696.8, height=757.595, viewOffsetX=-640.154, 
    viewOffsetY=200.128)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5281.14, 
    farPlane=6685.18, width=1750.63, height=781.626, cameraPosition=(2744.12, 
    3393.63, 4634.24), cameraUpVector=(-0.153418, 0.534898, -0.830871), 
    cameraTarget=(1967.9, -441.979, -181.069), viewOffsetX=-660.46, 
    viewOffsetY=206.476)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxValue=0.05, minValue=-0.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5273.87, 
    farPlane=6692.46, width=1748.22, height=780.552, viewOffsetX=-997.539, 
    viewOffsetY=279.806)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5092.02, 
    farPlane=6900.68, width=1687.94, height=753.639, cameraPosition=(3621.07, 
    -3679.05, 4050.13), cameraUpVector=(-0.348629, 0.838607, 0.418564), 
    cameraTarget=(1911.97, 296.422, -396.915), viewOffsetX=-963.143, 
    viewOffsetY=270.158)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5525.45, 
    farPlane=6907.47, width=1831.62, height=817.788, cameraPosition=(1115.36, 
    -5247.35, 3210.98), cameraUpVector=(-0.00678156, 0.809181, 0.58752), 
    cameraTarget=(2006.04, -172.962, -247.181), viewOffsetX=-1045.12, 
    viewOffsetY=293.154)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5209.27, 
    farPlane=6837.84, width=1726.81, height=770.993, cameraPosition=(3330.59, 
    -4584.82, 3284.03), cameraUpVector=(-0.157214, 0.820952, 0.548928), 
    cameraTarget=(2003.03, 182.924, -458.676), viewOffsetX=-985.315, 
    viewOffsetY=276.379)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4929, 
    farPlane=6989.52, width=1633.91, height=729.513, cameraPosition=(4185.65, 
    868.113, 5082.69), cameraUpVector=(-0.135167, 0.847933, -0.51258), 
    cameraTarget=(1901.27, -451.776, -533.456), viewOffsetX=-932.304, 
    viewOffsetY=261.509)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5092.58, 
    farPlane=6802.21, width=1688.14, height=753.726, cameraPosition=(3593.82, 
    3937.82, 3799.05), cameraUpVector=(-0.161026, 0.394184, -0.904815), 
    cameraTarget=(1986.03, -560.849, -160.58), viewOffsetX=-963.245, 
    viewOffsetY=270.188)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4737.31, 
    farPlane=7062.21, width=1570.37, height=701.147, cameraPosition=(4876.66, 
    225.012, 4640.44), cameraUpVector=(-0.389129, 0.897523, -0.207441), 
    cameraTarget=(1837.35, -37.0672, -762.851), viewOffsetX=-896.048, 
    viewOffsetY=251.339)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4907.29, 
    farPlane=6827.05, width=1626.72, height=726.305, cameraPosition=(4171.83, 
    4219.85, 2918.56), cameraUpVector=(-0.405786, 0.342954, -0.847184), 
    cameraTarget=(1947.12, -539.052, -383.744), viewOffsetX=-928.199, 
    viewOffsetY=260.357)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxAutoCompute=ON, minAutoCompute=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4900.41, 
    farPlane=6833.94, width=1624.44, height=725.287, viewOffsetX=-958.304, 
    viewOffsetY=270.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5325.27, 
    farPlane=6902.79, width=1765.28, height=788.168, cameraPosition=(753.449, 
    5244.81, 3033.13), cameraUpVector=(-0.30803, 0.0882538, -0.947275), 
    cameraTarget=(2180.66, 79.955, -95.603), viewOffsetX=-1041.39, 
    viewOffsetY=294.332)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5306.23, 
    farPlane=6921.81, width=1758.97, height=785.352, viewOffsetX=-1037.67, 
    viewOffsetY=293.28)
#: 
#: Element: A320-1.6235
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6211, 6212, 6229, 6228
#:   S, S11 (Not averaged): 0.0665542
session.viewports['Viewport: 1'].view.setValues(nearPlane=5306.19, 
    farPlane=6921.86, width=1758.96, height=785.346, viewOffsetX=-1272.19, 
    viewOffsetY=459.047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5406.24, 
    farPlane=6821.81, width=1073.13, height=479.135, viewOffsetX=-1296.18, 
    viewOffsetY=467.702)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5401.95, 
    farPlane=6918.97, width=1072.28, height=478.755, cameraPosition=(647.047, 
    4536.86, 4025.98), cameraUpVector=(-0.381702, 0.243671, -0.891588), 
    cameraTarget=(2156.85, 183.66, -129.948), viewOffsetX=-1295.15, 
    viewOffsetY=467.331)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5383.14, 
    farPlane=6908.62, width=1068.55, height=477.089, cameraPosition=(487.943, 
    5283.24, 2965.23), cameraUpVector=(-0.328423, 0.0594045, -0.942661), 
    cameraTarget=(2159.71, 173.873, -133.339), viewOffsetX=-1290.64, 
    viewOffsetY=465.704)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5401.71, 
    farPlane=6834.16, width=1072.24, height=478.737, cameraPosition=(709.573, 
    5306.92, 2926.35), cameraUpVector=(-0.330961, 0.0649956, -0.941403), 
    cameraTarget=(2174.16, 117.495, -143.898), viewOffsetX=-1295.09, 
    viewOffsetY=467.311)
#: 
#: Element: A320-1.4725
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 656, 4902, 4919, 657
#:   S, S11 (Not averaged): -0.079667
#: 
#: Element: A320-1.4726
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4902, 4903, 4920, 4919
#:   S, S11 (Not averaged): -0.0798628
#: 
#: Element: A320-1.4727
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4903, 4904, 4921, 4920
#:   S, S11 (Not averaged): -0.078638
#: 
#: Element: A320-1.4728
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4904, 4905, 4922, 4921
#:   S, S11 (Not averaged): -0.0750193
#: 
#: Element: A320-1.4692
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4870, 4871, 4888, 4887
#:   S, S11 (Not averaged): -0.079347
#: 
#: Element: A320-1.4782
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4955, 4956, 4973, 4972
#:   S, S11 (Not averaged): -0.0417948
#: 
#: Element: A320-1.4728
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4904, 4905, 4922, 4921
#:   S, S11 (Not averaged): -0.0750193
#: 
#: Element: A320-1.4763
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4937, 4938, 4955, 4954
#:   S, S11 (Not averaged): -0.0736665
#: 
#: Element: A320-1.4764
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4938, 4939, 4956, 4955
#:   S, S11 (Not averaged): -0.0706186
session.viewports['Viewport: 1'].view.setValues(nearPlane=5691.21, 
    farPlane=7203.48, width=1129.71, height=504.396, cameraPosition=(449.74, 
    -3321.13, 5364.29), cameraUpVector=(-0.687702, 0.72166, -0.0792061), 
    cameraTarget=(1885.82, 390.994, 604.109), viewOffsetX=-1364.5, 
    viewOffsetY=492.356)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5683.28, 
    farPlane=7211.4, width=1128.14, height=503.694, viewOffsetX=-1334.02, 
    viewOffsetY=512.783)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5490.6, 
    farPlane=7895.12, width=1089.89, height=486.62, cameraPosition=(-1744.21, 
    3499.57, 4703.04), cameraUpVector=(-0.109396, 0.446863, -0.887889), 
    cameraTarget=(1840, 665.05, 505.368), viewOffsetX=-1288.79, 
    viewOffsetY=495.398)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5495.86, 
    farPlane=7889.85, width=1090.94, height=487.086, viewOffsetX=-1359.85, 
    viewOffsetY=280.038)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5495.87, 
    farPlane=7889.85, width=1090.94, height=487.088, viewOffsetX=-1338.03, 
    viewOffsetY=283.684)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5640.6, 
    farPlane=7197.76, width=1119.67, height=499.916, cameraPosition=(741.564, 
    4019.77, 4906.61), cameraUpVector=(-0.0982372, 0.478599, -0.872521), 
    cameraTarget=(2280.3, 198.211, 266.62), viewOffsetX=-1373.27, 
    viewOffsetY=291.155)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5636.65, 
    farPlane=7201.71, width=1118.89, height=499.565, viewOffsetX=-1572.96, 
    viewOffsetY=298.429)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5630.06, 
    farPlane=7311.78, width=1117.58, height=498.983, cameraPosition=(469.594, 
    3385.33, 5374.17), cameraUpVector=(-0.0685744, 0.57734, -0.813619), 
    cameraTarget=(2252.09, 151.819, 387.321), viewOffsetX=-1571.12, 
    viewOffsetY=298.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5563.82, 
    farPlane=7238.68, width=1104.43, height=493.112, cameraPosition=(490.716, 
    -3288.1, 5340.4), cameraUpVector=(-0.10551, 0.979473, 0.171756), 
    cameraTarget=(2255.48, -105.084, 314.912), viewOffsetX=-1552.63, 
    viewOffsetY=294.573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5522.57, 
    farPlane=7063.43, width=1096.25, height=489.456, cameraPosition=(571.074, 
    -5246.99, 3341.07), cameraUpVector=(-0.144721, 0.802094, 0.579398), 
    cameraTarget=(2258.98, -134.993, 255.624), viewOffsetX=-1541.12, 
    viewOffsetY=292.389)
#: 
#: Element: A320-1.6276
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6250, 6251, 6268, 6267
#:   S, S11 (Not averaged): 0.0664037
session.viewports['Viewport: 1'].view.setValues(nearPlane=5629.44, 
    farPlane=7339.04, width=1117.46, height=498.93, cameraPosition=(330.722, 
    2622.95, 5776.67), cameraUpVector=(0.144972, 0.680993, -0.717796), 
    cameraTarget=(2182.66, -213.64, 578.051), viewOffsetX=-1570.94, 
    viewOffsetY=298.047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5625.63, 
    farPlane=7277.57, width=1116.71, height=498.592, cameraPosition=(385.362, 
    4002.72, 4930.77), cameraUpVector=(0.177833, 0.468607, -0.865322), 
    cameraTarget=(2165.79, -136.547, 664.843), viewOffsetX=-1569.88, 
    viewOffsetY=297.845)
#: 
#: Element: A320-1.4764
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4938, 4939, 4956, 4955
#:   S, S11 (Not averaged): -0.0706186
session.viewports['Viewport: 1'].view.setValues(nearPlane=5678.58, 
    farPlane=6934.23, width=1127.22, height=503.286, cameraPosition=(1043.68, 
    5626.92, 2893.58), cameraUpVector=(0.125587, 0.0604749, -0.990238), 
    cameraTarget=(2196.69, -24.5364, 605.952), viewOffsetX=-1584.66, 
    viewOffsetY=300.648)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4876.7, 
    farPlane=6890.79, width=968.045, height=432.217, cameraPosition=(4409.5, 
    2043.46, 4593.18), cameraUpVector=(0.100347, 0.526273, -0.844374), 
    cameraTarget=(1821.79, -1073.67, -106.7), viewOffsetX=-1360.89, 
    viewOffsetY=258.193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4898.59, 
    farPlane=6868.9, width=972.392, height=434.157, viewOffsetX=-1369.59, 
    viewOffsetY=271.701)
session.viewports['Viewport: 1'].view.setValues(farPlane=6868.89, 
    cameraPosition=(4615.1, 2628.31, 4092.08), cameraUpVector=(-0.301448, 
    0.645202, -0.702028), cameraTarget=(2027.39, -488.818, -607.797))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5151.06, 
    farPlane=6769.89, width=1022.51, height=456.534, cameraPosition=(3972.66, 
    4190.04, 3313.87), cameraUpVector=(-0.411144, 0.402167, -0.81806), 
    cameraTarget=(2120.47, -334, -507.644), viewOffsetX=-1440.18, 
    viewOffsetY=285.704)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5144.15, 
    farPlane=6776.79, width=1021.14, height=455.922, viewOffsetX=-1310.27, 
    viewOffsetY=443.665)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4159.97, 
    farPlane=6683.37, width=825.775, height=368.695, cameraPosition=(5680.93, 
    3651.38, 196.187), cameraUpVector=(0.0908897, -0.777603, -0.622152), 
    cameraTarget=(1309.77, -557.195, 1493.26), viewOffsetX=-1059.59, 
    viewOffsetY=358.783)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4186.89, 
    farPlane=6656.45, width=831.119, height=371.081, viewOffsetX=-967.267, 
    viewOffsetY=544.979)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4186.91, 
    farPlane=6656.43, width=831.123, height=371.083, viewOffsetX=-599.915, 
    viewOffsetY=710.525)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-463.611, 
    viewOffsetY=946.619)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-234.221, 
    viewOffsetY=1167.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4025.07, 
    farPlane=6690.35, width=798.996, height=356.739, cameraPosition=(6109.1, 
    2899.82, 598.889), cameraUpVector=(0.00801904, -0.737424, -0.675382), 
    cameraTarget=(1165.3, -749.205, 1461.97), viewOffsetX=-225.167, 
    viewOffsetY=1122.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4029.49, 
    farPlane=6685.92, width=799.872, height=357.13, viewOffsetX=-518.167, 
    viewOffsetY=1052.16)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-507.502, 
    viewOffsetY=1056.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4095.77, 
    farPlane=7044.25, width=813.029, height=363.005, cameraPosition=(6967.02, 
    1142.07, 984.066), cameraUpVector=(-0.308677, -0.274246, -0.910773), 
    cameraTarget=(1126.58, -926.953, 1315.54), viewOffsetX=-515.85, 
    viewOffsetY=1073.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4093.96, 
    farPlane=7046.07, width=812.671, height=362.845, cameraPosition=(7184.34, 
    444.746, 460.477), cameraUpVector=(-0.521874, 0.348763, -0.778468), 
    cameraTarget=(1343.9, -1624.28, 791.951), viewOffsetX=-515.622, 
    viewOffsetY=1073.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4093.96, 
    viewOffsetX=-520.498, viewOffsetY=1084.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3936.43, 
    farPlane=6831.19, width=781.402, height=348.883, cameraPosition=(6903.27, 
    -537.959, -1621.44), cameraUpVector=(-0.762316, 0.370041, -0.530984), 
    cameraTarget=(1636.92, -1180.23, 1596.4), viewOffsetX=-500.47, 
    viewOffsetY=1043.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3940.74, 
    farPlane=6826.88, width=782.257, height=349.265, viewOffsetX=-531.787, 
    viewOffsetY=1052.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4083.09, 
    farPlane=6892.51, width=810.515, height=361.882, cameraPosition=(7132.2, 
    903.011, -182.785), cameraUpVector=(-0.710269, 0.583308, -0.394043), 
    cameraTarget=(1660.35, -2006.64, 124.121), viewOffsetX=-550.997, 
    viewOffsetY=1090.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4079.2, 
    farPlane=6896.41, width=809.743, height=361.537, viewOffsetX=-404.178, 
    viewOffsetY=1064.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3997.04, 
    farPlane=7015.37, width=793.434, height=354.256, cameraPosition=(6961.25, 
    -389.279, -1505.35), cameraUpVector=(-0.604547, 0.767841, -0.211999), 
    cameraTarget=(1238.35, -1635.85, 543.063), viewOffsetX=-396.038, 
    viewOffsetY=1043.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4116.18, 
    farPlane=7108.42, width=817.085, height=364.815, cameraPosition=(7230.06, 
    32.1477, 145.392), cameraUpVector=(-0.562491, 0.792354, -0.236176), 
    cameraTarget=(1308.16, -1731.03, -423.572), viewOffsetX=-407.843, 
    viewOffsetY=1074.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4084.65, 
    farPlane=7067.04, width=810.826, height=362.021, cameraPosition=(7195.07, 
    115.394, -566.686), cameraUpVector=(-0.614934, 0.759103, -0.213586), 
    cameraTarget=(1309.97, -1783.4, -55.2382), viewOffsetX=-404.719, 
    viewOffsetY=1066.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4070.88, 
    farPlane=7080.81, width=910.296, height=406.433, viewOffsetX=-403.354, 
    viewOffsetY=1062.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4071.32, 
    farPlane=7080.36, width=910.396, height=406.477, viewOffsetX=-357.271, 
    viewOffsetY=1119.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4053.28, 
    farPlane=7083.78, width=906.361, height=404.676, cameraPosition=(7164.22, 
    37.9382, -784.146), cameraUpVector=(-0.612149, 0.767953, -0.188471), 
    cameraTarget=(1280.7, -1760.65, 22.5215), viewOffsetX=-355.687, 
    viewOffsetY=1114.79)
#: 
#: Element: A320-1.1870
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2436, 2437, 2445, 2444
#:   S, S12 (Not averaged): -0.0177813
session.viewports['Viewport: 1'].view.setValues(nearPlane=3951.2, 
    farPlane=6947.03, width=883.536, height=394.485, cameraPosition=(6760.62, 
    -292.436, -1999.99), cameraUpVector=(-0.59662, 0.800971, -0.0499069), 
    cameraTarget=(1249.77, -1659.08, 502.86), viewOffsetX=-346.729, 
    viewOffsetY=1086.72)
#: 
#: Element: A320-1.1867
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2433, 2434, 2442, 2441
#:   S, S12 (Not averaged): -0.0137962
#: 
#: Element: A320-1.1870
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2436, 2437, 2445, 2444
#:   S, S12 (Not averaged): -0.0177813
#: 
#: Element: A320-1.1866
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 480, 2433, 2441, 479
#:   S, S12 (Not averaged): -0.00926466
#: 
#: Element: A320-1.1869
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2435, 2436, 2444, 2443
#:   S, S12 (Not averaged): -0.0174561
#: 
#: Element: A320-1.1866
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 480, 2433, 2441, 479
#:   S, S12 (Not averaged): -0.00926466
session.viewports['Viewport: 1'].view.setValues(nearPlane=3877.93, 
    farPlane=7020.31, width=1395.8, height=623.204, viewOffsetX=-340.3, 
    viewOffsetY=1066.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3881.64, 
    farPlane=7016.6, width=1397.14, height=623.8, viewOffsetX=128.813, 
    viewOffsetY=1082.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3881.65, 
    farPlane=7016.59, width=1397.14, height=623.802, viewOffsetX=133.47, 
    viewOffsetY=1088.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2103.89, 
    farPlane=4706.78, width=757.263, height=338.106, cameraPosition=(-330.07, 
    -1406.12, -3099.58), cameraUpVector=(0.0782074, 0.942754, 0.324189), 
    cameraTarget=(3644.34, -1178.6, 1660.02), viewOffsetX=72.3419, 
    viewOffsetY=589.781)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1691.59, 
    farPlane=4602.33, width=608.863, height=271.848, cameraPosition=(-851.68, 
    -1162.88, -2606.33), cameraUpVector=(-0.0583233, 0.615963, 0.785613), 
    cameraTarget=(4553.17, -1180.4, 441.423), viewOffsetX=58.1652, 
    viewOffsetY=474.202)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1715.95, 
    farPlane=4577.97, width=617.633, height=275.763, viewOffsetX=-30.7597, 
    viewOffsetY=590.428)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1716.02, 
    farPlane=4577.91, width=617.657, height=275.774, viewOffsetX=-61.6437, 
    viewOffsetY=729.163)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1716.02, 
    viewOffsetX=-44.761, viewOffsetY=933.101)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1716.02, 
    farPlane=4577.91, width=617.654, height=275.773, viewOffsetX=-2.76043, 
    viewOffsetY=1087.91)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1716.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1716.02, 
    width=617.652, height=275.772, viewOffsetX=68.4755, viewOffsetY=1268.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1716.02, 
    width=617.651, height=275.771, viewOffsetX=150.829, viewOffsetY=1485.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1716.02, 
    farPlane=4577.91, width=617.65, height=275.771, viewOffsetX=257.888, 
    viewOffsetY=1752.15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1858.66, 
    farPlane=4175.21, width=668.991, height=298.694, cameraPosition=(-2605.08, 
    608.957, -1290.49), cameraUpVector=(0.81557, 0.217619, 0.536179), 
    cameraTarget=(1638.25, -3849.25, -2077.93), viewOffsetX=279.324, 
    viewOffsetY=1897.79)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1851.75, 
    farPlane=4182.11, width=666.503, height=297.583, viewOffsetX=286.283, 
    viewOffsetY=1891.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1851.72, 
    farPlane=4369.19, width=666.493, height=297.578, cameraPosition=(-2809.04, 
    132.571, -925.954), cameraUpVector=(0.843665, 0.374265, 0.384909), 
    cameraTarget=(1855.42, -3837.98, -1915.45), viewOffsetX=286.279, 
    viewOffsetY=1891.15)
#: 
#: Element: A320-1.5698
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5740, 5741, 5749, 5748
#:   S, S12 (Not averaged): 0.0191674
#: 
#: Element: A320-1.5695
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5737, 5738, 5746, 5745
#:   S, S12 (Not averaged): 0.018491
#: 
#: Element: A320-1.5730
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 674, 5769, 792, 13
#:   S, S12 (Not averaged): 0.0126495
#: 
#: Element: A320-1.5329
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 795, 796, 5429, 5428
#:   S, S12 (Not averaged): 0.000411678
#: 
#: Element: A320-1.5725
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5764, 5765, 5773, 5772
#:   S, S12 (Not averaged): 0.0204306
#: 
#: Element: A320-1.5722
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5761, 5762, 5770, 5769
#:   S, S12 (Not averaged): 0.0182984
#: 
#: Element: A320-1.5668
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5713, 5714, 5722, 5721
#:   S, S12 (Not averaged): 0.0172531
#: 
#: Element: A320-1.5671
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5716, 5717, 5725, 5724
#:   S, S12 (Not averaged): 0.0225849
#: 
#: Element: A320-1.5674
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5719, 5720, 5728, 5727
#:   S, S12 (Not averaged): 0.0176132
session.viewports['Viewport: 1'].view.setValues(nearPlane=1739.94, 
    farPlane=4480.97, width=1367.13, height=610.403, viewOffsetX=268.998, 
    viewOffsetY=1776.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1720.86, 
    farPlane=3832.24, width=1352.14, height=603.71, cameraPosition=(-2824.07, 
    903.484, 173.931), cameraUpVector=(0.990083, 0.113848, 0.0823025), 
    cameraTarget=(43.6411, -3779.54, -2715.2), viewOffsetX=266.048, 
    viewOffsetY=1757.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1760.32, 
    farPlane=4025.41, width=1383.15, height=617.553, cameraPosition=(-2654.91, 
    658.116, -1157.38), cameraUpVector=(0.880894, 0.218671, 0.419773), 
    cameraTarget=(1060.92, -4302.97, -1443.41), viewOffsetX=272.148, 
    viewOffsetY=1797.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1660.17, 
    farPlane=4205.85, width=1304.46, height=582.421, cameraPosition=(-2517.24, 
    -9.71859, -1564.82), cameraUpVector=(0.794052, 0.428769, 0.430857), 
    cameraTarget=(1616.4, -4377.44, -35.8843), viewOffsetX=256.665, 
    viewOffsetY=1695.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1669.69, 
    farPlane=4196.33, width=1311.94, height=585.761, viewOffsetX=253.764, 
    viewOffsetY=1717.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1729.3, 
    farPlane=3989.96, width=1358.78, height=606.673, cameraPosition=(-2552.97, 
    516.795, -1427.04), cameraUpVector=(0.849376, 0.266771, 0.455405), 
    cameraTarget=(1115.8, -4450.21, -818.295), viewOffsetX=262.823, 
    viewOffsetY=1778.84)
#: 
#: Element: A320-1.5716
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5756, 5757, 5765, 5764
#:   S, S12 (Not averaged): 0.0207399
session.viewports['Viewport: 1'].view.setValues(nearPlane=1745.14, 
    farPlane=4396.47, width=1371.23, height=612.23, cameraPosition=(-2896.57, 
    198.272, -576.287), cameraUpVector=(0.892577, 0.355395, 0.27749), 
    cameraTarget=(1518.43, -3892.44, -2084.72), viewOffsetX=265.23, 
    viewOffsetY=1795.13)
#: 
#: Element: A320-1.2186
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SPAR.Section-ASSEMBLY_A320-1_SPAR, Homogeneous Shell Section,Thickness = 2.9, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2717, 2718, 2726, 2725
#:   S, S12 (Not averaged): -0.021388
session.viewports['Viewport: 1'].view.setValues(nearPlane=1690.51, 
    farPlane=4451.09, width=1686.89, height=753.171, viewOffsetX=256.927, 
    viewOffsetY=1738.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1687.86, 
    farPlane=3250.7, width=1684.25, height=751.991, cameraPosition=(-1611.12, 
    1539.2, -2007.63), cameraUpVector=(0.650457, -0.0928063, 0.753852), 
    cameraTarget=(202.797, -4377.61, -1557.49), viewOffsetX=256.524, 
    viewOffsetY=1736.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1689.08, 
    farPlane=3249.49, width=1685.47, height=752.534, viewOffsetX=-348.935, 
    viewOffsetY=1810.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1689.1, 
    farPlane=3249.46, width=1685.49, height=752.545, viewOffsetX=-756.829, 
    viewOffsetY=1934.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1689.1, 
    farPlane=3249.46, width=1685.49, height=752.546, viewOffsetX=-696.152, 
    viewOffsetY=1981.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1648.16, 
    farPlane=3327.07, width=1644.64, height=734.305, cameraPosition=(-1421.41, 
    1337.04, -2278.55), cameraUpVector=(0.561071, -0.0170677, 0.827592), 
    cameraTarget=(551.704, -4452.81, -1236.42), viewOffsetX=-679.278, 
    viewOffsetY=1933.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1238.82, 
    farPlane=3822.53, width=1236.17, height=551.931, cameraPosition=(-2116.2, 
    122.896, -1549.03), cameraUpVector=(0.691559, 0.2098, 0.691181), 
    cameraTarget=(2226.3, -4309.28, -1556.11), viewOffsetX=-510.57, 
    viewOffsetY=1453.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1923.74, 
    farPlane=2940.55, width=1919.63, height=857.084, cameraPosition=(-243.46, 
    2208.16, -2692.92), cameraUpVector=(0.338245, -0.206607, 0.918098), 
    cameraTarget=(-939.509, -3850.22, -1547), viewOffsetX=-792.855, 
    viewOffsetY=2257.29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1810.06, 
    farPlane=3112.32, width=1806.2, height=806.438, cameraPosition=(-935.214, 
    1532.65, -2667.18), cameraUpVector=(0.456998, -0.0299418, 0.888964), 
    cameraTarget=(-29.9874, -4376.57, -1004.89), viewOffsetX=-746.004, 
    viewOffsetY=2123.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1813.11, 
    farPlane=3109.27, width=1809.24, height=807.797, viewOffsetX=-747.26, 
    viewOffsetY=2127.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1908.81, 
    farPlane=3039.76, width=1904.74, height=850.435, cameraPosition=(-1426.14, 
    2107.95, -1574.55), cameraUpVector=(0.681112, -0.235118, 0.693402), 
    cameraTarget=(-599.412, -4041.09, -1488.75), viewOffsetX=-786.703, 
    viewOffsetY=2239.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1918, 
    farPlane=2938.25, width=1913.91, height=854.532, cameraPosition=(-424.114, 
    1155.04, -3187.12), cameraUpVector=(0.335668, 0.115015, 0.934932), 
    cameraTarget=(-391.812, -4342.54, -310.125), viewOffsetX=-790.492, 
    viewOffsetY=2250.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1414.26, 
    farPlane=3516.65, width=1411.24, height=630.098, cameraPosition=(-1332.99, 
    35.6453, -2706.15), cameraUpVector=(0.487036, 0.382352, 0.785241), 
    cameraTarget=(1086.03, -4573.11, 671.613), viewOffsetX=-582.878, 
    viewOffsetY=1659.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1606.41, 
    farPlane=3302.08, width=1602.98, height=715.706, cameraPosition=(-1092.88, 
    321.654, -2915.42), cameraUpVector=(0.44462, 0.31799, 0.837374), 
    cameraTarget=(660.386, -4566.91, 480.101), viewOffsetX=-662.071, 
    viewOffsetY=1884.93)
#: 
#: Element: A320-1.2445
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2905, 2906, 2923, 2922
#:   S, S12 (Not averaged): -0.0995551
session.viewports['Viewport: 1'].view.setValues(nearPlane=1445.45, 
    farPlane=3430.45, width=1442.37, height=643.994, cameraPosition=(-796.399, 
    -825.329, -3008.99), cameraUpVector=(0.293896, 0.591951, 0.750479), 
    cameraTarget=(1416.07, -4306.56, 1626.48), viewOffsetX=-595.733, 
    viewOffsetY=1696.06)
#: 
#: Element: A320-1.3399
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 575, 576, 3790, 3789
#:   S, S12 (Not averaged): 0.00177263
session.viewports['Viewport: 1'].view.setValues(nearPlane=1820.43, 
    farPlane=3041.73, width=1816.55, height=811.063, cameraPosition=(-488.175, 
    538.358, -3302.53), cameraUpVector=(0.302083, 0.273867, 0.913095), 
    cameraTarget=(170.787, -4501.67, 256.324), viewOffsetX=-750.28, 
    viewOffsetY=2136.06)
#: 
#: Element: A320-1.2463
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2922, 2923, 2940, 2939
#:   S, S12 (Not averaged): -0.0980847
session.viewports['Viewport: 1'].view.setValues(nearPlane=1897.37, 
    farPlane=2946.14, width=1893.33, height=845.341, cameraPosition=(-81.7826, 
    1005.98, -3395.93), cameraUpVector=(0.220324, 0.154342, 0.963139), 
    cameraTarget=(-231.55, -4396.94, -348.364), viewOffsetX=-781.99, 
    viewOffsetY=2226.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1826.64, 
    farPlane=3016.87, width=2201.81, height=983.072, viewOffsetX=-752.84, 
    viewOffsetY=2143.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1834.12, 
    farPlane=3009.4, width=2210.82, height=987.096, viewOffsetX=-755.921, 
    viewOffsetY=2152.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1878.89, 
    farPlane=2994.27, width=2264.79, height=1011.19, cameraPosition=(-319.268, 
    1804.67, -2937.15), cameraUpVector=(0.319981, -0.0846484, 0.943635), 
    cameraTarget=(-547.366, -4148.37, -1201.94), viewOffsetX=-774.374, 
    viewOffsetY=2204.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1872.59, 
    farPlane=3000.58, width=2257.19, height=1007.8, viewOffsetX=-151.801, 
    viewOffsetY=2031.31)
#: 
#: Node: A320-1.5668
#:                                         1             2             3        Magnitude
#: Base coordinates:                  4.98800e+002,  1.25000e+001,  0.00000e+000,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   4.99080e+002,  1.87586e+001, -2.14242e-001,      -      
#: Deformed coordinates (scaled):     4.99080e+002,  1.87586e+001, -2.14242e-001,      -      
#: Displacement (unscaled):           2.80060e-001,  6.25858e+000, -2.14242e-001,  6.26850e+000
#: 
#: Node: A320-1.4973
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.23500e+002,  8.75000e+001, -9.65556e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.24643e+002,  9.37531e+001, -9.65288e+001,      -      
#: Deformed coordinates (scaled):     5.24643e+002,  9.37531e+001, -9.65288e+001,      -      
#: Displacement (unscaled):           1.14344e+000,  6.25309e+000,  2.68052e-002,  6.35683e+000
#: 
#: Node: A320-1.4940
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.72900e+002,  8.12500e+001, -1.20694e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.73931e+002,  8.69848e+001, -1.20723e+002,      -      
#: Deformed coordinates (scaled):     5.73931e+002,  8.69848e+001, -1.20723e+002,      -      
#: Displacement (unscaled):           1.03064e+000,  5.73481e+000, -2.81894e-002,  5.82675e+000
#: 
#: Node: A320-1.5620
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.47000e+002,  1.25000e+001,  0.00000e+000,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   6.47249e+002,  1.69240e+001, -2.77745e-001,      -      
#: Deformed coordinates (scaled):     6.47249e+002,  1.69240e+001, -2.77745e-001,      -      
#: Displacement (unscaled):           2.48540e-001,  4.42403e+000, -2.77745e-001,  4.43970e+000
#: 
#: Node: A320-1.4940
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.72900e+002,  8.12500e+001, -1.20694e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.73931e+002,  8.69848e+001, -1.20723e+002,      -      
#: Deformed coordinates (scaled):     5.73931e+002,  8.69848e+001, -1.20723e+002,      -      
#: Displacement (unscaled):           1.03064e+000,  5.73481e+000, -2.81894e-002,  5.82675e+000
#: 
#: Node: A320-1.4923
#:                                         1             2             3        Magnitude
#: Base coordinates:                  5.97600e+002,  8.12500e+001, -1.20694e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   5.98610e+002,  8.66800e+001, -1.20736e+002,      -      
#: Deformed coordinates (scaled):     5.98610e+002,  8.66800e+001, -1.20736e+002,      -      
#: Displacement (unscaled):           1.00995e+000,  5.43004e+000, -4.12323e-002,  5.52332e+000
session.viewports['Viewport: 1'].view.setValues(nearPlane=1609.3, 
    farPlane=3388.12, width=1939.83, height=866.102, cameraPosition=(-2031.6, 
    1528.72, -845.387), cameraUpVector=(0.858243, -0.0864325, 0.505913), 
    cameraTarget=(-52.6346, -4345.89, -1117.89), viewOffsetX=-130.458, 
    viewOffsetY=1745.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1941.86, 
    farPlane=2949.61, width=2340.69, height=1045.08, cameraPosition=(-1044.63, 
    2467.43, -1677.85), cameraUpVector=(0.647194, -0.30898, 0.696901), 
    cameraTarget=(-1385.31, -3703.88, -1129.7), viewOffsetX=-157.417, 
    viewOffsetY=2106.46)
#: 
#: Node: A320-1.2299
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.52180e+003, -1.06250e+002, -2.41389e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.52241e+003, -1.05267e+002, -2.45523e+001,      -      
#: Deformed coordinates (scaled):     1.52241e+003, -1.05267e+002, -2.45523e+001,      -      
#: Displacement (unscaled):           6.11793e-001,  9.82525e-001, -4.13395e-001,  1.22904e+000
session.viewports['Viewport: 1'].view.setValues(nearPlane=1901.11, 
    farPlane=2990.36, width=2291.57, height=1023.15, cameraPosition=(-866.827, 
    2432.89, -1956.21), cameraUpVector=(0.563007, -0.297755, 0.770951), 
    cameraTarget=(-1207.51, -3738.42, -1408.06), viewOffsetX=-154.114, 
    viewOffsetY=2062.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1899.92, 
    farPlane=2991.55, width=2290.14, height=1022.51, viewOffsetX=-532.654, 
    viewOffsetY=1946.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1343.92, 
    farPlane=3429.16, width=1619.94, height=723.279, cameraPosition=(64.6515, 
    2787.5, -2277.24), cameraUpVector=(0.434428, -0.381591, 0.81588), 
    cameraTarget=(-2412.13, -2760.66, -1018.25), viewOffsetX=-376.776, 
    viewOffsetY=1376.63)
#: 
#: Node: A320-1.2923
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.32767e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.32774e+003,  6.98310e+001, -1.68424e+002,      -      
#: Deformed coordinates (scaled):     1.32774e+003,  6.98310e+001, -1.68424e+002,      -      
#: Displacement (unscaled):           7.30438e-002,  1.08100e+000,  5.47901e-001,  1.21413e+000
session.viewports['Viewport: 1'].view.setValues(nearPlane=1422.69, 
    farPlane=3350.39, width=1714.89, height=765.671, viewOffsetX=-457.166, 
    viewOffsetY=1614.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1526.73, 
    farPlane=3246.35, width=1071.67, height=478.484, viewOffsetX=-490.598, 
    viewOffsetY=1732.4)
#: 
#: Node: A320-1.2906
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.35100e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.35104e+003,  6.99687e+001, -1.68344e+002,      -      
#: Deformed coordinates (scaled):     1.35104e+003,  6.99687e+001, -1.68344e+002,      -      
#: Displacement (unscaled):           3.54823e-002,  1.21874e+000,  6.28677e-001,  1.37179e+000
#: 
#: Node: A320-1.2889
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.37433e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.37433e+003,  7.01044e+001, -1.68257e+002,      -      
#: Deformed coordinates (scaled):     1.37433e+003,  7.01044e+001, -1.68257e+002,      -      
#: Displacement (unscaled):          -2.89663e-003,  1.35444e+000,  7.14864e-001,  1.53151e+000
#: 
#: Node: A320-1.2906
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.35100e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.35104e+003,  6.99687e+001, -1.68344e+002,      -      
#: Deformed coordinates (scaled):     1.35104e+003,  6.99687e+001, -1.68344e+002,      -      
#: Displacement (unscaled):           3.54823e-002,  1.21874e+000,  6.28677e-001,  1.37179e+000
#: 
#: Node: A320-1.2923
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.32767e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.32774e+003,  6.98310e+001, -1.68424e+002,      -      
#: Deformed coordinates (scaled):     1.32774e+003,  6.98310e+001, -1.68424e+002,      -      
#: Displacement (unscaled):           7.30438e-002,  1.08100e+000,  5.47901e-001,  1.21413e+000
#: 
#: Node: A320-1.2906
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.35100e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.35104e+003,  6.99687e+001, -1.68344e+002,      -      
#: Deformed coordinates (scaled):     1.35104e+003,  6.99687e+001, -1.68344e+002,      -      
#: Displacement (unscaled):           3.54823e-002,  1.21874e+000,  6.28677e-001,  1.37179e+000
#: 
#: Node: A320-1.2923
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.32767e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.32774e+003,  6.98310e+001, -1.68424e+002,      -      
#: Deformed coordinates (scaled):     1.32774e+003,  6.98310e+001, -1.68424e+002,      -      
#: Displacement (unscaled):           7.30438e-002,  1.08100e+000,  5.47901e-001,  1.21413e+000
session.viewports['Viewport: 1'].view.setValues(nearPlane=1680.4, 
    farPlane=3178.02, width=1179.54, height=526.644, cameraPosition=(629.516, 
    3491.08, -1297.86), cameraUpVector=(0.107576, -0.710951, 0.694965), 
    cameraTarget=(-1099.8, -1982.63, -3653.62), viewOffsetX=-539.977, 
    viewOffsetY=1906.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1665.73, 
    farPlane=3192.69, width=1169.24, height=522.048, viewOffsetX=-535.262, 
    viewOffsetY=1890.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1710.01, 
    farPlane=3100.36, width=1200.32, height=535.925, cameraPosition=(2177.05, 
    2846.02, 2102.61), cameraUpVector=(-0.470765, -0.849115, -0.239547), 
    cameraTarget=(1020.8, 2770.91, -3993.22), viewOffsetX=-549.49, 
    viewOffsetY=1940.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1706.03, 
    farPlane=3104.35, width=1197.53, height=534.678, viewOffsetX=-548.212, 
    viewOffsetY=1935.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1313.58, 
    farPlane=3617.23, width=922.057, height=411.684, cameraPosition=(-589.883, 
    1895.14, 2480.39), cameraUpVector=(0.153418, -0.748121, -0.645584), 
    cameraTarget=(2659.89, 3986.19, -2374.31), viewOffsetX=-422.104, 
    viewOffsetY=1490.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1886.48, 
    farPlane=2883.28, width=1324.2, height=591.234, cameraPosition=(249.903, 
    1242.32, 3211.31), cameraUpVector=(0.109174, -0.677734, -0.727158), 
    cameraTarget=(-39.0963, 4064.71, -2307.04), viewOffsetX=-606.199, 
    viewOffsetY=2140.62)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )

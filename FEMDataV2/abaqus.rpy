# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by Till on Thu Feb 28 13:46:01 2019
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
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4402.34, 
    farPlane=8083.29, width=2570.96, height=1147.89, cameraPosition=(7431.18, 
    1580.66, 452.499), cameraUpVector=(-0.532066, 0.786959, -0.312413), 
    cameraTarget=(1479, -60.2615, -164.316))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=4809.48, 
    farPlane=7542, width=2808.73, height=1254.05, cameraPosition=(4449.22, 
    2678.25, 4562.58), cameraUpVector=(-0.339658, 0.698511, -0.629852), 
    cameraTarget=(1460.92, -53.6063, -139.395))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5041.93, 
    farPlane=7499.53, width=2944.48, height=1314.66, cameraPosition=(3878.2, 
    -759.233, 5526.16), cameraUpVector=(-0.671799, 0.74057, 0.0155916), 
    cameraTarget=(1463.62, -37.3415, -143.954))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4459.37, 
    farPlane=8071.24, width=2604.26, height=1162.76, cameraPosition=(6743.15, 
    2465.97, -2428.78), cameraUpVector=(-0.647322, 0.730988, 0.215943), 
    cameraTarget=(1493.67, -3.51416, -227.389))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4801.36, 
    farPlane=7810.34, width=2803.98, height=1251.93, cameraPosition=(5322.81, 
    1092.12, -4996.03), cameraUpVector=(-0.466772, 0.846585, 0.255768), 
    cameraTarget=(1479.99, -16.7469, -252.116))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4711.74, 
    farPlane=7899.97, width=3219.08, height=1437.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5032.12, 
    farPlane=7579.59, width=1070.51, height=477.963)
#: 
#: Node: A320-1.371
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.64780e+003,  0.00000e+000, -4.34500e+002,      -      
#: Scale:                             1.47442e+001,  1.47442e+001,  1.47442e+001,      -      
#: Deformed coordinates (unscaled):   1.64759e+003, -1.70522e+000, -4.34934e+002,      -      
#: Deformed coordinates (scaled):     1.64470e+003, -2.51420e+001, -4.40904e+002,      -      
#: Displacement (unscaled):          -2.10269e-001, -1.70522e+000, -4.34329e-001,  1.77218e+000
session.viewports['Viewport: 1'].view.setValues(nearPlane=5098.15, 
    farPlane=7581.29, width=1084.56, height=484.238, cameraPosition=(5275.39, 
    -181.328, -5160.86), cameraUpVector=(-0.360672, 0.925539, 0.1153), 
    cameraTarget=(1479.23, -37.1215, -254.753))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5023, 
    farPlane=7656.43, width=1575.73, height=703.539)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5026.09, 
    farPlane=7653.34, width=1576.7, height=703.972)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4658.54, 
    farPlane=7989.12, width=1461.4, height=652.492, cameraPosition=(7648.06, 
    991.484, 100.666), cameraUpVector=(-0.485545, 0.855636, 0.179256), 
    cameraTarget=(1529.66, -12.1921, -142.914))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4715.64, 
    farPlane=7975.2, width=1479.31, height=660.489, cameraPosition=(7609.88, 
    418.435, -1325.69), cameraUpVector=(-0.345446, 0.884877, 0.312507), 
    cameraTarget=(1528.82, -24.7826, -174.253))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4782.79, 
    farPlane=8019.17, width=1500.38, height=669.894, cameraPosition=(7764.59, 
    -21.2363, 377.096), cameraUpVector=(-0.361146, 0.874733, 0.323135), 
    cameraTarget=(1590.64, 22.5696, -240.919))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4779.97, 
    farPlane=8021.98, width=1499.5, height=669.501, viewOffsetX=-21.9926)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4968.71, 
    farPlane=7799.25, width=1558.71, height=695.939, cameraPosition=(6248.57, 
    -1091.18, 3845.69), cameraUpVector=(-0.271072, 0.961131, 0.0524172), 
    cameraTarget=(1790.12, 30.6121, -321.491), viewOffsetX=-22.861)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4960.7, 
    farPlane=7807.27, width=1556.2, height=694.817, cameraPosition=(6223.78, 
    -1192.7, 3844.89), cameraUpVector=(0.0282005, 0.963226, -0.267209), 
    cameraTarget=(1765.33, -70.9047, -322.292), viewOffsetX=-22.8241)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4887.35, 
    farPlane=7788.13, width=1533.19, height=684.545, cameraPosition=(6465.74, 
    2732.77, 2511), cameraUpVector=(-0.457209, 0.619055, -0.638538), 
    cameraTarget=(1770.29, -240.355, -248.505), viewOffsetX=-22.4866)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4796.19, 
    farPlane=7879.29, width=2156.8, height=962.975, viewOffsetX=-22.0672)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4801.82, 
    farPlane=7873.66, width=2159.33, height=964.108, viewOffsetX=-121.422, 
    viewOffsetY=-56.2877)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4801.84, 
    farPlane=7873.64, width=2159.34, height=964.113, viewOffsetX=-121.423, 
    viewOffsetY=129.895)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4800.93, 
    farPlane=7901.15, width=2158.94, height=963.931, cameraPosition=(6498.54, 
    2359.17, 2814.89), cameraUpVector=(-0.434461, 0.689362, -0.579675), 
    cameraTarget=(1768.4, -214.125, -268.202), viewOffsetX=-121.4, 
    viewOffsetY=129.87)
a = mdb.models['A320-19'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4531.41, 
    farPlane=8048.13, width=2646.34, height=1181.55, cameraPosition=(7332.74, 
    2050.28, -98.9688), cameraUpVector=(-0.637271, 0.767416, 0.0704149), 
    cameraTarget=(1506.94, -83.1543, -199.284))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4588.58, 
    farPlane=7972.61, width=2679.73, height=1196.46, cameraPosition=(6639.17, 
    1186.45, 3072.11), cameraUpVector=(-0.537741, 0.835136, -0.115685), 
    cameraTarget=(1497.59, -94.8019, -156.526))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4781.09, 
    farPlane=7780.1, width=1366.82, height=610.264)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4773.54, 
    farPlane=7787.64, width=1364.66, height=609.301, viewOffsetX=-166.489, 
    viewOffsetY=187.898)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4856.07, 
    farPlane=7705.12, width=795.963, height=355.385, viewOffsetX=-169.367, 
    viewOffsetY=191.147)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4705.02, 
    farPlane=7741.13, width=771.204, height=344.33, cameraPosition=(7293.68, 
    580.053, 1709.21), cameraUpVector=(-0.48835, 0.865444, 0.111897), 
    cameraTarget=(1436.8, -84.3328, -229.119), viewOffsetX=-164.099, 
    viewOffsetY=185.201)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4708.41, 
    farPlane=7737.75, width=771.759, height=344.578, viewOffsetX=-160.101, 
    viewOffsetY=195.651)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4896.44, 
    farPlane=7683.72, width=802.579, height=358.339, cameraPosition=(6392.18, 
    1194.23, 3463.42), cameraUpVector=(-0.204372, 0.762801, -0.613488), 
    cameraTarget=(1438.25, -207.158, -0.148468), viewOffsetX=-166.495, 
    viewOffsetY=203.464)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5094.82, 
    farPlane=7575.55, width=835.095, height=372.857, cameraPosition=(5615.95, 
    2640.12, 3751.11), cameraUpVector=(-0.494225, 0.695867, -0.521067), 
    cameraTarget=(1540.31, -114.262, -30.9751), viewOffsetX=-173.24, 
    viewOffsetY=211.707)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5065.07, 
    farPlane=7596.97, width=830.219, height=370.68, cameraPosition=(5687.74, 
    1834.83, 4109.74), cameraUpVector=(-0.448682, 0.788424, -0.420799), 
    cameraTarget=(1529.71, -131.07, -55.3154), viewOffsetX=-172.228, 
    viewOffsetY=210.471)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5172.83, 
    farPlane=7529.16, width=847.884, height=378.567, cameraPosition=(5202.71, 
    1822.84, 4580.46), cameraUpVector=(-0.354789, 0.787832, -0.503434), 
    cameraTarget=(1519.2, -143.6, -9.36301), viewOffsetX=-175.892, 
    viewOffsetY=214.949)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5198.5, 
    farPlane=7515.07, width=852.091, height=380.445, cameraPosition=(5101.98, 
    2297.99, 4460.25), cameraUpVector=(-0.392388, 0.737067, -0.550241), 
    cameraTarget=(1529.24, -125.176, 3.18282), viewOffsetX=-176.765, 
    viewOffsetY=216.015)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5197.68, 
    farPlane=7515.89, width=853.233, height=380.955, viewOffsetX=-176.737, 
    viewOffsetY=215.981)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5241.79, 
    farPlane=7487.26, width=860.474, height=384.188, cameraPosition=(4916.54, 
    2506.47, 4507.93), cameraUpVector=(-0.381524, 0.712007, -0.589479), 
    cameraTarget=(1529.03, -118.763, 20.7648), viewOffsetX=-178.237, 
    viewOffsetY=217.814)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5180.9, 
    farPlane=7548.16, width=1268.12, height=566.198, viewOffsetX=-176.167, 
    viewOffsetY=215.284)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5182.91, 
    farPlane=7546.15, width=1268.62, height=566.417, viewOffsetX=-168.624, 
    viewOffsetY=115.312)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5041.53, 
    farPlane=7687.53, width=2204.07, height=984.082, viewOffsetX=-164.024, 
    viewOffsetY=112.167)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5070.91, 
    farPlane=7602.96, width=2216.92, height=989.818, cameraPosition=(4790.05, 
    3858.73, 3542.25), cameraUpVector=(-0.529102, 0.517364, -0.672596), 
    cameraTarget=(1539.19, -67.6197, 4.25967), viewOffsetX=-164.98, 
    viewOffsetY=112.821)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5059.08, 
    farPlane=7678.22, width=2211.75, height=987.509, cameraPosition=(4881.59, 
    2342.28, 4622.52), cameraUpVector=(-0.444607, 0.734192, -0.513114), 
    cameraTarget=(1533.91, -96.7851, 2.38084), viewOffsetX=-164.595, 
    viewOffsetY=112.558)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5167.19, 
    farPlane=7570.1, width=1484.59, height=662.847, viewOffsetX=-168.112, 
    viewOffsetY=114.963)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5162.99, 
    farPlane=7574.3, width=1483.39, height=662.309, viewOffsetX=-186.765, 
    viewOffsetY=329.029)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5190.38, 
    farPlane=7546.92, width=1297.04, height=579.107, viewOffsetX=-187.756, 
    viewOffsetY=330.774)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5189.44, 
    farPlane=7547.86, width=1296.81, height=579.003, viewOffsetX=-182.535, 
    viewOffsetY=164.294)
o3 = session.openOdb(
    name='D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['A320-19'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=4800.98, 
    farPlane=7901.1, width=2158.96, height=963.943, viewOffsetX=-269.65, 
    viewOffsetY=191.922)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5080.18, 
    farPlane=7630.15, width=2284.52, height=1020, cameraPosition=(5147, 
    3922.26, 3172.63), cameraUpVector=(-0.511585, 0.495031, -0.7023), 
    cameraTarget=(1829.59, -100.253, -191.249), viewOffsetX=-285.332, 
    viewOffsetY=203.083)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5108.24, 
    farPlane=7581.27, width=2297.14, height=1025.64, cameraPosition=(4753, 
    2728.65, 4499.03), cameraUpVector=(-0.611205, 0.656628, -0.441892), 
    cameraTarget=(1842.55, -20.7238, -241.398), viewOffsetX=-286.908, 
    viewOffsetY=204.205)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5407, 
    farPlane=7221.88, width=2431.5, height=1085.63, cameraPosition=(3245.19, 
    -5029.48, 3189.84), cameraUpVector=(-0.0743743, 0.817489, 0.571122), 
    cameraTarget=(1769.05, -156.302, -356.221), viewOffsetX=-303.688, 
    viewOffsetY=216.148)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5654.35, 
    farPlane=6968.42, width=2542.74, height=1135.29, cameraPosition=(1527.46, 
    -249.493, 6159.06), cameraUpVector=(0.176649, 0.925173, -0.33593), 
    cameraTarget=(1700.88, -299.064, -43.2655), viewOffsetX=-317.58, 
    viewOffsetY=226.036)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5631.06, 
    farPlane=6993.91, width=2532.26, height=1130.62, cameraPosition=(1674.08, 
    2578.3, 5614.99), cameraUpVector=(-0.0849543, 0.697577, -0.711455), 
    cameraTarget=(1775.18, -134.822, 35.5517), viewOffsetX=-316.272, 
    viewOffsetY=225.105)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5631.43, 
    farPlane=6993.53, width=2532.44, height=1130.69, viewOffsetX=-365.253, 
    viewOffsetY=101.556)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-366.942, 
    viewOffsetY=130.331)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5476.75, 
    farPlane=7074.91, width=2462.88, height=1099.64, cameraPosition=(1006.31, 
    4490.67, 4238.21), cameraUpVector=(-0.0102824, 0.386146, -0.92238), 
    cameraTarget=(1756.11, -56.7982, 83.7191), viewOffsetX=-356.863, 
    viewOffsetY=126.751)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5657.74, 
    farPlane=6893.94, width=1294.99, height=578.193, viewOffsetX=-368.656, 
    viewOffsetY=130.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5652.37, 
    farPlane=6899.31, width=1293.76, height=577.644, viewOffsetX=-627.921, 
    viewOffsetY=160.217)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-614.12, 
    viewOffsetY=162.811)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5405.85, 
    farPlane=6959.96, width=1237.34, height=552.451, cameraPosition=(3156.47, 
    3545.23, 4614.51), cameraUpVector=(-0.0902085, 0.530654, -0.842774), 
    cameraTarget=(1762.3, -258.463, -85.4516), viewOffsetX=-587.337, 
    viewOffsetY=155.711)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5464.08, 
    farPlane=6901.73, width=891.195, height=397.904, viewOffsetX=-593.664, 
    viewOffsetY=157.388)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5674.64, 
    farPlane=6752.51, width=925.538, height=413.238, cameraPosition=(2384.88, 
    4124.72, 4405.93), cameraUpVector=(-0.234854, 0.457657, -0.857551), 
    cameraTarget=(1799.08, -100.369, -100.381), viewOffsetX=-616.542, 
    viewOffsetY=163.453)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5705.54, 
    farPlane=6831.75, width=930.577, height=415.488, cameraPosition=(1106.17, 
    4334.83, 4388.88), cameraUpVector=(-0.134146, 0.409446, -0.902418), 
    cameraTarget=(1794.71, -17.1569, 19.9564), viewOffsetX=-619.899, 
    viewOffsetY=164.343)
#: 
#: Node: A320-1.681
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.14100e+003,  6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.14107e+003,  6.85132e+001, -1.68827e+002,      -      
#: Deformed coordinates (scaled):     1.14107e+003,  6.85132e+001, -1.68827e+002,      -      
#: Displacement (unscaled):           7.48205e-002, -2.36757e-001,  1.45224e-001,  2.87649e-001
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5229.66, 
    farPlane=7073.65, width=852.962, height=380.834, cameraPosition=(4074.52, 
    2890.59, 4588.31), cameraUpVector=(-0.162497, 0.619104, -0.768314), 
    cameraTarget=(1766.17, -313.792, -197.592), viewOffsetX=-568.196, 
    viewOffsetY=150.636)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5209.42, 
    farPlane=7093.9, width=1066.87, height=476.339, viewOffsetX=-565.997, 
    viewOffsetY=150.053)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5049.69, 
    farPlane=7253.63, width=2132.15, height=951.972, viewOffsetX=-548.643, 
    viewOffsetY=145.452)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5223.16, 
    farPlane=7140.33, width=2205.4, height=984.675, cameraPosition=(3444.27, 
    2878.9, 4937.37), cameraUpVector=(-0.0951899, 0.629945, -0.770784), 
    cameraTarget=(1790.11, -291.952, -133.218), viewOffsetX=-567.49, 
    viewOffsetY=150.449)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5325.12, 
    farPlane=7038.37, width=1447.36, height=646.222, viewOffsetX=-578.568, 
    viewOffsetY=153.386)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5384.06, 
    farPlane=6912.31, width=1463.38, height=653.375, cameraPosition=(3215.57, 
    4819.52, 3236.14), cameraUpVector=(-0.270717, 0.280281, -0.920953), 
    cameraTarget=(1818.9, -203.787, -127.945), viewOffsetX=-584.971, 
    viewOffsetY=155.084)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5379.51, 
    farPlane=6916.85, width=1477.63, height=659.738, viewOffsetX=-584.477, 
    viewOffsetY=154.953)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5379.59, 
    farPlane=6916.77, width=1477.65, height=659.748, viewOffsetX=-508.633, 
    viewOffsetY=86.8077)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5342.62, 
    farPlane=7158.9, width=1467.5, height=655.214, cameraPosition=(3659.07, 
    482.315, 5663.27), cameraUpVector=(0.0946667, 0.860133, -0.501207), 
    cameraTarget=(1759.56, -314.588, -189.78), viewOffsetX=-505.137, 
    viewOffsetY=86.2111)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5528.54, 
    farPlane=6936, width=1518.57, height=678.016, cameraPosition=(2708.77, 
    3324.45, 4971.41), cameraUpVector=(0.0751499, 0.558246, -0.826265), 
    cameraTarget=(1790.35, -240.191, -23.7054), viewOffsetX=-522.715, 
    viewOffsetY=89.2111)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4871.39, 
    farPlane=7381.81, width=1338.06, height=597.425, cameraPosition=(5423.3, 
    3773.08, 2535.28), cameraUpVector=(-0.515189, 0.481589, -0.70898), 
    cameraTarget=(1700.32, -232.042, -397.25), viewOffsetX=-460.582, 
    viewOffsetY=78.607)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5165.57, 
    farPlane=7170.35, width=1418.87, height=633.504, cameraPosition=(4259.15, 
    3886.48, 3706.18), cameraUpVector=(-0.507347, 0.508257, -0.695898), 
    cameraTarget=(1779.87, -89.0019, -361.999), viewOffsetX=-488.397, 
    viewOffsetY=83.3541)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5155.51, 
    farPlane=7180.42, width=1416.11, height=632.271, viewOffsetX=-466.677, 
    viewOffsetY=106.855)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5207.01, 
    farPlane=7128.5, width=1430.26, height=638.587, cameraPosition=(4058.57, 
    4256.79, 3452.51), cameraUpVector=(-0.498155, 0.436855, -0.748998), 
    cameraTarget=(1789.5, -98.5614, -340.062), viewOffsetX=-471.339, 
    viewOffsetY=107.922)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5518.82, 
    farPlane=6890.99, width=1515.91, height=676.829, cameraPosition=(2710.06, 
    3563.09, 4772.39), cameraUpVector=(-0.162049, 0.561455, -0.811485), 
    cameraTarget=(1841.65, -115.736, -148.332), viewOffsetX=-499.564, 
    viewOffsetY=114.385)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4753.69, 
    farPlane=7531.12, width=1305.75, height=582.994, cameraPosition=(5982.56, 
    2082.74, 3379.22), cameraUpVector=(-0.348103, 0.725498, -0.593697), 
    cameraTarget=(1689.48, -254.133, -443.073), viewOffsetX=-430.305, 
    viewOffsetY=98.5267)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5020.15, 
    farPlane=7255.29, width=1378.94, height=615.675, cameraPosition=(4983.79, 
    4275.92, 2438.15), cameraUpVector=(-0.512145, 0.384664, -0.767946), 
    cameraTarget=(1766.1, -228.279, -365.43), viewOffsetX=-454.424, 
    viewOffsetY=104.049)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4901.85, 
    farPlane=7373.58, width=2101.46, height=938.269, viewOffsetX=-443.716, 
    viewOffsetY=101.597)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4975.51, 
    farPlane=7299.92, width=1650.87, height=737.088, viewOffsetX=-450.384, 
    viewOffsetY=103.124)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5105.21, 
    farPlane=7170.22, width=732.842, height=327.202, viewOffsetX=-462.124, 
    viewOffsetY=105.812)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5102.56, 
    farPlane=7172.87, width=732.462, height=327.032, viewOffsetX=-524.388, 
    viewOffsetY=145.902)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5371.33, 
    farPlane=7007.08, width=771.043, height=344.258, cameraPosition=(3791.54, 
    3260.88, 4549.14), cameraUpVector=(-0.38057, 0.610816, -0.694313), 
    cameraTarget=(1848.78, -80.8055, -304.748), viewOffsetX=-552.009, 
    viewOffsetY=153.587)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5357.7, 
    farPlane=7020.71, width=827.295, height=369.374, viewOffsetX=-550.609, 
    viewOffsetY=153.197)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5357.88, 
    farPlane=7020.53, width=827.323, height=369.386, viewOffsetX=-561.658, 
    viewOffsetY=132.742)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5299.89, 
    farPlane=7078.52, width=1222.98, height=546.039, viewOffsetX=-555.579, 
    viewOffsetY=131.305)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5183.72, 
    farPlane=7166.5, width=1196.17, height=534.072, cameraPosition=(4270.07, 
    3062.13, 4392.24), cameraUpVector=(-0.417851, 0.639603, -0.64522), 
    cameraTarget=(1825.86, -93.4039, -358.533), viewOffsetX=-543.401, 
    viewOffsetY=128.427)
# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by Till on Wed Feb 27 17:21:21 2019
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='A320-19', 
    inputFileName='D:/Documents/Studium/AA_Courses/Semester_6/SVV/Structures_Docs/FEM/A320-19.inp')
#: The model "A320-19" has been created.
#: The part "A320" has been imported from the input file.
#: 
#: WARNING: Node-based surfaces are not yet supported in Abaqus/CAE. The following node sets have been created in place of the corresponding node-based surfaces so they can be used in Abaqus/CAE. 
#: Node Set Created            Node-Based Surface  
#: ------------------          -------------------- 
#:     HINGE_2_CNS_                 HINGE_2_CNS_
#:     POINT_10_CNS_                POINT_10_CNS_
#:     POINT_11_CNS_                POINT_11_CNS_
#:     POINT_12_CNS_                POINT_12_CNS_
#:     POINT_13_CNS_                POINT_13_CNS_
#:     POINT_14_CNS_                POINT_14_CNS_
#:     POINT_15_CNS_                POINT_15_CNS_
#:     POINT_16_CNS_                POINT_16_CNS_
#:     POINT_6_CNS_                 POINT_6_CNS_
#:     POINT_7_CNS_                 POINT_7_CNS_
#:     POINT_8_CNS_                 POINT_8_CNS_
#:     POINT_9_CNS_                 POINT_9_CNS_
#:     RIB_A_CNS_                   RIB_A_CNS_
#:     RIB_B_CNS_                   RIB_B_CNS_
#:     RIB_C_CNS_                   RIB_C_CNS_
#:     RIB_D_CNS_                   RIB_D_CNS_
#: Constraint type MPC in Abaqus/CAE is created for *MPC definition.
#: WARNING: Creation of loads on  set/surfaces SET-38 failed due to following reason
#: 		: Load must be created with a non-zero magnitude unless utilizing a user subroutine. 
#: WARNING: Creation of loads on  set/surfaces SET-39 failed due to following reason
#: 		: Load must be created with a non-zero magnitude unless utilizing a user subroutine. 
#: 
#: WARNING: The following keywords/parameters are not yet supported by the input file reader:
#: ---------------------------------------------------------------------------------
#: *PREPRINT
#: The model "A320-19" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['A320-19'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4767.77, 
    farPlane=7642.16, width=2784.37, height=1243.18, viewOffsetX=-59.3999, 
    viewOffsetY=-33.4988)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4769.18, 
    farPlane=7669.39, width=2785.2, height=1243.55, cameraPosition=(5199.07, 
    2945.72, 3773.57), cameraUpVector=(-0.552208, 0.65953, -0.509986), 
    cameraTarget=(1508.66, -76.6583, -194.764), viewOffsetX=-59.4174, 
    viewOffsetY=-33.5087)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4644.76, 
    farPlane=7828.2, width=2712.54, height=1211.11, cameraPosition=(5970.25, 
    2467.01, 3275.26), cameraUpVector=(-0.568024, 0.722535, -0.394071), 
    cameraTarget=(1503.1, -77.3033, -199.31), viewOffsetX=-57.8673, 
    viewOffsetY=-32.6345)
mdb.Job(name='Job-1', model='A320-19', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMData/Job-1.odb')
#: Model: D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMData/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          66
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Out-of-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5001.21, 
    farPlane=7183.99, width=2920.7, height=1304.04, cameraPosition=(3009.71, 
    2908.74, 5017.84), cameraUpVector=(-0.516583, 0.612453, -0.598367), 
    cameraTarget=(1527.75, -77.2443, -215.642))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4887.44, 
    farPlane=7349.5, width=2854.26, height=1274.38, cameraPosition=(3644.23, 
    2391.31, 5067.92), cameraUpVector=(-0.526044, 0.688132, -0.499752), 
    cameraTarget=(1516.05, -67.7012, -216.566))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5094.27, 
    farPlane=7091.74, width=2975.05, height=1328.31, cameraPosition=(2595.26, 
    2226.73, 5445.11), cameraUpVector=(-0.454213, 0.692938, -0.559935), 
    cameraTarget=(1530.88, -65.3745, -221.899))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4582.35, 
    farPlane=7728.5, width=2676.09, height=1194.83, cameraPosition=(5349.17, 
    2816.46, 3704.41), cameraUpVector=(-0.606406, 0.670815, -0.426941), 
    cameraTarget=(1480.27, -76.2117, -189.911))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4486.44, 
    farPlane=8056.46, width=2620.08, height=1169.82, cameraPosition=(7651.27, 
    373.893, -81.3265), cameraUpVector=(-0.395303, 0.795911, 0.458543), 
    cameraTarget=(1461.74, -56.5526, -159.441))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4498.54, 
    farPlane=8075.78, width=2627.15, height=1172.98, cameraPosition=(7154.23, 
    -928.616, 2166.7), cameraUpVector=(-0.406446, 0.815719, 0.411588), 
    cameraTarget=(1456.47, -70.3593, -135.612))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4498.48, 
    farPlane=8075.84, width=2627.12, height=1172.97, viewOffsetX=-110.339, 
    viewOffsetY=8.77967)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5231.35, 
    farPlane=7519.05, width=3055.13, height=1364.07, cameraPosition=(3514.97, 
    -1051.65, 5776.46), cameraUpVector=(-0.473972, 0.879392, -0.0449411), 
    cameraTarget=(1485.45, -89.1186, -7.68628), viewOffsetX=-128.315, 
    viewOffsetY=10.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5026.86, 
    farPlane=7705.8, width=2935.71, height=1310.75, cameraPosition=(4214.27, 
    -1115.2, 5452.27), cameraUpVector=(-0.424946, 0.905218, 0.000767786), 
    cameraTarget=(1501.06, -99.3446, -34.8274), viewOffsetX=-123.299, 
    viewOffsetY=9.81089)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5037.77, 
    farPlane=7694.87, width=2942.09, height=1313.6, viewOffsetX=-123.567, 
    viewOffsetY=9.83219)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5063.39, 
    farPlane=7599, width=2957.06, height=1320.28, cameraPosition=(4021.76, 
    106.13, 5630.39), cameraUpVector=(-0.447512, 0.873034, -0.193765), 
    cameraTarget=(1496.95, -76.292, -34.7408), viewOffsetX=-124.195, 
    viewOffsetY=9.8822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5061.45, 
    farPlane=7600.93, width=2955.93, height=1319.77, viewOffsetX=-597.096, 
    viewOffsetY=320.065)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5407.71, 
    farPlane=8721.6, width=3158.15, height=1410.06, cameraPosition=(-3353.38, 
    -1039.99, 5026.56), cameraUpVector=(0.112089, 0.972305, -0.205085), 
    cameraTarget=(1144.84, -319.943, 813.574), viewOffsetX=-637.944, 
    viewOffsetY=341.961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5643.05, 
    farPlane=8584.79, width=3295.59, height=1471.43, cameraPosition=(-3245.4, 
    4166.18, 3561.61), cameraUpVector=(0.856963, -0.21413, 0.468788), 
    cameraTarget=(-3.61121, 91.7556, 186.467), viewOffsetX=-665.707, 
    viewOffsetY=356.843)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5821, 
    farPlane=8615.76, width=3399.52, height=1517.83, cameraPosition=(-3245, 
    5620.96, 954.038), cameraUpVector=(0.655708, -0.162979, 0.737214), 
    cameraTarget=(-97.6777, 398.193, -194.344), viewOffsetX=-686.699, 
    viewOffsetY=368.096)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5805.82, 
    farPlane=8630.93, width=3390.66, height=1513.87, viewOffsetX=-219.259, 
    viewOffsetY=362.604)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5805.72, 
    farPlane=8631.04, width=3390.6, height=1513.85, cameraPosition=(-3277.45, 
    5566.34, 1113.53), cameraUpVector=(0.839073, -0.0099802, 0.543927), 
    cameraTarget=(-130.13, 343.568, -34.8545), viewOffsetX=-219.255, 
    viewOffsetY=362.598)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5701.23, 
    farPlane=9230.9, width=3329.58, height=1486.6, cameraPosition=(-5104.03, 
    3341.34, -2172.32), cameraUpVector=(0.563037, 0.510796, 0.649674), 
    cameraTarget=(-246.047, -125.018, -473.463), viewOffsetX=-215.309, 
    viewOffsetY=356.072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5709.17, 
    farPlane=9222.96, width=3334.22, height=1488.67, viewOffsetX=-113.359, 
    viewOffsetY=641.823)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6313.29, 
    farPlane=9506.12, width=3687.03, height=1646.2, cameraPosition=(-3838.94, 
    249.047, 5915.19), cameraUpVector=(0.67656, 0.735149, -0.04269), 
    cameraTarget=(-16.8047, -733.055, 1126.82), viewOffsetX=-125.354, 
    viewOffsetY=709.738)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6926.76, 
    farPlane=9010.29, width=4045.3, height=1806.16, cameraPosition=(2642, 
    -1436.85, 7679.52), cameraUpVector=(0.052717, 0.95189, -0.301871), 
    cameraTarget=(1698.13, -1154.52, 1553.26), viewOffsetX=-137.535, 
    viewOffsetY=778.704)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5987.44, 
    farPlane=9826.36, width=3496.73, height=1561.23, cameraPosition=(8330.8, 
    559.15, 3784.59), cameraUpVector=(-0.569662, 0.821169, -0.0341571), 
    cameraTarget=(3186.93, -626.161, 523.101), viewOffsetX=-118.884, 
    viewOffsetY=673.107)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6270.05, 
    farPlane=9676.49, width=3661.78, height=1634.93, cameraPosition=(7319.75, 
    -1573.82, 5051.57), cameraUpVector=(-0.558364, 0.808532, 0.185754), 
    cameraTarget=(3014.79, -971.386, 623.705), viewOffsetX=-124.495, 
    viewOffsetY=704.878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6428.26, 
    farPlane=9355.53, width=3754.18, height=1676.18, cameraPosition=(5605.82, 
    1263.47, 6522.04), cameraUpVector=(-0.665494, 0.702551, -0.25207), 
    cameraTarget=(2781.81, -362.174, 1241.52), viewOffsetX=-127.636, 
    viewOffsetY=722.664)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6414.93, 
    farPlane=9368.86, width=3746.4, height=1672.71, viewOffsetX=117.393, 
    viewOffsetY=926.498)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6616.04, 
    farPlane=9153.78, width=3863.85, height=1725.15, cameraPosition=(4219.08, 
    2122.34, 7018.29), cameraUpVector=(-0.602755, 0.654564, -0.456324), 
    cameraTarget=(2470.55, -161.005, 1520.05), viewOffsetX=121.073, 
    viewOffsetY=955.543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6600.76, 
    farPlane=9169.06, width=3854.93, height=1721.17, viewOffsetX=516.566, 
    viewOffsetY=726.595)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6528.51, 
    farPlane=9288.21, width=3812.75, height=1702.33, cameraPosition=(4804.86, 
    225.83, 7069.91), cameraUpVector=(-0.478104, 0.830299, -0.286391), 
    cameraTarget=(2455.61, -596.381, 1386.01), viewOffsetX=510.912, 
    viewOffsetY=718.642)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6533.99, 
    farPlane=9282.74, width=3815.95, height=1703.76, viewOffsetX=-147.547, 
    viewOffsetY=816.166)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6113.04, 
    farPlane=9919.74, width=3570.11, height=1594, cameraPosition=(-5352.81, 
    -1664.62, 3983.47), cameraUpVector=(0.25116, 0.965823, -0.0640601), 
    cameraTarget=(-39.8621, -1114.18, 825.733), viewOffsetX=-138.041, 
    viewOffsetY=763.585)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6281.79, 
    farPlane=9743.4, width=3668.67, height=1638, cameraPosition=(-4449.6, 
    -1060.53, 5343.51), cameraUpVector=(0.36139, 0.928409, -0.0863415), 
    cameraTarget=(60.546, -984.584, 1082.7), viewOffsetX=-141.852, 
    viewOffsetY=784.664)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7100.01, 
    farPlane=8921.76, width=4146.52, height=1851.36, cameraPosition=(1482.59, 
    -3141.74, 7281.01), cameraUpVector=(-0.137244, 0.988759, -0.05933), 
    cameraTarget=(1661.23, -1382, 1333.48), viewOffsetX=-160.329, 
    viewOffsetY=886.868)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6059, 
    farPlane=9937.97, width=3538.56, height=1579.91, cameraPosition=(8489.28, 
    582.284, 3656.39), cameraUpVector=(-0.575351, 0.81782, 0.0118827), 
    cameraTarget=(3287.41, -501.714, 452.135), viewOffsetX=-136.821, 
    viewOffsetY=756.834)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6132.84, 
    farPlane=9864.13, width=3581.68, height=1599.16, viewOffsetX=-138.488, 
    viewOffsetY=766.057)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6251.7, 
    farPlane=9738.49, width=3651.09, height=1630.16, cameraPosition=(7612.36, 
    1858.87, 4670.54), cameraUpVector=(-0.716136, 0.692912, -0.0837985), 
    cameraTarget=(3250.46, -140.093, 736.104), viewOffsetX=-141.172, 
    viewOffsetY=780.904)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6242.71, 
    farPlane=9747.48, width=3645.86, height=1627.82, viewOffsetX=622.23, 
    viewOffsetY=221.743)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6266.57, 
    farPlane=9826.56, width=3659.8, height=1634.04, cameraPosition=(7909.71, 
    663.073, 4676.92), cameraUpVector=(-0.687894, 0.722597, 0.0682303), 
    cameraTarget=(3315.01, -469.677, 663.511), viewOffsetX=624.608, 
    viewOffsetY=222.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6264.75, 
    farPlane=9828.38, width=3658.74, height=1633.57, viewOffsetX=624.427, 
    viewOffsetY=259.207)
#: 
#: Element: A320-1.2296
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2791, 2792, 2809, 2808
#:   S, S12 (Not averaged): 0.000224601
#: 
#: Element: A320-1.2296
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2791, 2792, 2809, 2808
#:   S, S12 (Not averaged): 0.000224601
#: 
#: Element: A320-1.975
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 1612, 1613, 1630, 1629
#:   S, S12 (Not averaged): -0.00153979
session.viewports['Viewport: 1'].view.setValues(nearPlane=6477.03, 
    farPlane=9616.1, width=2037.43, height=909.68, viewOffsetX=585.082, 
    viewOffsetY=357.813)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6493.8, 
    farPlane=9599.33, width=2042.71, height=912.035, viewOffsetX=257.04, 
    viewOffsetY=702.801)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6436.77, 
    farPlane=9656.37, width=2593.37, height=1157.9, viewOffsetX=283.97, 
    viewOffsetY=709.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6416.97, 
    farPlane=9676.16, width=2585.39, height=1154.34, viewOffsetX=-592.489, 
    viewOffsetY=1071.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6349.3, 
    farPlane=7917.92, width=2558.13, height=1142.17, cameraPosition=(2688.71, 
    -3223.6, 6187.93), cameraUpVector=(-0.47609, 0.879345, 0.00950763), 
    cameraTarget=(2429.03, -949.741, 420.436), viewOffsetX=-586.24, 
    viewOffsetY=1060.68)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6352.94, 
    farPlane=7914.28, width=2559.61, height=1142.82, viewOffsetX=-724.795, 
    viewOffsetY=1191.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4351.06, 
    farPlane=7770.72, width=1753.05, height=782.708, cameraPosition=(-3496.02, 
    -1780.82, 3023.8), cameraUpVector=(0.141726, 0.988905, -0.0444969), 
    cameraTarget=(1621.1, -570.914, -270.595), viewOffsetX=-496.404, 
    viewOffsetY=815.915)
#: 
#: Element: A320-1.975
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 1612, 1613, 1630, 1629
#:   S, S12 (Not averaged): -0.00153979
session.viewports['Viewport: 1'].view.setValues(nearPlane=4486.35, 
    farPlane=7734.83, width=1807.56, height=807.047, cameraPosition=(-4113.13, 
    -512.215, 2743.91), cameraUpVector=(0.528256, 0.845452, 0.0784642), 
    cameraTarget=(1238.43, -1123.71, -336.469), viewOffsetX=-511.839, 
    viewOffsetY=841.285)
#: 
#: Element: A320-1.5148
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5284, 5285, 5302, 5301
#:   S, S12 (Not averaged): -0.000248993
#: 
#: Element: A320-1.5148
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5284, 5285, 5302, 5301
#:   S, S12 (Not averaged): -0.000248993
#: 
#: Element: A320-1.6522
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6482, 6483, 6500, 6499
#:   S, S12 (Not averaged): 0.00823031
#: 
#: Element: A320-1.6522
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6482, 6483, 6500, 6499
#:   S, S12 (Not averaged): 0.00823031
session.viewports['Viewport: 1'].view.setValues(nearPlane=4456.19, 
    farPlane=7764.99, width=1998.89, height=892.472, viewOffsetX=-508.398, 
    viewOffsetY=835.629)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4457.91, 
    farPlane=7763.27, width=1999.66, height=892.818, viewOffsetX=-353.954, 
    viewOffsetY=842.635)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4322.62, 
    farPlane=6003.38, width=1938.98, height=865.722, cameraPosition=(41.4164, 
    -1663.73, 4661.29), cameraUpVector=(0.111751, 0.980946, -0.158925), 
    cameraTarget=(1047.87, -648.143, -1376.71), viewOffsetX=-343.212, 
    viewOffsetY=817.062)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3992.81, 
    farPlane=6333.18, width=3988.04, height=1780.6, viewOffsetX=-317.025, 
    viewOffsetY=754.721)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4033.94, 
    farPlane=6292.05, width=4029.13, height=1798.94, viewOffsetX=370.034, 
    viewOffsetY=767.881)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4034.76, 
    farPlane=6291.23, width=4029.95, height=1799.31, viewOffsetX=429.216, 
    viewOffsetY=776.119)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3883.6, 
    farPlane=5859.49, width=3878.98, height=1731.9, cameraPosition=(1231.14, 
    -67.102, 4831.41), cameraUpVector=(-0.0189247, 0.886414, -0.462505), 
    cameraTarget=(851.753, -941.06, -1299.99), viewOffsetX=413.136, 
    viewOffsetY=747.043)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3901.98, 
    farPlane=5841.12, width=3897.34, height=1740.1, viewOffsetX=415.091, 
    viewOffsetY=750.579)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3902.35, 
    farPlane=5840.76, width=3897.71, height=1740.27, viewOffsetX=-572.289, 
    viewOffsetY=768.886)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4126.85, 
    farPlane=7828.19, width=4121.96, height=1840.39, cameraPosition=(-3463.31, 
    662.457, 3494.53), cameraUpVector=(0.463798, 0.812788, -0.352517), 
    cameraTarget=(1294.21, -1064.49, -95.0993), viewOffsetX=-605.213, 
    viewOffsetY=813.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4438.97, 
    farPlane=7516.06, width=1838.53, height=820.875, viewOffsetX=-650.986, 
    viewOffsetY=874.618)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4450.35, 
    farPlane=7609.1, width=1843.25, height=822.98, cameraPosition=(-3441.77, 
    -1461.06, 3241.66), cameraUpVector=(0.226884, 0.972343, -0.0554289), 
    cameraTarget=(1552.6, -704.739, -361.953), viewOffsetX=-652.655, 
    viewOffsetY=876.861)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4400.27, 
    farPlane=7124.64, width=1822.51, height=813.72, cameraPosition=(-2418.82, 
    -677.428, 4245.16), cameraUpVector=(0.273224, 0.929945, -0.246071), 
    cameraTarget=(1395.08, -868.015, -645.611), viewOffsetX=-645.31, 
    viewOffsetY=866.993)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4402.93, 
    farPlane=7121.98, width=1823.61, height=814.214, cameraPosition=(-2666.96, 
    -868.24, 4059.09), cameraUpVector=(0.495576, 0.865725, -0.0701749), 
    cameraTarget=(1146.94, -1058.83, -831.682), viewOffsetX=-645.701, 
    viewOffsetY=867.518)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4474.2, 
    farPlane=7663.02, width=1853.13, height=827.394, cameraPosition=(-3972.79, 
    -810.997, 2863.89), cameraUpVector=(0.553095, 0.817997, 0.158011), 
    cameraTarget=(1200.75, -1121.61, -547.824), viewOffsetX=-656.153, 
    viewOffsetY=881.561)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4067.28, 
    farPlane=7935.05, width=3430.82, height=1531.81, viewOffsetX=-596.477, 
    viewOffsetY=801.385)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4146.84, 
    farPlane=7855.49, width=3120.92, height=1393.44, viewOffsetX=-608.145, 
    viewOffsetY=817.061)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4285.49, 
    farPlane=7862.66, width=3225.27, height=1440.03, viewOffsetX=-783.292, 
    viewOffsetY=1182.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4287.07, 
    farPlane=7861.08, width=3226.46, height=1440.56, viewOffsetX=-430.821, 
    viewOffsetY=874.882)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4287.09, 
    farPlane=7861.06, width=3226.47, height=1440.57, viewOffsetX=-469.541, 
    viewOffsetY=943.895)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4313.79, 
    farPlane=7967.4, width=3246.57, height=1449.54, cameraPosition=(-4371.25, 
    821.422, 2292.9), cameraUpVector=(0.663955, 0.747152, -0.0304547), 
    cameraTarget=(1010.41, -1284.83, 33.8618), viewOffsetX=-472.466, 
    viewOffsetY=949.774)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4394.13, 
    farPlane=8163.19, width=3307.03, height=1476.54, cameraPosition=(-4810.95, 
    127.568, 1446.09), cameraUpVector=(0.519482, 0.854418, 0.0104228), 
    cameraTarget=(1168.33, -1073.15, 302.279), viewOffsetX=-481.265, 
    viewOffsetY=967.461)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4437.46, 
    farPlane=8162.06, width=3339.65, height=1491.1, cameraPosition=(-5023.69, 
    642.733, 358.537), cameraUpVector=(0.576129, 0.817358, -0.00101132), 
    cameraTarget=(942.976, -1032.13, 667.716), viewOffsetX=-486.011, 
    viewOffsetY=977.001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4340.57, 
    farPlane=8096.5, width=3266.73, height=1458.54, cameraPosition=(-4518.45, 
    779.813, 2025.84), cameraUpVector=(0.541445, 0.804035, -0.245692), 
    cameraTarget=(1198.07, -996.48, 392.431), viewOffsetX=-475.399, 
    viewOffsetY=955.668)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4431.27, 
    farPlane=8005.81, width=2745.87, height=1225.99, viewOffsetX=-485.332, 
    viewOffsetY=975.637)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4424.78, 
    farPlane=8012.3, width=2741.85, height=1224.19, viewOffsetX=-484.621, 
    viewOffsetY=974.208)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4511.43, 
    farPlane=7925.64, width=2171.99, height=969.758, viewOffsetX=-494.111, 
    viewOffsetY=993.286)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4505.92, 
    farPlane=7931.16, width=2169.34, height=968.574, viewOffsetX=-623.667, 
    viewOffsetY=638.281)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4546.86, 
    farPlane=7890.21, width=1897.4, height=847.158, viewOffsetX=-629.334, 
    viewOffsetY=644.081)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4490.34, 
    farPlane=7739.37, width=1873.82, height=836.629, cameraPosition=(-4084.31, 
    1075.5, 2668.09), cameraUpVector=(0.563904, 0.765977, -0.308692), 
    cameraTarget=(1186.52, -1093.18, 215.135), viewOffsetX=-621.511, 
    viewOffsetY=636.075)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#: 
#: Element: A320-1.6522
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6482, 6483, 6500, 6499
#:   S, Mises (Not averaged): 0.0151912
#: 
#: Element: A320-1.5148
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5284, 5285, 5302, 5301
#:   S, Mises (Not averaged): 0.000496533
#: 
#: Element: A320-1.975
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 1612, 1613, 1630, 1629
#:   S, Mises (Not averaged): 0.00713625
#: 
#: Element: A320-1.2296
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 2791, 2792, 2809, 2808
#:   S, Mises (Not averaged): 0.000403995
#: 
#: Element: A320-1.975
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 1612, 1613, 1630, 1629
#:   S, Mises (Not averaged): 0.00713625
#: 
#: Element: A320-1.5148
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5284, 5285, 5302, 5301
#:   S, Mises (Not averaged): 0.000496533
#: 
#: Element: A320-1.6522
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 6482, 6483, 6500, 6499
#:   S, Mises (Not averaged): 0.0151912
#: 
#: Node: A320-1.2808
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.72600e+003, -6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.72715e+003,  2.47695e+001, -2.00012e+002,      -      
#: Deformed coordinates (scaled):     2.72715e+003,  2.47695e+001, -2.00012e+002,      -      
#: Displacement (unscaled):           1.14908e+000,  9.35195e+001, -3.10401e+001,  9.85429e+001
#: 
#: Node: A320-1.1629
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.50460e+003, -6.25000e+001, -1.93111e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.50563e+003,  3.80489e+001, -2.21438e+002,      -      
#: Deformed coordinates (scaled):     2.50563e+003,  3.80489e+001, -2.21438e+002,      -      
#: Displacement (unscaled):           1.03300e+000,  1.00549e+002, -2.83273e+001,  1.04468e+002
#: 
#: Node: A320-1.5301
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.55000e+001, -5.62500e+001, -2.17250e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.46943e+001,  5.50406e+001, -2.42768e+002,      -      
#: Deformed coordinates (scaled):     2.46943e+001,  5.50406e+001, -2.42768e+002,      -      
#: Displacement (unscaled):          -8.05656e-001,  1.11291e+002, -2.55183e+001,  1.14182e+002
#: 
#: Node: A320-1.6522
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.77700e+002, -9.37500e+001, -7.24167e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   1.76378e+002, -5.02236e+001, -1.14930e+002,      -      
#: Deformed coordinates (scaled):     1.76378e+002, -5.02236e+001, -1.14930e+002,      -      
#: Displacement (unscaled):          -1.32152e+000,  4.35264e+001, -4.25135e+001,  6.08579e+001
session.viewports['Viewport: 1'].view.setValues(nearPlane=4493.35, 
    farPlane=7736.36, width=1875.08, height=837.192, cameraPosition=(-4152.53, 
    991.089, 2596.13), cameraUpVector=(0.607412, 0.764939, -0.214286), 
    cameraTarget=(1118.3, -1177.59, 143.172), viewOffsetX=-621.928, 
    viewOffsetY=636.502)
#: 
#: Node: A320-1.6499
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02400e+002, -5.62500e+001, -2.17250e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Deformed coordinates (scaled):     2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Displacement (unscaled):          -8.02620e-001,  1.08852e+002, -2.55023e+001,  1.11802e+002
#: 
#: Node: A320-1.1629
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.50460e+003, -6.25000e+001, -1.93111e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.50563e+003,  3.80489e+001, -2.21438e+002,      -      
#: Deformed coordinates (scaled):     2.50563e+003,  3.80489e+001, -2.21438e+002,      -      
#: Displacement (unscaled):           1.03300e+000,  1.00549e+002, -2.83273e+001,  1.04468e+002
#: 
#: Node: A320-1.2808
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.72600e+003, -6.87500e+001, -1.68972e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.72715e+003,  2.47695e+001, -2.00012e+002,      -      
#: Deformed coordinates (scaled):     2.72715e+003,  2.47695e+001, -2.00012e+002,      -      
#: Displacement (unscaled):           1.14908e+000,  9.35195e+001, -3.10401e+001,  9.85429e+001
session.viewports['Viewport: 1'].view.setValues(nearPlane=4446.56, 
    farPlane=7783.15, width=2182.24, height=974.334, viewOffsetX=-615.452, 
    viewOffsetY=629.874)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4449.59, 
    farPlane=7780.12, width=2183.73, height=975, viewOffsetX=-615.872, 
    viewOffsetY=630.303)
#: 
#: Node: A320-1.6499
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02400e+002, -5.62500e+001, -2.17250e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Deformed coordinates (scaled):     2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Displacement (unscaled):          -8.02620e-001,  1.08852e+002, -2.55023e+001,  1.11802e+002
#: 
#: Node: A320-1.5301
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.55000e+001, -5.62500e+001, -2.17250e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.46943e+001,  5.50406e+001, -2.42768e+002,      -      
#: Deformed coordinates (scaled):     2.46943e+001,  5.50406e+001, -2.42768e+002,      -      
#: Displacement (unscaled):          -8.05656e-001,  1.11291e+002, -2.55183e+001,  1.14182e+002
session.viewports['Viewport: 1'].view.setValues(nearPlane=4449.61, 
    farPlane=7780.1, width=2183.74, height=975.004, viewOffsetX=-615.874, 
    viewOffsetY=630.305)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4138.64, 
    farPlane=5582.64, width=2031.13, height=906.866, cameraPosition=(1064.76, 
    -711.88, 4807.91), cameraUpVector=(0.216264, 0.892416, -0.396008), 
    cameraTarget=(590.44, -1021.26, -1371.18), viewOffsetX=-572.833, 
    viewOffsetY=586.255)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3386.23, 
    farPlane=5636.71, width=1661.87, height=741.998, cameraPosition=(3096.61, 
    2944.85, 2874.97), cameraUpVector=(-0.579366, 0.464335, -0.669872), 
    cameraTarget=(712.243, -1231.93, -1045.63), viewOffsetX=-468.692, 
    viewOffsetY=479.674)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3703.92, 
    farPlane=5577.22, width=1817.78, height=811.611, cameraPosition=(2571.46, 
    2182.85, 3809.87), cameraUpVector=(-0.745428, 0.512511, -0.426227), 
    cameraTarget=(933.865, -579.063, -1499.74), viewOffsetX=-512.664, 
    viewOffsetY=524.676)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4381.61, 
    farPlane=5815.38, width=2150.37, height=960.107, cameraPosition=(710.775, 
    -407.089, 4900.28), cameraUpVector=(-0.558928, 0.752949, -0.347372), 
    cameraTarget=(1392.76, 7.19823, -1253.19), viewOffsetX=-606.464, 
    viewOffsetY=620.673)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4336.55, 
    farPlane=5860.44, width=2128.26, height=950.234, viewOffsetX=-594.552, 
    viewOffsetY=639.895)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4427.07, 
    farPlane=7669.72, width=2172.69, height=970.07, cameraPosition=(-3599.95, 
    -125.843, 3403.22), cameraUpVector=(0.340467, 0.894792, -0.288841), 
    cameraTarget=(1451.29, -874.275, -121.941), viewOffsetX=-606.963, 
    viewOffsetY=653.252)
#: 
#: Node: A320-1.6499
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02400e+002, -5.62500e+001, -2.17250e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Deformed coordinates (scaled):     2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Displacement (unscaled):          -8.02620e-001,  1.08852e+002, -2.55023e+001,  1.11802e+002
session.viewports['Viewport: 1'].view.setValues(nearPlane=4354.57, 
    farPlane=5926.41, width=2137.11, height=954.185, cameraPosition=(159.461, 
    3006.91, 4043.28), cameraUpVector=(0.249334, 0.419758, -0.872718), 
    cameraTarget=(832.954, -1412.48, -259.89), viewOffsetX=-597.023, 
    viewOffsetY=642.554)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4352.69, 
    farPlane=6027.56, width=2136.19, height=953.774, cameraPosition=(-47.7549, 
    2900.88, 4112.3), cameraUpVector=(0.263903, 0.447614, -0.854399), 
    cameraTarget=(873.109, -1391.53, -272.803), viewOffsetX=-596.766, 
    viewOffsetY=642.277)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4209.87, 
    farPlane=5761.52, cameraPosition=(211.885, 3066.94, 3834.43), 
    cameraUpVector=(0.169948, 0.531634, -0.829749), cameraTarget=(197.033, 
    -96.2811, -280.327))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4343.76, 
    farPlane=5627.63, width=1974.78, height=881.707, cameraPosition=(212.513, 
    3024.41, 3867.12), cameraTarget=(197.661, -138.809, -247.636))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4376.93, 
    farPlane=5607.82, cameraPosition=(276.095, 3992.39, 2948.51), 
    cameraUpVector=(0.12965, 0.299154, -0.945356), cameraTarget=(201.932, 
    -134.751, -197.694))
#: 
#: Node: A320-1.6499
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02400e+002, -5.62500e+001, -2.17250e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Deformed coordinates (scaled):     2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Displacement (unscaled):          -8.02620e-001,  1.08852e+002, -2.55023e+001,  1.11802e+002
#: 
#: Node: A320-1.5191
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02400e+002,  1.06250e+002, -2.41389e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.03793e+002,  1.27516e+002,  2.40573e+001,      -      
#: Deformed coordinates (scaled):     2.03793e+002,  1.27516e+002,  2.40573e+001,      -      
#: Displacement (unscaled):           1.39290e+000,  2.12664e+001,  4.81962e+001,  5.26980e+001
#: 
#: Node: A320-1.5191
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02400e+002,  1.06250e+002, -2.41389e+001,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.03793e+002,  1.27516e+002,  2.40573e+001,      -      
#: Deformed coordinates (scaled):     2.03793e+002,  1.27516e+002,  2.40573e+001,      -      
#: Displacement (unscaled):           1.39290e+000,  2.12664e+001,  4.81962e+001,  5.26980e+001
#: 
#: ODB: Job-1.odb
#:    Number of nodes: 6570
#:    Number of elements: 6608
#:    Element types: S4R 
#: 
#: Element: A320-1.5013
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 672, 5174, 5191, 673
#:   S, Mises (Not averaged): 0.0149251
#: 
#: Node: A320-1.6499
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.02400e+002, -5.62500e+001, -2.17250e+002,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Deformed coordinates (scaled):     2.01597e+002,  5.26018e+001, -2.42752e+002,      -      
#: Displacement (unscaled):          -8.02620e-001,  1.08852e+002, -2.55023e+001,  1.11802e+002
#: 
#: Node: A320-1.672
#:                                         1             2             3        Magnitude
#: Base coordinates:                  2.27100e+002,  1.12500e+002,  0.00000e+000,      -      
#: Scale:                             1.00000e+000,  1.00000e+000,  1.00000e+000,      -      
#: Deformed coordinates (unscaled):   2.28582e+002,  1.22464e+002,  5.10344e+001,      -      
#: Deformed coordinates (scaled):     2.28582e+002,  1.22464e+002,  5.10344e+001,      -      
#: Displacement (unscaled):           1.48195e+000,  9.96408e+000,  5.10344e+001,  5.20191e+001
#: 
#: Element: A320-1.5013
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 672, 5174, 5191, 673
#:   S, Mises (Not averaged): 0.0149251
#: 
#: Element: A320-1.5013
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 672, 5174, 5191, 673
#:   S, Mises (Not averaged): 0.0149251
#: 
#: Element: A320-1.4995
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 671, 5157, 5174, 672
#:   S, Mises (Not averaged): 0.0221179
#: 
#: Element: A320-1.4996
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 5157, 5158, 5175, 5174
#:   S, Mises (Not averaged): 0.0139318
#: 
#: Element: A320-1.4310
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4525, 4526, 671, 672
#:   S, Mises (Not averaged): 0.0253085
#: 
#: Element: A320-1.4150
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4369, 4370, 4409, 4408
#:   S, Mises (Not averaged): 0.0372795
session.viewports['Viewport: 1'].view.setValues(nearPlane=4171.14, 
    farPlane=5813.61, width=3426.37, height=1529.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1875.35, 
    farPlane=5694.9, cameraPosition=(4980.45, 115.769, 1084.09), 
    cameraUpVector=(-0.138587, 0.458254, -0.87795), cameraTarget=(-39.4005, 
    -114.404, -214.171))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1875.35, 
    farPlane=5694.9, cameraPosition=(4996.67, 110.624, 1022.28), cameraTarget=(
    -23.1786, -119.549, -275.982))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1884.92, 
    farPlane=5674.24, cameraPosition=(5128.82, -100.67, -712.07), 
    cameraUpVector=(-0.403491, 0.529158, -0.746449), cameraTarget=(-40.1435, 
    -112.532, -244.071))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(5117.45, 
    -21.287, -835.626), cameraUpVector=(-0.344923, 0.934373, -0.0893029), 
    cameraTarget=(-51.5125, -33.149, -367.627))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1884.92, 
    farPlane=5674.24, cameraPosition=(5107.37, -132.977, -949.812), 
    cameraTarget=(-61.5946, -144.839, -481.813))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1884.92, 
    farPlane=5674.25, cameraPosition=(5104.91, -94.567, -976.028), 
    cameraUpVector=(-0.333241, 0.941996, 0.0399126), cameraTarget=(-64.0563, 
    -106.429, -508.029))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1884.92, 
    farPlane=5674.25, cameraPosition=(5132.64, -38.1995, -668.305), 
    cameraTarget=(-36.3244, -50.0615, -200.306))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(5152.98, 
    0.693893, -442.667), cameraTarget=(-15.9844, -11.1681, 25.3318))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1966.56, 
    farPlane=5733.6, cameraPosition=(4587.78, 532.769, 2055.2), 
    cameraUpVector=(-0.42548, 0.89761, -0.115168), cameraTarget=(-114.825, 
    -40.9583, -64.6283))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1966.55, 
    farPlane=5733.6, cameraPosition=(4715.76, 419.034, 1802.06), cameraTarget=(
    13.1588, -154.694, -317.764))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(4681.77, 
    419.788, 1877.25), cameraTarget=(-20.8278, -153.94, -242.572))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1966.54, 
    farPlane=5733.59, cameraPosition=(4861.89, 445.781, 1470.64), 
    cameraTarget=(159.293, -127.947, -649.185))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2362.44, 
    farPlane=5480.76, cameraPosition=(3674.76, 1329.56, 2779.71), 
    cameraUpVector=(-0.398895, 0.767038, -0.502529), cameraTarget=(711.018, 
    -482.623, -1076.38))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2532.6, 
    farPlane=5310.6, width=2226.12, height=993.925)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(3488.56, 
    1485.22, 2849.66), cameraTarget=(524.823, -326.96, -1006.43))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2480.43, 
    farPlane=5353.08, cameraPosition=(3646.39, 1415.63, 2759.98), 
    cameraUpVector=(-0.407795, 0.779865, -0.474884), cameraTarget=(465.528, 
    -298.126, -965.912))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2192.36, 
    farPlane=5544.37, cameraPosition=(4548.88, 958.727, 1910.58), 
    cameraUpVector=(-0.489878, 0.850241, -0.192637), cameraTarget=(129.022, 
    -119.086, -587.485))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2192.36, 
    farPlane=5544.37, cameraPosition=(4722.31, 809.069, 1668.3), cameraTarget=(
    302.452, -268.744, -829.765))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2192.36, 
    farPlane=5544.37, cameraPosition=(4908.76, 751.669, 1363.18), 
    cameraTarget=(488.903, -326.144, -1134.89))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2163.95, 
    farPlane=5550.42, cameraPosition=(4957.84, 918.209, 1106.8), 
    cameraUpVector=(-0.522911, 0.823534, -0.219899), cameraTarget=(432.093, 
    -429.776, -1046.75))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2163.95, 
    farPlane=5550.42, cameraPosition=(5006.76, 914.005, 1006.63), 
    cameraTarget=(481.01, -433.98, -1146.92))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2227.58, 
    farPlane=5695.94, cameraPosition=(5269.01, 285.748, 702.66), 
    cameraUpVector=(-0.378664, 0.92478, -0.0373618), cameraTarget=(325.823, 
    69.1184, -864.251))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2227.58, 
    farPlane=5695.94, cameraPosition=(5262.48, 282.408, 723.73), cameraTarget=(
    319.291, 65.7779, -843.181))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2154.74, 
    farPlane=4980.91, cameraPosition=(4282.98, 245.598, 2118.83), 
    cameraUpVector=(-0.278756, 0.930073, -0.23929), cameraTarget=(1074.41, 
    95.1668, -1957.9))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(3608.51, 
    180.641, 2652.07), cameraTarget=(399.937, 30.2095, -1424.66))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2147.27, 
    farPlane=4726.38, cameraPosition=(3217.7, 399.605, 2753.02), 
    cameraUpVector=(-0.22777, 0.909656, -0.347341), cameraTarget=(589.519, 
    -56.6391, -1699.15))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2192.03, 
    farPlane=5586.93, cameraPosition=(4686.43, -265.968, 1927.27), 
    cameraUpVector=(-0.307531, 0.950174, 0.0509273), cameraTarget=(76.4818, 
    188.189, -413.554))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(4935.96, 
    -165.813, 1455.28), cameraTarget=(326.015, 288.344, -885.544))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(5053.28, 
    -123.281, 1232.48), cameraTarget=(443.338, 330.876, -1108.34))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2165.35, 
    farPlane=5436.66, cameraPosition=(4829.84, 357.925, 1544.21), 
    cameraUpVector=(-0.398052, 0.907675, -0.132971), cameraTarget=(573.66, 
    -33.914, -1400.05))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2165.35, 
    farPlane=5436.66, cameraPosition=(4627.98, 372.147, 1834.12), 
    cameraTarget=(371.799, -19.6918, -1110.14))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2116.84, 
    farPlane=5085.21, cameraPosition=(4058.3, 1102.14, 2072.73), 
    cameraUpVector=(-0.498678, 0.778296, -0.381543), cameraTarget=(654.235, 
    -588.692, -1461.49))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2116.84, 
    farPlane=5085.2, cameraPosition=(3408.08, 1150.6, 2675.82), cameraTarget=(
    4.01471, -540.229, -858.401))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2116.84, 
    farPlane=5085.2, cameraPosition=(2961.77, 1628.41, 2877.11), cameraTarget=(
    -442.298, -62.4238, -657.114))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(3108.93, 
    1563.82, 2766.27), cameraTarget=(-295.134, -127.011, -767.958))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2112.42, 
    farPlane=4830.07, cameraPosition=(2645.73, 2116.21, 2463.65), 
    cameraUpVector=(-0.531302, 0.635886, -0.559792), cameraTarget=(-193.044, 
    -553.102, -964.68))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(2085.78, 
    2198.6, 2863.16), cameraTarget=(-752.993, -470.71, -565.174))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(2131.35, 
    2336.32, 2718.2), cameraUpVector=(-0.0372656, 0.501587, -0.864304), 
    cameraTarget=(-707.425, -332.989, -710.136))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3348.25, 
    farPlane=4849.98, cameraPosition=(320.976, 1498.64, 3798.5), 
    cameraUpVector=(0.53482, 0.615443, -0.578962), cameraTarget=(-55.3721, 
    -18.9361, -1150.51))
#: 
#: Element: A320-1.4150
#:   Type: S4R
#:   Material: ALUMINIUM
#:   Section: SKIN.Section-ASSEMBLY_A320-1_SKIN, Homogeneous Shell Section,Thickness = 1.65, num Int Pts = 5, poisson = 0.5, integration rule = SIMPSON
#: 
#:   Connect: 4369, 4370, 4409, 4408
#:   S, Mises (Not averaged): 0.0372795
session.viewports['Viewport: 1'].view.setValues(nearPlane=3348.26, 
    farPlane=4849.98, cameraPosition=(662.659, 1235.07, 3853.34), 
    cameraTarget=(286.311, -282.506, -1095.67))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3350.5, 
    farPlane=6210.86, cameraPosition=(-2250.13, -2548.2, 1763.23), 
    cameraUpVector=(0.0330262, 0.804474, 0.593069), cameraTarget=(1073.28, 
    917.831, -206.278))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3350.5, 
    farPlane=6210.86, cameraPosition=(-2236.95, -2693.72, 1529.39), 
    cameraTarget=(1086.46, 772.315, -440.12))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3347.35, 
    farPlane=6146.2, cameraPosition=(-2194.39, -2888.78, 1161.72), 
    cameraUpVector=(-0.0223085, 0.748072, 0.663243), cameraTarget=(1083.38, 
    847.268, -333.471))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-2212.14, 
    -2832.72, 1262.87), cameraTarget=(1065.63, 903.325, -232.317))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3449.61, 
    farPlane=5961.55, cameraPosition=(-1571.09, 1149.79, 3467.39), 
    cameraUpVector=(0.627153, 0.717921, -0.302106), cameraTarget=(825.227, 
    -363.437, -880.619))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3490.72, 
    farPlane=5721.58, cameraPosition=(-1185.33, -275.613, 3787.37), 
    cameraUpVector=(0.476327, 0.872901, -0.105627), cameraTarget=(725.837, 
    81.1278, -1024.86))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1327.07, 
    farPlane=4713.66, cameraPosition=(3690.56, 1034.7, 1677.26), 
    cameraUpVector=(-0.554986, 0.82166, -0.129865), cameraTarget=(-834.707, 
    -261.819, -508.697))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(3955.24, 
    844.245, 1242.29), cameraTarget=(-570.027, -452.274, -943.664))
odb = session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMData/Job-1.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Element Label', odb=odb, step=1, frame=1, 
    outputPosition=INTEGRATION_POINT, variable=(('S', INTEGRATION_POINT, ((
    INVARIANT, 'Mises'), )), ))
odb = session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMData/Job-1.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=OFF, 
    sortItem='Element Label', odb=odb, step=1, frame=1, 
    outputPosition=ELEMENT_NODAL, variable=(('S', INTEGRATION_POINT, ((
    INVARIANT, 'Mises'), )), ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1007.2, 
    farPlane=4475.62, cameraPosition=(4053.88, -54.4633, -953.035), 
    cameraUpVector=(-0.362803, 0.928652, 0.0773258), cameraTarget=(-1094.58, 
    -254.93, -328.029))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(4131.2, 
    -91.4095, -327.972), cameraTarget=(-1017.26, -291.876, 297.034))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1205.96, 
    farPlane=4519.58, cameraPosition=(3581.75, -1173.72, 1281.1), 
    cameraUpVector=(-0.0872044, 0.984982, 0.149016), cameraTarget=(-724.278, 
    553.442, -1045.39))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2387.56, 
    farPlane=3798.26, cameraPosition=(1152.26, -1820.47, 2328.13), 
    cameraUpVector=(-0.293435, 0.930658, 0.218568), cameraTarget=(1330.4, 
    1101.22, -1957.84))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(1112.8, 
    -1815.27, 2330.03), cameraTarget=(1290.94, 1106.42, -1955.93))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1378.84, 
    farPlane=4733.16, cameraPosition=(-1272.54, -1031.81, -1236.33), 
    cameraUpVector=(0.150447, 0.973858, -0.170194), cameraTarget=(3150.7, 
    458.055, 1033.61))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1394.47, 
    farPlane=4871.5, cameraPosition=(-1733.2, 141.861, -484.676), 
    cameraUpVector=(0.360152, 0.813121, 0.457302), cameraTarget=(3395.01, 
    -354.313, 141.965))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1685.92, 
    farPlane=4648.08, cameraPosition=(-802.151, -1725.68, 1325.22), 
    cameraUpVector=(0.172267, 0.851452, 0.495333), cameraTarget=(2644.63, 
    1134.42, -1297.16))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1751.08, 
    farPlane=4191.58, cameraPosition=(2352.85, -1988.55, 1838.73), 
    cameraUpVector=(0.189364, 0.943593, 0.271613), cameraTarget=(86.6769, 
    1264.01, -1511.29))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(2386.88, 
    -1975.93, 1827.97), cameraTarget=(120.704, 1276.63, -1522.05))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1328.94, 
    farPlane=4485.69, cameraPosition=(3508.33, 110.019, 1865.65), 
    cameraUpVector=(-0.602764, 0.793325, 0.0855014), cameraTarget=(-440.663, 
    -350.068, -1470.69))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1208.06, 
    farPlane=4606.57, width=3078.77, height=1374.62)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(3552.75, 
    236.916, 1795.57), cameraTarget=(-396.243, -223.171, -1540.77))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1244.22, 
    farPlane=4584.47, cameraPosition=(3434.43, 822.392, 1789.76), 
    cameraUpVector=(-0.647045, 0.749183, -0.141623), cameraTarget=(-288.247, 
    -703.342, -1489.15))
o1 = session.openOdb(
    name='D:/Documents/Studium/AA_Courses/Semester_6/SVV/Structures_Docs/FEMv3/A320-19.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#* OdbError: 
#* D:/Documents/Studium/AA_Courses/Semester_6/SVV/Structures_Docs/FEMv3/A320-19.odb 
#* is from a more recent release of Abaqus.
#* 
#*  The current Abaqus installation must be upgraded before this output 
#* database can be opened.
session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMData/Job-1.odb'].close(
    )
del mdb.models['A320-19']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='A320-19', 
    inputFileName='D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMData/A320-19.inp')
#: The model "A320-19" has been created.
#: The part "A320" has been imported from the input file.
#: 
#: WARNING: Node-based surfaces are not yet supported in Abaqus/CAE. The following node sets have been created in place of the corresponding node-based surfaces so they can be used in Abaqus/CAE. 
#: Node Set Created            Node-Based Surface  
#: ------------------          -------------------- 
#:     HINGE_2_CNS_                 HINGE_2_CNS_
#:     POINT_10_CNS_                POINT_10_CNS_
#:     POINT_11_CNS_                POINT_11_CNS_
#:     POINT_12_CNS_                POINT_12_CNS_
#:     POINT_13_CNS_                POINT_13_CNS_
#:     POINT_14_CNS_                POINT_14_CNS_
#:     POINT_15_CNS_                POINT_15_CNS_
#:     POINT_16_CNS_                POINT_16_CNS_
#:     POINT_6_CNS_                 POINT_6_CNS_
#:     POINT_7_CNS_                 POINT_7_CNS_
#:     POINT_8_CNS_                 POINT_8_CNS_
#:     POINT_9_CNS_                 POINT_9_CNS_
#:     RIB_A_CNS_                   RIB_A_CNS_
#:     RIB_B_CNS_                   RIB_B_CNS_
#:     RIB_C_CNS_                   RIB_C_CNS_
#:     RIB_D_CNS_                   RIB_D_CNS_
#: Constraint type MPC in Abaqus/CAE is created for *MPC definition.
#: WARNING: Creation of loads on  set/surfaces SET-38 failed due to following reason
#: 		: Load must be created with a non-zero magnitude unless utilizing a user subroutine. 
#: WARNING: Creation of loads on  set/surfaces SET-39 failed due to following reason
#: 		: Load must be created with a non-zero magnitude unless utilizing a user subroutine. 
#: 
#: WARNING: The following keywords/parameters are not yet supported by the input file reader:
#: ---------------------------------------------------------------------------------
#: *PREPRINT
#: The model "A320-19" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
a = mdb.models['A320-19'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
import os
os.chdir(
    r"D:\Documents\Studium\AA_Courses\Semester_6\SVV\A15_SVV_Structures\FEMDataV2")
mdb.saveAs(
    pathName='D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/A320_V2')
#: The model database has been saved to "D:\Documents\Studium\AA_Courses\Semester_6\SVV\A15_SVV_Structures\FEMDataV2\A320_V2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=4497.26, 
    farPlane=8138.59, width=2626.39, height=1172.64, cameraPosition=(7683.22, 
    295.359, 260.949), cameraUpVector=(-0.376595, 0.907413, -0.18649), 
    cameraTarget=(1506.94, -83.1546, -199.284))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4535.86, 
    farPlane=8099.99, width=2648.93, height=1182.71, cameraPosition=(7683.22, 
    295.359, 260.949), cameraUpVector=(-0.38896, 0.920716, -0.0314901), 
    cameraTarget=(1506.94, -83.1546, -199.284))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4536.12, 
    farPlane=8099.73, width=2649.1, height=1182.78, viewOffsetX=-134.221, 
    viewOffsetY=65.5132)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4820.25, 
    farPlane=7984.88, width=2815.04, height=1256.87, cameraPosition=(6094.05, 
    1154.32, 4023.04), cameraUpVector=(-0.405396, 0.858642, -0.313668), 
    cameraTarget=(1597.42, -57.7636, -77.2872), viewOffsetX=-142.628, 
    viewOffsetY=69.6168)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4562.21, 
    farPlane=8143.93, width=2664.34, height=1189.59, cameraPosition=(7366.84, 
    1394.89, 1469.65), cameraUpVector=(-0.489188, 0.827641, -0.275145), 
    cameraTarget=(1571.31, -81.303, -183.869), viewOffsetX=-134.993, 
    viewOffsetY=65.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4717.76, 
    farPlane=8033.03, width=2755.19, height=1230.15, cameraPosition=(6567.41, 
    2308.7, 2751.85), cameraUpVector=(-0.531576, 0.741957, -0.408568), 
    cameraTarget=(1602.54, -47.2836, -129.276), viewOffsetX=-139.596, 
    viewOffsetY=68.1365)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='RotationUp')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
mdb.models['A320-19'].boundaryConditions['Disp-BC-10'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Jam1')
mdb.models['A320-19'].boundaryConditions['Disp-BC-12'].setValues(fixed=OFF, 
    u1=UNSET, u2=UNSET, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='RotationDown')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Jam2')
mdb.models['A320-19'].boundaryConditions['Disp-BC-21'].setValues(fixed=OFF, 
    u1=UNSET, u2=UNSET, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET)
mdb.models['A320-19'].boundaryConditions['Disp-BC-18'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#* WindowsError: (32, 'The process cannot access the file because it is being 
#* used by another process')
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=3743.4, 
    farPlane=7590.29, cameraPosition=(7013.38, 247.742, -776.411), 
    cameraUpVector=(-0.346132, 0.899623, 0.266216))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3743.4, 
    farPlane=7590.29, cameraPosition=(7013.38, 247.742, -776.411), 
    cameraUpVector=(-0.376865, 0.926259, -0.00410748), cameraTarget=(1385.5, 0, 
    -161))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4064.92, 
    farPlane=7268.77, cameraPosition=(4923.77, 2633.72, 3396.71), 
    cameraUpVector=(-0.432252, 0.673496, -0.599635), cameraTarget=(1385.5, 
    -0.000244141, -161))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4124.89, 
    farPlane=7208.8, cameraPosition=(4742.95, 3569.14, 2685.39), 
    cameraUpVector=(-0.574056, 0.517085, -0.634888), cameraTarget=(1385.5, 
    -0.000183105, -161))
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
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3791.32, 
    farPlane=7542.38, cameraPosition=(6515.19, 1914.77, 1299.5), 
    cameraUpVector=(-0.570334, 0.766551, -0.295159), cameraTarget=(1385.5, 
    -3.05176e-005, -161))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3800.55, 
    farPlane=7526.66, cameraPosition=(6374.55, 2022.29, 1608.96), 
    cameraUpVector=(-0.574193, 0.756492, -0.313086), cameraTarget=(1385.58, 
    -0.0582466, -161.168))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1)
odb = session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb']
session.writeFieldReport(fileName='A320_SLC1rpt', append=OFF, 
    sortItem='Element Label', odb=odb, step=1, frame=1, 
    outputPosition=ELEMENT_NODAL, variable=(('S', INTEGRATION_POINT, ((
    INVARIANT, 'Mises'), )), ))
odb = session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb']
session.writeFieldReport(fileName='A320_S12LC1.rpt', append=OFF, 
    sortItem='Element Label', odb=odb, step=1, frame=1, 
    outputPosition=ELEMENT_NODAL, variable=(('S', INTEGRATION_POINT, ((
    COMPONENT, 'S12'), )), ))
odb = session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb']
session.writeFieldReport(fileName='A320_ULC1.rpt', append=OFF, 
    sortItem='Node Label', odb=odb, step=1, frame=1, outputPosition=NODAL, 
    variable=(('RF', NODAL), ('U', NODAL), ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
odb = session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb']
session.writeFieldReport(fileName='A320_SR1_V2.rpt', append=OFF, 
    sortItem='Node Label', odb=odb, step=0, frame=1, 
    outputPosition=ELEMENT_NODAL, variable=(('S', INTEGRATION_POINT, ((
    INVARIANT, 'Mises'), )), ))
odb = session.odbs['D:/Documents/Studium/AA_Courses/Semester_6/SVV/A15_SVV_Structures/FEMDataV2/Job-1.odb']
session.writeFieldReport(fileName='A320_UR1_V2.rpt', append=OFF, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('RF', NODAL), ('U', NODAL), ))
mdb.save()
#: The model database has been saved to "D:\Documents\Studium\AA_Courses\Semester_6\SVV\A15_SVV_Structures\FEMDataV2\A320_V2.cae".

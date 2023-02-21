# 10,000ft: Data Overview

Knowing how data is organized will help you use and find things much faster.  This is shown early in the docs for easy reference as questions may arise throughout the progression of the docs. 

:::{tip}
The SDKs (which are optimized for machine-to-machine integration) can be used in concert with the [NavAbility App][nva-app-url] (which is optimized for human-to-machine interaction).
:::

## Data Structures

The following summary is used to organize user interaction, data storage, retrieval, queried search, SLAM solving and much more.  From the top:

- User
  - Robots
    - Sessions
      - Variables
        - BlobEntries (this includes raw, processing, and product data)
        - PPEs (parametric point estimates)
        - SolverData (Gaussian and non-Gaussian solutions)
      - Factors
        - mathematical structure

## Data Example

So for example:

- my@user.com
  - RoboticAgent_e3ddc
    - Session_2001_01_d8
      - Variable: pose0
        - BlobEntries: {CameraFwd_1225, LidarScan_643, IMU_4677, FusedPointCloud_High, VisualDescriptors, ObjectMap, ...}
        - PPEs: {parametric, nonparametric, verification}
        - SolverData: {init, parametric, multimodal, 3_hypo, ...}
      - pose1
      - pose2
      - ...
  - HandheldDevice7
    - Session_sdc9hk2
      - x0
      - tag4
      - ...

Let's start by looking at variables on the next page. 

[nva-app-url]: https://app.navability.io/home
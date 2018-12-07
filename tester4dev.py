#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
##
   без имени.py
   
   @Copyright: 2018 by iop <iop@com.ny>
   
   @license: GNU GPL, see COPYING for details.
##
## Fluid information
##
import CoolProp.CoolProp as CP
for k in ['formula','CAS','aliases','ASHRAE34','REFPROP_name','pure','INCHI','INCHI_Key','CHEMSPIDER_ID']:
	item = k + ' --> ' + CP.get_fluid_param_string("R125", k)
print(item)


## PhaseSI function
import CoolProp.CoolProp as CP
CP.PhaseSI('P',101325,'Q',0,'Water')
CP.PropsSI('Phase','P',101325,'Q',0,'Water')
CP.get_phase_index('phase_twophase')
CP.get_phase_index('phase_liquid')

"""
#import the things you need
In [1]: from CoolProp.HumidAirProp import HAPropsSI

#Enthalpy (J per kg dry air) as a function of temperature, pressure,
#    and relative humidity at dry bulb temperature T of 25C, pressure
#    P of one atmosphere, relative humidity R of 50%
In [2]: h = HAPropsSI('H','T',298.15,'P',101325,'R',0.5); print(h)
50423.4503908

#Temperature of saturated air at the previous enthalpy
In [3]: T = HAPropsSI('T','P',101325,'H',h,'R',1.0); print(T)
290.962089195

#Temperature of saturated air - order of inputs doesn't matter
In [4]: T = HAPropsSI('T','H',h,'R',1.0,'P',101325); print(T)
290.962089195"""


### Humid Air Validation
execfile('fluid_properties/Validation/HAValidation.py')
"""
Replicating the tables from ASHRAE RP-1485
  
A.6.1 Psychrometric Properties of Moist Air at 0C and Below
Saturated air at 101.325 kPa
====================================================
   T          Ws         v       h          s   
   C      kgw/kg_da   m3/kgda  kJ/kgda  kJ/kgda/K
----------------------------------------------------
     -60 0.0000067    0.6027   -60.325   -0.2494
     -55 0.0000129    0.6169   -55.280   -0.2260
     -50 0.0000243    0.6312   -50.222   -0.2030
     -45 0.0000445    0.6454   -45.144   -0.1805
     -40 0.0000793    0.6597   -40.031   -0.1583
     -35 0.0001379    0.6740   -34.859   -0.1364
     -30 0.0002345    0.6883   -29.593   -0.1145
     -25 0.0003905    0.7027   -24.181   -0.0924
     -20 0.0006373    0.7172   -18.542   -0.0699
     -15 0.0010207    0.7319   -12.560   -0.0465
     -10 0.0016062    0.7468    -6.070   -0.0215
      -5 0.0024863    0.7622     1.165    0.0057
       0 0.0037900    0.7780     9.475    0.0364
====================================================
 
A.6.2 Psychrometric Properties of Moist Air at 0C and Above
Saturated air at 101.325 kPa
====================================================
   T          Ws         v       h          s   
   C      kgw/kg_da   m3/kgda  kJ/kgda  kJ/kgda/K
----------------------------------------------------
       0 0.0037900     0.778      9.47    0.0364
       5 0.0054247     0.794     18.64    0.0697
      10 0.0076626     0.812     29.35    0.1079
      15 0.0106938     0.830     42.12    0.1525
      20 0.0147605     0.850     57.56    0.2057
      25 0.0201734     0.872     76.50    0.2699
      30 0.0273329     0.896    100.01    0.3482
      35 0.0367601     0.924    129.46    0.4448
      40 0.0491445     0.957    166.69    0.5650
      45 0.0654161     0.995    214.17    0.7162
      50 0.0868629     1.042    275.35    0.9081
      55 0.1153262     1.101    355.15    1.1549
      60 0.1535446     1.175    460.89    1.4776
      65 0.2057936     1.273    604.00    1.9084
      70 0.2791668     1.405    803.48    2.5012
      75 0.3863984     1.593   1093.39    3.3518
      80 0.5529259     1.881   1541.79    4.6511
      85 0.8381052     2.367   2307.52    6.8431
      90 1.4202351     3.349   3867.63   11.2559
====================================================
 
A.8.1 Psychrometric Properties of Moist Air at 101.325 kPa 
Dry Bulb temperature of 200C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00     45.07     1.341    202.52    0.5562    0.0000
      0.05     55.38     1.448    346.49    1.0299    0.4850
      0.10     61.85     1.556    490.43    1.4736    0.9028
      0.20     69.95     1.771    778.25    2.3337    1.5859
      0.30     75.00     1.986   1066.01    3.1752    2.1208
      0.40     78.51     2.201   1353.73    4.0059    2.5510
      0.50     81.12     2.416   1641.42    4.8295    2.9045
      0.60     83.14     2.630   1929.09    5.6479    3.2002
      0.70     84.76     2.845   2216.73    6.4624    3.4511
      0.80     86.09     3.060   2504.37    7.2737    3.6668
      0.90     87.20     3.274   2791.99    8.0824    3.8541
      1.00     88.15     3.489   3079.60    8.8891    4.0183
================================================================
 
A.8.2 Psychrometric Properties of Moist Air at 1000 kPa 
Dry Bulb temperature of 200C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00     90.47     0.136    201.94   -0.1002    0.0000
      0.05    107.30     0.147    345.60    0.3175    4.7863
      0.10    117.69     0.158    488.97    0.7078    8.9096
      0.20    180.72     0.179    775.07    1.4603   15.6512
      0.30    138.66     0.200   1060.53    2.1936   20.9304
      0.40    144.29     0.222   1345.53    2.9157   25.1764
      0.50    148.49     0.243   1630.17    3.6303   28.6655
      0.60    151.76     0.264   1914.54    4.3394   31.5835
      0.70    154.39     0.284   2198.70    5.0443   34.0601
      0.80    156.56     0.305   2482.69    5.7459   36.1883
      0.90    158.37     0.326   2766.53    6.4448   38.0369
      1.00    159.92     0.347   3050.26    7.1414   39.6575
================================================================
 
A.8.3 Psychrometric Properties of Moist Air at 2000 kPa 
Dry Bulb temperature of 200C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00    105.93     0.068    201.34   -0.2982    0.0000
      0.05    125.81     0.074    344.62    0.1000    9.3475
      0.10    138.03     0.079    487.33    0.4735   17.4003
      0.20    153.19     0.089    771.38    1.1917   30.5666
      0.30    162.65     0.100   1054.03    1.8898   40.8768
      0.40    169.28     0.110   1335.64    2.5761   49.1691
      0.50    174.23     0.120   1616.43    3.2542   55.9833
      0.60    178.11     0.130   1896.58    3.9265   61.6822
      0.70    181.23     0.140   2176.21    4.5942   66.5189
      0.80    183.81     0.150   2455.41    5.2582   70.6753
      0.90    185.98     0.160   2734.26    5.9193   74.2855
      1.00    187.83     0.169   3012.79    6.5780   77.4505
================================================================
 
A.8.4 Psychrometric Properties of Moist Air at 5000 kPa 
Dry Bulb temperature of 200C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00    126.87     0.028    199.72   -0.5581    0.0000
      0.05    151.76     0.030    341.85   -0.1918   21.5445
      0.10    166.94     0.032    482.37    0.1580   40.1047
      0.15    177.63     0.034    621.47    0.4958   56.2606
      0.20    185.72     0.036    759.34    0.8257   70.4509
      0.25    192.15     0.037    896.09    1.1499   83.0138
      0.30    197.42     0.039   1031.82    1.4695   94.2140
================================================================
 
A.8.5 Psychrometric Properties of Moist Air at 10,000 kPa 
Dry Bulb temperature of 200C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00    142.19     0.014    197.66   -0.7512    0.0000
      0.05    171.31     0.015    337.69   -0.4188   39.4620
      0.10    188.92     0.016    473.92   -0.0901   73.4579
================================================================
 
A.9.1 Psychrometric Properties of Moist Air at 101.325 kPa 
Dry Bulb temperature of 320C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00     54.90     1.681    326.93    0.7903    0.0000
      0.05     62.07     1.816    482.76    1.2864    0.0668
      0.10     67.00     1.951    638.59    1.7525    0.1244
      0.20     73.54     2.221    950.21    2.6573    0.2185
      0.30     77.79     2.491   1261.80    3.5436    0.2922
      0.40     80.80     2.761   1573.37    4.4192    0.3515
      0.50     83.07     3.030   1884.93    5.2876    0.4002
      0.60     84.85     3.300   2196.47    6.1509    0.4409
      0.70     86.28     3.570   2508.01    7.0102    0.4755
      0.80     87.46     3.840   2819.54    7.8664    0.5052
      0.90     88.45     4.109   3131.07    8.7200    0.5310
      1.00     89.29     4.379   3442.59    9.5715    0.5536
================================================================
 
A.9.2 Psychrometric Properties of Moist Air at 1000 kPa 
Dry Bulb temperature of 320C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00    107.70     0.171    326.80    0.1341    0.0000
      0.05    118.99     0.185    482.46    0.5751    0.6594
      0.10    126.74     0.198    637.99    0.9880    1.2275
      0.20    137.03     0.225    948.77    1.7865    2.1564
      0.30    143.73     0.252   1259.26    2.5661    2.8838
      0.40    148.52     0.279   1569.56    3.3350    3.4688
      0.50    152.14     0.306   1879.70    4.0966    3.9495
      0.60    154.99     0.333   2189.73    4.8529    4.3515
      0.70    157.29     0.360   2499.68    5.6053    4.6927
      0.80    159.19     0.387   2809.55    6.3544    4.9860
      0.90    160.79     0.414   3119.37    7.1010    5.2407
      1.00    162.16     0.441   3429.15    7.8454    5.4639
================================================================
 
A.9.3 Psychrometric Properties of Moist Air at 2000 kPa 
Dry Bulb temperature of 320C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00    126.92     0.086    326.68   -0.0638    0.0000
      0.05    140.12     0.093    482.14    0.3587    1.3189
      0.10    149.16     0.099    637.35    0.7553    2.4551
      0.20    161.20     0.113    947.16    1.5209    4.3128
      0.30    169.07     0.126   1256.41    2.2675    5.7675
      0.40    174.71     0.140   1565.23    3.0031    6.9375
      0.50    178.98     0.153   1873.75    3.7313    7.8990
      0.60    182.35     0.166   2182.04    4.4542    8.7031
      0.70    185.08     0.179   2490.14    5.1730    9.3855
      0.80    187.34     0.192   2798.09    5.8886    9.9719
      0.90    189.25     0.206   3105.93    6.6015   10.4813
      1.00    190.88     0.219   3413.67    7.3123   10.9279
================================================================
 
A.9.4 Psychrometric Properties of Moist Air at 5000 kPa 
Dry Bulb temperature of 320C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00    154.63     0.035    326.46   -0.3235    0.0000
      0.05    170.96     0.037    481.31    0.0702    3.2972
      0.10    182.17     0.040    635.49    0.4448    6.1377
      0.15    190.55     0.043    789.13    0.8084    8.6103
      0.20    197.14     0.045    942.31    1.1653   10.7820
      0.25    202.51     0.048   1095.11    1.5175   12.7047
      0.30    206.99     0.050   1247.59    1.8662   14.4188
      0.40    214.09     0.056   1551.73    2.5554   17.3438
      0.50    219.52     0.061   1855.02    3.2369   19.7474
      0.60    223.82     0.066   2157.63    3.9126   21.7577
      0.70    227.33     0.071   2459.71    4.5840   23.4637
      0.80    230.25     0.076   2761.36    5.2518   24.9298
      0.90    232.72     0.081   3062.64    5.9169   26.2033
      1.00    234.85     0.085   3363.63    6.5796   27.3197
================================================================
 
A.9.5 Psychrometric Properties of Moist Air at 10,000 kPa 
Dry Bulb temperature of 320C
================================================================
      W        Twb         v       h          s        RH   
  kgw/kg_da      C      m3/kgda  kJ/kgda  kJ/kgda/K    %     
----------------------------------------------------------------
      0.00    176.72     0.018    326.51   -0.5165    0.0000
      0.05    195.85     0.019    480.31   -0.1514    6.5945
      0.10    209.00     0.020    632.70    0.2054   12.2755
      0.15    218.85     0.022    783.90    0.5507   17.2206
      0.20    226.63     0.023    934.12    0.8889   21.5640
      0.25    233.00     0.024   1083.47    1.2220   25.4093
      0.30    238.33     0.025   1232.08    1.5512   28.8376
      0.40    246.84     0.028   1527.40    2.2005   34.6877
      0.50    253.40     0.030   1820.61    2.8409   39.4949
      0.60    258.63     0.032   2112.08    3.4747   43.5153
      0.70    262.94     0.034   2402.10    4.1033   46.9275
      0.80    266.55     0.036   2690.88    4.7277   49.8597
      0.90    269.63     0.039   2978.59    5.3487   52.4066
      1.00    272.29     0.041   3265.36    5.9667   54.6395
================================================================

Pure fluid Virial Coefficients
------------------------------
T         Baa                 Caaa                Bww                 Cwww                
C         m^3/mol             m^6/mol^2           m^3/mol             m^6/mol^2           
-60.0     -3.3064504913e-05   2.1778728776e-09    -1.1174019230e-02   -1.5162998768e-04   
-50.0     -2.8932056455e-05   2.1163810315e-09    -7.8721344601e-03   -8.7876439931e-05   
-40.0     -2.5223205510e-05   2.0616570944e-09    -5.7127237936e-03   -5.5471167065e-05   
-30.0     -2.1877241883e-05   2.0127116499e-09    -4.2586206439e-03   -3.6054467433e-05   
-20.0     -1.8844568169e-05   1.9687328800e-09    -3.2532396168e-03   -2.3880058317e-05   
-10.0     -1.6084254149e-05   1.9290492160e-09    -2.5411800904e-03   -1.6072254169e-05   
0.0       -1.3562212432e-05   1.8931009119e-09    -2.0256198165e-03   -1.0976416841e-05   
10.0      -1.1249818308e-05   1.8604181700e-09    -1.6446680868e-03   -7.5982156425e-06   
20.0      -9.1228522265e-06   1.8306041394e-09    -1.3578320706e-03   -5.3262047265e-06   
30.0      -7.1606799362e-06   1.8033215779e-09    -1.1380508933e-03   -3.7775456074e-06   
40.0      -5.3456100212e-06   1.7782822977e-09    -9.6688526113e-04   -2.7086426379e-06   
50.0      -3.6623854498e-06   1.7552387450e-09    -8.3154379347e-04   -1.9621726463e-06   
60.0      -2.0977774966e-06   1.7339772333e-09    -7.2300490095e-04   -1.4351072804e-06   
70.0      -6.4025867871e-07   1.7143124658e-09    -6.3480699108e-04   -1.0590893108e-06   
80.0      7.2026273739e-07    1.6960830728e-09    -5.6225490863e-04   -7.8820574569e-07   
90.0      1.9926598215e-06    1.6791479533e-09    -5.0189060427e-04   -5.9126044774e-07   
100.0     3.1847656914e-06    1.6633832580e-09    -4.5113452236e-04   -4.4682462927e-07   
110.0     4.3035215681e-06    1.6486798883e-09    -4.0803910950e-04   -3.4002636972e-07   
120.0     5.3551001609e-06    1.6349414114e-09    -3.7111708564e-04   -2.6044318239e-07   
130.0     6.3450090665e-06    1.6220823143e-09    -3.3922027793e-04   -2.0070296438e-07   
140.0     7.2781778723e-06    1.6100265349e-09    -3.1145310612e-04   -1.5554524200e-07   
150.0     8.1590318924e-06    1.5987062200e-09    -2.8711011151e-04   -1.2118485357e-07   
160.0     8.9915548780e-06    1.5880606719e-09    -2.6563036496e-04   -9.4876457701e-08   
170.0     9.7793425843e-06    1.5780354497e-09    -2.4656385529e-04   -7.4613740198e-08   
180.0     1.0525648716e-05    1.5685816023e-09    -2.2954647025e-04   -5.8919833627e-08   
190.0     1.1233424489e-05    1.5596550080e-09    -2.1428120144e-04   -4.6700067957e-08   
200.0     1.1905352827e-05    1.5512158075e-09    -2.0052390022e-04   -3.7137687457e-08   
T         Baw                 Caaw                Caww                
C         m^3/mol             m^6/mol^2           m^6/mol^2           
-60.0     -6.8305808721e-05   1.0273000716e-09    -1.8214316825e-06   
-50.0     -6.1680233064e-05   1.0001595421e-09    -1.1787612409e-06   
-40.0     -5.5836203092e-05   9.7107903308e-10    -7.9593677251e-07   
-30.0     -5.0645881561e-05   9.4180678583e-10    -5.5678343751e-07   
-20.0     -4.6007498746e-05   9.1337025409e-10    -4.0128618357e-07   
-10.0     -4.1839118849e-05   8.8634392341e-10    -2.9668474376e-07   
0.0       -3.8074090909e-05   8.6101819497e-10    -2.2423408862e-07   
10.0      -3.4657682115e-05   8.3750672364e-10    -1.7276396504e-07   
20.0      -3.1544553729e-05   8.1581500536e-10    -1.3537862024e-07   
30.0      -2.8696845981e-05   7.9588431449e-10    -1.0768721224e-07   
40.0      -2.6082708793e-05   7.7761982700e-10    -8.6816421215e-08   
50.0      -2.3675162869e-05   7.6090853025e-10    -7.0839762898e-08   
60.0      -2.1451208360e-05   7.4563050528e-10    -5.8437245597e-08   
70.0      -1.9391120996e-05   7.3166589756e-10    -4.8686625860e-08   
80.0      -1.7477891584e-05   7.1889908286e-10    -4.0932107713e-08   
90.0      -1.5696776156e-05   7.0722101405e-10    -3.4699849863e-08   
100.0     -1.4034932249e-05   6.9653039669e-10    -2.9642457363e-08   
110.0     -1.2481122776e-05   6.8673412025e-10    -2.5501820730e-08   
120.0     -1.1025473368e-05   6.7774722643e-10    -2.2083805133e-08   
130.0     -9.6592722783e-06   6.6949259959e-10    -1.9240735645e-08   
140.0     -8.3748044505e-06   6.6190050073e-10    -1.6859099163e-08   
150.0     -7.1652131416e-06   6.5490802360e-10    -1.4850792059e-08   
160.0     -6.0243839304e-06   6.4845852337e-10    -1.3146812982e-08   
170.0     -4.9468470096e-06   6.4250104926e-10    -1.1692664630e-08   
180.0     -3.9276944932e-06   6.3698980018e-10    -1.0444965002e-08   
190.0     -2.9625101219e-06   6.3188361380e-10    -9.3689246298e-09   
200.0     -2.0473092535e-06   6.2714549461e-10    -8.4364506623e-09   

Pure fluid Virial Coefficients Derivatives
------------------------------------------
T         dBaa                dCaaa               dBww                dCwww               
C         m^3/mol             m^6/mol^2           m^3/mol             m^6/mol^2           
-60.0     4.3678901718e-07    -6.5259421081e-12   4.0907134267e-04    9.7890225556e-06    
-50.0     3.9094567047e-07    -5.7925951449e-12   2.6368394754e-04    4.2599502143e-06    
-40.0     3.5183089770e-07    -5.1686009316e-12   1.7524578197e-04    2.4534392599e-06    
-30.0     3.1818443574e-07    -4.6339568007e-12   1.1972698408e-04    1.5168064804e-06    
-20.0     2.8902947780e-07    -4.1729431726e-12   8.3872099442e-05    9.6398589135e-07    
-10.0     2.6359917737e-07    -3.7730826593e-12   6.0116039515e-05    6.2432365587e-07    
0.0       2.4128450184e-07    -3.4243800668e-12   4.4005975878e-05    4.1098205932e-07    
10.0      2.2159662973e-07    -3.1187604739e-12   3.2846510930e-05    2.7460401649e-07    
20.0      2.0413943007e-07    -2.8496489141e-12   2.4963984884e-05    1.8603615349e-07    
30.0      1.8858904489e-07    -2.6116525842e-12   1.9294782853e-05    1.2767075965e-07    
40.0      1.7467855065e-07    -2.4003181623e-12   1.5148499662e-05    8.8680535853e-08    
50.0      1.6218630137e-07    -2.2119447569e-12   1.2068194612e-05    6.2299015990e-08    
60.0      1.5092697458e-07    -2.0434384795e-12   9.7459891450e-06    4.4233623231e-08    
70.0      1.4074462510e-07    -1.8921984596e-12   7.9709845791e-06    3.1722699778e-08    
80.0      1.3150724657e-07    -1.7560268233e-12   6.5964818172e-06    2.2965936560e-08    
90.0      1.2310247686e-07    -1.6330570877e-12   5.5189694206e-06    1.6775064043e-08    
100.0     1.1543417961e-07    -1.5216968216e-12   4.6644255474e-06    1.2356543007e-08    
110.0     1.0841970276e-07    -1.4205814367e-12   3.9792467564e-06    9.1745422056e-09    
120.0     1.0198766459e-07    -1.3285367274e-12   3.4241524938e-06    6.8634353500e-09    
130.0     9.6076153981e-08    -1.2445483295e-12   2.9700329278e-06    5.1712456914e-09    
140.0     9.0631258338e-08    -1.1677366865e-12   2.5950842306e-06    3.9226742483e-09    
150.0     8.5605852607e-08    -1.0973364250e-12   2.2828082790e-06    2.9946678537e-09    
160.0     8.0958597486e-08    -1.0326792823e-12   2.0206000698e-06    2.3001072716e-09    
170.0     7.6653106484e-08    -9.7317990685e-13   1.7987394663e-06    1.7768097568e-09    
180.0     7.2657249944e-08    -9.1832399823e-13   1.6096642209e-06    1.3800452917e-09    
190.0     6.8942570813e-08    -8.6765835911e-13   1.4474407409e-06    1.0773984832e-09    
200.0     6.5483792067e-08    -8.2078251748e-13   1.3073752610e-06    8.4521088732e-10    
T         dBaw                dCaaw               dCaww               
C         m^3/mol             m^6/mol^2           m^6/mol^2           
-60.0     7.0671067841e-07    -2.5329306643e-12   8.3652108680e-08    
-50.0     6.2109405080e-07    -2.8479923244e-12   4.8634111869e-08    
-40.0     5.4982837510e-07    -2.9396633262e-12   2.9766967562e-08    
-30.0     4.8992187794e-07    -2.8980941059e-12   1.9020412856e-08    
-20.0     4.3911281598e-07    -2.7799104397e-12   1.2604799172e-08    
-10.0     3.9566848048e-07    -2.6206893674e-12   8.6179394263e-09    
0.0       3.5824516845e-07    -2.4426731561e-12   6.0532052853e-09    
10.0      3.2578908214e-07    -2.2596007123e-12   4.3529611359e-09    
20.0      2.9746516934e-07    -2.0797672895e-12   3.1957227862e-09    
30.0      2.7260533603e-07    -1.9079803096e-12   2.3895374649e-09    
40.0      2.5067028507e-07    -1.7468190020e-12   1.8161835419e-09    
50.0      2.3122106772e-07    -1.5974502672e-12   1.4008122071e-09    
60.0      2.1389764536e-07    -1.4601590182e-12   1.0948500459e-09    
70.0      1.9840257004e-07    -1.3346933582e-12   8.6606704976e-10    
80.0      1.8448844334e-07    -1.2204888941e-12   6.9264384038e-10    
90.0      1.7194819305e-07    -1.1168137618e-12   5.5953719449e-10    
100.0     1.6060747132e-07    -1.0228614572e-12   4.5620187444e-10    
110.0     1.5031866448e-07    -9.3780925812e-13   3.7513243420e-10    
120.0     1.4095613794e-07    -8.6085397191e-13   3.1091182225e-10    
130.0     1.3241243488e-07    -7.9123279439e-13   2.5957962745e-10    
140.0     1.2459521736e-07    -7.2823445525e-13   2.1820572123e-10    
150.0     1.1742478936e-07    -6.7120410110e-13   1.8459817415e-10    
160.0     1.1083207914e-07    -6.1954421544e-13   1.5710036152e-10    
170.0     1.0475698647e-07    -5.7271310484e-13   1.3444819325e-10    
180.0     9.9147021510e-08    -5.3022196394e-13   1.1566843627e-10    
190.0     9.3956178059e-08    -4.9163118437e-13   1.0000548446e-10    
200.0     8.9143996459e-08    -4.5654633851e-13   8.6868060073e-11    

Water saturation pressure p_ws [kPa]
T          p_ws                
C          Pa                  
-60.00    1.0813475449e+00    
-30.00    3.8005139487e+01    
0.00      6.1115347506e+02    
30.00     4.2466883405e+03    
60.00     1.9945801925e+04    
90.00     7.0182360745e+04    
120.00    1.9866539974e+05    
150.00    4.7610138108e+05    
180.00    1.0026345688e+06    
210.00    1.9073906643e+06    
240.00    3.3466518715e+06    
270.00    5.5028394741e+06    
300.00    8.5877083296e+06    

Henry Constant (zero for T < 273.15 K)
T          beta_H              
C          1/Pa                
0.01      2.2594633839e-10    
30.01     1.3058555542e-10    
60.01     1.0117905765e-10    
90.01     9.5497073897e-11    
120.01    1.0310894778e-10    
150.01    1.2209642969e-10    
180.01    1.5416532918e-10    
210.01    2.0384427379e-10    
240.01    2.7939520108e-10    
270.01    3.9586839028e-10    
300.01    5.8396949465e-10    

Isothermal Compressibility of water (kT) [1/Pa]
T         p = 101325.000 Pa   p = 200000.000 Pa   p = 500000.000 Pa   p = 1000000.000 Pa  
-60.00    1.0771099108e-10    1.0770400843e-10    1.0768278304e-10    1.0764742021e-10    
-30.00    1.1257575753e-10    1.1256891351e-10    1.1254810951e-10    1.1251344878e-10    
0.00      1.1778484390e-10    1.1777815515e-10    1.1775782318e-10    1.1772394894e-10    
30.00     1.0048218396e-03    1.0047775852e-03    1.0046431164e-03    1.0044192594e-03    
60.00     1.0173376853e-03    1.0172931915e-03    1.0171579998e-03    1.0169329553e-03    
90.00     1.0360937793e-03    1.0360454263e-03    1.0358985238e-03    1.0356540343e-03    
120.00    1.7695003917e+00    1.0604394263e-03    1.0602707553e-03    1.0599901229e-03    
150.00    1.9111838106e+00    9.5989413316e-01    1.0905701909e-03    1.0902325237e-03    
180.00    2.0511819911e+00    1.0326461304e+00    4.0465521554e-01    1.9441817992e-01    
210.00    2.1901914433e+00    1.1043221088e+00    4.3506032354e-01    2.1154168024e-01    
240.00    2.3285841090e+00    1.1753398746e+00    4.6467604880e-01    2.2755082652e-01    
270.00    2.4665706339e+00    1.2459309799e+00    4.9380122272e-01    2.4295534461e-01    
300.00    2.6042765544e+00    1.3162310320e+00    5.2260279146e-01    2.5797921396e-01    

Molar volume of saturated liquid water or ice (vbar_ws) [m^3/mol_H2O]
T         p = 101325.000 Pa   p = 200000.000 Pa   p = 500000.000 Pa   p = 1000000.000 Pa  
-60.00    1.9483157215e-11    1.9482950148e-11    1.9482320703e-11    1.9481271948e-11    
-30.00    1.9562306493e-11    1.9562089195e-11    1.9561428642e-11    1.9560328042e-11    
0.00      1.9651836970e-11    1.9651608576e-11    1.9650914289e-11    1.9649757465e-11    
30.00     1.8094773222e-05    1.8094773222e-05    1.8094773222e-05    1.8094773222e-05    
60.00     1.8323837443e-05    1.8323837443e-05    1.8323837443e-05    1.8323837443e-05    
90.00     1.8662959891e-05    1.8662959891e-05    1.8662959891e-05    1.8662959891e-05    
120.00    1.9102048132e-05    1.9102048132e-05    1.9102048132e-05    1.9102048132e-05    
150.00    1.9645709876e-05    1.9645709876e-05    1.9645709876e-05    1.9645709876e-05    
180.00    2.0310359748e-05    2.0310359748e-05    2.0310359748e-05    2.0310359748e-05    
210.00    2.1126885602e-05    2.1126885602e-05    2.1126885602e-05    2.1126885602e-05    
240.00    2.2149039824e-05    2.2149039824e-05    2.2149039824e-05    2.2149039824e-05    
270.00    2.3473849596e-05    2.3473849596e-05    2.3473849596e-05    2.3473849596e-05    
300.00    2.5297523418e-05    2.5297523418e-05    2.5297523418e-05    2.5297523418e-05    

Enhancement factor (f) [no units]
T         p = 101325.000 Pa   p = 200000.000 Pa   p = 500000.000 Pa   p = 1000000.000 Pa  p = 10000000.000 Pa 
-60.00    1.0070775889e+00    1.0140339780e+00    1.0356182628e+00    1.0730973444e+00    2.2389383691e+00    
-40.00    1.0056000404e+00    1.0110608386e+00    1.0279266142e+00    1.0569409210e+00    1.8450348547e+00    
-20.00    1.0046363568e+00    1.0090315492e+00    1.0225621564e+00    1.0456875555e+00    1.6193678937e+00    
0.00      1.0041972674e+00    1.0078137836e+00    1.0189177377e+00    1.0378059886e+00    1.4778432214e+00    
40.00     1.0048337245e+00    1.0074421047e+00    1.0151963013e+00    1.0282275373e+00    1.3082436191e+00    
80.00     1.0057272574e+00    1.0097059521e+00    1.0168897805e+00    1.0272924735e+00    1.2343415184e+00    
120.00    1.0000000000e+00    1.0001669826e+00    1.0183856131e+00    1.0312270756e+00    1.2048250858e+00    
160.00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.0231647493e+00    1.2031653250e+00    
200.00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.2128825018e+00    
250.00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.1903236875e+00    
300.00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.0480338998e+00    
350.00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00    1.0000000000e+00
"""

def main( foo ):

	return 0

if __name__ == "__main__":
	import sys
	sys.exit(main(sys.argv))

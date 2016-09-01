"""
Hermite Genz-Keister quadrature rules

Adapted from John Burkardt's implementation in Matlab

Licensing
---------
This code is distributed under the GNU LGPL license.

"""

import numpy as np
from scipy.special import ndtr
from .utils import combine


def gk16(n):
    """
HERMITE_GK16_SET sets a Hermite Genz-Keister 16 rule.

The integral:

    integral ( -oo <= x <= +oo ) f(x) exp ( - x * x ) dx

The quadrature rule:

    sum ( 1 <= i <= n ) w(i) * f ( x(i) )

A nested family of rules for the Hermite integration problem
was produced by Genz and Keister.  The structure of the nested
family was denoted by 1+2+6+10+16, that is, it comprised rules 
of successive orders O = 1, 3, 9, 19, and 35.

The precisions of these rules are P = 1, 5, 15, 29, and 51.

Consider, however, the special cases where a rule of precision 
at least 7, 17, 31 or 33 is desired.  Ordinarily, this would
suggest using the nested rule of order 9, 19, 51 or 51 respectively.
In these cases, however, the order of the rule that is used exceeds
the precision requested.  Hence, it is possible simply to select
a subset of the points in the higher precision rule and get a 
rule of lower order and the desired precision.  This accounts for
the four extra rules in this family.

The entire list of rules is therefore:

L   P   N

0   1   1  <-- Full rule
1   5   3  <-- Full rule
2   7   7  <-- Partial rule
3  15   9  <-- Full rule
4  17  17  <-- Partial rule
5  29  19  <-- Full rule
6  31  31  <-- Partial rule
7  33  33  <-- Partial rule
8  51  35  <-- Full rule 4


Reference
---------
Alan Genz, Bradley Keister,
Fully symmetric interpolatory rules for multiple integrals
over infinite regions with Gaussian weight,
Journal of Computational and Applied Mathematics,
Volume 71, 1996, pages 299-309

Florian Heiss, Viktor Winschel,
Likelihood approximation by numerical integration on sparse grids,
Journal of Econometrics,
Volume 144, 2008, pages 62-80.

Thomas Patterson,
The Optimal Addition of Points to Quadrature Formulae,
Mathematics of Computation,
Volume 22, Number 104, October 1968, pages 847-856.

Parameters
----------
N : int
    The quadrature order. Must be in the interval (0,8).

Returns
-------
X : np.ndarray
    Abscissas
W : np.ndarray
    Weights
    """

    n = [1,3,7,9,17,19,31,33,35][n]

    x = np.zeros ( n );
    w = np.zeros ( n );

    if n==1 :

      x[ 0] =   0.0000000000000000E+00;

      w[ 0] =   1.7724538509055159E+00;

    elif n==3 :

      x[ 0] =  -1.2247448713915889E+00;
      x[ 1] =   0.0000000000000000E+00;
      x[ 2] =   1.2247448713915889E+00;

      w[ 0] =   2.9540897515091930E-01;
      w[ 1] =   1.1816359006036772E+00;
      w[ 2] =   2.9540897515091930E-01;

    elif  n == 7 :

      x[ 0] =  -2.9592107790638380E+00;
      x[ 1] =  -1.2247448713915889E+00;
      x[ 2] =  -5.2403354748695763E-01;
      x[ 3] =   0.0000000000000000E+00;
      x[ 4] =   5.2403354748695763E-01;
      x[ 5] =   1.2247448713915889E+00;
      x[ 6] =   2.9592107790638380E+00;

      w[ 0] =   1.2330680655153448E-03;
      w[ 1] =   2.4557928535031393E-01;
      w[ 2] =   2.3286251787386100E-01;
      w[ 3] =   8.1310410832613500E-01;
      w[ 4] =   2.3286251787386100E-01;
      w[ 5] =   2.4557928535031393E-01;
      w[ 6] =   1.2330680655153448E-03;

    elif n == 9 :

      x[ 0] =  -2.9592107790638380E+00;
      x[ 1] =  -2.0232301911005157E+00;
      x[ 2] =  -1.2247448713915889E+00;
      x[ 3] =  -5.2403354748695763E-01;
      x[ 4] =   0.0000000000000000E+00;
      x[ 5] =   5.2403354748695763E-01;
      x[ 6] =   1.2247448713915889E+00;
      x[ 7] =   2.0232301911005157E+00;
      x[ 8] =   2.9592107790638380E+00;

      w[ 0] =   1.6708826306882348E-04;
      w[ 1] =   1.4173117873979098E-02;
      w[ 2] =   1.6811892894767771E-01;
      w[ 3] =   4.7869428549114124E-01;
      w[ 4] =   4.5014700975378197E-01;
      w[ 5] =   4.7869428549114124E-01;
      w[ 6] =   1.6811892894767771E-01;
      w[ 7] =   1.4173117873979098E-02;
      w[ 8] =   1.6708826306882348E-04;

    elif n == 17 :

      x[ 0] =  -4.4995993983103881E+00;
      x[ 1] =  -3.6677742159463378E+00;
      x[ 2] =  -2.9592107790638380E+00;
      x[ 3] =  -2.0232301911005157E+00;
      x[ 4] =  -1.8357079751751868E+00;
      x[ 5] =  -1.2247448713915889E+00;
      x[ 6] =  -8.7004089535290285E-01;
      x[ 7] =  -5.2403354748695763E-01;
      x[ 8] =   0.0000000000000000E+00;
      x[ 9] =   5.2403354748695763E-01;
      x[10] =   8.7004089535290285E-01;
      x[11] =   1.2247448713915889E+00;
      x[12] =   1.8357079751751868E+00;
      x[13] =   2.0232301911005157E+00;
      x[14] =   2.9592107790638380E+00;
      x[15] =   3.6677742159463378E+00;
      x[16] =   4.4995993983103881E+00;

      w[ 0] =   3.7463469943051758E-08;
      w[ 1] =  -1.4542843387069391E-06;
      w[ 2] =   1.8723818949278350E-04;
      w[ 3] =   1.2466519132805918E-02;
      w[ 4] =   3.4840719346803800E-03;
      w[ 5] =   1.5718298376652240E-01;
      w[ 6] =   2.5155825701712934E-02;
      w[ 7] =   4.5119803602358544E-01;
      w[ 8] =   4.7310733504965385E-01;
      w[ 9] =   4.5119803602358544E-01;
      w[10] =   2.5155825701712934E-02;
      w[11] =   1.5718298376652240E-01;
      w[12] =   3.4840719346803800E-03;
      w[13] =   1.2466519132805918E-02;
      w[14] =   1.8723818949278350E-04;
      w[15] =  -1.4542843387069391E-06;
      w[16] =   3.7463469943051758E-08;

    elif n == 19 :

      x[ 0] =  -4.4995993983103881E+00;
      x[ 1] =  -3.6677742159463378E+00;
      x[ 2] =  -2.9592107790638380E+00;
      x[ 3] =  -2.2665132620567876E+00;
      x[ 4] =  -2.0232301911005157E+00;
      x[ 5] =  -1.8357079751751868E+00;
      x[ 7] =  -1.2247448713915889E+00;
      x[ 8] =  -8.7004089535290285E-01;
      x[ 8] =  -5.2403354748695763E-01;
      x[ 9] =   0.0000000000000000E+00;
      x[10] =   5.2403354748695763E-01;
      x[11] =   8.7004089535290285E-01;
      x[12] =   1.2247448713915889E+00;
      x[13] =   1.8357079751751868E+00;
      x[14] =   2.0232301911005157E+00;
      x[15] =   2.2665132620567876E+00;
      x[16] =   2.9592107790638380E+00;
      x[17] =   3.6677742159463378E+00;
      x[18] =   4.4995993983103881E+00;

      w[ 0] =   1.5295717705322357E-09;
      w[ 1] =   1.0802767206624762E-06;
      w[ 2] =   1.0656589772852267E-04;
      w[ 3] =   5.1133174390883855E-03;
      w[ 4] =  -1.1232438489069229E-02;
      w[ 5] =   3.2055243099445879E-02;
      w[ 6] =   1.1360729895748269E-01;
      w[ 7] =   1.0838861955003017E-01;
      w[ 8] =   3.6924643368920851E-01;
      w[ 9] =   5.3788160700510168E-01;
      w[10] =   3.6924643368920851E-01;
      w[11] =   1.0838861955003017E-01;
      w[12] =   1.1360729895748269E-01;
      w[13] =   3.2055243099445879E-02;
      w[14] =  -1.1232438489069229E-02;
      w[15] =   5.1133174390883855E-03;
      w[16] =   1.0656589772852267E-04;
      w[17] =   1.0802767206624762E-06;
      w[18] =   1.5295717705322357E-09;

    elif n == 31 :

      x[ 0] =  -6.3759392709822356E+00;
      x[ 1] =  -5.6432578578857449E+00;
      x[ 2] =  -5.0360899444730940E+00;
      x[ 3] =  -4.4995993983103881E+00;
      x[ 4] =  -3.6677742159463378E+00;
      x[ 5] =  -2.9592107790638380E+00;
      x[ 6] =  -2.5705583765842968E+00;
      x[ 7] =  -2.2665132620567876E+00;
      x[ 8] =  -2.0232301911005157E+00;
      x[ 9] =  -1.8357079751751868E+00;
      x[10] =  -1.5794121348467671E+00;
      x[11] =  -1.2247448713915889E+00;
      x[12] =  -8.7004089535290285E-01;
      x[13] =  -5.2403354748695763E-01;
      x[14] =  -1.7606414208200893E-01;
      x[15] =   0.0000000000000000E+00;
      x[16] =   1.7606414208200893E-01;
      x[17] =   5.2403354748695763E-01;
      x[18] =   8.7004089535290285E-01;
      x[19] =   1.2247448713915889E+00;
      x[20] =   1.5794121348467671E+00;
      x[21] =   1.8357079751751868E+00;
      x[22] =   2.0232301911005157E+00;
      x[23] =   2.2665132620567876E+00;
      x[24] =   2.5705583765842968E+00;
      x[25] =   2.9592107790638380E+00;
      x[26] =   3.6677742159463378E+00;
      x[27] =   4.4995993983103881E+00;
      x[28] =   5.0360899444730940E+00;
      x[29] =   5.6432578578857449E+00;
      x[30] =   6.3759392709822356E+00;

      w[ 0] =   2.2365645607044459E-15;
      w[ 1] =  -2.6304696458548942E-13;
      w[ 2] =   9.0675288231679823E-12;
      w[ 3] =   1.4055252024722478E-09;
      w[ 4] =   1.0889219692128120E-06;
      w[ 5] =   1.0541662394746661E-04;
      w[ 6] =   2.6665159778939428E-05;
      w[ 7] =   4.8385208205502612E-03;
      w[ 8] =  -9.8566270434610019E-03;
      w[ 9] =   2.9409427580350787E-02;
      w[10] =   3.1210210352682834E-03;
      w[11] =   1.0939325071860877E-01;
      w[12] =   1.1594930984853116E-01;
      w[13] =   3.5393889029580544E-01;
      w[14] =   4.9855761893293160E-02;
      w[15] =   4.5888839636756751E-01;
      w[16] =   4.9855761893293160E-02;
      w[17] =   3.5393889029580544E-01;
      w[18] =   1.1594930984853116E-01;
      w[19] =   1.0939325071860877E-01;
      w[20] =   3.1210210352682834E-03;
      w[21] =   2.9409427580350787E-02;
      w[22] =  -9.8566270434610019E-03;
      w[23] =   4.8385208205502612E-03;
      w[24] =   2.6665159778939428E-05;
      w[25] =   1.0541662394746661E-04;
      w[26] =   1.0889219692128120E-06;
      w[27] =   1.4055252024722478E-09;
      w[28] =   9.0675288231679823E-12;
      w[29] =  -2.6304696458548942E-13;
      w[30] =   2.2365645607044459E-15;

    elif n == 33 :

      x[ 0] =  -6.3759392709822356E+00;
      x[ 1] =  -5.6432578578857449E+00;
      x[ 2] =  -5.0360899444730940E+00;
      x[ 3] =  -4.4995993983103881E+00;
      x[ 4] =  -4.0292201405043713E+00;
      x[ 5] =  -3.6677742159463378E+00;
      x[ 6] =  -2.9592107790638380E+00;
      x[ 7] =  -2.5705583765842968E+00;
      x[ 8] =  -2.2665132620567876E+00;
      x[ 9] =  -2.0232301911005157E+00;
      x[10] =  -1.8357079751751868E+00;
      x[11] =  -1.5794121348467671E+00;
      x[12] =  -1.2247448713915889E+00;
      x[13] =  -8.7004089535290285E-01;
      x[14] =  -5.2403354748695763E-01;
      x[15] =  -1.7606414208200893E-01;
      x[16] =   0.0000000000000000E+00;
      x[17] =   1.7606414208200893E-01;
      x[18] =   5.2403354748695763E-01;
      x[19] =   8.7004089535290285E-01;
      x[20] =   1.2247448713915889E+00;
      x[21] =   1.5794121348467671E+00;
      x[22] =   1.8357079751751868E+00;
      x[23] =   2.0232301911005157E+00;
      x[24] =   2.2665132620567876E+00;
      x[25] =   2.5705583765842968E+00;
      x[26] =   2.9592107790638380E+00;
      x[27] =   3.6677742159463378E+00;
      x[28] =   4.0292201405043713E+00;
      x[29] =   4.4995993983103881E+00;
      x[30] =   5.0360899444730940E+00;
      x[31] =   5.6432578578857449E+00;
      x[32] =   6.3759392709822356E+00;

      w[ 0] =  -1.7602932805372496E-15;
      w[ 1] =   4.7219278666417693E-13;
      w[ 2] =  -3.4281570530349562E-11;
      w[ 3] =   2.7547825138935901E-09;
      w[ 4] =  -2.3903343382803510E-08;
      w[ 5] =   1.2245220967158438E-06;
      w[ 6] =   9.8710009197409173E-05;
      w[ 7] =   1.4753204901862772E-04;
      w[ 8] =   3.7580026604304793E-03;
      w[ 9] =  -4.9118576123877555E-03;
      w[10] =   2.0435058359107205E-02;
      w[11] =   1.3032872699027960E-02;
      w[12] =   9.6913444944583621E-02;
      w[13] =   1.3726521191567551E-01;
      w[14] =   3.1208656194697448E-01;
      w[15] =   1.8411696047725790E-01;
      w[16] =   2.4656644932829619E-01;
      w[17] =   1.8411696047725790E-01;
      w[18] =   3.1208656194697448E-01;
      w[19] =   1.3726521191567551E-01;
      w[20] =   9.6913444944583621E-02;
      w[21] =   1.3032872699027960E-02;
      w[22] =   2.0435058359107205E-02;
      w[23] =  -4.9118576123877555E-03;
      w[24] =   3.7580026604304793E-03;
      w[25] =   1.4753204901862772E-04;
      w[26] =   9.8710009197409173E-05;
      w[27] =   1.2245220967158438E-06;
      w[28] =  -2.3903343382803510E-08;
      w[29] =   2.7547825138935901E-09;
      w[30] =  -3.4281570530349562E-11;
      w[31] =   4.7219278666417693E-13;
      w[32] =  -1.7602932805372496E-15;

    elif n == 35 :

      x[ 0] =  -6.3759392709822356E+00;
      x[ 1] =  -5.6432578578857449E+00;
      x[ 2] =  -5.0360899444730940E+00;
      x[ 3] =  -4.4995993983103881E+00;
      x[ 4] =  -4.0292201405043713E+00;
      x[ 5] =  -3.6677742159463378E+00;
      x[ 6] =  -3.3491639537131945E+00;
      x[ 7] =  -2.9592107790638380E+00;
      x[ 8] =  -2.5705583765842968E+00;
      x[ 9] =  -2.2665132620567876E+00;
      x[10] =  -2.0232301911005157E+00;
      x[11] =  -1.8357079751751868E+00;
      x[12] =  -1.5794121348467671E+00;
      x[13] =  -1.2247448713915889E+00;
      x[14] =  -8.7004089535290285E-01;
      x[15] =  -5.2403354748695763E-01;
      x[16] =  -1.7606414208200893E-01;
      x[17] =   0.0000000000000000E+00;
      x[18] =   1.7606414208200893E-01;
      x[19] =   5.2403354748695763E-01;
      x[20] =   8.7004089535290285E-01;
      x[21] =   1.2247448713915889E+00;
      x[22] =   1.5794121348467671E+00;
      x[23] =   1.8357079751751868E+00;
      x[24] =   2.0232301911005157E+00;
      x[25] =   2.2665132620567876E+00;
      x[26] =   2.5705583765842968E+00;
      x[27] =   2.9592107790638380E+00;
      x[28] =   3.3491639537131945E+00;
      x[29] =   3.6677742159463378E+00;
      x[30] =   4.0292201405043713E+00;
      x[31] =   4.4995993983103881E+00;
      x[32] =   5.0360899444730940E+00;
      x[33] =   5.6432578578857449E+00;
      x[34] =   6.3759392709822356E+00;

      w[ 0] =   1.8684014894510604E-18;
      w[ 1] =   9.6599466278563243E-15;
      w[ 2] =   5.4896836948499462E-12;
      w[ 3] =   8.1553721816916897E-10;
      w[ 4] =   3.7920222392319532E-08;
      w[ 5] =   4.3737818040926989E-07;
      w[ 6] =   4.8462799737020461E-06;
      w[ 7] =   6.3328620805617891E-05;
      w[ 8] =   4.8785399304443770E-04;
      w[ 9] =   1.4515580425155904E-03;
      w[10] =   4.0967527720344047E-03;
      w[11] =   5.5928828911469180E-03;
      w[12] =   2.7780508908535097E-02;
      w[13] =   8.0245518147390893E-02;
      w[14] =   1.6371221555735804E-01;
      w[15] =   2.6244871488784277E-01;
      w[16] =   3.3988595585585218E-01;
      w[17] =   9.1262675363737921E-04;
      w[18] =   3.3988595585585218E-01;
      w[19] =   2.6244871488784277E-01;
      w[20] =   1.6371221555735804E-01;
      w[21] =   8.0245518147390893E-02;
      w[22] =   2.7780508908535097E-02;
      w[23] =   5.5928828911469180E-03;
      w[24] =   4.0967527720344047E-03;
      w[25] =   1.4515580425155904E-03;
      w[26] =   4.8785399304443770E-04;
      w[27] =   6.3328620805617891E-05;
      w[28] =   4.8462799737020461E-06;
      w[29] =   4.3737818040926989E-07;
      w[30] =   3.7920222392319532E-08;
      w[31] =   8.1553721816916897E-10;
      w[32] =   5.4896836948499462E-12;
      w[33] =   9.6599466278563243E-15;
      w[34] =   1.8684014894510604E-18;

    w /= np.sum(w)
    x *= np.sqrt(2)

    return x,w



def gk18 ( n ):
    """
HERMITE_GK18_SET sets a Hermite Genz-Keister 18 rule.

Discussion:

    The integral:

    integral ( -oo <= x <= +oo ) f(x) exp ( - x * x ) dx

    The quadrature rule:

    sum ( 1 <= i <= n ) w(i) * f ( x(i) )

    A nested family of rules for the Hermite integration problem
    was produced by Genz and Keister.  The structure of the nested
    family was denoted by 1+2+6+10+18, that is, it comprised rules 
    of successive orders O = 1, 3, 9, 19, and 37.

    The precisions of these rules are P = 1, 5, 15, 29, and 55.

    Some of the data in this function was kindly supplied directly by
    Alan Genz on 24 April 2011.

Licensing:

    This code is distributed under the GNU LGPL license. 

Modified:

    30 April 2011

Author:

    John Burkardt

Reference:

    Alan Genz, Bradley Keister,
    Fully symmetric interpolatory rules for multiple integrals
    over infinite regions with Gaussian weight,
    Journal of Computational and Applied Mathematics,
    Volume 71, 1996, pages 299-309

    Florian Heiss, Viktor Winschel,
    Likelihood approximation by numerical integration on sparse grids,
    Journal of Econometrics,
    Volume 144, 2008, pages 62-80.

    Thomas Patterson,
    The Optimal Addition of Points to Quadrature Formulae,
    Mathematics of Computation,
    Volume 22, Number 104, October 1968, pages 847-856.

Parameters:

    Input, integer N, the order.

    N must be 1, 3, 9, 19, or 37.

    Output, real X(N,1), the abscissas.

    Output, real W(N,1), the weights.
    """

    n = [1,3,9,19,37][n]
    x = np.zeros ( n );
    w = np.zeros ( n );

    if n==1 :

        x[ 0] =   0.0000000000000000E+00;

        w[ 0] =   1.7724538509055159E+00;

    elif n==3 :

        x[ 0] =  -1.2247448713915889E+00;
        x[ 1] =   0.0000000000000000E+00;
        x[ 2] =   1.2247448713915889E+00;

        w[ 0] =   2.9540897515091930E-01;
        w[ 1] =   1.1816359006036772E+00;
        w[ 2] =   2.9540897515091930E-01;

    elif n==9 :

        x[ 0] =  -2.9592107790638380E+00;
        x[ 1] =  -2.0232301911005157E+00;
        x[ 2] =  -1.2247448713915889E+00;
        x[ 3] =  -5.2403354748695763E-01;
        x[ 4] =   0.0000000000000000E+00;
        x[ 5] =   5.2403354748695763E-01;
        x[ 6] =   1.2247448713915889E+00;
        x[ 7] =   2.0232301911005157E+00;
        x[ 8] =   2.9592107790638380E+00;

        w[ 0] =   1.6708826306882348E-04;
        w[ 1] =   1.4173117873979098E-02;
        w[ 2] =   1.6811892894767771E-01;
        w[ 3] =   4.7869428549114124E-01;
        w[ 4] =   4.5014700975378197E-01;
        w[ 5] =   4.7869428549114124E-01;
        w[ 6] =   1.6811892894767771E-01;
        w[ 7] =   1.4173117873979098E-02;
        w[ 8] =   1.6708826306882348E-04;

    elif n==19 :

        x[ 0] =  -4.4995993983103881E+00;
        x[ 1] =  -3.6677742159463378E+00;
        x[ 2] =  -2.9592107790638380E+00;
        x[ 3] =  -2.2665132620567876E+00;
        x[ 4] =  -2.0232301911005157E+00;
        x[ 5] =  -1.8357079751751868E+00;
        x[ 6] =  -1.2247448713915889E+00;
        x[ 7] =  -8.7004089535290285E-01;
        x[ 8] =  -5.2403354748695763E-01;
        x[ 9] =   0.0000000000000000E+00;
        x[10] =   5.2403354748695763E-01;
        x[11] =   8.7004089535290285E-01;
        x[12] =   1.2247448713915889E+00;
        x[13] =   1.8357079751751868E+00;
        x[14] =   2.0232301911005157E+00;
        x[15] =   2.2665132620567876E+00;
        x[16] =   2.9592107790638380E+00;
        x[17] =   3.6677742159463378E+00;
        x[18] =   4.4995993983103881E+00;

        w[ 0] =   1.5295717705322357E-09;
        w[ 1] =   1.0802767206624762E-06;
        w[ 2] =   1.0656589772852267E-04;
        w[ 3] =   5.1133174390883855E-03;
        w[ 4] =  -1.1232438489069229E-02;
        w[ 5] =   3.2055243099445879E-02;
        w[ 6] =   1.1360729895748269E-01;
        w[ 7] =   1.0838861955003017E-01;
        w[ 8] =   3.6924643368920851E-01;
        w[ 9] =   5.3788160700510168E-01;
        w[10] =   3.6924643368920851E-01;
        w[11] =   1.0838861955003017E-01;
        w[12] =   1.1360729895748269E-01;
        w[13] =   3.2055243099445879E-02;
        w[14] =  -1.1232438489069229E-02;
        w[15] =   5.1133174390883855E-03;
        w[16] =   1.0656589772852267E-04;
        w[17] =   1.0802767206624762E-06;
        w[18] =   1.5295717705322357E-09;

    elif n==37 :

        x[ 0] =  -6.853200069757519;
        x[ 1] =  -6.124527854622158;
        x[ 2] =  -5.521865209868350;
        x[ 3] =  -4.986551454150765;
        x[ 4] =  -4.499599398310388;
        x[ 5] =  -4.057956316089741;
        x[ 6] =  -3.667774215946338;
        x[ 7] =  -3.315584617593290;
        x[ 8] =  -2.959210779063838;
        x[9] =  -2.597288631188366;
        x[10] =  -2.266513262056788;
        x[11] =  -2.023230191100516;
        x[12] =  -1.835707975175187;
        x[13] =  -1.561553427651873;
        x[14] =  -1.224744871391589;
        x[15] =  -0.870040895352903;
        x[16] =  -0.524033547486958;
        x[17] =  -0.214618180588171;
        x[18] =   0.000000000000000;
        x[19] =   0.214618180588171;
        x[20] =   0.524033547486958;
        x[21] =   0.870040895352903;
        x[22] =   1.224744871391589;
        x[23] =   1.561553427651873;
        x[24] =   1.835707975175187;
        x[25] =   2.023230191100516;
        x[26] =   2.266513262056788;
        x[27] =   2.597288631188366;
        x[28] =   2.959210779063838;
        x[29] =   3.315584617593290;
        x[30] =   3.667774215946338;
        x[31] =   4.057956316089741;
        x[32] =   4.499599398310388;
        x[33] =   4.986551454150765;
        x[34] =   5.521865209868350;
        x[35] =   6.124527854622158;
        x[36] =   6.853200069757519;

        w[ 0] = 0.19030350940130498E-20;
        w[ 1] = 0.187781893143728947E-16;
        w[ 2] = 0.182242751549129356E-13;
        w[ 3] = 0.45661763676186859E-11;
        w[ 4] = 0.422525843963111041E-09;
        w[ 5] = 0.16595448809389819E-07;
        w[ 6] = 0.295907520230744049E-06;
        w[ 7] = 0.330975870979203419E-05;
        w[ 8] = 0.32265185983739747E-04;
        w[ 9] = 0.234940366465975222E-03;
        w[10] = 0.985827582996483824E-03;
        w[11] = 0.176802225818295443E-02;
        w[12] = 0.43334988122723492E-02;
        w[13] = 0.15513109874859354E-01;
        w[14] = 0.442116442189845444E-01;
        w[15] = 0.937208280655245902E-01;
        w[16] = 0.143099302896833389E+00;
        w[17] = 0.147655710402686249E+00;
        w[18] = 0.968824552928425499E-01;
        w[19] = 0.147655710402686249E+00;
        w[20] = 0.143099302896833389E+00;
        w[21] = 0.937208280655245902E-01;
        w[22] = 0.442116442189845444E-01;
        w[23] = 0.15513109874859354E-01;
        w[24] = 0.43334988122723492E-02;
        w[25] = 0.176802225818295443E-02;
        w[26] = 0.985827582996483824E-03;
        w[27] = 0.234940366465975222E-03;
        w[28] = 0.32265185983739747E-04;
        w[29] = 0.330975870979203419E-05;
        w[30] = 0.295907520230744049E-06;
        w[31] = 0.16595448809389819E-07;
        w[32] = 0.422525843963111041E-09;
        w[33] = 0.45661763676186859E-11;
        w[34] = 0.182242751549129356E-13;
        w[35] = 0.187781893143728947E-16;
        w[36] = 0.19030350940130498E-20;

    w /= np.sum(w)
    x *= np.sqrt(2)

    return x,w




def gk22 ( n ):

    """
HERMITE_GK22_SET sets a Genz-Keister 22 Hermite rule.

Discussion:

    The integral:

    integral ( -oo <= x <= +oo ) f(x) exp ( - x * x ) dx

    The quadrature rule:

    sum ( 1 <= i <= n ) w(i) * f ( x(i) )

    A nested family of rules for the Hermite integration problem
    was produced by Genz and Keister.  The structure of the nested
    family was denoted by 1+2+6+10+22, that is, it comprised rules
    of successive orders O = 1, 3, 9, 19, and 41.

    The precisions of these rules are P = 1, 5, 15, 29, and 63.

    Some of the data in this function was kindly supplied directly by
    Alan Genz on 24 April 2011.

Licensing:

    This code is distributed under the GNU LGPL license.

Modified:

    26 April 2011

Author:

    John Burkardt

Reference:

    Alan Genz, Bradley Keister,
    Fully symmetric interpolatory rules for multiple integrals
    over infinite regions with Gaussian weight,
    Journal of Computational and Applied Mathematics,
    Volume 71, 1996, pages 299-309

    Thomas Patterson,
    The Optimal Addition of Points to Quadrature Formulae,
    Mathematics of Computation,
    Volume 22, Number 104, October 1968, pages 847-856.

Parameters:

    Input, integer N, the order.
    Legal values are 1, 3, 9, 19, and 41.

    Output, real X(N,1), the abscissas.

    Output, real W(N,1), the weights.
    """

    n = [1,3,9,19,41][n]

    x = np.zeros ( n );
    w = np.zeros ( n );

    if n==1 :

        x[ 0] =   0.0000000000000000;

        w[ 0] =   1.7724538509055159E+00;

    elif n==3 :

        x[ 0] =  -1.2247448713915889;
        x[ 1] =   0.0000000000000000;
        x[ 2] =   1.2247448713915889;

        w[ 0] =   2.9540897515091930E-01;
        w[ 1] =   1.1816359006036772E+00;
        w[ 2] =   2.9540897515091930E-01;

    elif n==9 :

        x[ 0] =  -2.9592107790638380;
        x[ 1] =  -2.0232301911005157;
        x[ 2] =  -1.2247448713915889;
        x[ 3] =  -0.52403354748695763;
        x[ 4] =   0.0000000000000000;
        x[ 5] =   0.52403354748695763;
        x[ 6] =   1.2247448713915889;
        x[ 7] =   2.0232301911005157;
        x[ 8] =   2.9592107790638380;

        w[ 0] =   1.6708826306882348E-04;
        w[ 1] =   1.4173117873979098E-02;
        w[ 2] =   1.6811892894767771E-01;
        w[ 3] =   4.7869428549114124E-01;
        w[ 4] =   4.5014700975378197E-01;
        w[ 5] =   4.7869428549114124E-01;
        w[ 6] =   1.6811892894767771E-01;
        w[ 7] =   1.4173117873979098E-02;
        w[ 8] =   1.6708826306882348E-04;

    elif n==19 :

        x[ 0] =  -4.4995993983103881;
        x[ 1] =  -3.6677742159463378;
        x[ 2] =  -2.9592107790638380;
        x[ 3] =  -2.2665132620567876;
        x[ 4] =  -2.0232301911005157;
        x[ 5] =  -1.8357079751751868;
        x[ 6] =  -1.2247448713915889;
        x[ 7] =  -0.87004089535290285;
        x[ 8] =  -0.52403354748695763;
        x[9] =   0.0000000000000000;
        x[10] =   0.52403354748695763;
        x[11] =   0.87004089535290285;
        x[12] =   1.2247448713915889;
        x[13] =   1.8357079751751868;
        x[14] =   2.0232301911005157;
        x[15] =   2.2665132620567876;
        x[16] =   2.9592107790638380;
        x[17] =   3.6677742159463378;
        x[18] =   4.4995993983103881;

        w[ 0] =   1.5295717705322357E-09;
        w[ 1] =   1.0802767206624762E-06;
        w[ 2] =   1.0656589772852267E-04;
        w[ 3] =   5.1133174390883855E-03;
        w[ 4] =  -1.1232438489069229E-02;
        w[ 5] =   3.2055243099445879E-02;
        w[ 6] =   1.1360729895748269E-01;
        w[ 7] =   1.0838861955003017E-01;
        w[ 8] =   3.6924643368920851E-01;
        w[9] =   5.3788160700510168E-01;
        w[10] =   3.6924643368920851E-01;
        w[11] =   1.0838861955003017E-01;
        w[12] =   1.1360729895748269E-01;
        w[13] =   3.2055243099445879E-02;
        w[14] =  -1.1232438489069229E-02;
        w[15] =   5.1133174390883855E-03;
        w[16] =   1.0656589772852267E-04;
        w[17] =   1.0802767206624762E-06;
        w[18] =   1.5295717705322357E-09;

    elif n==41 :

        x[ 0] =  -7.251792998192644;
        x[ 1] =  -6.547083258397540;
        x[ 2] =  -5.961461043404500;
        x[ 3] =  -5.437443360177798;
        x[ 4] =  -4.953574342912980;
        x[ 5] =  -4.4995993983103881;
        x[ 6] =  -4.070919267883068;
        x[ 7] =  -3.6677742159463378;
        x[ 8] =  -3.296114596212218;
        x[9] =  -2.9592107790638380;
        x[10] =  -2.630415236459871;
        x[11] =  -2.2665132620567876;
        x[12] =  -2.043834754429505;
        x[13] =  -2.0232301911005157;
        x[14] =  -1.8357079751751868;
        x[15] =  -1.585873011819188;
        x[16] =  -1.2247448713915889;
        x[17] =  -0.87004089535290285;
        x[18] =  -0.52403354748695763;
        x[19] =  -0.195324784415805;
        x[20] =   0.0000000000000000;
        x[21] =   0.195324784415805;
        x[22] =   0.52403354748695763;
        x[23] =   0.87004089535290285;
        x[24] =   1.2247448713915889;
        x[25] =   1.585873011819188;
        x[26] =   1.8357079751751868;
        x[27] =   2.0232301911005157;
        x[28] =   2.043834754429505;
        x[29] =   2.2665132620567876;
        x[30] =   2.630415236459871;
        x[31] =   2.9592107790638380;
        x[32] =   3.296114596212218;
        x[33] =   3.6677742159463378;
        x[34] =   4.070919267883068;
        x[35] =   4.4995993983103881;
        x[36] =   4.953574342912980;
        x[37] =   5.437443360177798;
        x[38] =   5.961461043404500;
        x[39] =   6.547083258397540;
        x[40] =   7.251792998192644;

        w[ 0] =   0.664195893812757801E-23;
        w[ 1] =   0.860427172512207236E-19;
        w[ 2] =   0.1140700785308509E-15;
        w[ 3] =   0.408820161202505983E-13;
        w[ 4] =   0.581803393170320419E-11;
        w[ 5] =   0.400784141604834759E-09;
        w[ 6] =   0.149158210417831408E-07;
        w[ 7] =   0.315372265852264871E-06;
        w[ 8] =   0.381182791749177506E-05;
        w[9] =   0.288976780274478689E-04;
        w[10] =   0.189010909805097887E-03;
        w[11] =   0.140697424065246825E-02;
        w[12] = - 0.144528422206988237E-01;
        w[13] =   0.178852543033699732E-01;
        w[14] =   0.705471110122962612E-03;
        w[15] =   0.165445526705860772E-01;
        w[16] =   0.45109010335859128E-01;
        w[17] =   0.928338228510111845E-01;
        w[18] =   0.145966293895926429E+00;
        w[19] =   0.165639740400529554E+00;
        w[20] =   0.562793426043218877E-01;
        w[21] =   0.165639740400529554E+00;
        w[22] =   0.145966293895926429E+00;
        w[23] =   0.928338228510111845E-01;
        w[24] =   0.45109010335859128E-01;
        w[25] =   0.165445526705860772E-01;
        w[26] =   0.705471110122962612E-03;
        w[27] =   0.178852543033699732E-01;
        w[28] = - 0.144528422206988237E-01;
        w[29] =   0.140697424065246825E-02;
        w[30] =   0.189010909805097887E-03;
        w[31] =   0.288976780274478689E-04;
        w[32] =   0.381182791749177506E-05;
        w[33] =   0.315372265852264871E-06;
        w[34] =   0.149158210417831408E-07;
        w[35] =   0.400784141604834759E-09;
        w[36] =   0.581803393170320419E-11;
        w[37] =   0.408820161202505983E-13;
        w[38] =   0.1140700785308509E-15;
        w[39] =   0.860427172512207236E-19;
        w[40] =   0.664195893812757801E-23;

    w /= np.sum(w)
    x *= np.sqrt(2)

    return x,w




def gk24 ( n ):

    """

HERMITE_GK24_SET sets a Genz-Keister 24 Hermite rule.

Discussion:

    The integral:

    integral ( -oo <= x <= +oo ) f(x) exp ( - x * x ) dx

    The quadrature rule:

    sum ( 1 <= i <= n ) w(i) * f ( x(i) )

    A nested family of rules for the Hermite integration problem
    was produced by Genz and Keister.  The structure of the nested
    family was denoted by 1+2+6+10+24, that is, it comprised rules
    of successive orders O = 1, 3, 9, 19, and 43.

    The precisions of these rules are P = 1, 5, 15, 29, and 67.

    Some of the data in this function was kindly supplied directly by
    Alan Genz on 24 April 2011.

Licensing:

    This code is distributed under the GNU LGPL license.

Modified:

    30 April 2011

Author:

    John Burkardt

Reference:

    Alan Genz, Bradley Keister,
    Fully symmetric interpolatory rules for multiple integrals
    over infinite regions with Gaussian weight,
    Journal of Computational and Applied Mathematics,
    Volume 71, 1996, pages 299-309

    Thomas Patterson,
    The Optimal Addition of Points to Quadrature Formulae,
    Mathematics of Computation,
    Volume 22, Number 104, October 1968, pages 847-856.

Parameters:

    Input, integer N, the order.
    Legal values are 1, 3, 9, 19, and 43.

    Output, real X(N,1), the abscissas.

    Output, real W(N,1), the weights.
    """

    n = [1, 3, 9, 19, 43][n]

    w = np.zeros ( n );
    x = np.zeros ( n );

    if n==1 :

        x[ 0] =   0.0000000000000000;

        w[ 0] =   1.7724538509055159E+00;

    elif n==3 :

        x[ 0] =  -1.2247448713915889;
        x[ 1] =   0.0000000000000000;
        x[ 2] =   1.2247448713915889;

        w[ 0] =   2.9540897515091930E-01;
        w[ 1] =   1.1816359006036772E+00;
        w[ 2] =   2.9540897515091930E-01;

    elif n==9 :

        x[ 0] =  -2.9592107790638380;
        x[ 1] =  -2.0232301911005157;
        x[ 2] =  -1.2247448713915889;
        x[ 3] =  -0.52403354748695763;
        x[ 4] =   0.0000000000000000;
        x[ 5] =   0.52403354748695763;
        x[ 6] =   1.2247448713915889;
        x[ 7] =   2.0232301911005157;
        x[ 8] =   2.9592107790638380;

        w[ 0] =   1.6708826306882348E-04;
        w[ 1] =   1.4173117873979098E-02;
        w[ 2] =   1.6811892894767771E-01;
        w[ 3] =   4.7869428549114124E-01;
        w[ 4] =   4.5014700975378197E-01;
        w[ 5] =   4.7869428549114124E-01;
        w[ 6] =   1.6811892894767771E-01;
        w[ 7] =   1.4173117873979098E-02;
        w[ 8] =   1.6708826306882348E-04;

    elif n==19 :

        x[ 0] =  -4.4995993983103881;
        x[ 1] =  -3.6677742159463378;
        x[ 2] =  -2.9592107790638380;
        x[ 3] =  -2.2665132620567876;
        x[ 4] =  -2.0232301911005157;
        x[ 5] =  -1.8357079751751868;
        x[ 6] =  -1.2247448713915889;
        x[ 7] =  -0.87004089535290285;
        x[ 8] =  -0.52403354748695763;
        x[ 9] =   0.0000000000000000;
        x[10] =   0.52403354748695763;
        x[11] =   0.87004089535290285;
        x[12] =   1.2247448713915889;
        x[13] =   1.8357079751751868;
        x[14] =   2.0232301911005157;
        x[15] =   2.2665132620567876;
        x[16] =   2.9592107790638380;
        x[17] =   3.6677742159463378;
        x[18] =   4.4995993983103881;

        w[ 0] =   1.5295717705322357E-09;
        w[ 1] =   1.0802767206624762E-06;
        w[ 2] =   1.0656589772852267E-04;
        w[ 3] =   5.1133174390883855E-03;
        w[ 4] =  -1.1232438489069229E-02;
        w[ 5] =   3.2055243099445879E-02;
        w[ 6] =   1.1360729895748269E-01;
        w[ 7] =   1.0838861955003017E-01;
        w[ 8] =   3.6924643368920851E-01;
        w[ 9] =   5.3788160700510168E-01;
        w[10] =   3.6924643368920851E-01;
        w[11] =   1.0838861955003017E-01;
        w[12] =   1.1360729895748269E-01;
        w[13] =   3.2055243099445879E-02;
        w[14] =  -1.1232438489069229E-02;
        w[15] =   5.1133174390883855E-03;
        w[16] =   1.0656589772852267E-04;
        w[17] =   1.0802767206624762E-06;
        w[18] =   1.5295717705322357E-09;

    elif n==43 :

        x[ 0] = -10.167574994881873;
        x[ 1] =  -7.231746029072501;
        x[ 2] =  -6.535398426382995;
        x[ 3] =  -5.954781975039809;
        x[ 4] =  -5.434053000365068;
        x[ 5] =  -4.952329763008589;
        x[ 6] =  -4.4995993983103881;
        x[ 7] =  -4.071335874253583;
        x[ 8] =  -3.6677742159463378;
        x[ 9] =  -3.295265921534226;
        x[10] =  -2.9592107790638380;
        x[11] =  -2.633356763661946;
        x[12] =  -2.2665132620567876;
        x[13] =  -2.089340389294661;
        x[14] =  -2.0232301911005157;
        x[15] =  -1.8357079751751868;
        x[16] =  -1.583643465293944;
        x[17] =  -1.2247448713915889;
        x[18] =  -0.87004089535290285;
        x[19] =  -0.52403354748695763;
        x[20] =  -0.196029453662011;
        x[21] =   0.0000000000000000;
        x[22] =   0.196029453662011;
        x[23] =   0.52403354748695763;
        x[24] =   0.87004089535290285;
        x[25] =   1.2247448713915889;
        x[26] =   1.583643465293944;
        x[27] =   1.8357079751751868;
        x[28] =   2.0232301911005157;
        x[29] =   2.089340389294661;
        x[30] =   2.2665132620567876;
        x[31] =   2.633356763661946;
        x[32] =   2.9592107790638380;
        x[33] =   3.295265921534226;
        x[34] =   3.6677742159463378;
        x[35] =   4.071335874253583;
        x[36] =   4.4995993983103881;
        x[37] =   4.952329763008589;
        x[38] =   5.434053000365068;
        x[39] =   5.954781975039809;
        x[40] =   6.535398426382995;
        x[41] =   7.231746029072501;
        x[42] =  10.167574994881873;

        w[ 0] =   0.546191947478318097E-37;
        w[ 1] =   0.87544909871323873E-23;
        w[ 2] =   0.992619971560149097E-19;
        w[ 3] =   0.122619614947864357E-15;
        w[ 4] =   0.421921851448196032E-13;
        w[ 5] =   0.586915885251734856E-11;
        w[ 6] =   0.400030575425776948E-09;
        w[ 7] =   0.148653643571796457E-07;
        w[ 8] =   0.316018363221289247E-06;
        w[ 9] =   0.383880761947398577E-05;
        w[10] =   0.286802318064777813E-04;
        w[11] =   0.184789465688357423E-03;
        w[12] =   0.150909333211638847E-02;
        w[13] = - 0.38799558623877157E-02;
        w[14] =   0.67354758901013295E-02;
        w[15] =   0.139966252291568061E-02;
        w[16] =   0.163616873493832402E-01;
        w[17] =   0.450612329041864976E-01;
        w[18] =   0.928711584442575456E-01;
        w[19] =   0.145863292632147353E+00;
        w[20] =   0.164880913687436689E+00;
        w[21] =   0.579595986101181095E-01;
        w[22] =   0.164880913687436689E+00;
        w[23] =   0.145863292632147353E+00;
        w[24] =   0.928711584442575456E-01;
        w[25] =   0.450612329041864976E-01;
        w[26] =   0.163616873493832402E-01;
        w[27] =   0.139966252291568061E-02;
        w[28] =   0.67354758901013295E-02;
        w[29] = - 0.38799558623877157E-02;
        w[30] =   0.150909333211638847E-02;
        w[31] =   0.184789465688357423E-03;
        w[32] =   0.286802318064777813E-04;
        w[33] =   0.383880761947398577E-05;
        w[34] =   0.316018363221289247E-06;
        w[35] =   0.148653643571796457E-07;
        w[36] =   0.400030575425776948E-09;
        w[37] =   0.586915885251734856E-11;
        w[38] =   0.421921851448196032E-13;
        w[39] =   0.122619614947864357E-15;
        w[40] =   0.992619971560149097E-19;
        w[41] =   0.87544909871323873E-23;
        w[42] =   0.546191947478318097E-37;

    w /= np.sum(w)
    x *= np.sqrt(2)

    return x,w


def gk(order, dist, rule=24):

    assert isinstance(rule, int)

    if len(dist) > 1:

        if isinstance(order, int):
            xw = [gk(order, d, rule) for d in dist]
        else:
            xw = [gk(order[i], dist[i], rule)
                    for i in xrange(len(dist))]

        x = [_[0][0] for _ in xw]
        x = combine(x).T
        w = [_[1] for _ in xw]
        w = np.prod(combine(w), -1)

        return x, w

    foo = eval("gk"+str(rule))
    x,w = foo(order)
    x = dist.inv(ndtr(x))
    x = x.reshape(1, x.size)

    return x, w





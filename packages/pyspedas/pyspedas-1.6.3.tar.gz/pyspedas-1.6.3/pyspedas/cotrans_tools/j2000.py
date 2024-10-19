"""
Parameters for J2000 coordinate system conversions.

Notes
-----
This is used in cotrans_lib.
This is addapted from file spd_get_nut_angles_vec.pro of IDL spedas.

"""
import numpy as np


def set_j2000_params():
    """
    Set J2000 parameters.

    Parameters
    ----------
    none

    Returns
    -------
    funar: array(106, 5) of float

    sinco: array(106, 2) of float

    cosco: array(106, 2) of float

    """
    funar = np.array([[0.0, 1.0, 0.0, 0.0, 0.0],
                      [0.0, 2.0, 0.0, 0.0, 0.0],
                      [2.0, 1.0, 0.0, -2.0, 0.0],
                      [-2.0, 0.0, 0.0, 2.0, 0.0],
                      [2.0, 2.0, 0.0, -2.0, 0.0],
                      [0.0, 0.0, -1.0, 1.0, -1.0],
                      [2.0, 1.0, -2.0, 0.0, -2.0],
                      [-2.0, 1.0, 0.0, 2.0, 0.0],
                      [2.0, 2.0, 0.0, 0.0, -2.0],
                      [0.0, 0.0, 1.0, 0.0, 0.0],
                      [2.0, 2.0, 1.0, 0.0, -2.0],
                      [2.0, 2.0, -1.0, 0.0, -2.0],
                      [2.0, 1.0, 0.0, 0.0, -2.0],
                      [0.0, 0.0, 0.0, 2.0, -2.0],
                      [2.0, 0.0, 0.0, 0.0, -2.0],
                      [0.0, 0.0, 2.0, 0.0, 0.0],
                      [0.0, 1.0, 1.0, 0.0, 0.0],
                      [2.0, 2.0, 2.0, 0.0, -2.0],
                      [0.0, 1.0, -1.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -2.0, 2.0],
                      [2.0, 1.0, -1.0, 0.0, -2.0],
                      [0.0, 1.0, 0.0, 2.0, -2.0],
                      [2.0, 1.0, 1.0, 0.0, -2.0],
                      [0.0, 0.0, 0.0, 1.0, -1.0],
                      [0.0, 0.0, 1.0, 2.0, -2.0],
                      [-2.0, 1.0, 0.0, 0.0, 2.0],
                      [-2.0, 0.0, 1.0, 0.0, 2.0],
                      [0.0, 2.0, 1.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0, -1.0, 1.0],
                      [2.0, 0.0, 1.0, 0.0, -2.0],
                      [2.0, 2.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 1.0, 0.0],
                      [2.0, 1.0, 0.0, 0.0, 0.0],
                      [2.0, 2.0, 0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0, 1.0, -2.0],
                      [2.0, 2.0, 0.0, -1.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 2.0],
                      [0.0, 1.0, 0.0, 1.0, 0.0],
                      [0.0, 1.0, 0.0, -1.0, 0.0],
                      [2.0, 2.0, 0.0, -1.0, 2.0],
                      [2.0, 1.0, 0.0, 1.0, 0.0],
                      [2.0, 2.0, 0.0, 0.0, 2.0],
                      [0.0, 0.0, 0.0, 2.0, 0.0],
                      [2.0, 2.0, 0.0, 1.0, -2.0],
                      [2.0, 2.0, 0.0, 2.0, 0.0],
                      [2.0, 0.0, 0.0, 0.0, 0.0],
                      [2.0, 1.0, 0.0, -1.0, 0.0],
                      [0.0, 1.0, 0.0, -1.0, 2.0],
                      [0.0, 1.0, 0.0, 1.0, -2.0],
                      [2.0, 1.0, 0.0, -1.0, 2.0],
                      [0.0, 0.0, 1.0, 1.0, -2.0],
                      [2.0, 2.0, 1.0, 0.0, 0.0],
                      [2.0, 2.0, -1.0, 0.0, 0.0],
                      [2.0, 2.0, 0.0, 1.0, 2.0],
                      [0.0, 0.0, 0.0, 1.0, 2.0],
                      [2.0, 2.0, 0.0, 2.0, -2.0],
                      [0.0, 1.0, 0.0, 0.0, 2.0],
                      [2.0, 1.0, 0.0, 0.0, 2.0],
                      [2.0, 1.0, 0.0, 1.0, -2.0],
                      [0.0, 1.0, 0.0, 0.0, -2.0],
                      [0.0, 0.0, -1.0, 1.0, 0.0],
                      [2.0, 1.0, 0.0, 2.0, 0.0],
                      [0.0, 0.0, 1.0, 0.0, -2.0],
                      [-2.0, 0.0, 0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 1.0],
                      [0.0, 0.0, 1.0, 1.0, 0.0],
                      [2.0, 0.0, 0.0, 1.0, 0.0],
                      [2.0, 2.0, -1.0, 1.0, 0.0],
                      [2.0, 2.0, -1.0, -1.0, 2.0],
                      [0.0, 1.0, 0.0, -2.0, 0.0],
                      [2.0, 2.0, 0.0, 3.0, 0.0],
                      [2.0, 2.0, -1.0, 0.0, 2.0],
                      [2.0, 2.0, 1.0, 1.0, 0.0],
                      [2.0, 1.0, 0.0, -1.0, -2.0],
                      [0.0, 1.0, 0.0, 2.0, 0.0],
                      [0.0, 2.0, 0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0, 3.0, 0.0],
                      [2.0, 2.0, 0.0, 0.0, 1.0],
                      [0.0, 2.0, 0.0, -1.0, 0.0],
                      [0.0, 0.0, 0.0, 1.0, -4.0],
                      [2.0, 2.0, 0.0, -2.0, 2.0],
                      [2.0, 2.0, 0.0, -1.0, 4.0],
                      [0.0, 0.0, 0.0, 2.0, -4.0],
                      [2.0, 2.0, 1.0, 1.0, -2.0],
                      [2.0, 1.0, 0.0, 1.0, 2.0],
                      [2.0, 2.0, 0.0, -2.0, 4.0],
                      [4.0, 2.0, 0.0, -1.0, 0.0],
                      [0.0, 0.0, -1.0, 1.0, -2.0],
                      [2.0, 1.0, 0.0, 2.0, -2.0],
                      [2.0, 2.0, 0.0, 2.0, 2.0],
                      [0.0, 1.0, 0.0, 1.0, 2.0],
                      [4.0, 2.0, 0.0, 0.0, -2.0],
                      [2.0, 2.0, 0.0, 3.0, -2.0],
                      [2.0, 0.0, 0.0, 1.0, -2.0],
                      [2.0, 1.0, 1.0, 0.0, 0.0],
                      [0.0, 1.0, -1.0, -1.0, 2.0],
                      [-2.0, 1.0, 0.0, 0.0, 0.0],
                      [2.0, 2.0, 0.0, 0.0, -1.0],
                      [0.0, 0.0, 1.0, 0.0, 2.0],
                      [-2.0, 0.0, 0.0, 1.0, -2.0],
                      [2.0, 1.0, -1.0, 0.0, 0.0],
                      [0.0, 1.0, 1.0, 1.0, -2.0],
                      [-2.0, 0.0, 0.0, 1.0, 2.0],
                      [0.0, 0.0, 0.0, 2.0, 2.0],
                      [2.0, 2.0, 0.0, 0.0, 4.0],
                      [0.0, 0.0, 1.0, 0.0, 1.0]])

    sinco = np.array([[-171996.0, -174.2],
                      [2062.0, 0.2],
                      [46.0, 0.0],
                      [11.0, 0.0],
                      [-3.0, 0.0],
                      [-3.0, 0.0],
                      [-2.0, 0.0],
                      [1.0, 0.0],
                      [-13187.0, -1.6],
                      [1426.0, -3.4],
                      [-517.0, 1.2],
                      [217.0, -0.5],
                      [129.0, 0.1],
                      [48.0, 0.0],
                      [-22.0, 0.0],
                      [17.0, -0.1],
                      [-15.0, 0.0],
                      [-16.0, 0.1],
                      [-12.0, 0.0],
                      [-6.0, 0.0],
                      [-5.0, 0.0],
                      [4.0, 0.0],
                      [4.0, 0.0],
                      [-4.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [-2274.0, -0.2],
                      [712.0, 0.1],
                      [-386.0, -0.4],
                      [-301.0, 0.0],
                      [-158.0, 0.0],
                      [123.0, 0.0],
                      [63.0, 0.0],
                      [63.0, 0.1],
                      [-58.0, -0.1],
                      [-59.0, 0.0],
                      [-51.0, 0.0],
                      [-38.0, 0.0],
                      [29.0, 0.0],
                      [29.0, 0.0],
                      [-31.0, 0.0],
                      [26.0, 0.0],
                      [21.0, 0.0],
                      [16.0, 0.0],
                      [-13.0, 0.0],
                      [-10.0, 0.0],
                      [-7.0, 0.0],
                      [7.0, 0.0],
                      [-7.0, 0.0],
                      [-8.0, 0.0],
                      [6.0, 0.0],
                      [6.0, 0.0],
                      [-6.0, 0.0],
                      [-7.0, 0.0],
                      [6.0, 0.0],
                      [-5.0, 0.0],
                      [5.0, 0.0],
                      [-5.0, 0.0],
                      [-4.0, 0.0],
                      [4.0, 0.0],
                      [-4.0, 0.0],
                      [-3.0, 0.0],
                      [3.0, 0.0],
                      [-3.0, 0.0],
                      [-3.0, 0.0],
                      [-2.0, 0.0],
                      [-3.0, 0.0],
                      [-3.0, 0.0],
                      [2.0, 0.0],
                      [-2.0, 0.0],
                      [2.0, 0.0],
                      [-2.0, 0.0],
                      [2.0, 0.0],
                      [2.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [-2.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0]])

    cosco = np.array([[92025.0, 8.9],
                      [-895.0, 0.5],
                      [-24.0, 0.0],
                      [0.0, 0.0],
                      [1.0, 0.0],
                      [0.0, 0.0],
                      [1.0, 0.0],
                      [0.0, 0.0],
                      [5736.0, -3.1],
                      [54.0, -0.10],
                      [224.0, -0.6],
                      [-95.0, 0.3],
                      [-70.0, 0.0],
                      [1.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [9.0, 0.0],
                      [7.0, 0.0],
                      [6.0, 0.0],
                      [3.0, 0.0],
                      [3.0, 0.0],
                      [-2.0, 0.0],
                      [-2.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [977.0, -0.5],
                      [-7.0, 0.0],
                      [200.0, 0.0],
                      [129.0, -0.1],
                      [-1.0, 0.0],
                      [-53.0, 0.0],
                      [-2.0, 0.0],
                      [-33.0, 0.0],
                      [32.0, 0.0],
                      [26.0, 0.0],
                      [27.0, 0.0],
                      [16.0, 0.0],
                      [-1.0, 0.0],
                      [-12.0, 0.0],
                      [13.0, 0.0],
                      [-1.0, 0.0],
                      [-10.0, 0.0],
                      [-8.0, 0.0],
                      [7.0, 0.0],
                      [5.0, 0.0],
                      [0.0, 0.0],
                      [-3.0, 0.0],
                      [3.0, 0.0],
                      [3.0, 0.0],
                      [0.0, 0.0],
                      [-3.0, 0.0],
                      [3.0, 0.0],
                      [3.0, 0.0],
                      [-3.0, 0.0],
                      [3.0, 0.0],
                      [0.0, 0.0],
                      [3.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [0.0, 0.0],
                      [-1.0, 0.0],
                      [-1.0, 0.0],
                      [0.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [0.0, 0.0],
                      [-1.0, 0.0],
                      [1.0, 0.0],
                      [1.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [-1.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0],
                      [0.0, 0.0]])

    return funar, sinco, cosco

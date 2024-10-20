#!/usr/bin/python3

import numpy as np

def from_numpy_array(arr,environment="bmatrix"):
    """
    Converts a NumPy array into a LaTeX string representation, formatted as a matrix 
    or vector within a LaTeX environment (e.g., bmatrix, pmatrix, etc.).

    Parameters:
    -----------
    arr : np.ndarray
        The input NumPy array. The array can be one-dimensional or two-dimensional.
        or 
        a list
    
    environment : str, optional
        The LaTeX environment to use for the matrix. By default, "bmatrix" is used, 
        which produces square brackets around the matrix. Other valid environments 
        include "pmatrix" (parentheses), "Bmatrix" (curly braces), etc.

    Returns:
    --------
    latex_str : str
        A string representing the NumPy array in LaTeX matrix format, enclosed within
        the specified environment.

    Raises:
    -------
    ValueError
        If the input is not a NumPy array or if the array has more than two dimensions.

    Examples:
    ---------
    >>> arr1d = np.array([1, 2, 3])
    >>> print(from_numpy_array(arr1d))
    \begin{bmatrix}
    1\\
    2\\
    3
    \end{bmatrix}

    >>> arr2d = np.array([[1, 2], [3, 4], [5, 6]])
    >>> print(from_numpy_array(arr2d, "pmatrix"))
    \begin{pmatrix}
    1 & 2\\
    3 & 4\\
    5 & 6
    \end{pmatrix}
    """
    if not isinstance(arr, (list,np.ndarray)):
        raise ValueError("Input must be a NumPy array.")
    
    # Verifica se o array é unidimensional ou bidimensional
    if isinstance(arr,list) or len(arr.shape) == 1:
        latex_str = "\\begin{"+environment+"}\n" + "\\\\\n".join(map(str, arr)) + "\n\\end{"+environment+"}"
    
    elif len(arr.shape) == 2:
        rows = []
        for row in arr:
            rows.append(" & ".join(map(str, row)))
        latex_str = "\\begin{"+environment+"}\n" + "\\\\\n".join(rows) + "\n\\end{"+environment+"}"
    
    else:
        raise ValueError("The function only supports one- or two-dimensional arrays.")
    
    return latex_str

if __name__ == "__main__":
    # Exemplo de uso:
    arr1d = np.array([1, 2, 3])
    arr2d = np.array([[1, 2], [3, 4], [5, 6]])

    print("")
    print([-1,3,-2])
    print(from_numpy_array([-1,3,-2]))  # Exemplo com array 1D

    print("")
    print(arr1d)
    print(from_numpy_array(arr1d))  # Exemplo com array 1D
    
    print("")
    print(arr2d)
    print(from_numpy_array(arr2d))  # Exemplo com array 2D

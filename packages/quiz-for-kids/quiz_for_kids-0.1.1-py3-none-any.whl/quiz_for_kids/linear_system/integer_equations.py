#!/usr/bin/python

import random
import numpy as np

def integer_equations(input_data, var_min=1,var_max=5, coef_min=-2,coef_max=2, in_extensive=False):
    """
    Generate a system of integer equations based on provided variables or a dictionary of variable values.

    Parameters:
    - input_data (list or dict): 
        - If a list, it should contain variable names as strings.
        - If a dictionary, keys should be strings representing variable names, and values should be numeric (int or float).
    - var_min (int, optional): Minimum value for randomly generated integer variables (default is 1).
    - var_max (int, optional): Maximum value for randomly generated integer variables (default is 5).
    - coef_min (int, optional): Minimum value for randomly generated coefficients (default is -2).
    - coef_max (int, optional): Maximum value for randomly generated coefficients (default is 2).
    - in_extensive (bool, optional): If True, generates equations in an extensive form, allowing multiple occurrences of variables (default is False).

    Returns:
    - tuple: A tuple containing:
        - A list of strings representing the generated equations.
        - A dictionary with the following keys:
            - "values": A dictionary mapping each variable to its integer value.
            - "variables": A list of variable names.
            - "coefficients": A numpy array representing the coefficients of the equations.
            - "unknowns": A numpy array representing the values of the variables.
            - "constants": A numpy array representing the results of the equations (the right-hand side).

    Example:
    >>> equations, data = integer_equations(["x", "y", "z"], in_extensive=True)
    >>> print(equations)
    ['x+y=5', '2x-y=1', ...]
    
    >>> equations, data = integer_equations({'x': 1, 'y': 2, 'z': 3})
    >>> print(data['values'])
    {'x': 1, 'y': 2, 'z': 3}

    Notes:
    - The function generates a maximum of 100 trials to ensure that the determinant of the coefficients matrix is not zero, which would indicate that the equations do not have a unique solution.
    - If no valid equations can be generated after 100 trials, the function will return empty results.
    """
    variables=[];
    values={};
    
    # Verifica se é uma lista de strings
    if isinstance(input_data, list):
        if all(isinstance(item, str) for item in input_data):
            variables = input_data.copy();
            # Gera valores inteiros aleatórios para cada variável
            values = {var: random.randint(var_min, var_max) for var in variables}
        else:
            return [],{}
    
    # Verifica se é um dicionário com chaves de string e valores numéricos
    elif isinstance(input_data, dict):
        if all(isinstance(key, str) and isinstance(value, (int, float)) for key, value in input_data.items()):
            values=dict(input_data)
            variables=list(input_data)
        else:
            return [],{}
     
    # Caso não seja nem uma lista nem um dicionário, retorna False
    else:
        return [],{}
    


    num_equations = len(variables)

    coef=np.zeros((num_equations,num_equations))
    x=np.array([values[x] for x in variables])

    trials=100;
    for _ in range(trials):

        equations = []
        
        # Gera um número aleatório de equações
        for l in range(num_equations):
            # Seleciona aleatoriamente variáveis e coeficientes
            terms = []
            total_sum = 0
            first_coef = True
            for n,var in enumerate(variables):
                coefficient = random.randint(coef_min,coef_max)  # Gera coeficientes aleatórios entre -3 e 3
                coef[l,n]=coefficient;
                
                if coefficient != 0:
                    if in_extensive:
                        if first_coef == True:
                            if coefficient>0:
                                terms.append(f"{var}")
                                if coefficient>1:
                                    for _ in range(coefficient-1):
                                        terms.append(f"+{var}")
                            else:
                                for _ in range(abs(coefficient)):
                                    terms.append(f"-{var}")
                            first_coef = False;
                        else:
                            if coefficient>0:
                                for _ in range(coefficient):
                                    terms.append(f"+{var}")
                            else:
                                for _ in range(abs(coefficient)):
                                    terms.append(f"-{var}")
                    else:
                        if first_coef == True:
                            if   coefficient==1:
                                terms.append(f"{var}")
                            elif coefficient==-1:
                                terms.append(f"-{var}")
                            else:
                                terms.append(f"{coefficient}{var}")
                            first_coef = False
                        else:
                            if   coefficient==1:
                                terms.append(f"+{var}")
                            elif coefficient==-1:
                                terms.append(f"-{var}")
                            else:
                                terms.append(f"{coefficient:+d}{var}")
                    total_sum += coefficient * values[var]
            
            # Cria a equação
            equation = ''.join(terms) + f"={total_sum}"
            equations.append(equation)
            
        if np.linalg.det(coef)!=0:
            break
    
    if np.linalg.det(coef)==0:
        return [],{}
    
    # Retorna o sistema de equações e os valores das variáveis
    return equations, {"values":values,"variables":variables,"coefficients":coef,"unknowns":x,"constants":coef@x}

if __name__ == "__main__":
    # Exemplo de uso
    variables = ["x", "y", "z"]
    equations, data = integer_equations(variables, in_extensive=True)

    print("Sistema de equações:")
    for equation in equations:
        print(equation)
     
    print("\nData:")
    print(data)


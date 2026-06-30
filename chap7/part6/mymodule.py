def taxcalculator(salary, percentage):
    """Parameters salary (int) and percentage (0-100)
    returns final salary after taxes"""
    final = (salary * ((100 - percentage) / 100))
    return final
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Multiply by 2
    employees['salary'] = employees['salary']*2
    return employees
    
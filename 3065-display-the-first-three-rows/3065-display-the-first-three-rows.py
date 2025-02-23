import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Use of Head() buit-in function to display the three rows 
    return employees.head(3) # Slicing: employees[:3] would works too
    
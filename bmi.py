import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df_male = pd.read_csv('BMI-chart-male.csv')
df_female = pd.read_csv('BMI-chart-female.csv')

@app.get('/percentile')
async def get_percentile(gender: str, age: float, bmi: float):
    ''' 
    API endpoint for finding BMI percentile based on BMI charts from the CDC.

    Parameters
    ----------
    gender : str
        Specify ['male','Male','M','m'] or ['female','Female','F','f']
    age : int
        Specify age in months (24months-240months)
    bmi : float
        Specify BMI number (5 decimal places)
    
    '''
    try:
        if gender in ['male','Male','M','m']:
            closest_age_percentiles = df_male.loc[(df_male['Age (in months)']-age).abs().idxmin()]
            diffs = abs(closest_age_percentiles- bmi)
            closest_col = diffs.idxmin()
            percentile = closest_col.split()[0]
            return {'percentile': f'{percentile} percentile' }
        if gender in ['female','Female','F','f']:
            closest_age_percentiles = df_female.loc[(df_female['Age (in months)']-age).abs().idxmin()]
            diffs = abs(closest_age_percentiles- bmi)
            closest_col = diffs.idxmin()
            percentile = closest_col.split()[0]
            return {'percentile': f'{percentile} percentile' }
    except Exception as e:
        pass
    
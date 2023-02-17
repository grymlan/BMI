import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df_male = pd.read_csv('BMI-chart-male.csv')
df_female = pd.read_csv('BMI-chart-female.csv')

@app.get('/percentile')
async def get_percentile(gender: str, age: float, bmi: float):
    ''' 
    api endpoint for finding BMI percentile

    Parameters
    ----------
    gender : str
        Specify 'male' or 'female'
    
    '''
    if gender == 'male':
        closest_age_percentiles = df_male.loc[(df_male['Age (in months)']-age).abs().idxmin()]
        diffs = abs(closest_age_percentiles- bmi)
        closest_col = diffs.idxmin()
        percentile = closest_col.split()[0]
        return {'percentile': f'{percentile} percentile' }
    if gender == 'female':
        closest_age_percentiles = df_female.loc[(df_female['Age (in months)']-age).abs().idxmin()]
        diffs = abs(closest_age_percentiles- bmi)
        closest_col = diffs.idxmin()
        percentile = closest_col.split()[0]
        return {'percentile': f'{percentile} percentile' }
    
import json
import pandas as pd

patient_table = 'PATIENTS'

table_names = ['ADMISSIONS', 'CALLOUT', 'CHARTEVENTS', 'CPTEVENTS', 'DATETIMEEVENTS', 'DIAGNOSES_ICD', 'DRGCODES', 'ICUSTAYS', 'INPUTEVENTS_CV', 'INPUTEVENTS_MV',
               'LABEVENTS', 'MICROBIOLOGYEVENTS', 'NOTEEVENTS', 'OUTPUTEVENTS', 'PRESCRIPTIONS', 'PROCEDUREEVENTS_MV', 'PROCEDURES_ICD', 'SERVICES', 'TRANSFERS']

patients = pd.read_csv(
    f'./data/{patient_table}.csv', dtype='object').fillna('NA')

tables = dict()

for table in table_names:
    tables[table] = pd.read_csv(
        f'./data/{table}.csv', dtype='object').fillna('NA')


patient_list = []

for index, row in patients.iterrows():
    # fetch patient ID
    patient_ID = row['subject_id']

    # fetch patient object
    patient = row.to_dict()

    # print(patient)

    for table_name in tables.keys():
        table = tables[table_name]
        patient[table_name] = table[table['subject_id']
                                    == patient_ID].to_dict(orient='records')

    # print(patient)
    patient_list.append(patient)

    break

with open('./patients.json', 'w') as f:
    json.dump(patient_list, f, indent=4)

print('done')

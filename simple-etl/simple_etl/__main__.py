import os
import pandas
import pandera
import json
from datetime import datetime
from loguru import logger

CHECK_IDX = 2
INDEX_IDX = 5
EXCEL_STARTING_INDEX = 2

schema = pandera.DataFrameSchema(
    columns={
        'description': pandera.Column(str, [
            pandera.Check(lambda x: x.isascii(), element_wise=True, error='description: Has found non-ascii characters'),
            pandera.Check(lambda x: "war" not in x, element_wise=True, error="description: Has a word 'war'"),
        ]),
        'is_ancient': pandera.Column(int),
        'decades_old': pandera.Column(int),
    },
    checks=[
        pandera.Check(
            lambda row: row.is_ancient == 1 and row.decades_old > 0,
            element_wise=True,
            error='decades_old: Has no decades old',
        ),
    ],
)


def handle_schema_errors(errors: pandera.errors.SchemaErrors):
    indexed_failure_cases = {}
    for case in errors.failure_cases.sort_values('index').values:
        index = case[INDEX_IDX]
        if index not in indexed_failure_cases:
            indexed_failure_cases[index] = set()
        indexed_failure_cases[index].add(case[CHECK_IDX])
    errors_data = [{'row': idx + EXCEL_STARTING_INDEX, 'errors': list(indexed_failure_cases[idx])} for idx in indexed_failure_cases]

    folder = './output'
    os.makedirs(folder, exist_ok=True)

    file_path = folder + f'/{datetime.now()}.json'
    open(file_path, 'w').write(json.dumps(errors_data, indent=4))

    logger.error(f'Found errors in the data. Check errors at {file_path}')


def main():
    logger.add('./logs/{time}.log')

    # Prompt
    logger.info('Running an ETL pipeline')

    # Read the data
    data = pandas.read_excel('./res/data.xlsx')

    try:
        schema.validate(data, lazy=True)
    except pandera.errors.SchemaErrors as errors:
        handle_schema_errors(errors)

    # read the data
    # transform the data
    # write the data to a csv file
    logger.success('Successfully completed an ETL pipeline')


if __name__ == '__main__':
    main()
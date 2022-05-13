# Experiments in Dataprep

Attempts at optimizing data access for analytics projects.

Goals:
1. Push customization of imports out to the import itself.
2. Remove dangling strings and 'dataset descriptors as variables in code' (variables representing column names for general use) wherever possible
   1. We're looking for cleaner definitions for when using string_variable, string or object notation when slicing dataframes is most appropriate. (`df[PATIENT_ID]`, `df['patient_id']`, or `df.patient_id`)
3. Enable custom 'validation' of the dataset
4. Enable custom 'describe' and 'sample' type operations per dataset
5. Work well/seamlessly with pandas

## Notes

Directory structure is intentional.  If anything is prescriptive, it's directory structure.  All modules / packages should be importable using absolute module pathing.

`from model.data.lib.iris import dataset`

## Requirements

[poetry](https://python-poetry.org/)

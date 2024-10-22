# MRT MODULE
MRT_COLUMNS = ['reason_to_end_the_behavioral_task_code', #'participant_quality', 
           'participant_id', 'group_id', 'provider_id', 'module_name',
           'project_identifier', 'reaction_time', 'task_name', 'trial_name','given_response_label_presented', 'procedure_name',
           'trial_stimulus_category','expected_response', 'given_response_accuracy', 'given_response_label_english', 'Gender', 'Age'
          ]
PROJECT = 'neurons-ml'
LOCATION = 'us-central1'

MODEL_TYPE = 'text-unicorn'
PARAMETERS = {
    "candidate_count": 1,
    "max_output_tokens": 32,
    "temperature": 0.1,
    "top_p": 0.4,
    "top_k": 10
}

# FRT MODULE

FRT_COLUMNS_RENAME = {
    'procedure_stimulus' : 'frt_stimulus',
    'trial_association_english' : 'frt_association',
    'given_response_label_english': 'frt_response'
}
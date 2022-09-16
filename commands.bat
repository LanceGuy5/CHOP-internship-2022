
rem creates a new model based on the training data below with the davinci base model named "eng_2_cyph_proto1"
openai api fine_tunes.create -t C:\Users\zlhartma\PycharmProjects\eng2cyphCFDIKG\training_data.jsonl -m davinci --suffix "eng_2_cyph_proto1"

rem OUTLINE FOR TRAINING DATA: {"prompt":  "", "completion":  " _______###"}

rem For multiclass classification
openai api fine_tunes.create \
  -t <TRAIN_FILE_ID_OR_PATH> \
  -v <VALIDATION_FILE_OR_PATH> \
  -m <MODEL> \
  --compute_classification_metrics \
  --classification_n_classes <N_CLASSES>

rem For binary classification
openai api fine_tunes.create \
  -t <TRAIN_FILE_ID_OR_PATH> \
  -v <VALIDATION_FILE_OR_PATH> \
  -m <MODEL> \
  --compute_classification_metrics \
  --classification_n_classes 2 \
  --classification_positive_class <POSITIVE_CLASS_FROM_DATASET>

rem Resuming if interrupted
openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>

Rem List all created fine-tunes
openai api fine_tunes.list

rem Retrieve the state of a fine-tune. The resulting object includes
rem job status (which can be one of pending, running, succeeded, or failed)
rem and other information
openai api fine_tunes.get -i <YOUR_FINE_TUNE_JOB_ID>

rem Cancel a job
openai api fine_tunes.cancel -i <YOUR_FINE_TUNE_JOB_ID>

rem Running from command line
openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>

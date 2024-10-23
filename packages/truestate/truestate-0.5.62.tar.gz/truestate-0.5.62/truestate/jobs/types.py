from enum import Enum


class JobType(str, Enum):
    DataTransform = "data-transform"
    ZeroShot = "zero-shot"
    ClassificationTraining = "classification-training"
    ClassificationInference = "classification-inference"
    PreferenceTraining = "preference-training"
    PreferenceInference = "preference-inference"
    ApplyEmbeddings = "apply-embeddings"
    BulkPrompt = "bulk-prompt"
    # XGBoostTraining = "xgboost-training"
    # XGBoostInference = "xgboost-inference"
    TabularRegressorTraining = "tabular-regressor-training"
    TabularRegressorInference = "tabular-regressor-inference"
    TabularClassifierTraining = "tabular-classifier-training"
    TabularClassifierInference = "tabular-classifier-inference"
    Integration = "integration"
    EntityMatch = "entity-match"
    SFTTraining = "supervised-fine-tuning"

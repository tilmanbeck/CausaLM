from os import path
from utils import count_num_cpu_gpu

CAUSALM_DIR = path.dirname(path.realpath(__file__)) # This must be set to the path which specifies where the CausaLM project resides

NUM_CPU = count_num_cpu_gpu()[0]
NUM_GPU = 1

RANDOM_SEED = 212

BERT_PRETRAINED_MODEL = 'bert-base-uncased'
MAX_POMS_SEQ_LENGTH = 32
MAX_SENTIMENT_SEQ_LENGTH = 384
MAX_ARGUMENT_SEQ_LENGTH = 300

MODELS_DIR = f"{CAUSALM_DIR}/Models"
EXPERIMENTS_DIR = f"{CAUSALM_DIR}/Experiments"

SENTIMENT_MODELS_DIR = f"{MODELS_DIR}/Sentiment"
SENTIMENT_EXPERIMENTS_DIR = f"{EXPERIMENTS_DIR}/Sentiment"

SENTIMENT_ADJECTIVES_DATASETS_DIR = f"{CAUSALM_DIR}/Sentiment_Adjectives/datasets"
SENTIMENT_ADJECTIVES_MODELS_DIR = f"{SENTIMENT_MODELS_DIR}/Adjectives"
SENTIMENT_ADJECTIVES_PRETRAIN_DIR = f"{SENTIMENT_ADJECTIVES_MODELS_DIR}/Pretrain"
SENTIMENT_ADJECTIVES_PRETRAIN_DATA_DIR = f"{SENTIMENT_ADJECTIVES_PRETRAIN_DIR}/data"
SENTIMENT_ADJECTIVES_PRETRAIN_MLM_DIR = f"{SENTIMENT_ADJECTIVES_PRETRAIN_DIR}/MLM"
SENTIMENT_ADJECTIVES_PRETRAIN_IMA_DIR = f"{SENTIMENT_ADJECTIVES_PRETRAIN_DIR}/IMA"

SENTIMENT_TOPICS_DATASETS_DIR = f"{CAUSALM_DIR}/Sentiment_Topics/datasets"
SENTIMENT_TOPICS_MODELS_DIR = f"{SENTIMENT_MODELS_DIR}/Topics"
SENTIMENT_TOPICS_PRETRAIN_DIR = f"{SENTIMENT_TOPICS_MODELS_DIR}/Pretrain"
SENTIMENT_TOPICS_PRETRAIN_DATA_DIR = f"{SENTIMENT_TOPICS_PRETRAIN_DIR}/data"
SENTIMENT_TOPICS_PRETRAIN_MLM_DIR = f"{SENTIMENT_TOPICS_PRETRAIN_DIR}/MLM"
SENTIMENT_TOPICS_PRETRAIN_IXT_DIR = f"{SENTIMENT_TOPICS_PRETRAIN_DIR}/IXT"

SENTIMENT_DOMAINS = ("movies", "books", "electronics", "kitchen", "dvd")
SENTIMENT_TOPICS_DOMAIN_TREAT_CONTROL_MAP_FILE = f"{SENTIMENT_TOPICS_DATASETS_DIR}/domain_treat_control_topics.json"

ARGUMENT_MODELS_DIR = f"{MODELS_DIR}/Argument"
ARGUMENT_EXPERIMENTS_DIR = f"{EXPERIMENTS_DIR}/Argument"

ARGUMENT_TOPICS_DATASETS_DIR = f"{CAUSALM_DIR}/Argument_Topics/datasets"
ARGUMENT_TOPICS_MODELS_DIR = f"{ARGUMENT_MODELS_DIR}/Topics"
ARGUMENT_TOPICS_PRETRAIN_DIR = f"{ARGUMENT_TOPICS_MODELS_DIR}/Pretrain"
ARGUMENT_TOPICS_PRETRAIN_DATA_DIR = f"{ARGUMENT_TOPICS_PRETRAIN_DIR}/data"
ARGUMENT_TOPICS_PRETRAIN_MLM_DIR = f"{ARGUMENT_TOPICS_PRETRAIN_DIR}/MLM"
ARGUMENT_TOPICS_PRETRAIN_IXT_DIR = f"{ARGUMENT_TOPICS_PRETRAIN_DIR}/IXT"

ARGUMENT_ID2INT = f"{ARGUMENT_TOPICS_DATASETS_DIR}/id2int.json"
ARGUMENT_INT2ID = f"{ARGUMENT_TOPICS_DATASETS_DIR}/int2id.json"

ARGUMENT_DOMAINS = ("abortion", "cloning", "gun control", "school uniforms", "minimum wage", "nuclear energy", "death penalty", "marijuana legalization")
ARGUMENT_TOPICS_DOMAIN_TREAT_CONTROL_MAP_FILE = f"{ARGUMENT_TOPICS_DATASETS_DIR}/domain_treat_control_topics.json"


POMS_EXPERIMENTS_DIR = f"{EXPERIMENTS_DIR}/POMS"
POMS_MODELS_DIR = f"{MODELS_DIR}/POMS"
POMS_MLM_DIR = f"{POMS_MODELS_DIR}/MLM"
POMS_GENDERACE_DATASETS_DIR = f"{CAUSALM_DIR}/POMS_GendeRace/datasets"

POMS_GENDER_MODEL_DIR = f"{POMS_MODELS_DIR}/Gender"
POMS_GENDER_PRETRAIN_DATA_DIR = f"{POMS_GENDER_MODEL_DIR}/Pretrain"

POMS_RACE_MODEL_DIR = f"{POMS_MODELS_DIR}/Race"
POMS_RACE_PRETRAIN_DATA_DIR = f"{POMS_RACE_MODEL_DIR}/Pretrain"
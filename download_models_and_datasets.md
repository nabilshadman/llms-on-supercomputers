Download the models and datasets to a local folder using the following commands:

```
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/microsoft--phi-3.5-mini-instruct "microsoft/Phi-3.5-mini-instruct"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/unsloth--Phi-3.5-mini-instruct-bnb-4bit "unsloth/Phi-3.5-mini-instruct-bnb-4bit"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/distilbert--distilbert-base-uncased "distilbert/distilbert-base-uncased"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/mistralai--Mistral-7B-Instruct-v0.3 "mistralai/Mistral-7B-Instruct-v0.3"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/mistralai--Mistral-7B-v0.3 "mistralai/Mistral-7B-v0.3"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/google--bert-base-uncased "google-bert/bert-base-uncased"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/facebookai--xlm-roberta-base "FacebookAI/xlm-roberta-base"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/openai-community--gpt2 "openai-community/gpt2"
huggingface-cli download --repo-type model --local-dir /gpfs/data/fs70824/LLMs_models_datasets/models/distilbert--distilbert-base-uncased-finetuned-sst-2-english "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

huggingface-cli download --repo-type dataset --local-dir /gpfs/data/fs70824/LLMs_models_datasets/datasets/stanfordnlp--imdb "stanfordnlp/imdb"
huggingface-cli download --repo-type dataset --local-dir /gpfs/data/fs70824/LLMs_models_datasets/datasets/openlifescienceai--medmcqa "openlifescienceai/medmcqa"
huggingface-cli download --repo-type dataset --local-dir /gpfs/data/fs70824/LLMs_models_datasets/datasets/timdettmers--openassistant-guanaco "timdettmers/openassistant-guanaco"
huggingface-cli download --repo-type dataset --local-dir /gpfs/data/fs70824/LLMs_models_datasets/datasets/dair-ai--emotion "dair-ai/emotion"
huggingface-cli download --repo-type dataset --local-dir /gpfs/data/fs70824/LLMs_models_datasets/datasets/fancyzhx--ag_news "fancyzhx/ag_news"
huggingface-cli download --repo-type dataset --local-dir /gpfs/data/fs70824/LLMs_models_datasets/datasets/abisee--cnn_dailymail "abisee/cnn_dailymail"
```
# NLP project
This is an attempt to build a language model for generating trading signals. It uses a limited vocabulary such as 'go-long', 'go-short' and 'do-nothing'. 
It uses the language model combined with an expert trader data also referred to as imitation learning. The assumption here is that you have data of an expert trader with at least 5 trades e.g. labeled ['go-long', 'go-short', 'do-nothing', 'go-short', 'go-long'] the model returns one of these inputs as the signal.
## Usage
Install the project with:
```
pip install nlp-project
```
Then:
```
from nlp.imit_main import imit_signal as imit
from nlp.nlp_main import nlp_signal as nlp
```
The training (expert) data were simulated with imit_signal and the language model was build with a series of these inputs.

# Warning
This is not financial advise. NLP project is entirely on its preliminary stages. Use it at your own risk.

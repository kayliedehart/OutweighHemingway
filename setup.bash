pip install spacy
python -m spacy.en.download
mkdir lib/
cd lib/
git clone https://github.com/honnibal/spaCy.git
cd spaCy
export PYTHONPATH=`pwd`
pip install -r requirements.txt
python setup.py build_ext --inplace
python -m spacy.en.download
pip install pytest
py.test tests/
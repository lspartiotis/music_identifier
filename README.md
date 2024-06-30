# music_identifier
This project uses audfprint to extract fingerprintd from .mp3 files and add them to a hash table. Then we can check if any of the songs in the database are contained in the input that can be either a youtube link or a recording.


Authors\
Leandros Atherinis-Spartiotis\
Orestis Vaggelis





to setup:

git clone https://github.com/dpwe/audfprint.git

pip install -r requirements.txt

Relative pathing is universal if all are in the same directory, run notebook as it is


Check notebook.ipynb to test code with ease, as long as fingerprints.pklz exists and you have cloned audfprint into the main directory each cell can run on its own.
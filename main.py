from nudenet import NudeClassifier
import os
files = os.listdir('Valid')
files.remove('get_skin.py')
files.remove('Valid')
files.remove('main.py')
files.remove('sort.py')
classifier = NudeClassifier()
for i in files:
    try:
        data = classifier.classify(i)[i]['unsafe']
        if data > 0.7:
            print(i + ' is OK')
            os.rename('Valid/'+ i, 'Valid/Pron/' + i)
        else:
            os.rename('Valid/' + i, 'Valid/Error/' + i)
    except:
        continue
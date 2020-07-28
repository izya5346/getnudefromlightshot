from nudenet import NudeClassifier
import os
files = os.listdir('Valid')    
if not os.path.exists('Valid/Pron'):
    os.makedirs('Valid/Pron')
if not os.path.exists('Valid/Error'):
    os.makedirs('Valid/Error')
files.remove('Pron')
files.remove('Error')
classifier = NudeClassifier()
for i in files:
    try:
        data = classifier.classify('Valid/' + i)[i]['unsafe']
        if data > 0.7:
            print(i + ' is OK')
            os.rename('Valid/'+ i, 'Valid/Pron/' + i)
        else:
            os.rename('Valid/' + i, 'Valid/Error/' + i)
    except:
        continue
# Install the firebase-admin package before running this script:
#    pip3 install firebase-admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


if __name__ == '__main__':
    # fetch data from firebase
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    subjects = db.collection('2025prod_data').stream()

    # iterate over all subjects
    for subj in subjects:
        data = subj.to_dict()
        times = [k for k in data.keys() if k.startswith('1')]
        print('Subject ID:', subj.id)
        print('Survey start times:', times)

        # now you can explore the subject's data and do whatever you want with it
        for t in times:
            for i in range(5):
                print(data[t][f'1.{i}'])

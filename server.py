from flask import Flask
from flask import jsonify
from os import listdir
import h5lib
import h5py


app = Flask(__name__)


@app.route('/h5files')
def h5files():
    files = listdir('./data')

    if files:
        success = {
            'status': 'success',
            'fileList': files
        }, 200
        return success
    else:
        failure = {
            'status': 'failure',
            'fileList': None
        }, 400
        return failure
    """
    This function returns a list of h5 files under './data'.

    Returns: possible values:
        {
            'status': 'success',
            'fileList': [
                'fileOne.h5',
                'fileTwo.h5'
            ]
        }, 200

        {
            'status': 'failure',
            'fileList': None
        }, 400
    """



@app.route('/ion_mode/<filename>')
def ion_mode(filename: str):
    h5 = h5py.File(f"./data/{filename}.h5",'r')
    ion_mode = h5.attrs['IonMode']

    if ion_mode.decode() == 'positive':
        success = {
            'status': 'success',
            'ionMode': 'positive'
        }, 200
        return success
    else:
        failure = {
            'status': 'failure',
            'ionMode': None
        }, 400
        return failure
    """
    This function returns ion mode attribute in h5 file:
        attribute location: '/'
        attribute name: 'IonMode'

    Args:
        filename: h5 file name.

    Returns: possible values:
        {
            'status': 'success',
            'ionMode': 'positive'
        }, 200

        {
            'status': 'failure',
            'ionMode': None
        }, 400
    """
    pass


@app.route('/nbr_samples/<filename>')
def nbr_samples(filename: str):
    h5 = h5py.File(f"./data/{filename}.h5",'r')
    samples = h5.attrs['NbrSamples']

    if samples != 0:
        success = {
            'status': 'success',
            'nbrSamples': int(samples)
        }, 200
        return success
    else:
        failure = {
            'status': 'failure',
            'nbrSamples': None
        }, 400
        return failure
    """
    This function returns NbrSamples attribute in h5 file:
        attribute location: '/'
        attribute name: 'NbrSamples'

    Args:
        filename: h5 file name.

    Returns: possible values:
        {
            'status': 'success',
            'nbrSamples': 100
        }, 200

        {
            'status': 'failure',
            'nbrSamples': None
        }, 400
    """
    pass


@app.route('/sample_interval/<filename>')
def sample_interval(filename: str):
    # should sample interval be equal to 0.5 or just a number?
    h5 = h5py.File(f"./data/{filename}.h5",'r')
    full_spec = h5['FullSpectra']
    interval = full_spec.attrs['SampleInterval']

    if interval:
        success = {
            'status': 'success',
            'sampleInterval': float(interval)
        }, 200
        return success
    else:
        failure = {
            'status': 'failure',
            'sampleInterval': None
        }, 400
        return failure
    """
    This function returns sample interval attribute in h5 file:
        attribute location: '/FullSpectra'
        attribute name: 'SampleInterval'

    Args:
        filename: h5 file name.

    Returns: possible values:
        {
            'status': 'success',
            'sampleInterval': 0.5
        }, 200

        {
            'status': 'failure',
            'sampleInterval': None
        }, 400
    """
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

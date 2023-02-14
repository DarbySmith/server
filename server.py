from flask import Flask
from os import listdir
import h5lib


app = Flask(__name__)


@app.route('/h5files')
def h5files():
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


@app.route('/ion_mode/<path:filename>')
def ion_mode(filename: str):
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
    try:
        ion_mode = h5lib.get_str_attribute(filename, '/', 'IonMode')

        if ion_mode[1].decode() == 'positive':
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
    except FileNotFoundError:
        file_not_found = {
            'status': 'file not found',
            'ionMode': None
        }, 404
        return file_not_found 


@app.route('/nbr_samples/<path:filename>')
def nbr_samples(filename: str):
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
    try:
        samples = h5lib.get_int_attribute(filename, '/', 'NbrSamples')
    
        if samples != 0:
            success = {
                'status': 'success',
                'nbrSamples': int(samples[1])
            }, 200
            return success
        else:
            failure = {
                'status': 'failure',
                'nbrSamples': None
            }, 400
            return failure
    except FileNotFoundError:
        file_not_found = {
            'status': 'file not found',
            'nbrSamples': None
        }, 404
        return file_not_found


@app.route('/sample_interval/<path:filename>')
def sample_interval(filename: str):
    # should sample interval be equal to 0.5 or just a number?
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
    try:
        interval = h5lib.get_float_attribute(filename, '/FullSpectra', 'SampleInterval')

        if interval:
            success = {
                'status': 'success',
                'sampleInterval': float(interval[1])
            }, 200
            return success
        else:
            failure = {
                'status': 'failure',
                'sampleInterval': None
            }, 400
            return failure
    except FileNotFoundError:
        file_not_found = {
            'status': 'file not found',
            'sampleInterval': None
        }, 404
        return file_not_found


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

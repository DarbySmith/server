from flask import Flask


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
    pass


@app.route('/ion_mode/<filename>')
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
    pass


@app.route('/nbr_samples/<filename>')
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
    pass


@app.route('/sample_interval/<filename>')
def sample_interval(filename: str):
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

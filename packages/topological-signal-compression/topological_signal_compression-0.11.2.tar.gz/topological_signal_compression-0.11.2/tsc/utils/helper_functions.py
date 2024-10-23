"""
Helper utility functions for various compression and reconstruction capabilities.
"""

import numpy as np

try:
    from pydub import AudioSegment
except ImportError as ie:  # pragma: no cover
    raise ImportError(
        "pydub not installed, but can be installed by running "
        "`pip install topological-signal-compression[extras]`"
    ) from ie


def min_max_normalize(arr: np.ndarray) -> np.ndarray:
    """
    Convert ``numpy`` array ``arr`` to a form suitable for encoding as ``wav`` file.

    Then min-max normalize the array (e.g. make signal values span [0, 1]) and change ``dtype`` to 32-bit floating
    point.

    :param arr: 1D ``numpy`` array.
    :return: 1D array.
    """
    res = (arr - arr.min()) / (arr.max() - arr.min())
    return res.astype(np.float32)


def pydub_to_numpy(audiosegment: AudioSegment) -> np.ndarray:
    """
    Turn a multichannel ``pydub.AudioSegment`` instance to a ``numpy.ndarray`` with only a single channel of sound.

    :param audiosegment: ``pydub.AudioSegment`` instance to convert.
    :return: 1d array of signal with type ``float32`` for consistency with other compression schemes.
    """
    # get numpy array of sound
    samples = np.array(audiosegment.get_array_of_samples()).reshape(
        audiosegment.channels, -1, order="F"
    )
    # convert to single channel audio array
    samples = samples.sum(axis=0) / audiosegment.channels
    return samples.astype(np.float32)

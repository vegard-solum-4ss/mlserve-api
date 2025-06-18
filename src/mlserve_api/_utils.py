import waveresponse as wr


def wave_from_dict(wave_dict):
    """
    Construct a wave spectrum object from a dictionary representation.
    """

    TYPE_MAP = {
        "WaveSpectrum": wr.WaveSpectrum,
        "WaveBinSpectrum": wr.WaveBinSpectrum,
    }

    wave = TYPE_MAP[wave_dict["type"]](**wave_dict["params"])

    return wave


"""Note module."""

from ._require import require

Scale = require('Scale').Scale

_scales = {
    'major': [
        0,  # C¹
        0.5,  # C#¹ | Db¹
        1,  # D¹
        1.5,  # D#¹ | Eb¹
        2,  # E¹ | Fb¹
        2,  # E#¹ | F¹
        2.5,  # F#¹ | Gb¹
        3,  # G¹
        3.5,  # G#¹ | Ab¹
        4,  # A¹
        4.5,  # A#¹ | Bb¹
        5,  # B¹ | Cb²
        5,  # B#¹ | C²
        5.5,  # C#² | Db²
        6,  # D²
        6.5,  # D#² | Eb²
        7,  # E² | Fb²
        7,  # E#² | F²
        7.5,  # F#² | Gb²
        8,  # G²
        8.5,  # G#² | Ab²
        9,  # A²
        9.5,  # A#² | Bb²
        10,  # B² | Cb³
        10,  # B#³ | C³
        10.5,  # C#³ | Db³
        11,  # D³
        11.5,  # D#³ | Eb³
        12,  # E³ | Fb³
        12,  # E#³ | F³
        12.5,  # F#³ | Gb³
        13,  # G³
        13.5,  # G#³ | Ab³
        14,  # A³
        14.5,  # A#³ | Bb³
        15,  # B³ | Cb⁴
    ],
    # 'majorPentatonic': [0, 2, 4, 7, 9],
    # 'minor': [0 for _ in range(36)],
    # 'aeolian': [0, 2, 3, 5, 7, 8, 10],
    # 'minorPentatonic': [0, 3, 5, 7, 10],
    # 'mixolydian': [0, 2, 4, 5, 7, 9, 10],
    # 'melodicMinor': [0, 2, 3, 5, 7, 9, 11],
    # 'melodicMajor': [0, 2, 4, 5, 7, 8, 11],
    # 'harmonicMinor': [0, 2, 3, 5, 7, 8, 11],
    # 'harmonicMajor': [0, 2, 4, 5, 7, 8, 11],
    # 'justMajor': [0, 2, 4, 5, 7, 9, 11],  # tuning=Tuning.just
    # 'justMinor': [0, 2, 3, 5, 7, 8, 10],  # tuning=Tuning.just
    # 'dorian': [0, 2, 3, 5, 7, 9, 10],
    # 'dorian2': [0, 1, 3, 5, 6, 8, 9, 11],
    # 'diminished': [0, 1, 3, 4, 6, 7, 9, 10],
    # 'egyptian': [0, 2, 5, 7, 10],
    # 'yu': [0, 3, 5, 7, 10],
    # 'zhi': [0, 2, 5, 7, 9],
    # 'phrygian': [0, 1, 3, 5, 7, 8, 10],
    # 'prometheus': [0, 2, 4, 6, 11],
    # 'indian': [0, 4, 5, 7, 10],
    # 'locrian': [0, 1, 3, 5, 6, 8, 10],
    # 'locrianMajor': [0, 2, 4, 5, 6, 8, 10],
    # 'lydian': [0, 2, 4, 6, 7, 9, 11],
    # 'lydianMinor': [0, 2, 4, 6, 7, 8, 10],
    # 'custom': [0, 2, 3, 5, 6, 9, 10],
    # 'hungarianMinor': [0, 2, 3, 6, 7, 8, 11],
    # 'romanianMinor': [0, 2, 3, 6, 7, 9, 10],
    # 'chinese': [0, 4, 6, 7, 11],
    # 'wholeTone': [0, 2, 4, 6, 8, 10],
    # 'halfWhole': [0, 1, 3, 4, 6, 7, 9, 10],
    # 'wholeHalf': [0, 2, 3, 5, 6, 8, 9, 11],
    # 'bebopMaj': [0, 2, 4, 5, 7, 8, 9, 11],
    # 'bebopDorian': [0, 2, 3, 4, 5, 9, 10],  # aka Bebop Minor
    # 'bebopDom': [0, 2, 4, 5, 7, 9, 10, 11],  # Bebop Dominant/Mixolydian
    # 'bebopMelMin': [0, 2, 3, 5, 7, 8, 9, 11],  # Bebop Melodic Minor
    # 'blues': [0, 3, 5, 6, 7, 10],
    # 'minMaj': [0, 2, 3, 5, 7, 9, 11],
    # 'susb9': [0, 1, 3, 5, 7, 9, 10],
    # 'lydianAug': [0, 2, 4, 6, 8, 9, 11],
    # 'lydianDom': [0, 2, 4, 6, 7, 9, 10],
    # 'melMin5th': [0, 2, 4, 5, 7, 8, 10],
    # 'halfDim': [0, 2, 3, 5, 6, 8, 10],
    # 'altered': [0, 1, 3, 4, 6, 8, 10],
}


def from_chromatic(note: int) -> int:
    """Get note from chromatic.

    Parameters
    ----------
    note : int
        Note on the chromatic scale.

    Returns
    -------
    int
        Chromatic scale note converted to current scale.

    Raises
    ------
    ValueError
        Scale not supported.
    """
    scale = Scale.default.name

    if scale == 'chromatic':
        return note
    if scale not in _scales:
        raise ValueError(
            f'Scale {scale} does not support, '
            f'the supported scales are: chromatic, {", ".join(_scales.keys())}'
        )
    return note - _scales[Scale.default.name][note]

import pandas
from packaging.version import Version

if Version(pandas.__version__) < Version("1.2"):
    from pandas.io.common import get_filepath_or_buffer as _get_filepath_or_buffer
    def get_filepath_or_buffer(*args, **kwargs):
        fpb, encoding, compression, _ = _get_filepath_or_buffer(*args, **kwargs)
        return fpb, encoding, compression
else:
    from pandas.io.common import _get_filepath_or_buffer
    def get_filepath_or_buffer(*args, **kwargs):
        io_args = _get_filepath_or_buffer(*args, **kwargs)
        fpb, encoding, compression = io_args.filepath_or_buffer, io_args.encoding, io_args.compression
        return fpb, encoding, compression

        
if Version(pandas.__version__) < Version("1.2"):
    from pandas.core.internals import _safe_reshape
else:
    def _safe_reshape(arr, new_shape):
        """
        If possible, reshape `arr` to have shape `new_shape`,
        with a couple of exceptions (see gh-13012):

        1) If `arr` is a ExtensionArray or Index, `arr` will be
        returned as is.
        2) If `arr` is a Series, the `_values` attribute will
        be reshaped and returned.

        Parameters
        ----------
        arr : array-like, object to be reshaped
        new_shape : int or tuple of ints, the new shape
        """
        if isinstance(arr, ABCSeries):
            arr = arr._values
        if not is_extension_array_dtype(arr.dtype):
            # Note: this will include TimedeltaArray and tz-naive DatetimeArray
            # TODO(EA2D): special case will be unnecessary with 2D EAs
            arr = np.asarray(arr).reshape(new_shape)
        return arr

        
if Version(pandas.__version__) < Version("2.0"):
    from pandas import Int64Index, Float64Index
else:
    Int64Index = None
    Float64Index = None

if Version(pandas.__version__) < Version("2.1"):
    from pandas.core.arrays.sparse import SparseDtype
else:
    from pandas import SparseDtype
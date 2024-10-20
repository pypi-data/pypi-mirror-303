
i32 = int32 = 'int32'
i64 = int64 = 'int64'
f32 = float32 = 'float32'
f64 = float64 = 'float64'
bool = 'bool'

class Array(object):
    def __init__(self, shape_or_ndim, ty=None):
        if isinstance(shape_or_ndim, int):
            self.ndim = shape_or_ndim
            self.shape = None
        else:
            assert isinstance(shape_or_ndim, tuple)
            self.ndim = None
            self.shape = shape_or_ndim
        self.ty = ty

    def __repr__(self):
        return 'Array(ndim={}, shape={}, ty={})'.format(self.ndim, self.shape, self.ty)
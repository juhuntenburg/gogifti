import nibabel as nb
# utility functions to make GiftiImages easy to use

def add_data(data, gii=None, intent='NIFTI_INTENT_NONE'):
    # if no gii given, create one, otherwise this code changes the given nii in place, is that good?
    if gii is None:
        gii = nb.gifti.GiftiImage()
    if isinstance(data, list):
        for i in range(len(list)):
            if isinstance(intent, list):
                gii.add_gifti_data_array(nb.gifti.GiftiDataArray(data[i], intent=intent[i]))
            else:
                gii.add_gifti_data_array(nb.gifti.GiftiDataArray(data[i], intent=intent))
    else:
        gii.add_gifti_data_array(nb.gifti.GiftiDataArray(data, intent=intent))
    return gii


def get_data(gii, intent=None):
    if len(gii.darrays) != 0:
        data = []
        for darray in gii.darrays:
            # do not return POINTSETS or TRIANGLES
            if darray.intent in [1008, 1009]:
                pass
            else:
                data.append(darray.data)
        if len(data) == 0:
            ValueError('The GiftiImage only contains geometric information.\
                        Use .get_geometry() to access this information.')
    else:
        raise IOError('The GiftiImage contains no data')

    return data


def add_geometry(coords, faces, gii=None):
    # if no gii given, create one, otherwise this code changes the given nii in place, is that good?
    if gii is None:
        gii = nb.gifti.GiftiImage()

    gii.add_gifti_data_array(nb.gifti.GiftiDataArray(coords, intent='NIFTI_INTENT_POINTSET'))
    gii.add_gifti_data_array(nb.gifti.GiftiDataArray(faces, intent='NIFTI_INTENT_TRIANGLE'))

    return gii


def get_geometry(gii):

    coords = gii.get_arrays_from_intent('NIFTI_INTENT_POINTSET')[0].data
    if len(coords) == 0:
        raise IOError('GiftiImage contains no node coordinates')
    faces = gii.get_arrays_from_intent('NIFTI_INTENT_TRIANGLE')[0].data
    if len(faces) == 0:
        raise IOError('GiftiImage contains no face indices')

    return coords, faces


def make_gii(data=None, intent=None, nodes=None, faces=None):
    darrays = []
    if nodes is not None:
        darrays.append(nb.gifti.GiftiDataArray(nodes, intent='NIFTI_INTENT_POINTSET'))
    if faces is not None:
        darrays.append(nb.gifti.GiftiDataArray(faces, intent='NIFTI_INTENT_TRIANGLE'))
    if data is not None:
        if isinstance(data, list):
            for i in range(len(i)):
                if isinstance(intent, list):
                    darray.append(nb.gifti.GiftiDataArray(data[i], intent=intent[i]))
                else:
                    darray.append(nb.gifti.GiftiDataArray(data[i], intent=intent))
        else:
            darray.append(nb.gifti.GiftiDataArray(data, intent=intent))

    gii = nb.gifti.GiftiImage(darrays=darrays)
    return gii

import pandas as pd
from pytplot import time_float
from pytplot import store_data

from ..load import load


from typing import List, Optional

def att(
    trange: List[str] = ['2017-04-01', '2017-04-02'],
    level: str = 'l2',
    downloadonly: bool = False,
    notplot: bool = False,
    no_update: bool = False,
    uname: Optional[str] = None,
    passwd: Optional[str] = None,
    force_download: bool = False,
) -> List[str]:
    """
    This function loads attitude data from the Arase mission

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2017-04-01', '2017-04-02']

        level: str
            Data level; Valid options: 'l2'
            Default: 'l2'

        downloadonly: bool
            Set this flag to download the files, but not load them into
            tplot variables. Default: False

        notplot: bool
            Return the data in hash tables instead of creating tplot variables. Default: False

        no_update: bool
            If set, only load data from your local cache. Default: False

        uname: str
            User name. Default: None

        passwd: str
            Password. Default: None

        force_download: bool
            Download file even if local version is more recent than server version
            Default: False

    Returns
    -------
        list of str
            List of tplot variables loaded

    Examples
    --------
    >>> import pyspedas
    >>> from pytplot import tplot
    >>> att_vars = pyspedas.erg.att(trange=['2017-04-01', '2017-04-02'])
    >>> tplot(['erg_att_sprate', 'erg_att_spphase', 'erg_att_izras', 'erg_att_izdec', 'erg_att_gxras', 'erg_att_gxdec', 'erg_att_gzras', 'erg_att_gzdec'])


    """
    file_res = 24*3600.
    pathformat = 'satellite/erg/att/txt/erg_att_'+level+'_%Y%m%d_v??.txt'

    out_files = load(pathformat=pathformat, trange=trange, file_res=file_res,
                     downloadonly=True, no_update=no_update, uname=uname, passwd=passwd, force_download=force_download)

    if downloadonly:
        return out_files

    data_flame_list = []
    for file in out_files:
        raw_read_table = pd.read_table(file)
        data_flame_list.append(
            raw_read_table[10:][raw_read_table.keys()[0]].str.split(expand=True))

    concat_frame_for_tplot = pd.concat(data_flame_list)
    time_float_array = time_float(concat_frame_for_tplot.iloc[:, 0])

    Omega_float_array = concat_frame_for_tplot.iloc[:, 1].astype(float)
    Phase_float_array = concat_frame_for_tplot.iloc[:, 9].astype(float)
    I_Alpha_float_array = concat_frame_for_tplot.iloc[:, 2].astype(float)
    I_Delta_float_array = concat_frame_for_tplot.iloc[:, 3].astype(float)
    GX_Alpha_float_array = concat_frame_for_tplot.iloc[:, 10].astype(float)
    GX_Delta_float_array = concat_frame_for_tplot.iloc[:, 11].astype(float)
    GZ_Alpha_float_array = concat_frame_for_tplot.iloc[:, 12].astype(float)
    GZ_Delta_float_array = concat_frame_for_tplot.iloc[:, 13].astype(float)

    if notplot:
        output_dictionary = {}
        output_dictionary['erg_att_sprate'] = {
            'x': time_float_array, 'y': Omega_float_array}
        output_dictionary['erg_att_spphase'] = {
            'x': time_float_array, 'y': Phase_float_array}
        output_dictionary['erg_att_izras'] = {
            'x': time_float_array, 'y': I_Alpha_float_array}
        output_dictionary['erg_att_izdec'] = {
            'x': time_float_array, 'y': I_Delta_float_array}
        output_dictionary['erg_att_gxras'] = {
            'x': time_float_array, 'y': GX_Alpha_float_array}
        output_dictionary['erg_att_gxdec'] = {
            'x': time_float_array, 'y': GX_Delta_float_array}
        output_dictionary['erg_att_gzras'] = {
            'x': time_float_array, 'y': GZ_Alpha_float_array}
        output_dictionary['erg_att_gzdec'] = {
            'x': time_float_array, 'y': GZ_Delta_float_array}
        return output_dictionary
    else:
        store_data('erg_att_sprate', data={
            'x': time_float_array, 'y': Omega_float_array})
        store_data('erg_att_spphase', data={
            'x': time_float_array, 'y': Phase_float_array})
        store_data('erg_att_izras', data={
            'x': time_float_array, 'y': I_Alpha_float_array})
        store_data('erg_att_izdec', data={
            'x': time_float_array, 'y': I_Delta_float_array})
        store_data('erg_att_gxras', data={
            'x': time_float_array, 'y': GX_Alpha_float_array})
        store_data('erg_att_gxdec', data={
            'x': time_float_array, 'y': GX_Delta_float_array})
        store_data('erg_att_gzras', data={
            'x': time_float_array, 'y': GZ_Alpha_float_array})
        store_data('erg_att_gzdec', data={
            'x': time_float_array, 'y': GZ_Delta_float_array})

    return ['erg_att_sprate','erg_att_spphase','erg_att_izras','erg_att_gxras','erg_att_gxdec','erg_att_gzras','erg_att_gzdec']

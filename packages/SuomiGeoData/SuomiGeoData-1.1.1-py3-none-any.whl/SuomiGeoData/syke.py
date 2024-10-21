import os
import io
import zipfile
import typing
import geopandas
import requests
from .core import Core


class Syke:

    '''
    Provides functionality for downloading and extracting data from Syke
    (https://www.syke.fi/en-US/Open_information/Spatial_datasets/Downloadable_spatial_dataset).
    '''

    def download_corine_land_cover_2018(
        self,
        folder_path: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Downloads raster files of Finland's CORINE land cover for the year 2018 and
        returns a confirmation message.

        Parameters
        ----------
        folder_path : str
            Folder path to save the downloaded files.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that download is complete.
        '''

        # check the existence of the given folder path
        if os.path.isdir(folder_path):
            pass
        else:
            raise Exception(
                'The folder path does not exist.'
            )

        # web request headers
        headers = Core().default_http_headers if http_headers is None else http_headers

        # download land cover
        url = 'https://wwwd3.ymparisto.fi/d3/Static_rs/spesific/clc2018_fi20m.zip'
        response = requests.get(
            url=url,
            headers=headers
        )
        downloaded_data = io.BytesIO(response.content)
        with zipfile.ZipFile(downloaded_data, 'r') as downloaded_zip:
            downloaded_zip.extractall(
                folder_path
            )

        return 'All downloads are complete.'

    def download_catchment_divisions_2023(
        self,
        folder_path: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Downloads shapefiles of Finland's catchment area divisions for the year 2023 and
        returns a confirmation message.

        Parameters
        ----------
        folder_path : str
            Path of empty folder to save the downloaded shapefiles.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that download is complete.
        '''

        # check the existence of the given folder path
        if os.path.isdir(folder_path):
            pass
        else:
            raise Exception(
                'The folder path does not exist.'
            )

        # web request headers
        headers = Core().default_http_headers if http_headers is None else http_headers

        # download land cover
        url = 'https://wwwd3.ymparisto.fi/d3/gis_data/spesific/valumaalueet.zip'
        response = requests.get(
            url=url,
            headers=headers
        )
        downloaded_data = io.BytesIO(response.content)
        with zipfile.ZipFile(downloaded_data, 'r') as downloaded_zip:
            downloaded_zip.extractall(
                folder_path
            )
            for file in os.listdir(folder_path):
                if file.startswith('Valumaaluejako_taso'):
                    renamed_file = file.replace(
                        'Valumaaluejako_taso', 'catchment_division_level_'
                    )
                else:
                    renamed_file = file.replace(
                        'Valumaaluejako_purkupiste', 'catchment_discharge_point'
                    )
                os.rename(
                    os.path.join(folder_path, file),
                    os.path.join(folder_path, renamed_file)
                )

        return 'All downloads are complete.'

    def select_subcatchments(
        self,
        input_file: str,
        level: int,
        id_subcatchments: list[int],
        output_file: str,
        percentage_cutoff: float = -1,
    ) -> geopandas.GeoDataFrame:

        '''
        Selects subcatchments from the shapefile of
        Syke's catachment divisions and returns a GeoDataFrame.

        Parameters
        ----------
        input_file : str
            Path to the shapefile of catchment area divisions, obtained from the
            :meth:`SuomiGeoData.Syke.download_catchment_divisions_2023` method.

        level : int
            Catchment division level, must be one of 1, 2, 3, 4, or 5.

        id_subcatchments : list
            List of selected integer values from the 'taso<level>_osai' column in the shapefile.

        output_file : str
            Shapefile path to save the output GeoDataFrame.

        percentage_cutoff : float, optional
            Excludes polygon below the specified area percentage, ranging between 0 to 100,
            relative to the total area of all polygons. Default is -1 for no exclusion.

        Returns
        -------
        GeoDataFrame
            A GeoDataFrame containing the selected subcatchments.
        '''

        # check output file
        check_file = Core().is_valid_ogr_driver(output_file)
        if check_file is True:
            pass
        else:
            raise Exception('Could not retrieve driver from the file path.')

        # check level
        if level in [1, 2, 3, 4, 5]:
            pass
        else:
            raise Exception('Input level must be one of 1, 2, 3, 4, or 5.')

        # input GeoDataFrame
        gdf = geopandas.read_file(input_file)

        # processing of selected subcatchments
        id_col = f'taso{level}_osai'
        area_gdf = gdf[gdf[id_col].isin(id_subcatchments)].reset_index(drop=True)
        if area_gdf.shape[0] == 0:
            raise Exception('Selected ID(s) do not exist in the subcatchment divisions map.')
        else:
            area_gdf = area_gdf.dissolve()[['geometry']]
            area_gdf = area_gdf.explode(ignore_index=True)
            total_area = area_gdf.geometry.area.sum()
            area_gdf['area_%'] = round(100 * area_gdf.geometry.area / total_area).astype('int')
            area_gdf = area_gdf[area_gdf['area_%'] > percentage_cutoff].reset_index(drop=True)
            area_gdf = area_gdf.drop(columns=['area_%'])
            area_gdf['PID'] = list(range(1, area_gdf.shape[0] + 1))

        # saving GeoDataFrame
        area_gdf.to_file(output_file)

        return area_gdf

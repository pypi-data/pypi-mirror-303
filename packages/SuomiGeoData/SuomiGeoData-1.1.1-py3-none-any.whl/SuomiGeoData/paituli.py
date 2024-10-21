import os
import io
import zipfile
import typing
import pandas
import geopandas
import requests
import tempfile
from .core import Core
from .syke import Syke


class Paituli:

    '''
    Provides functionality for downloading and extracting data from Paituli
    (https://paituli.csc.fi/download.html).
    '''

    @property
    def indexmap_dem(
        self
    ) -> geopandas.GeoDataFrame:

        '''
        Returns a GeoDataFrame containing the DEM index map.
        '''

        output = geopandas.read_file(
            os.path.join(
                os.path.dirname(__file__), 'data', 'nls_dem_index.shp'
            )
        )

        return output

    @property
    def indexmap_tdb(
        self
    ) -> geopandas.GeoDataFrame:

        '''
        Returns a GeoDataFrame containing the topographic database index map.
        '''

        output = geopandas.read_file(
            os.path.join(
                os.path.dirname(__file__), 'data', 'nls_td_index.shp'
            )
        )

        return output

    def save_indexmap_dem(
        self,
        file_path: str
    ) -> str:

        '''
        Saves the GeoDataFrame of the DEM index map to the specified file path
        and return a success message.

        Parameters
        ----------
        file_path : str
            File path to save the GeoDataFrame.

        Returns
        -------
        str
            A confirmation message indicating the output file has been saved.
        '''

        check_file = Core().is_valid_ogr_driver(file_path)
        if check_file is True:
            self.indexmap_dem.to_file(file_path)
        else:
            raise Exception(
                'Could not retrieve driver from the file path.'
            )

        return 'GeoDataFrame saved to the output file.'

    def save_indexmap_tdb(
        self,
        file_path: str
    ) -> str:

        '''
        Saves the GeoDataFrame of the topographic database
        index map to the specified file path and returns a success message.

        Parameters
        ----------
        file_path : str
            File path to save the GeoDataFrame.

        Returns
        -------
        str
            A confirmation message indicating the output file has been saved.
        '''

        check_file = Core().is_valid_ogr_driver(file_path)
        if check_file is True:
            self.indexmap_tdb.to_file(file_path)
        else:
            raise Exception(
                'Could not retrieve driver from the file path.'
            )

        return 'GeoDataFrame saved to the output file.'

    @property
    def dem_labels(
        self
    ) -> list[str]:

        '''
        Returns the list of labels from the DEM index map.
        '''

        output = list(self.indexmap_dem['label'])

        return output

    @property
    def tdb_labels(
        self
    ) -> list[str]:

        '''
        Returns the list of labels from the topographic database index map.
        '''

        output = list(self.indexmap_tdb['label'])

        return output

    def is_valid_label_dem(
        self,
        label: str
    ) -> bool:

        '''
        Returns whether the label exists in the DEM index map.

        Parameters
        ----------
        label : str
            Name of the label.

        Returns
        -------
        bool
            True if the label exists, False otherwise.
        '''

        return label in self.dem_labels

    def is_valid_label_tdb(
        self,
        label: str
    ) -> bool:

        '''
        Returns whether the label exists in the topographic database index map.

        Parameters
        ----------
        label : str
            Name of the label.

        Returns
        -------
        bool
            True if the label exists, False otherwise.
        '''

        return label in self.tdb_labels

    def dem_download_by_labels(
        self,
        labels: list[str],
        folder_path: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Downloads the DEM raster files for the given labels and
        returns a confirmation message.

        Parameters
        ----------
        labels : list
            List of label names from the DEM index map.

        folder_path : str
            Path of empty folder to save the downloaded raster files.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that all downloads are complete.
        '''

        # check empty folder path
        if len(os.listdir(folder_path)) > 0:
            raise Exception(
                'Output folder must be empty.'
            )
        else:
            pass

        # check whether the input labels exist
        for label in labels:
            if self.is_valid_label_dem(label):
                pass
            else:
                raise Exception(
                    f'The label {label} does not exist in the index map.'
                )

        # web request headers
        headers = Core().default_http_headers if http_headers is None else http_headers

        # download topographic database
        suffix_urls = self.indexmap_dem[self.indexmap_dem['label'].isin(labels)]['path']
        count = 1
        for label, url in zip(labels, suffix_urls):
            label_url = Core()._url_prefix_paituli_dem_tdb + url
            response = requests.get(
                url=label_url,
                headers=headers
            )
            downloaded_file = os.path.join(
                folder_path, f'{label}.tif'
            )
            with open(downloaded_file, 'wb') as downloaded_raster:
                downloaded_raster.write(response.content)
            print(
                f'Download of label {label} completed (count {count}/{len(labels)}).'
            )
            count = count + 1

        return 'All downloads are complete.'

    def tdb_download_by_labels(
        self,
        labels: list[str],
        folder_path: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Downloads the topographic database folders of shapefiles for the given labels and
        returns a confirmation message.

        Parameters
        ----------
        labels : list
            List of label names from the topographic database index map.

        folder_path : str
            Path of empty folder to save the downloaded folder of shapefiles.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that all downloads are complete.
        '''

        # check empty folder path
        if len(os.listdir(folder_path)) > 0:
            raise Exception(
                'Output folder must be empty.'
            )
        else:
            pass

        # check whether the input labels exist
        for label in labels:
            if self.is_valid_label_tdb(label):
                pass
            else:
                raise Exception(
                    f'The label {label} does not exist in the index map.'
                )

        # web request headers
        headers = Core().default_http_headers if http_headers is None else http_headers

        # download topographic database
        suffix_urls = self.indexmap_tdb[self.indexmap_tdb['label'].isin(labels)]['path']
        count = 1
        for label, url in zip(labels, suffix_urls):
            label_url = Core()._url_prefix_paituli_dem_tdb + url
            response = requests.get(
                url=label_url,
                headers=headers
            )
            downloaded_data = io.BytesIO(response.content)
            with zipfile.ZipFile(downloaded_data, 'r') as downloaded_zip:
                downloaded_zip.extractall(
                    os.path.join(folder_path, label)
                )
            print(
                f'Download of label {label} completed (count {count}/{len(labels)}).'
            )
            count = count + 1

        return 'All downloads are complete.'

    @property
    def get_example_area(
        self
    ) -> geopandas.GeoDataFrame:

        '''
        Returns a GeoDataFrame of example area to test
        raster and vector downloads.
        '''

        output = geopandas.read_file(
            os.path.join(
                os.path.dirname(__file__), 'data', 'example_area.shp'
            )
        )

        return output

    def dem_labels_download_by_area(
        self,
        shape_file: str,
        folder_path: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Downloads the DEM raster files for the given area and
        returns a confirmation message.

        Parameters
        ----------
        shape_file : str
            Shapefile path of the input area.

        folder_path : str
            Path of empty folder to save the downloaded raster files.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that all downloads are complete.
        '''

        # input area
        area_gdf = geopandas.read_file(shape_file)

        # check crs of input area
        target_crs = 'EPSG:3067'
        if area_gdf.crs is None:
            area_gdf = area_gdf.set_crs(target_crs)
        elif str(area_gdf.crs) != target_crs:
            area_gdf = area_gdf.to_crs(target_crs)
        else:
            pass

        # DEM index map
        index_gdf = self.indexmap_dem

        # labels
        label_gdf = geopandas.sjoin(index_gdf, area_gdf, how='inner').reset_index(drop=True)
        label_gdf = label_gdf.drop_duplicates(subset=['label']).reset_index(drop=True)

        # download labels
        if label_gdf.shape[0] == 0:
            raise Exception('The index map does not intersect with the given area.')
        else:
            message = self.dem_download_by_labels(
                labels=list(label_gdf['label']),
                folder_path=folder_path,
                http_headers=http_headers
            )

        return message

    def tdb_labels_download_by_area(
        self,
        shape_file: str,
        folder_path: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Downloads the topographic database label folders of shapefiles
        for the given area and returns a confirmation message.

        Parameters
        ----------
        shape_file : str
            Shapefile path of the input area.

        folder_path : str
            Path of empty folder to save the downloaded folders of shapefiles.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that all downloads are complete.
        '''

        # input area
        area_gdf = geopandas.read_file(shape_file)

        # check crs of input area
        target_crs = 'EPSG:3067'
        if area_gdf.crs is None:
            area_gdf = area_gdf.set_crs(target_crs)
        elif str(area_gdf.crs) != target_crs:
            area_gdf = area_gdf.to_crs(target_crs)
        else:
            pass

        # topographic database index map
        index_gdf = self.indexmap_tdb

        # labels
        label_gdf = geopandas.sjoin(index_gdf, area_gdf, how='inner').reset_index(drop=True)
        label_gdf = label_gdf.drop_duplicates(subset=['label']).reset_index(drop=True)

        # download labels
        if label_gdf.shape[0] == 0:
            raise Exception('The index map does not intersect with the given area.')
        else:
            message = self.tdb_download_by_labels(
                labels=list(label_gdf['label']),
                folder_path=folder_path,
                http_headers=http_headers
            )

        return message

    def dem_clipped_download_by_area(
        self,
        shape_file: str,
        raster_file: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Downloads the clipped DEM raster file for the given area and
        returns a confirmation message.

        Parameters
        ----------
        shape_file : str
            Shapefile path of the input area.

        raster_file : str
            File path to save the output raster.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that the raster clipping is complete.
        '''

        with tempfile.TemporaryDirectory() as tmp_dir:
            # download DEM label rasters
            message = self.dem_labels_download_by_area(
                shape_file=shape_file,
                folder_path=tmp_dir,
                http_headers=http_headers
            )
            print(message)
            # merging rasters
            message = Core().raster_merging(
                folder_path=tmp_dir,
                raster_file=os.path.join(tmp_dir, 'merged.tif'),
                compress='lzw'
            )
            print(message)
            # clipping rasters
            message = Core().raster_clipping_by_mask(
                input_file=os.path.join(tmp_dir, 'merged.tif'),
                mask_file=shape_file,
                output_file=raster_file
            )

        return message

    def dem_clipped_download_by_syke_subcatchment(
        self,
        shape_file: str,
        level: int,
        id_subcatchments: list[int],
        raster_file: str,
        percentage_cutoff: float = 0,
        http_headers: typing.Optional[dict[str, str]] = None,
    ) -> str:

        '''
        Downloads the clipped DEM raster file for the given subcatchment division of Syke and
        returns a confirmation message.

        Parameters
        ----------
        shape_file : str
            Shapefile path of catchment area divisions, obtained from the
            :meth:`SuomiGeoData.Syke.download_catchment_divisions_2023` method.

        level : int
            Level of catchment division and must be one of 1, 2, 3, 4 or 5.

        id_subcatchments : list
            List of selected integer values from the 'taso<level>_osai' column in the shapefile.

        raster_file : str
            File path to save the output raster.

        percentage_cutoff : float, optional
            Excludes polygon below the specified area percentage, ranging from 0 to 100,
            relative to the total area of all polygons. Default is 0, excluding negligible polygons.
            Provide -1 for no exclusion.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that the raster clipping is complete.
        '''

        with tempfile.TemporaryDirectory() as tmp_dir:
            area_file = os.path.join(tmp_dir, 'area.shp')
            # select Syke subcatchments
            Syke().select_subcatchments(
                input_file=shape_file,
                level=level,
                id_subcatchments=id_subcatchments,
                output_file=area_file,
                percentage_cutoff=percentage_cutoff
            )
            # clipping DEM by area
            message = self.dem_clipped_download_by_area(
                shape_file=area_file,
                raster_file=raster_file,
                http_headers=http_headers
            )

        return message

    def get_tdb_metadata(
        self,
        excel_file: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> pandas.DataFrame:

        '''
        Downloads topographic database metadata,
        converts it to a multi-index DataFrame, and saves it to an Excel file.

        Parameters
        ----------
        excel_file : str
            Path to an Excel file to save the DataFrame.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        DataFrame
            A multi-index DataFrame of the topographic database metadata.
        '''

        # web request headers
        headers = Core().default_http_headers if http_headers is None else http_headers

        # downloading topographic database metadata
        with tempfile.TemporaryDirectory() as tmp_dir:
            url = 'https://www.nic.funet.fi/index/geodata/mml/maastotietokanta/2022/maastotietokanta_kohdemalli_eng_2019.xlsx'
            response = requests.get(
                url=url,
                headers=headers
            )
            download_file = os.path.join(tmp_dir, 'tdb_metadata.xlsx')
            with open(download_file, 'wb') as download_write:
                download_write.write(response.content)
            df = pandas.read_excel(download_file)

        # processing of the Dataframe
        df = df.dropna(
            thresh=3,
            ignore_index=True
        )
        df = df.iloc[:, :-2]
        df = df.drop(index=0).reset_index(drop=True)
        df = df.dropna(subset=[df.columns[-1]]).reset_index(drop=True)
        df.columns = ['Name', 'Category', 'Shape', 'Group', 'Class']
        index_columns = ['Category', 'Shape', 'Group']
        df = df.set_index(index_columns)
        df = df.sort_index(
            level=index_columns,
            ascending=[True] * len(index_columns)
        )
        df = df.groupby(level=index_columns, group_keys=False).apply(
            lambda x: x.sort_values('Class')
        )
        df = df.set_index('Name', append=True)

        # saving DataFrame to the input Excel file
        excel_ext = Core()._excel_file_extension(excel_file)
        if excel_ext != '.xlsx':
            raise Exception(f'Input file extension "{excel_ext}" does not match the required ".xlsx".')
        else:
            with pandas.ExcelWriter(excel_file, engine='xlsxwriter') as excel_writer:
                df.to_excel(excel_writer)
                workbook = excel_writer.book
                worksheet = excel_writer.sheets['Sheet1']
                # excel sheet column width
                worksheet.set_column(len(df.index.names), len(df.index.names) + len(df.columns) - 1, 20)
                for idx, i in enumerate(df.index.names):
                    if i == 'Category':
                        worksheet.set_column(idx, idx, 30)
                    elif i == 'Name':
                        worksheet.set_column(idx, idx, 50)
                    else:
                        worksheet.set_column(idx, idx, 20)
                # index formatting
                for i in range(len(df.index.names)):
                    if df.index.names[i] != 'Name':
                        for jdx, j in enumerate(df.index.get_level_values(i)):
                            worksheet.write(
                                jdx + 1, i, j, workbook.add_format(
                                    {
                                        'align': 'center', 'valign': 'vcenter', 'bold': True, 'border': 1, 'font_size': 14
                                    }
                                )
                            )
                    else:
                        for jdx, j in enumerate(df.index.get_level_values(i)):
                            worksheet.write(
                                jdx + 1, i, j, workbook.add_format(
                                    {
                                        'align': 'left', 'valign': 'vcenter', 'bold': True, 'border': 1
                                    }
                                )
                            )
                # column formatting
                for i in range(len(df.columns)):
                    for jdx, j in enumerate(df[df.columns[i]]):
                        worksheet.write(
                            jdx + 1, len(df.index.names) + i, j,
                            workbook.add_format(
                                {
                                    'align': 'right', 'valign': 'vcenter', 'border': 1
                                }
                            )
                        )
                # header formatting
                for idx, i in enumerate(list(df.index.names) + list(df.columns)):
                    worksheet.write(
                        0, idx, i, workbook.add_format(
                            {
                                'align': 'center', 'bold': True, 'border': 1, 'font_size': 18, 'fg_color': 'cyan'
                            }
                        )
                    )

        return df

    def tdb_feature_extraction(
        self,
        folder_path: str,
        class_number: int,
        shape_file: str
    ) -> str:

        '''
        Extracts feature class geometries from the downloaded topographic database label folders
        for the specified class number and saves the output to a shapefile.

        Parameters
        ----------
        folder_path : str
            Folder path containing the downloaded topographic database label folders.

        class_number : int
            Feature class number in the topographic database meta data, obtained from the
            :meth:`SuomiGeoData.Paituli.get_tdb_metadata` method.

        shape_file : str
            Shapefile path to save the output GeoDataFrame.

        Returns
        -------
        str
            A confirmation message indicating that the feature class geometry extraction is complete.
        '''

        # check output file
        check_file = Core().is_valid_ogr_driver(shape_file)
        if check_file is True:
            pass
        else:
            raise Exception('Could not retrieve driver from the file path.')

        # DataFrame of topographic database metadat
        meta_df = pandas.read_excel(
            os.path.join(
                os.path.dirname(__file__), 'data', 'tdb_metadata.xlsx'
            )
        )

        # dictionary for mapping between geometry type and shapeffile
        shapefile_ends = {
            'Point': '_s',
            'Text': '_t',
            'Line': '_v',
            'Area': '_p'
        }

        # check class
        check_class = class_number in list(meta_df.iloc[:, -1])
        if check_class is True:
            class_df = meta_df[meta_df.iloc[:, -1] == class_number].reset_index(drop=True)
            class_shape = class_df.loc[0, 'Shape']
            class_sfe = shapefile_ends[class_shape]
        else:
            raise Exception(f'Input feature class {class_number} does not exist.')

        # targeted shapefiles
        feature_paths = []
        for sub_folder in os.listdir(folder_path):
            sf_path = os.path.join(folder_path, sub_folder)
            shapefiles = filter(
                lambda x: x.endswith('.shp'), os.listdir(sf_path)
            )
            required_files = filter(
                lambda x: x.split('.')[0].endswith(class_sfe), shapefiles
            )
            required_paths = map(
                lambda x: os.path.join(sf_path, x), required_files
            )
            feature_paths.extend(list(required_paths))

        # geometry extraction
        total_paths = len(feature_paths)
        gdf_columns = ['File', 'geometry']
        gdf = geopandas.GeoDataFrame(columns=gdf_columns)
        count = 1
        for file_path in feature_paths:
            file_name = os.path.split(file_path)[-1]
            print(f'Searching shapefile ({file_name}): {count}/{total_paths}')
            fp_gdf = geopandas.read_file(file_path)
            fp_gdf = fp_gdf[fp_gdf['LUOKKA'] == class_number]
            fp_gdf = fp_gdf[['geometry']]
            fp_gdf['File'] = file_name
            gdf = pandas.concat([gdf, fp_gdf], ignore_index=True)
            count = count + 1
        if len(gdf) == 0:
            raise Exception(
                f'No geometry is found in the downloaded files for the feature class number {class_number}.'
            )
        else:
            gdf.to_file(shape_file)

        return 'Feature class geometries extraction completed.'

    def tdb_feature_extraction_by_area(
        self,
        input_file: str,
        class_number: int,
        output_file: str,
        http_headers: typing.Optional[dict[str, str]] = None
    ) -> str:

        '''
        Extracts topographic database feature class for the given area
        and saves the output to a shapefile.

        Parameters
        ----------
        input_file : str
            Shapefile path of the input area GeoDataFrame.

        class_number : int
            Feature class number in the topographic database meta data, obtained from the
            :meth:`SuomiGeoData.Paituli.get_tdb_metadata` method.

        output_file : str
            Shapefile path to save the output GeoDataFrame.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that the feature class geometry extraction is complete.
        '''

        with tempfile.TemporaryDirectory() as tmp_dir:
            # download topographic database label folders
            message = self.tdb_labels_download_by_area(
                shape_file=input_file,
                folder_path=tmp_dir,
                http_headers=http_headers
            )
            print(message)
            # extracting feature class geometries by area
            extract_file = os.path.join(tmp_dir, 'extract.shp')
            message = self.tdb_feature_extraction(
                folder_path=tmp_dir,
                class_number=class_number,
                shape_file=extract_file
            )
            print(message)
            # shapefile clipping
            message = Core().shape_clipping_by_mask(
                input_file=extract_file,
                mask_file=input_file,
                output_file=output_file
            )

        return message

    def tdb_feature_extraction_by_syke_subcatchment(
        self,
        input_file: str,
        level: int,
        id_subcatchments: list[int],
        class_number: int,
        output_file: str,
        percentage_cutoff: float = 0,
        http_headers: typing.Optional[dict[str, str]] = None,
    ) -> str:

        '''
        Extracts topographic database feature class for the given
        subcatchment division of Syke and returns a confirmation message.

        Parameters
        ----------
        input_file : str
            Shapefile path of catchment area divisions, obtained from the
            :meth:`SuomiGeoData.Syke.download_catchment_divisions_2023` method.

        level : int
            Level of catchment division and must be one of 1, 2, 3, 4 or 5.

        id_subcatchments : list
            List of selected integer values from the 'taso<level>_osai' column in the shapefile.

        class_number : int
            Feature class number in the topographic database meta data, obtained from the
            :meth:`SuomiGeoData.Paituli.get_tdb_metadata` method.

        output_file : str
            Shapefile path to save the output GeoDataFrame.

        percentage_cutoff : float, optional
            Excludes polygon below the specified area percentage, ranging from 0 to 100,
            relative to the total area of all polygons. Default is 0, excluding negligible polygons.
            Provide -1 for no exclusion.

        http_headers : dict, optional
            HTTP headers to be used for the web request. Defaults to
            :attr:`SuomiGeoData.core.Core.default_http_headers` attribute if not provided.

        Returns
        -------
        str
            A confirmation message indicating that the GeoDataFrame clipping is complete.
        '''

        with tempfile.TemporaryDirectory() as tmp_dir:
            area_file = os.path.join(tmp_dir, 'area.shp')
            # select Syke subcatchments
            Syke().select_subcatchments(
                input_file=input_file,
                level=level,
                id_subcatchments=id_subcatchments,
                output_file=area_file,
                percentage_cutoff=percentage_cutoff
            )
            # clipping topographic database feature by area
            message = self.tdb_feature_extraction_by_area(
                input_file=area_file,
                class_number=class_number,
                output_file=output_file,
                http_headers=http_headers
            )

        return message

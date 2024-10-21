import pytest
import SuomiGeoData
import os
import tempfile
import geopandas
import shapely
import rasterio
import warnings


@pytest.fixture(scope='class')
def paituli():

    yield SuomiGeoData.Paituli()


@pytest.fixture(scope='class')
def syke():

    yield SuomiGeoData.Syke()


@pytest.fixture(scope='class')
def core():

    yield SuomiGeoData.core.Core()


@pytest.fixture
def message():

    output = {
        'download': 'All downloads are complete.',
        'folder_empty': 'Output folder must be empty.',
        'gdf_write': 'GeoDataFrame saved to the output file.',
        'error_area': 'The index map does not intersect with the given area.',
        'error_driver': 'Could not retrieve driver from the file path.',
        'error_folder': 'The folder path does not exist.',
        'error_label': 'The label ABCDE does not exist in the index map.'
    }

    return output


def test_save_indexmap(
    paituli,
    message
):

    with tempfile.TemporaryDirectory() as tmp_dir:
        # pass test for saving DEM index map
        dem_file = os.path.join(tmp_dir, 'indexmap_dem.shp')
        save_dem = paituli.save_indexmap_dem(dem_file)
        assert save_dem == message['gdf_write']
        dem_gdf = geopandas.read_file(dem_file)
        assert isinstance(dem_gdf, geopandas.GeoDataFrame) is True
        assert dem_gdf.shape[0] == 10320
        # pass test for saving topographic database index map
        tdb_file = os.path.join(tmp_dir, 'indexmap_tdb.shp')
        save_tdb = paituli.save_indexmap_tdb(tdb_file)
        assert save_tdb == message['gdf_write']
        tdb_gdf = geopandas.read_file(tdb_file)
        assert isinstance(tdb_gdf, geopandas.GeoDataFrame) is True
        assert tdb_gdf.shape[0] == 3132


def test_is_valid_label(
    paituli
):

    # pass test for valid label of DEM index map
    assert paituli.is_valid_label_dem('K3244G') is True
    assert paituli.is_valid_label_dem('invalid_label') is False

    # pass test for valid label of topographic database index map
    assert paituli.is_valid_label_tdb('K2344R') is True
    assert paituli.is_valid_label_tdb('invalid_label') is False


def test_download_by_labels(
    paituli,
    message
):

    with tempfile.TemporaryDirectory() as tmp_dir:
        # create sub folder
        sub_dir = os.path.join(tmp_dir, 'sub_dir')
        os.makedirs(sub_dir)
        # error test for invalid folder path of DEM
        with pytest.raises(Exception) as exc_info:
            paituli.dem_download_by_labels(['X4344A'], tmp_dir)
        assert exc_info.value.args[0] == message['folder_empty']
        # error test for invalid folder path of topographic database
        with pytest.raises(Exception) as exc_info:
            paituli.tdb_download_by_labels(['J3224R'], tmp_dir)
        assert exc_info.value.args[0] == message['folder_empty']

    with tempfile.TemporaryDirectory() as tmp_dir:
        # error test for invalid DEM label
        with pytest.raises(Exception) as exc_info:
            paituli.dem_download_by_labels(['ABCDE'], tmp_dir)
        assert exc_info.value.args[0] == message['error_label']
        # error test for invalid topographic database label
        with pytest.raises(Exception) as exc_info:
            paituli.tdb_download_by_labels(['ABCDE'], tmp_dir)
        assert exc_info.value.args[0] == message['error_label']


def test_dem_labels_download_by_area(
    paituli,
    message
):

    # error test
    with tempfile.TemporaryDirectory() as tmp_dir:
        # empty subdirectory
        sub_dir = os.path.join(tmp_dir, 'sub_dir')
        os.makedirs(sub_dir)
        # exmaple area with no Coordinate Reference System
        nocrs_gdf = geopandas.GeoDataFrame(
            geometry=[shapely.Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        )
        nocrs_file = os.path.join(tmp_dir, 'no_crs.shp')
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            nocrs_gdf.to_file(nocrs_file)
        # error test for no intersection between given area and DEM index map
        with pytest.raises(Exception) as exc_info:
            paituli.dem_labels_download_by_area(nocrs_file, sub_dir)
        assert exc_info.value.args[0] == message['error_area']
        # exmaple area with Coordinate Reference System other than EPSG:3067
        crs_gdf = nocrs_gdf.set_crs(crs='EPSG:4326')
        crs_file = os.path.join(tmp_dir, 'crs.shp')
        crs_gdf.to_file(crs_file)
        # error test for no intersection between given area and DEM index map
        with pytest.raises(Exception) as exc_info:
            paituli.dem_labels_download_by_area(crs_file, sub_dir)
        assert exc_info.value.args[0] == message['error_area']


def test_tdb_labels_download_by_area(
    paituli,
    message
):

    # error test
    with tempfile.TemporaryDirectory() as tmp_dir:
        # empty subdirectory
        sub_dir = os.path.join(tmp_dir, 'sub_dir')
        os.makedirs(sub_dir)
        # exmaple area with no Coordinate Reference System
        nocrs_gdf = geopandas.GeoDataFrame(
            geometry=[shapely.Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        )
        nocrs_file = os.path.join(tmp_dir, 'no_crs.shp')
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            nocrs_gdf.to_file(nocrs_file)
        # error test for no intersection between given area and topographic database index map
        with pytest.raises(Exception) as exc_info:
            paituli.tdb_labels_download_by_area(nocrs_file, sub_dir)
        assert exc_info.value.args[0] == message['error_area']
        # exmaple area with Coordinate Reference System other than EPSG:3067
        crs_gdf = nocrs_gdf.set_crs(crs='EPSG:4326')
        crs_file = os.path.join(tmp_dir, 'crs.shp')
        crs_gdf.to_file(crs_file)
        # error test for no intersection between given area and topographic database index map
        with pytest.raises(Exception) as exc_info:
            paituli.tdb_labels_download_by_area(crs_file, sub_dir)
        assert exc_info.value.args[0] == message['error_area']


def test_download_corine_land_cover_2018(
    syke,
    message
):

    # pass test for downloading Syke's land cover map
    with tempfile.TemporaryDirectory() as tmp_dir:
        assert len(os.listdir(tmp_dir)) == 0
        assert syke.download_corine_land_cover_2018(tmp_dir) == message['download']
        assert len(os.listdir(tmp_dir)) > 0


def test_get_tdb_metadata(
    paituli,
    message
):

    # pass test for topographic database to multi-index DataFrame
    with tempfile.TemporaryDirectory() as tmp_dir:
        excel_file = os.path.join(tmp_dir, 'tdb_metadata.xlsx')
        df = paituli.get_tdb_metadata(
            excel_file=excel_file
        )
        assert len(df.index.names) == 4

    # error test for invalid Excel file input
    with pytest.raises(Exception) as exc_info:
        paituli.get_tdb_metadata('tdb_metadata.xl')
    assert exc_info.value.args[0] == 'Input file extension ".xl" does not match the required ".xlsx".'


def test_error_folder_driver(
    paituli,
    syke,
    core,
    message
):

    # error test for undetected OGR driver while saving DEM index map
    with pytest.raises(Exception) as exc_info:
        paituli.save_indexmap_dem('invalid_file_extension.sh')
    assert exc_info.value.args[0] == message['error_driver']

    # error test for undetected OGR driver while saving topographic database index map
    with pytest.raises(Exception) as exc_info:
        paituli.save_indexmap_tdb('invalid_file_extension.sh')
    assert exc_info.value.args[0] == message['error_driver']

    # error test for invalid output shapefile path of Syke subcatchment selection
    with pytest.raises(Exception) as exc_info:
        syke.select_subcatchments(
            input_file='catchment_division_level_5.shp',
            level=5,
            id_subcatchments=[15730214505],
            output_file='select_subcatchments.sh'
        )
    assert exc_info.value.args[0] == message['error_driver']

    # error test for invalid output file path of shape clipping
    with pytest.raises(Exception) as exc_info:
        core.shape_clipping_by_mask(
            input_file='input.shp',
            mask_file='mask.shp',
            output_file='output.sh'
        )
    assert exc_info.value.args[0] == message['error_driver']

    # error test for invalid output file path of raster clipping
    with pytest.raises(Exception) as exc_info:
        core.raster_clipping_by_mask(
            input_file='input.tif',
            mask_file='mask.shp',
            output_file='output.t'
        )
    assert exc_info.value.args[0] == message['error_driver']

    with tempfile.TemporaryDirectory() as tmp_dir:
        # error test for invalid output raster path of raster merging
        with pytest.raises(Exception) as exc_info:
            core.raster_merging(
                folder_path=tmp_dir,
                raster_file=os.path.join(tmp_dir, 'raster.t')
            )
        assert exc_info.value.args[0] == message['error_driver']
        # error test for invalid output shapefile path of topographic database feature extraction
        with pytest.raises(Exception) as exc_info:
            paituli.tdb_feature_extraction(
                folder_path=tmp_dir,
                class_number=36311,
                shape_file=os.path.join(tmp_dir, 'shape.sh')
            )
        assert exc_info.value.args[0] == message['error_driver']

    # error test for invalid folder path of Syke catchment download
    with pytest.raises(Exception) as exc_info:
        syke.download_catchment_divisions_2023(
            folder_path=tmp_dir
        )
    assert exc_info.value.args[0] == message['error_folder']

    # error test for invalid folder path of Syke land cover download
    with pytest.raises(Exception) as exc_info:
        syke.download_corine_land_cover_2018(tmp_dir)
    assert exc_info.value.args[0] == message['error_folder']


def test_clipped_download_by_syke_subcatchment(
    paituli,
    syke,
    message
):

    # temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        # pass test for downloading Syke's catchment divisions
        assert syke.download_catchment_divisions_2023(tmp_dir) == message['download']
        catchd5_path = os.path.join(tmp_dir, 'catchment_division_level_5.shp')
        #########################
        # Digital Elevation Model
        #########################
        # pass test for DEM clipped download by Syke subcatchments
        raster_file = os.path.join(tmp_dir, 'clipped_dem_by_syke_subcatchment.tif')
        assert paituli.dem_clipped_download_by_syke_subcatchment(
            shape_file=catchd5_path,
            level=5,
            id_subcatchments=[15730214505, 15730214514],
            raster_file=raster_file
        ) == 'Raster clipping completed.'
        with rasterio.open(raster_file) as tmp_raster:
            assert tmp_raster.bounds.left == 582480.0
            assert tmp_raster.bounds.right == 589690.0
        # error test for Syke's invalid level subctachment divisions
        with pytest.raises(Exception) as exc_info:
            paituli.dem_clipped_download_by_syke_subcatchment(
                shape_file=catchd5_path,
                level=7,
                id_subcatchments=[15730214505, 15730214514],
                raster_file=raster_file
            )
        assert exc_info.value.args[0] == 'Input level must be one of 1, 2, 3, 4, or 5.'
        # error test for Syke's invalid subcatchment ID(s)
        with pytest.raises(Exception) as exc_info:
            paituli.dem_clipped_download_by_syke_subcatchment(
                shape_file=catchd5_path,
                level=5,
                id_subcatchments=[157302],
                raster_file=raster_file
            )
        assert exc_info.value.args[0] == 'Selected ID(s) do not exist in the subcatchment divisions map.'
        ######################
        # Topographic Database
        ######################
        # pass test topographic database feature extraction by Syke's subcatchment ID(s)
        assert paituli.tdb_feature_extraction_by_syke_subcatchment(
            input_file=catchd5_path,
            level=5,
            id_subcatchments=[15730216003],
            class_number=36311,
            output_file=os.path.join(tmp_dir, 'clipped_feature_class.shp')
        ) == 'Shape clipping completed.'


def test_tdb_feature_extraction(
    paituli,
    core,
    message
):

    # temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        # example area
        example_gdf = paituli.get_example_area
        example_file = os.path.join(tmp_dir, 'example.shp')
        example_gdf.to_file(example_file)
        # create sub folder
        sub_dir = os.path.join(tmp_dir, 'sub_dir')
        os.makedirs(sub_dir)
        # download topographic dadabase folder labels
        assert paituli.tdb_labels_download_by_area(
            shape_file=example_file,
            folder_path=sub_dir
        ) == message['download']
        assert len(os.listdir(sub_dir)) == 2
        # error test for non-existence class of topographic database feature extraction
        with pytest.raises(Exception) as exc_info:
            paituli.tdb_feature_extraction(
                folder_path=sub_dir,
                class_number=10000,
                shape_file=os.path.join(tmp_dir, 'output.shp')
            )
        assert exc_info.value.args[0] == 'Input feature class 10000 does not exist.'
        # error test for no geometry in the input area of topographic database feature class
        assert paituli.tdb_feature_extraction(
            folder_path=sub_dir,
            class_number=36312,
            shape_file=os.path.join(tmp_dir, 'extract.shp')
        ) == 'Feature class geometries extraction completed.'
        with pytest.raises(Exception) as exc_info:
            core.shape_clipping_by_mask(
                input_file=os.path.join(tmp_dir, 'extract.shp'),
                mask_file=example_file,
                output_file=os.path.join(tmp_dir, 'output.shp')
            )
        assert exc_info.value.args[0] == 'No geometry is found in the input area.'
        # error test for no geometry in the downloaded files of topographic database feature class
        with pytest.raises(Exception) as exc_info:
            paituli.tdb_feature_extraction(
                folder_path=sub_dir,
                class_number=38400,
                shape_file=os.path.join(tmp_dir, 'output.shp')
            )
        assert exc_info.value.args[0] == 'No geometry is found in the downloaded files for the feature class number 38400.'

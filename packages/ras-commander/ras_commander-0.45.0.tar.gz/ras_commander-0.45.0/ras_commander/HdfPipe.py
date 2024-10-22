import h5py
import numpy as np
import pandas as pd
import geopandas as gpd
import xarray as xr
from pathlib import Path
from shapely.geometry import LineString, Point
from typing import List, Dict, Any, Optional, Union
from .HdfBase import HdfBase
from .HdfUtils import HdfUtils
from .Decorators import standardize_input, log_call
from .LoggingConfig import get_logger

logger = get_logger(__name__)

class HdfPipe:
    """
    A class for handling pipe network related data from HEC-RAS HDF files.
    """

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def get_pipe_conduits(hdf_path: Path) -> gpd.GeoDataFrame:
        """
        Extract pipe conduit data from the HDF file.

        Args:
            hdf_path (Path): Path to the HDF file.

        Returns:
            gpd.GeoDataFrame: GeoDataFrame containing pipe conduit data.

        Raises:
            KeyError: If the required datasets are not found in the HDF file.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf:
                # Extract pipe conduit data
                polyline_info = hdf['/Geometry/Pipe Conduits/Polyline Info'][()]
                polyline_points = hdf['/Geometry/Pipe Conduits/Polyline Points'][()]
                terrain_profiles_info = hdf['/Geometry/Pipe Conduits/Terrain Profiles Info'][()]

                # Create geometries
                geometries = []
                for start, count, _, _ in polyline_info:
                    points = polyline_points[start:start+count]
                    geometries.append(LineString(points))

                # Create GeoDataFrame
                gdf = gpd.GeoDataFrame(geometry=geometries)
                gdf['conduit_id'] = range(len(gdf))
                gdf['terrain_profile_start'] = terrain_profiles_info[:, 0]
                gdf['terrain_profile_count'] = terrain_profiles_info[:, 1]

                # Set CRS if available
                crs = HdfUtils.projection(hdf_path)
                if crs:
                    gdf.set_crs(crs, inplace=True)

                return gdf

        except KeyError as e:
            logger.error(f"Required dataset not found in HDF file: {e}")
            raise
        except Exception as e:
            logger.error(f"Error extracting pipe conduit data: {e}")
            raise

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def get_pipe_nodes(hdf_path: Path) -> gpd.GeoDataFrame:
        """
        Extract pipe node data from the HDF file.

        Args:
            hdf_path (Path): Path to the HDF file.

        Returns:
            gpd.GeoDataFrame: GeoDataFrame containing pipe node data.

        Raises:
            KeyError: If the required datasets are not found in the HDF file.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf:
                # Extract pipe node data
                points = hdf['/Geometry/Pipe Nodes/Points'][()]
                attributes = hdf['/Geometry/Pipe Nodes/Attributes'][()]

                # Create geometries
                geometries = [Point(x, y) for x, y in points]

                # Create GeoDataFrame
                gdf = gpd.GeoDataFrame(geometry=geometries)
                gdf['node_id'] = range(len(gdf))

                # Add attributes
                for name in attributes.dtype.names:
                    gdf[name] = attributes[name]

                # Set CRS if available
                crs = HdfUtils.projection(hdf_path)
                if crs:
                    gdf.set_crs(crs, inplace=True)

                return gdf

        except KeyError as e:
            logger.error(f"Required dataset not found in HDF file: {e}")
            raise
        except Exception as e:
            logger.error(f"Error extracting pipe node data: {e}")
            raise

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def get_pipe_network_timeseries(hdf_path: Path, variable: str) -> xr.DataArray:
        """
        Extract timeseries data for a specific variable in the pipe network.

        Args:
            hdf_path (Path): Path to the HDF file.
            variable (str): Variable to extract (e.g., "Cell Courant", "Cell Water Surface").

        Returns:
            xr.DataArray: DataArray containing the timeseries data.

        Raises:
            KeyError: If the required datasets are not found in the HDF file.
            ValueError: If an invalid variable is specified.
        """
        valid_variables = [
            "Cell Courant", "Cell Water Surface", "Face Flow", "Face Velocity",
            "Face Water Surface", "Pipes/Pipe Flow DS", "Pipes/Pipe Flow US",
            "Pipes/Vel DS", "Pipes/Vel US", "Nodes/Depth", "Nodes/Drop Inlet Flow",
            "Nodes/Water Surface"
        ]

        if variable not in valid_variables:
            raise ValueError(f"Invalid variable. Must be one of: {', '.join(valid_variables)}")

        try:
            with h5py.File(hdf_path, 'r') as hdf:
                # Extract timeseries data
                data_path = f"/Results/Unsteady/Output/Output Blocks/DSS Hydrograph Output/Unsteady Time Series/Pipe Networks/Davis/{variable}"
                data = hdf[data_path][()]

                # Extract time information
                time = HdfBase._get_unsteady_datetimes(hdf)

                # Create DataArray
                da = xr.DataArray(
                    data=data,
                    dims=['time', 'location'],
                    coords={'time': time, 'location': range(data.shape[1])},
                    name=variable
                )

                # Add attributes
                da.attrs['units'] = hdf[data_path].attrs.get('Units', b'').decode('utf-8')
                da.attrs['variable'] = variable

                return da

        except KeyError as e:
            logger.error(f"Required dataset not found in HDF file: {e}")
            raise
        except Exception as e:
            logger.error(f"Error extracting pipe network timeseries data: {e}")
            raise

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def get_pipe_network_summary(hdf_path: Path) -> pd.DataFrame:
        """
        Extract summary data for pipe networks from the HDF file.

        Args:
            hdf_path (Path): Path to the HDF file.

        Returns:
            pd.DataFrame: DataFrame containing pipe network summary data.

        Raises:
            KeyError: If the required datasets are not found in the HDF file.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf:
                # Extract summary data
                summary_path = "/Results/Unsteady/Summary/Pipe Network"
                if summary_path not in hdf:
                    logger.warning("Pipe Network summary data not found in HDF file")
                    return pd.DataFrame()

                summary_data = hdf[summary_path][()]
                
                # Create DataFrame
                df = pd.DataFrame(summary_data)

                # Convert column names
                df.columns = [col.decode('utf-8') for col in df.columns]

                return df

        except KeyError as e:
            logger.error(f"Required dataset not found in HDF file: {e}")
            raise
        except Exception as e:
            logger.error(f"Error extracting pipe network summary data: {e}")
            raise

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def get_pipe_profile(hdf_path: Path, conduit_id: int) -> pd.DataFrame:
        """
        Extract the profile data for a specific pipe conduit.

        Args:
            hdf_path (Path): Path to the HDF file.
            conduit_id (int): ID of the conduit to extract profile for.

        Returns:
            pd.DataFrame: DataFrame containing the pipe profile data.

        Raises:
            KeyError: If the required datasets are not found in the HDF file.
            IndexError: If the specified conduit_id is out of range.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf:
                # Get conduit info
                terrain_profiles_info = hdf['/Geometry/Pipe Conduits/Terrain Profiles Info'][()]
                
                if conduit_id >= len(terrain_profiles_info):
                    raise IndexError(f"conduit_id {conduit_id} is out of range")

                start, count = terrain_profiles_info[conduit_id]

                # Extract profile data
                profile_values = hdf['/Geometry/Pipe Conduits/Terrain Profiles Values'][start:start+count]

                # Create DataFrame
                df = pd.DataFrame(profile_values, columns=['Station', 'Elevation'])

                return df

        except KeyError as e:
            logger.error(f"Required dataset not found in HDF file: {e}")
            raise
        except IndexError as e:
            logger.error(f"Invalid conduit_id: {e}")
            raise
        except Exception as e:
            logger.error(f"Error extracting pipe profile data: {e}")
            raise
        
        


set OUTPUT=%~dp1output

del %OUTPUT%.tif
del %~dpn1.exr
del %~dpn1.png

"C:\Program Files\QGIS 2.18\bin\gdal_translate.exe" -ot Float32 -of GTiff -scale -co worldfile=yes %1 %OUTPUT%.tif
"C:\Program Files\QGIS 2.18\bin\gdal_translate.exe" -of png -scale -co worldfile=yes %1 %~dpn1.png

%~dp0to_opnexr.exe %OUTPUT%.tif

ren %OUTPUT%.exr %~n1.exr

pause
exit

Usage: gdal_translate [--help-general] [--long-usage]
       [-ot {Byte/Int16/UInt16/UInt32/Int32/Float32/Float64/
             CInt16/CInt32/CFloat32/CFloat64}] [-strict]
       [-of format] [-b band] [-mask band] [-expand {gray|rgb|rgba}]
       [-outsize xsize[%]|0 ysize[%]|0] [-tr xres yres]
       [-r {nearest,bilinear,cubic,cubicspline,lanczos,average,mode}]
       [-unscale] [-scale[_bn] [src_min src_max [dst_min dst_max]]]* [-exponent[
_bn] exp_val]*
       [-srcwin xoff yoff xsize ysize] [-epo] [-eco]
       [-projwin ulx uly lrx lry] [-projwin_srs srs_def]
       [-a_srs srs_def] [-a_ullr ulx uly lrx lry] [-a_nodata value]
       [-gcp pixel line easting northing [elevation]]*
       [-mo "META-TAG=VALUE"]* [-q] [-sds]
       [-co "NAME=VALUE"]* [-stats] [-norat]
       [-oo NAME=VALUE]*
       src_dataset dst_dataset

ERROR 5: Output driver `ssss' not recognised.
ERROR 5: The following format drivers are configured and support outp
ERROR 5:   GeoRaster: Oracle Spatial GeoRaster
ERROR 5:   VRT: Virtual Raster
ERROR 5:   GTiff: GeoTIFF
ERROR 5:   NITF: National Imagery Transmission Format
ERROR 5:   HFA: Erdas Imagine Images (.img)
ERROR 5:   ELAS: ELAS
ERROR 5:   AAIGrid: Arc/Info ASCII Grid
ERROR 5:   DTED: DTED Elevation Raster
ERROR 5:   PNG: Portable Network Graphics
ERROR 5:   JPEG: JPEG JFIF
ERROR 5:   MEM: In Memory Raster
ERROR 5:   GIF: Graphics Interchange Format (.gif)
ERROR 5:   XPM: X11 PixMap Format
ERROR 5:   BMP: MS Windows Device Independent Bitmap
ERROR 5:   PCIDSK: PCIDSK Database File
ERROR 5:   PCRaster: PCRaster Raster File
ERROR 5:   ILWIS: ILWIS Raster Map
ERROR 5:   SGI: SGI Image File Format 1.0
ERROR 5:   SRTMHGT: SRTMHGT File Format
ERROR 5:   Leveller: Leveller heightfield
ERROR 5:   Terragen: Terragen heightfield
ERROR 5:   GMT: GMT NetCDF Grid Format
ERROR 5:   netCDF: Network Common Data Format
ERROR 5:   HDF4Image: HDF4 Dataset
ERROR 5:   ISIS2: USGS Astrogeology ISIS cube (Version 2)
ERROR 5:   ERS: ERMapper .ers Labelled
ERROR 5:   JP2OpenJPEG: JPEG-2000 driver based on OpenJPEG library
ERROR 5:   FIT: FIT Image
ERROR 5:   RMF: Raster Matrix Format
ERROR 5:   WMS: OGC Web Map Service
ERROR 5:   RST: Idrisi Raster A.1
ERROR 5:   INGR: Intergraph Raster
ERROR 5:   GSAG: Golden Software ASCII Grid (.grd)
ERROR 5:   GSBG: Golden Software Binary Grid (.grd)
ERROR 5:   GS7BG: Golden Software 7 Binary Grid (.grd)
ERROR 5:   R: R Object Data Store
ERROR 5:   KMLSUPEROVERLAY: Kml Super Overlay
ERROR 5:   PDF: Geospatial PDF
ERROR 5:   Rasterlite: Rasterlite
ERROR 5:   MBTiles: MBTiles
ERROR 5:   CALS: CALS (Type 1)
ERROR 5:   WMTS: OGC Web Mab Tile Service
ERROR 5:   MRF: Meta Raster Format
ERROR 5:   PNM: Portable Pixmap Format (netpbm)
ERROR 5:   PAux: PCI .aux Labelled
ERROR 5:   MFF: Vexcel MFF Raster
ERROR 5:   MFF2: Vexcel MFF2 (HKV) Raster
ERROR 5:   BT: VTP .bt (Binary Terrain) 1.3 Format
ERROR 5:   LAN: Erdas .LAN/.GIS
ERROR 5:   IDA: Image Data and Analysis
ERROR 5:   LCP: FARSITE v.4 Landscape File (.lcp)
ERROR 5:   GTX: NOAA Vertical Datum .GTX
ERROR 5:   NTv2: NTv2 Datum Grid Shift
ERROR 5:   CTable2: CTable2 Datum Grid Shift
ERROR 5:   KRO: KOLOR Raw
ERROR 5:   ROI_PAC: ROI_PAC raster
ERROR 5:   ENVI: ENVI .hdr Labelled
ERROR 5:   EHdr: ESRI .hdr Labelled
ERROR 5:   ISCE: ISCE raster
ERROR 5:   ARG: Azavea Raster Grid format
ERROR 5:   USGSDEM: USGS Optional ASCII DEM (and CDED)
ERROR 5:   ADRG: ARC Digitized Raster Graphics
ERROR 5:   BLX: Magellan topo (.blx)
ERROR 5:   PostGISRaster: PostGIS Raster driver
ERROR 5:   SAGA: SAGA GIS Binary Grid (.sdat)
ERROR 5:   XYZ: ASCII Gridded XYZ
ERROR 5:   HF2: HF2/HFZ heightfield raster
ERROR 5:   ZMap: ZMap Plus Grid
ERROR 5:   DB2ODBC: IBM DB2 Spatial Database
ERROR 5:   GPKG: GeoPackage
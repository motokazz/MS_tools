docName = activeDocument.fullName;
fileObj = new File(docName);
tiffOpt = new TiffSaveOptions();
tiffOpt.alphaChannels = true;
tiffOpt.annotations = true;
tiffOpt.byteOrder = ByteOrder.IBM;
tiffOpt.embedColorProfile = false;
tiffOpt.imageCompression = TIFFEncoding.NONE;
tiffOpt.jpegQuality = 3;
tiffOpt.layerCompression = LayerCompression.RLE;
tiffOpt.layers = true;
tiffOpt.saveImagePyramid = false;
tiffOpt.spotColors = false;
tiffOpt.transparency = false;
activeDocument.saveAs(fileObj, tiffOpt, true, Extension.LOWERCASE);
activeDocument.close ()


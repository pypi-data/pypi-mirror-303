import pydicom as pd
import numpy as np
import SimpleITK as sitk
import argparse
import copy

def resample(moving_rtdose, reference_rtdose):
    # moves moving_rtdose to reference_rtdose grid
    dicom_1 = moving_rtdose
    dicom_2 = reference_rtdose

    # Load DICOM files using pydicom
    # dicom_1 = pd.dcmread("input_rtdose_1.dcm")
    # dicom_2 = pd.dcmread("input_rtdose_2.dcm")

    # Extract pixel data and convert to numpy array
    pixel_data_1 = (dicom_1.pixel_array * dicom_1.DoseGridScaling).astype(np.float32)
    pixel_data_2 = (dicom_2.pixel_array * dicom_2.DoseGridScaling).astype(np.float32)

    # Get PixelSpacing from DICOM metadata
    pixel_spacing2 = np.array(dicom_2.PixelSpacing, dtype=np.float32)
    pixel_spacing1 = np.array(dicom_1.PixelSpacing, dtype=np.float32)

    # Get SliceThickness from DICOM metadata
    #slice_thickness2 = np.array([dicom_2.SliceThickness], dtype=np.float32)
    slice_thickness2 = np.array([dicom_2.GridFrameOffsetVector[1]-dicom_2.GridFrameOffsetVector[0]], dtype=np.float32)
    #slice_thickness1 = np.array([dicom_1.SliceThickness], dtype=np.float32)
    slice_thickness1 = np.array([dicom_1.GridFrameOffsetVector[1]-dicom_1.GridFrameOffsetVector[0]], dtype=np.float32)

    # Calculate spacing array
    spacing2 = np.concatenate([pixel_spacing2, slice_thickness2])
    spacing1 = np.concatenate([pixel_spacing1, slice_thickness1])

    # Convert spacing to a list of doubles
    spacing_list2 = spacing2.tolist()
    spacing_list1 = spacing1.tolist()

    # Get origin from DICOM metadata
    origin2 = np.array(dicom_2.ImagePositionPatient)
    origin1 = np.array(dicom_1.ImagePositionPatient)

    # Extract direction cosines from the DICOM metadata
    direction_cosines2 = dicom_2.ImageOrientationPatient
    direction_cosines1 = dicom_1.ImageOrientationPatient
    direction_matrix2 = np.array(direction_cosines2).reshape(2, 3)
    direction_matrix1 = np.array(direction_cosines1).reshape(2, 3)

    # Calculate the third dimension of the direction matrix using cross product
    direction_matrix2 = np.vstack([direction_matrix2, np.cross(direction_matrix2[0], direction_matrix2[1])])
    direction_matrix1 = np.vstack([direction_matrix1, np.cross(direction_matrix1[0], direction_matrix1[1])])

    # Create SimpleITK images
    image_1 = sitk.GetImageFromArray(pixel_data_1)
    image_2 = sitk.GetImageFromArray(pixel_data_2)

    # Set image properties
    image_2.SetSpacing(spacing_list2)
    image_2.SetOrigin(origin2)
    image_2.SetDirection(direction_matrix2.flatten())
    image_1.SetSpacing(spacing_list1)
    image_1.SetOrigin(origin1)
    image_1.SetDirection(direction_matrix1.flatten())


    # Resample image_1 to match image_2
    resampled_image_1 = sitk.Resample(image_1, image_2.GetSize(), sitk.Transform(), sitk.sitkLinear, image_2.GetOrigin(), image_2.GetSpacing(), image_2.GetDirection(), 0.0, sitk.sitkFloat32)

    resampled_image_1.SetSpacing(spacing_list2)
    resampled_image_1.SetOrigin(origin2)
    resampled_image_1.SetDirection(direction_matrix2.flatten())
    # Convert resampled SimpleITK image back to numpy array
    resampled_pixel_data_1 = sitk.GetArrayFromImage(resampled_image_1)

    # Save the resampled pixel data as DICOM
    # You may need to adjust this depending on your requirements
    resampled_dicom = copy.deepcopy(moving_rtdose)

    dgs = np.max(resampled_pixel_data_1) / (2**16 -1)
    resampled_pixel_data_1 = resampled_pixel_data_1 / dgs


    resampled_dicom.BitsAllocated = 16
    resampled_dicom.BitsStored = 16
    resampled_dicom.HighBit = 15
    resampled_dicom.NumberOfFrames = dicom_2.NumberOfFrames
    resampled_dicom.Columns = dicom_2.Columns
    resampled_dicom.Rows = dicom_2.Rows
    resampled_dicom.PixelSpacing = dicom_2.PixelSpacing
    resampled_dicom.ImagePositionPatient = dicom_2.ImagePositionPatient
    resampled_dicom.SliceThickness = dicom_2.SliceThickness
    resampled_dicom.GridFrameOffsetVector = dicom_2.GridFrameOffsetVector
    resampled_dicom.DoseGridScaling = dgs
    resampled_dicom.PixelData = resampled_pixel_data_1.astype(np.uint16).tobytes()
    return resampled_dicom

def main():
    parser = argparse.ArgumentParser(description='Tool for resampling an RTDOSE DICOM to another RTDOSE DICOM grid. ')
    parser.add_argument('moving', type=str, \
                help='Path to moving RTDOSE DICOM file. Will be resampled to reference.')
    parser.add_argument('reference', type=str, \
                help='Path to reference RTDOSE DICOM file.')
    parser.add_argument('-o','--output', type=str, required=False,\
                help='Path to output the new DICOM file to')    
        
    args = parser.parse_args()

    dcm_1 = pd.read_file(args.moving)
    dcm_2 = pd.read_file(args.reference)

    resampled_dicom = resample(dcm_1, dcm_2)
    if not args.output:
        print(resampled_dicom)
        exit()

    resampled_dicom.save_as(args.output)

if __name__ == "__main__":
    main()


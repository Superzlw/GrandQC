# MAIN LOOP TO PROCESS WSI
import numpy as np
from PIL import Image
import segmentation_models_pytorch as smp
import torch
from tqdm import tqdm

#Helper functions
def to_tensor_x(x, **kwargs):
    return x.transpose(2, 0, 1).astype('float32')

def get_preprocessing(image, preprocessing_fn, model_size):
    if image.size != model_size:
        image = image.resize(model_size)
        print('resized')
    image = np.array(image)
    x = preprocessing_fn(image)
    x = to_tensor_x(x)
    return x

def make_1class_map_thr (mask, class_colors):
    r = np.zeros_like(mask).astype(np.uint8)
    g = np.zeros_like(mask).astype(np.uint8)
    b = np.zeros_like(mask).astype(np.uint8)
    for l in range(1, len(class_colors)+1):
        idx = mask == l
        r[idx] = class_colors [l-1][0]
        g[idx] = class_colors [l-1][1]
        b[idx] = class_colors [l-1][2]

    rgb = np.stack([r, g, b], axis=2)
    return rgb


def slide_process_single(model, tis_det_map_mpp, slide, patch_n_w_l0, patch_n_h_l0, p_s, m_p_s, colors,
                         ENCODER_MODEL_1,ENCODER_WEIGHTS, DEVICE, BACK_CLASS):
    '''
    Tissue detection map is generated under MPP = 4, therefore model patch size of (512,512) corresponds to tis_det_map patch
    size of (128,128).
    '''

    model_size = (m_p_s, m_p_s)
    preprocessing_fn = smp.encoders.get_preprocessing_fn(ENCODER_MODEL_1, ENCODER_WEIGHTS)

    # Start loop
    for he in tqdm(range(patch_n_h_l0), total=patch_n_h_l0):
        h = he * p_s + 1
        if he == 0:
            h = 0
        # print("Current cycle ", he + 1, " of ", patch_n_h_l0)
        for wi in range(patch_n_w_l0):
            w = wi * p_s + 1
            if wi == 0:
                w = 0
            td_patch = tis_det_map_mpp[he*m_p_s:(he+1)*m_p_s, wi*m_p_s:(wi+1)*m_p_s]
            if td_patch.shape != (512,512):
                # td_patch padding (incase td_patch does not equal (512,512))
                original_shape = td_patch.shape

                # Desired shape
                desired_shape = (512, 512)

                # Calculate padding needed
                padding = [(0, desired_shape[i] - original_shape[i]) for i in range(2)]

                # Apply padding
                td_patch = np.pad(td_patch, padding, mode='constant')

            if np.count_nonzero(td_patch == 0) > 50:    # here change to check of segmentation map
                # Generate patch
                # Extract the region from the NumPy array
                work_patch_np = slide[:, h:h+p_s, w:w+p_s]
                work_patch_np = np.transpose(work_patch_np, (1, 2, 0))
                # print(work_patch_np.shape)

                # Create a PIL Image from the NumPy array
                work_patch_pil = Image.fromarray(work_patch_np)

                # Resize the image to the model patch size (m_p_s)
                work_patch_resized = work_patch_pil.resize((m_p_s, m_p_s), Image.ANTIALIAS)

                # If needed, convert the image to RGB mode
                work_patch_resized_rgb = work_patch_resized.convert('RGB')

                work_patch = work_patch_resized_rgb

                image_pre = get_preprocessing(work_patch, preprocessing_fn, model_size)
                x_tensor = torch.from_numpy(image_pre).to(DEVICE).unsqueeze(0)
                predictions = model.predict(x_tensor)
                predictions = (predictions.squeeze().cpu().numpy())

                mask_raw = np.argmax(predictions, axis=0).astype('int8')
                mask = np.where(td_patch == 1, BACK_CLASS, mask_raw)


            else:
                #print('else!')
                mask = np.full((512, 512), BACK_CLASS)

            if wi == 0:
                temp_image = mask

            else:
                temp_image = np.concatenate((temp_image, mask), axis=1)

        if he == 0:
            end_image = temp_image

        else:
            end_image = np.concatenate((end_image, temp_image), axis=0)

    end_image_1class = make_1class_map_thr(end_image, colors)
    end_image_1class = Image.fromarray(end_image_1class)
    end_image_1class = end_image_1class.resize((patch_n_w_l0*200, patch_n_h_l0*200), Image.ANTIALIAS) #what is 50 here?

    return end_image_1class, end_image


def slide_process_double(model, model_sec, tis_det_map_mpp, slide, patch_n_w_l0, patch_n_h_l0, p_s, m_p_s, colors,
                         ENCODER_MODEL_1, ENCODER_MODEL_SEC, ENCODER_WEIGHTS, DEVICE, BACK_CLASS, TU_CLASS,
                         CLASS_SHIFT):

    '''
    Tissue detection map is generated under MPP = 4, therefore model patch size of (512,512) corresponds to tis_det_map patch
    size of (128,128).
    '''

    model_size = (m_p_s, m_p_s)

    preprocessing_fn_1 = smp.encoders.get_preprocessing_fn(ENCODER_MODEL_1, ENCODER_WEIGHTS)
    preprocessing_fn_2 = smp.encoders.get_preprocessing_fn(ENCODER_MODEL_SEC, ENCODER_WEIGHTS)

    # Start loop
    for he in range(patch_n_h_l0):
        h = he * p_s + 1
        if (he == 0):
            h = 0
        print("Current cycle ", he + 1, " of ", patch_n_h_l0)
        for wi in range(patch_n_w_l0):
            w = wi * p_s + 1
            if (wi == 0):
                w = 0
            #he = 12
            #wi = 15
            td_patch = tis_det_map_mpp [he*m_p_s:(he+1)*m_p_s,wi*m_p_s:(wi+1)*m_p_s]
            if np.count_nonzero(td_patch == 0) > 50: #here change to check of segmentation map
                # Generate patch
                work_patch = slide.read_region((w, h), 0, (p_s, p_s))
                work_patch = work_patch.convert('RGB')

                # Resize to model patch size
                work_patch = work_patch.resize((m_p_s, m_p_s), Image.ANTIALIAS)

                image_pre = get_preprocessing(work_patch, preprocessing_fn_1, model_size)
                x_tensor = torch.from_numpy(image_pre).to(DEVICE).unsqueeze(0)
                predictions = model.predict(x_tensor)
                predictions = (predictions.squeeze().cpu().numpy())

                mask_raw = np.argmax(predictions, axis=0).astype('int8')
                mask = np.where(td_patch == 1, BACK_CLASS, mask_raw) #mask with tumor detection

                if np.count_nonzero(mask == TU_CLASS) > 0:
                    image_pre = get_preprocessing(work_patch, preprocessing_fn_2, model_size)
                    x_tensor = torch.from_numpy(image_pre).to(DEVICE).unsqueeze(0)
                    predictions_s = model_sec.predict(x_tensor)
                    predictions_s = (predictions_s.squeeze().cpu().numpy())
                    mask_raw_s = np.argmax(predictions_s, axis=0).astype('int8')
                    mask_sub = np.where(mask == TU_CLASS, mask_raw_s+CLASS_SHIFT, mask)              #
                    mask_1class_sub = make_1class_map_thr(mask_sub, colors)
                else:
                    mask_sub = mask
                    mask_1class_sub = make_1class_map_thr(mask_sub, colors)

                mask_1class = make_1class_map_thr(mask, colors)

            else:
                mask = np.full((512,512), BACK_CLASS)
                mask_sub = np.full((512, 512), BACK_CLASS)
                mask_1class = make_1class_map_thr(mask, colors)
                mask_1class_sub = make_1class_map_thr(mask_sub, colors)


            if (wi == 0):
                temp_image = mask
                temp_image_1class = mask_1class
                temp_image_sub = mask_sub
                temp_image_1class_sub = mask_1class_sub
            else:
                temp_image = np.concatenate((temp_image, mask), axis=1)
                temp_image_1class = np.concatenate((temp_image_1class, mask_1class), axis=1)
                temp_image_sub = np.concatenate((temp_image_sub, mask_sub), axis=1)
                temp_image_1class_sub = np.concatenate((temp_image_1class_sub, mask_1class_sub), axis=1)
        if (he == 0):
            end_image = temp_image
            end_image_sub = temp_image_sub
            end_image_1class = temp_image_1class
            end_image_1class_sub = temp_image_1class_sub
        else:
            end_image = np.concatenate((end_image, temp_image), axis=0)
            end_image_1class = np.concatenate((end_image_1class, temp_image_1class), axis=0)
            end_image_sub = np.concatenate((end_image_sub, temp_image_sub), axis=0)
            end_image_1class_sub = np.concatenate((end_image_1class_sub, temp_image_1class_sub), axis=0)

    end_image_1class = Image.fromarray(end_image_1class)
    end_image_1class = end_image_1class.resize((patch_n_w_l0*50, patch_n_h_l0*50), Image.ANTIALIAS)

    end_image_1class_sub = Image.fromarray(end_image_1class_sub)
    end_image_1class_sub = end_image_1class_sub.resize((patch_n_w_l0 * 50, patch_n_h_l0 * 50), Image.ANTIALIAS)


    return (end_image_1class, end_image, end_image_1class_sub, end_image_sub)

import numpy as np
import cv2 as cv
import copy

def get_text_size(text:str, fontScale, fontFace = cv.FONT_HERSHEY_SIMPLEX, return_baseline = False):
    ((fw,fh), baseline) = cv.getTextSize(
            text, fontFace=fontFace, fontScale=fontScale, thickness=1) # empty string is good enough
    if return_baseline:
        return fh, fw, baseline
    return fh, fw

def add_rectangle(img, p1, p2, opacity, color):
    if img.dtype != np.uint8:
        out_img = np.array(img * 255, dtype=np.uint8)
    else:
        out_img = copy.copy(img)

    if type(color[0]) != int:
        color = (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

    if p1[0] == p2[0]:
        return out_img
    if p1[1] == p2[1]:
        return out_img
    
    sub_img = out_img[p1[1]:p2[1], p1[0]:p2[0]]

    rect = np.ones(sub_img.shape, dtype=np.uint8)
    if len(rect.shape) == 2:
        rect[:, :] = int(np.round(np.average(color)))
    else:
        rect[:, :, 0] = color[0]
        rect[:, :, 1] = color[1]
        rect[:, :, 2] = color[2]
    res = cv.addWeighted(sub_img, 1. - opacity, rect, opacity, 10.)

    out_img[p1[1]:p2[1], p1[0]:p2[0]] = res

    return out_img

def add_text(img, text, p, width = None, height = None, scale = 1., foreground = (0, 0, 0), background = None,
             background_opacity = 0.5, vertical_align = 'top', horizontal_align = 'left',
             fontFace = cv.FONT_HERSHEY_SIMPLEX, margin = 0, text_thickness = 1):
    fh, fw, baseline = 0, 0, 0

    if img.dtype != np.uint8:
        img = np.ascontiguousarray(img * 255, dtype=np.uint8)
    
    lines = text.split('\n')
    for line in lines:
        fh, l_fw, baseline = get_text_size(line, scale, fontFace, return_baseline=True)
        if l_fw > fw:
            fw = l_fw

    baseline = int(np.round(1.5 * baseline))

    if width is None:
        width = fw + 2 * margin
    if height is None:
        height = (fh + baseline) * len(lines) + 2 * margin

    if background is not None:
        img = add_rectangle(img, p, (p[0] + width, p[1] + height), background_opacity, background)

    text_pos = [p[0], p[1]]
    if horizontal_align == 'left':
        text_pos[0] = p[0] + margin
    elif horizontal_align == 'center':
        text_pos[0] = p[0] + width // 2 - fw // 2
    elif horizontal_align == 'right':
        text_pos[0] = p[0] + width - margin - fw

    if type(foreground[0]) != int:
        foreground = (int(foreground[0] * 255), int(foreground[1] * 255), int(foreground[2] * 255))
    
    for i, line in enumerate(lines):
        text_pos = [0, 0]
        if horizontal_align == 'left':
            text_pos[0] = p[0] + margin
        elif horizontal_align == 'center':
            text_pos[0] = p[0] + width // 2 - fw // 2
        elif horizontal_align == 'right':
            text_pos[0] = p[0] + width - margin - fw

        if vertical_align == 'top':
            text_pos[1] = p[1] + margin + i * baseline + (i + 1) * fh
        elif vertical_align == 'center':
            inner_h = len(lines) * fh + (len(lines) - 1) * baseline
            text_pos[1] = p[1] + height // 2 - inner_h // 2 + i * baseline + (i + 1) * fh
        elif vertical_align == 'bottom':
            text_pos[1] = p[1] + height - margin - (len(lines) - i) * fh - (len(lines) - i - 1) * baseline

        img = cv.putText(img, line, (text_pos[0], text_pos[1]), fontFace=fontFace, fontScale=scale, color=foreground, thickness=text_thickness)

    return img

def line(img, kpts, i1, i2, color, thickness):
    if kpts[i1, 0] <= 0 or kpts[i1, 1] <= 0 or kpts[i2, 0] <= 0 or kpts[i2, 1] <= 0:
        return img
    p1 = (int(np.round(kpts[i1, 0] * img.shape[1])), int(np.round(kpts[i1, 1] * img.shape[0])))
    p2 = (int(np.round(kpts[i2, 0] * img.shape[1])), int(np.round(kpts[i2, 1] * img.shape[0])))
    img = cv.line(img, p1, p2, color=color, thickness=thickness)
    return img

def draw_progress(img, val, absolute, vertical_align = 'top'):
    m = 2
    m_i = 1
    h = 20

    p1 = [0, 0]
    p1_val = [0, 0]
    p2 = [0, 0]
    p2_val = [0, 0]

    if vertical_align == 'top':
        p1[1] = m
        p2[1] = h - m
    elif vertical_align == 'bottom':
        p1[1] = img.shape[0] - h + m
        p2[1] = img.shape[0] - m
    elif vertical_align == 'center':
        p1[1] = img.shape[0] // 2 - h // 2 + m
        p2[1] = img.shape[0] // 2 + h // 2 - m

    p1[0] = m
    p2[0] = img.shape[1] - m

    p1_val[0] = p1[0] + m_i
    p1_val[1] = p1[1] + m_i
    p2_val[0] = int(np.round(m + m_i + (val / absolute * (img.shape[1] - 2 * m - 2 * m_i))))
    p2_val[1] = p2[1] - m_i

    img = add_rectangle(img, p1, p2, opacity=0.5, color=(0.2, 0.2, 0.2))

    img = add_rectangle(img, p1_val, p2_val, opacity=0.8, color=(0.8, 0.4, 0.4))
    img = add_text(img, f'{val / absolute * 100:0.2f}% ({val}|{absolute})', p1, height=h - 2 * m,
                   vertical_align='center', horizontal_align='center', width=img.shape[1],
                   scale=0.3, foreground=(1., 1., 1.))

    return img
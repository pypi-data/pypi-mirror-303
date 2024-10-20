import numpy as np
import cv2

def apply_perspective_transform(image, interpolation='none'):
    """
    Applies a perspective transformation to an image, with options for different interpolation methods.
    
    This function generates a random perspective transformation and applies it to the provided image.
    The transformation maps the corners of the image to new locations based on random perturbations,
    simulating a 3D perspective change. The new image is created by mapping pixels from the original
    image to their new locations according to the transformation matrix.

    The transformation is applied differently based on the interpolation parameter:
    - 'none': No interpolation is used. Pixels are directly mapped from the source to the target
              positions. If a target position does not correspond directly to a source position,
              it is left unfilled, resulting in black areas in the output image.
    - 'full': Nearest neighbor interpolation. Every pixel in the output image is filled. If a
              target pixel's corresponding source pixel is out of bounds, it is filled with the
              nearest valid pixel's value. This ensures there are no black areas in the output.
    - 'inner': Similar to 'full', but only pixels that map directly to valid source positions are
               filled. If a transformed pixel position falls outside the source image, it remains
               black. This method fills the image without extrapolating the transformation beyond
               the original image boundaries.

    Parameters:
    - image (numpy.ndarray): The input image to transform.
    - interpolation (str): The type of interpolation to use ('none', 'full', 'inner').

    Returns:
    - numpy.ndarray: The transformed image with the specified type of interpolation applied.
    """
    h, w = image.shape[:2]
    src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
    perturbation = np.random.uniform(-w/4, w/4, (4, 2))
    dst = src + perturbation
    matrix = compute_perspective_transform(src, dst)
    
    # Create an empty image to place the transformed pixels
    warped_image = np.zeros_like(image)

    if interpolation == 'none':
        # Direct transformation without filling the gaps
        for y in range(h):
            for x in range(w):
                trans_coords = np.array([x, y, 1])
                src_coords = matrix @ trans_coords
                tx, ty, tz = src_coords / src_coords[2]
                if 0 <= int(ty) < h and 0 <= int(tx) < w:
                    warped_image[int(ty), int(tx)] = image[y, x]

    elif interpolation == 'full' or interpolation == 'inner':
        inv_matrix = np.linalg.inv(matrix)
        for y in range(h):
            for x in range(w):
                src_coords = inv_matrix @ np.array([x, y, 1])
                src_x, src_y, src_z = src_coords / src_coords[2]

                src_x, src_y = int(src_x), int(src_y)
                if 0 <= src_y < h and 0 <= src_x < w:
                    warped_image[y, x] = image[src_y, src_x]
                elif interpolation == 'full':
                    nearest_x, nearest_y = min(max(src_x, 0), w - 1), min(max(src_y, 0), h - 1)
                    warped_image[y, x] = image[nearest_y, nearest_x]

    return warped_image

def compute_perspective_transform(src, dst):
    A = np.zeros((8, 9))
    for i in range(4):
        x, y = src[i]
        X, Y = dst[i]
        A[2 * i] = [x, y, 1, 0, 0, 0, -X*x, -X*y, -X]
        A[2 * i + 1] = [0, 0, 0, x, y, 1, -Y*x, -Y*y, -Y]
    B = dst.reshape(8)
    params = np.linalg.solve(A[:, :-1], B)
    params = np.append(params, 1)
    return params.reshape(3, 3)


def multi_lens_distortion(image, num_lenses, radius_range, strength_range):
    """
    Apply a smooth lens distortion effect with multiple lenses to an image.

    Parameters:
        image (np.array): Input image of shape (H, W, C).
        num_lenses (int): Number of lenses to apply.
        radius_range (tuple): A tuple of (min_radius, max_radius) for the lens effect.
        strength_range (tuple): A tuple of (min_strength, max_strength) for the lens effect.

    Returns:
        np.array: Image with multiple lens effects applied.
    """
    H, W, C = image.shape
    # Randomly generate lens centers within the image boundaries.
    cx = np.random.randint(0, W, size=num_lenses)
    cy = np.random.randint(0, H, size=num_lenses)

    # Initialize distorted_image to be the original image.
    # It will be updated as each lens is applied.
    distorted_image = np.copy(image)
    yidx, xidx = np.indices((H, W))

    # Apply each lens.
    for i in range(num_lenses):
        # Randomly select radius and strength for the current lens within the provided ranges.
        radius = np.random.randint(radius_range[0], radius_range[1])
        strength = np.random.uniform(strength_range[0], strength_range[1])

        # Calculate the Euclidean distance to the center of the lens for each point in the image.
        dx = xidx - cx[i]
        dy = yidx - cy[i]
        r = np.sqrt(dx**2 + dy**2)

        # Normalized distance within the lens.
        normalized_r = r / radius

        # Calculate a smooth scaling factor that goes from 1 at the lens center (r=0)
        # to 0 at the lens perimeter (r=radius).
        scaling_factor = np.maximum(1 - normalized_r, 0)

        # Compute the distortion for each point in the image, scaled by the
        # distance to the lens center.
        distorted_y = dy * (1 - strength * scaling_factor) + cy[i]
        distorted_x = dx * (1 - strength * scaling_factor) + cx[i]

        # Ensure the new indices are not out of bounds.
        distorted_y = np.clip(distorted_y, 0, H - 1).astype(int)
        distorted_x = np.clip(distorted_x, 0, W - 1).astype(int)

        # Create the distorted image by mixing original and distorted coordinates.
        distorted_image = distorted_image[distorted_y, distorted_x]

    return distorted_image


def convolve2d(array, kernel):
    output_shape = array.shape
    array_padded = np.pad(array,
                          ((kernel.shape[0]//2, kernel.shape[0]//2),
                           (kernel.shape[1]//2, kernel.shape[1]//2)),
                          mode='constant')
    output_array = np.zeros(output_shape)

    for x in range(array.shape[1]):
        for y in range(array.shape[0]):
            output_array[y, x] = (
                kernel * array_padded[y:y+kernel.shape[0], x:x+kernel.shape[1]]
            ).sum()

    return output_array


def smooth_random_map(rmap, sigma):
    k_size = int(7 * sigma) + 1
    if k_size % 2 == 0:  # Ensure kernel size is odd
        k_size += 1

    blur_kern = np.zeros((k_size, k_size))
    ax = np.arange(-k_size // 2 + 1., k_size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)

    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    kernel = kernel / kernel.sum()

    smooth_map = convolve2d(rmap, kernel)

    return smooth_map


def elastic_transform(image, alpha, sigma):
    random_state = np.random.RandomState(None)

    shape = image.shape
    dx = (random_state.rand(shape[0], shape[1]) * 2 - 1)
    dy = (random_state.rand(shape[0], shape[1]) * 2 - 1)

    dx = smooth_random_map(dx, sigma) * alpha
    dy = smooth_random_map(dy, sigma) * alpha

    x, y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    indices = np.reshape(y+dy, (-1, 1)), np.reshape(x+dx, (-1, 1))

    distorted_image = np.zeros_like(image)
    for k in range(shape[2]):
        for i in range(shape[0]):
            for j in range(shape[1]):
                src_y = min(max(0, int(i + dy[i, j])), shape[0] - 1)
                src_x = min(max(0, int(j + dx[i, j])), shape[1] - 1)
                distorted_image[i, j, k] = image[src_y, src_x, k]

    return distorted_image




def twirl_distortion01(image, center, radius, strength):
    '''
    Apply a twirl distortion effect to an image.

    Parameters:
        image (numpy.ndarray): The input image as a numpy array of shape (height, width, channels).
        center (tuple): The (x, y) coordinates of the twirl center.
        strength (float): The strength of the twirl effect.
        radius (float): The radius within which the twirl effect is applied.

    Returns:
        numpy.ndarray: The distorted image as a numpy array.
    '''
    distorted_image = np.copy(image)

    height, width = image.shape[:2]
    for y in range(height):
        for x in range(width):
            dx = x - center[0]
            dy = y - center[1]
            distance = np.sqrt(dx**2 + dy**2)

            if distance < radius:
                displacement = (radius - distance) / radius
                displacement *= strength

                angle = np.arctan2(dy, dx) + displacement
                nx = center[0] + distance * np.cos(angle)
                ny = center[1] + distance * np.sin(angle)

                nx = min(max(nx, 0), width - 1)
                ny = min(max(ny, 0), height - 1)

                distorted_image[y, x] = image[int(ny), int(nx)]
            else:
                distorted_image[y, x] = image[y, x]

    return distorted_image



def twirl_distortion02(image, center, radius, strength):
    '''
    Apply a twirl distortion effect to an image.

    Parameters:
        image (numpy.ndarray): The input image as a numpy array of shape (height, width, channels).
        center (tuple): The (x, y) coordinates of the twirl center.
        strength (float): The strength of the twirl effect.
        radius (float): The radius within which the twirl effect is applied.

    Returns:
        numpy.ndarray: The distorted image as a numpy array.
    '''
    distorted_image = np.copy(image)

    height, width = image.shape[:2]
    for y in range(height):
        for x in range(width):
            dx = x - center[0]
            dy = y - center[1]
            distance = np.sqrt(dx**2 + dy**2)

            if distance > radius:
                displacement = (radius - distance) / radius
                displacement *= strength
              
                angle = np.arctan2(dy, dx) + displacement
                nx = center[0] + distance * np.cos(angle)
                ny = center[1] + distance * np.sin(angle)

                nx = min(max(nx, 0), width - 1)
                ny = min(max(ny, 0), height - 1)

                distorted_image[y, x] = image[int(ny), int(nx)]
            else:
                distorted_image[y, x] = image[y, x]

    return distorted_image



def wave_distortion01(image, center, amplitude, wavelength):
    '''
    Apply a wave distortion effect to an image.

    Parameters:
    - image (numpy.ndarray): The input image as a numpy array of shape (height, width, channels).
    - center (tuple): The center point (x, y) for the distortion effect, where distortions are minimized.
    - amplitude (float): The amplitude of the wave distortion, controlling the maximum displacement of pixels.
    - wavelength (float): The wavelength of the wave distortion, controlling the frequency of the wave pattern.

    Returns:
    - numpy.ndarray: The distorted image as a numpy array of the same shape as the input image.
    '''

    distorted_image = np.copy(image)

    height, width = image.shape[:2]

    X, Y = np.meshgrid(np.arange(width), np.arange(height))

    distance_from_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)

    epsilon = 1e-5
    distance_from_center += epsilon

    displacement = amplitude * np.sin(2 * np.pi * distance_from_center / wavelength)

    new_X = X + displacement * (X - center[0]) / distance_from_center
    new_Y = Y + displacement * (Y - center[1]) / distance_from_center

    new_X = np.clip(new_X, 0, width - 1).astype(int)
    new_Y = np.clip(new_Y, 0, height - 1).astype(int)

    for channel in range(image.shape[2]):
        distorted_image[new_Y, new_X, channel] = image[Y, X, channel]

    return distorted_image




def wave_distortion02(image, center, amplitude, wavelength):
    '''
    Apply a wave distortion effect to an image.

    Parameters:
    - image (numpy.ndarray): The input image as a numpy array of shape (height, width, channels).
    - center (tuple): The center point (x, y) for the distortion effect, where distortions are minimized.
    - amplitude (float): The amplitude of the wave distortion, controlling the maximum displacement of pixels.
    - wavelength (float): The wavelength of the wave distortion, controlling the frequency of the wave pattern.

    Returns:
    - numpy.ndarray: The distorted image as a numpy array of the same shape as the input image.
    '''
    distorted_image = np.copy(image)

    height, width = image.shape[:2]

    X, Y = np.meshgrid(np.arange(width), np.arange(height))

    distance_from_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)

    epsilon = 1e-5
    distance_from_center += epsilon

    displacement = amplitude * np.tan(2 * np.pi * distance_from_center / wavelength)

    new_X = X + displacement * (X - center[0]) / distance_from_center
    new_Y = Y + displacement * (Y - center[1]) / distance_from_center

    new_X = np.clip(new_X, 0, width - 1).astype(int)
    new_Y = np.clip(new_Y, 0, height - 1).astype(int)

    for channel in range(image.shape[2]):
        distorted_image[new_Y, new_X, channel] = image[Y, X, channel]

    return distorted_image


def wave_distortion(image, amplitude=20, frequency=10):
    '''
    Applies a wave distortion effect to an input image.

    Parameters:
    - image (numpy.ndarray): The input image as a 3D numpy array (H x W x C).
    - amplitude (int): The amplitude of the wave distortion. Higher values result in more pronounced waves.
    - frequency (int): The frequency of the wave distortion. Higher values result in more waves.

    Returns:
    - numpy.ndarray: The distorted image as a 3D numpy array (H x W x C).
    '''
    distorted_image = np.zeros_like(image)

    height, width = image.shape[:2]

    for y in range(height):
        for x in range(width):
            dx = int(amplitude * np.sin(2 * np.pi * y / frequency))

            new_x = x + dx
            if new_x < 0:
                new_x = 0
            if new_x >= width:
                new_x = width - 1
              
            distorted_image[y, x] = image[y, new_x]

    return distorted_image




def pixelate_image(image, pixelation_level, region=None):
    '''
    Apply a pixelation distortion to an image.

    Parameters:
    - image (numpy.ndarray): The input image as a numpy array of shape (height, width, channels).
    - pixelation_level (int): The size of the squares used to pixelate the image. Higher values increase the pixelation effect.
    - region (tuple, optional): A tuple specifying the region to pixelate in the format (start_row, start_col, end_row, end_col).
      If None, the entire image is pixelated.

    Returns:
    - numpy.ndarray: The pixelated image as a numpy array of the same shape as the input image.
    '''

    pixelated_image = np.copy(image)

    if region is None:
        region = (0, 0, image.shape[0], image.shape[1])

    start_row, start_col, end_row, end_col = region

    pixelation_level = min(pixelation_level, end_row - start_row, end_col - start_col)

    for row in range(start_row, end_row, pixelation_level):
        for col in range(start_col, end_col, pixelation_level):
            row_end = min(row + pixelation_level, end_row)
            col_end = min(col + pixelation_level, end_col)

            block_average = np.mean(pixelated_image[row:row_end, col:col_end], axis=(0, 1)).astype(int)

            pixelated_image[row:row_end, col:col_end] = block_average

    return pixelated_image





def cartesian_to_polar_image_stretched(image, center=None):
    """
    Transforms an image from Cartesian to polar coordinates, stretching the pixels
    to cover the whole space.

    Parameters:
    - image: numpy.ndarray, the input image as a 2D or 3D array.
    - center: tuple of int, the center of the polar transformation (x, y).

    Returns:
    - polar_image: numpy.ndarray, the transformed image in polar coordinates.
    """
    if center is None:
        center = (image.shape[1] // 2, image.shape[0] // 2)

    height, width = image.shape[:2]
    max_radius = np.hypot(*[dim//2 for dim in [width, height]])

    polar_height = int(max_radius)
    polar_width = 360


    polar_image = np.zeros((polar_height, polar_width, *image.shape[2:]), dtype=image.dtype)

    for r in range(polar_height):
        for theta in range(polar_width):
            angle = np.deg2rad(theta)
            # Scale radius to fit the polar image height
            radius = float(r) / polar_height * max_radius
            x = int(center[0] + radius * np.cos(angle))
            y = int(center[1] + radius * np.sin(angle))

            # Check if (x, y) lies inside the original image boundaries
            if 0 <= x < width and 0 <= y < height:
                polar_image[r, theta] = image[y, x]

    return polar_image




def mirror_effect(image, direction='horizontal', mirror_line_position=None, side='left'):
    '''
    Apply a mirroring effect to an image based on the specified side of a mirror line.

    Parameters:
    - image (numpy.ndarray): The input image as a numpy array of shape (height, width, channels).
    - direction (str): The direction of the mirroring effect. Can be 'horizontal' or 'vertical'.
    - mirror_line_position (int, optional): The position of the mirror line.
        For horizontal direction, it's the column index.
        For vertical direction, it's the row index.
        If None, the mirror line will be at the center of the corresponding dimension.
    - side (str): The side of the mirror line to be mirrored.
        For 'horizontal' direction, can be 'left' or 'right'.
        For 'vertical' direction, can be 'top' or 'bottom'.

    Returns:
    - numpy.ndarray: The distorted image with the mirroring effect applied.

    Notes:
    - The function makes a copy of the original image and then applies the mirroring effect.
    - The displacement calculation and pixel replacement are done without using external libraries other than numpy.
    '''

    distorted_image = np.copy(image)

    if mirror_line_position is None:
        if direction == 'horizontal':
            mirror_line_position = image.shape[1] // 2
        else:  # vertical
            mirror_line_position = image.shape[0] // 2

    if direction == 'horizontal':
        if side == 'left':
            if mirror_line_position > 0 and mirror_line_position < image.shape[1]:
                for col in range(mirror_line_position):
                    mirrored_col = 2 * mirror_line_position - col - 1
                    if mirrored_col < image.shape[1]:
                        distorted_image[:, mirrored_col, :] = image[:, col, :]
        else:  # right side
            for col in range(mirror_line_position, image.shape[1]):
                mirrored_col = 2 * mirror_line_position - col - 1
                if mirrored_col >= 0:
                    distorted_image[:, mirrored_col, :] = image[:, col, :]
    else:  # Vertical mirroring
        if side == 'top':
            for row in range(mirror_line_position):
                mirrored_row = 2 * mirror_line_position - row - 1
                if mirrored_row < image.shape[0]:
                    distorted_image[mirrored_row, :, :] = image[row, :, :]
        else:  # bottom side
            for row in range(mirror_line_position, image.shape[0]):
                mirrored_row = 2 * mirror_line_position - row - 1
                if mirrored_row >= 0:
                    distorted_image[mirrored_row, :, :] = image[row, :, :]

    return distorted_image




def tilt_shift_effect(image, focus_start, focus_end, blur_strength, transition_width):
    '''
    Apply a vertical tilt-shift effect to an image with a smooth transition between focused and blurred areas.

    Parameters:
    - image (numpy.ndarray): The input image as a 3D numpy array of shape (height, width, channels).
    - focus_start (float): The starting position (between 0 and 1) of the in-focus region, relative to the image height.
    - focus_end (float): The ending position (between 0 and 1) of the in-focus region, relative to the image height.
    - blur_strength (int): The strength of the blur effect outside the in-focus region.
    - transition_width (float): The width of the transition region (between 0 and 1), relative to the image height,
                                where the blur smoothly increases to its maximum strength.

    Returns:
    - numpy.ndarray: The image with the tilt-shift effect applied.
    '''

    if not (0 <= focus_start < focus_end <= 1):
        raise ValueError("focus_start must be less than focus_end, and both must be between 0 and 1.")
    if blur_strength < 1:
        raise ValueError("blur_strength must be a positive integer.")
    if not (0 < transition_width <= 1):
        raise ValueError("transition_width must be between 0 and 1.")

    height = image.shape[0]
    focus_start_px = int(height * focus_start)
    focus_end_px = int(height * focus_end)
    transition_height_px = int(height * transition_width / 2)

    blurred_image = np.copy(image)

    for y in range(height):
        if y < focus_start_px - transition_height_px or y > focus_end_px + transition_height_px:
            # Full blur outside transition regions
            dynamic_strength = blur_strength
        elif focus_start_px - transition_height_px <= y <= focus_start_px:
            # Gradual increase in blur strength approaching the focus region from above
            dynamic_strength = int(blur_strength * (focus_start_px - y) / transition_height_px)
        elif focus_end_px < y <= focus_end_px + transition_height_px:
            # Gradual increase in blur strength moving away from the focus region below
            dynamic_strength = int(blur_strength * (y - focus_end_px) / transition_height_px)
        else:
            dynamic_strength = 0

        for x in range(image.shape[1]):
            if dynamic_strength > 0:
                x_start = max(0, x - dynamic_strength)
                x_end = min(image.shape[1], x + dynamic_strength + 1)
                y_start = max(0, y - dynamic_strength)
                y_end = min(height, y + dynamic_strength + 1)

                blurred_image[y, x] = np.mean(image[y_start:y_end, x_start:x_end], axis=(0, 1))

    return blurred_image


def ripple_effect(image, amplitude=3, wavelength=7):
    '''
    Applies a ripple effect to the input image.

    Parameters:
    - image: np.array
      A numpy array representing the input image. It should be a 3D array with dimensions (height, width, channels).
    - amplitude: int, optional
      The maximum displacement of the ripple in pixels. Default is 20.
    - wavelength: int, optional
      The distance between wave peaks in pixels. Default is 10.

    Returns:
    - np.array
      The distorted image as a numpy array with the same shape as the input.
    '''

    output_image = np.copy(image)

    height, width, channels = image.shape

    X, Y = np.meshgrid(np.arange(width), np.arange(height))

    displacement_X = amplitude * np.sin(2 * np.pi * Y / wavelength)
    displacement_Y = amplitude * np.cos(2 * np.pi * X / wavelength)

    new_X = X + displacement_X
    new_Y = Y + displacement_Y

    new_X = np.clip(new_X, 0, width - 1).astype(int)
    new_Y = np.clip(new_Y, 0, height - 1).astype(int)

    for channel in range(channels):
        output_image[:, :, channel] = image[new_Y, new_X, channel]

    return output_image



def zoom_blur(image, center, intensity=0.1, blend=0.5):
    intensity = max(min(intensity, 1.0), 0.0)
    blend = max(min(blend, 1.0), 0.0)

    original_image = image.copy()
    height, width, _ = original_image.shape
    distorted_image = np.zeros_like(original_image)

    for y in range(height):
        for x in range(width):
            dy, dx = center[1] - y, center[0] - x
            distance = np.sqrt(dx**2 + dy**2)
            vector = np.array([dx, dy])

            if distance == 0:
                continue

            displacement = vector * intensity

            new_y = int(y + displacement[1])
            new_x = int(x + displacement[0])

            new_y = np.clip(new_y, 0, height-1)
            new_x = np.clip(new_x, 0, width-1)

            distorted_image[y, x] = original_image[new_y, new_x]

    output_image = cv2.addWeighted(original_image, 1-blend, distorted_image, blend, 0)

    return output_image





def space_distortion_v1(image, direction=(1, 1)):
    '''
    Applies a "Space Distortion" effect to an image using NumPy.

    Parameters:
    - image: numpy.ndarray
        The input image as a NumPy array of shape (height, width, channels).
    - direction: tuple of int
        The direction vector of the effect. For example, (1, 0) for right,
        (-1, 0) for left, (0, 1) for down, and (0, -1) for up.

    Returns:
    - distorted_image: numpy.ndarray
        The output image with the "Space Distortion" effect applied.
    '''

    distorted_image = np.copy(image)

    height, width, channels = image.shape
    dx, dy = direction

    distortion_strength = np.random.randint(1, 15)
    distortion_scale = max(width, height) // np.random.randint(10, 30)

    for x in range(0, width, distortion_scale):
        for y in range(0, height, distortion_scale):
            end_x = x + distortion_scale
            end_y = y + distortion_scale

            if end_x > width:
                end_x = width
            if end_y > height:
                end_y = height

            for channel in range(channels):
                displacement = np.random.randint(-distortion_strength, distortion_strength)
                if dx != 0:  # Horizontal distortion
                    distorted_image[y:end_y, x:end_x, channel] = np.roll(
                        distorted_image[y:end_y, x:end_x, channel], shift=dx*displacement, axis=1)
                if dy != 0:  # Vertical distortion
                    distorted_image[y:end_y, x:end_x, channel] = np.roll(
                        distorted_image[y:end_y, x:end_x, channel], shift=dy*displacement, axis=0)

    return distorted_image


def wind_distortion(image, direction=(0, 1), strength=5, randomness=0.5):
    """
    Applies a "Wind Distortion" effect to an image, with randomness affecting different parts differently.

    Parameters:
    - image: np.array. The original image array in HxWxC format (Height x Width x Channels).
    - direction: tuple. The direction vector for distortion as (dx, dy).
    - strength: int. The strength of the distortion effect.
    - randomness: float. Factor controlling the variability of the effect across the image.

    Returns:
    - np.array: The distorted image.

    This function creates a distortion effect where random parts of the image are shifted more than others,
    simulating a wind-like movement across the image.
    """
    distorted_image = np.copy(image)

    height, width, channels = image.shape
    dx, dy = direction
    random_map = np.random.rand(height, width) * randomness * strength

    for channel in range(channels):
        for i in range(height):
            for j in range(width):
                rand_strength_i = int(dy * random_map[i, j])
                rand_strength_j = int(dx * random_map[i, j])

                new_i = (i + rand_strength_i) % height
                new_j = (j + rand_strength_j) % width

                distorted_image[i, j, channel] = image[new_i, new_j, channel]

    return distorted_image


def squeeze_stretch_effect(image, segments=7, max_stretch_factor=3.0, max_squeeze_factor=2.5):
    '''
    Apply a more pronounced "Squeeze and Stretch" effect to an image, targeting specific segments.

    Parameters:
    - image: np.ndarray
        The input image as a NumPy array of shape (height, width, channels).
    - segments: int
        The number of segments to apply the distortion effect to. Default is 4.
    - max_stretch_factor: float
        The maximum factor by which segments of the image will be stretched. Default is 2.0.
    - max_squeeze_factor: float
        The maximum factor by which segments of the image will be squeezed (must be less than 1). Default is 0.5.

    Returns:
    - distorted_image: np.ndarray
        The output image with the "Squeeze and Stretch" effect applied, as a NumPy array of the same shape as the input.
    '''
    distorted_image = image.copy()
    height, width, _ = image.shape

    direction = np.random.choice([0, 1])

    segment_size = (height if direction == 0 else width) // segments

    for i in range(segments):
        if direction == 0:  # Vertical direction
            start = i * segment_size
            end = min((i + 1) * segment_size, height)
            segment = distorted_image[start:end, :, :]
        else:  # Horizontal direction
            start = i * segment_size
            end = min((i + 1) * segment_size, width)
            segment = distorted_image[:, start:end, :]

        if np.random.rand() > 0.5:
            factor = np.random.uniform(1, max_stretch_factor)
        else:
            factor = np.random.uniform(max_squeeze_factor, 1)

        distorted_segment = np.repeat(segment, factor, axis=0 if direction == 0 else 1)

        if direction == 0:  # Vertical adjustment
            end_fit = start + distorted_segment.shape[0]
            distorted_image[start:end_fit, :, :] = distorted_segment[:min(distorted_segment.shape[0], height-start), :, :]
        else:  # Horizontal adjustment
            end_fit = start + distorted_segment.shape[1]
            distorted_image[:, start:end_fit, :] = distorted_segment[:, :min(distorted_segment.shape[1], width-start), :]

    if direction == 0:
        distorted_image = distorted_image[:height, :, :]
    else:
        distorted_image = distorted_image[:, :width, :]

    return distorted_image



def smooth_lens_distortion(image, cx, cy, radius, strength):
    """
    Apply a smooth lens distortion effect to an image.

    Parameters:
        image (np.array): Input image of shape (H, W, C).
        cx, cy (int): The center of the lens.
        radius (int): The radius of the lens effect.
        strength (float): Strength of the lens effect.

    Returns:
        np.array: Image with lens effect applied.
    """
    distorted_image = np.zeros_like(image)
    yidx, xidx = np.indices((image.shape[0], image.shape[1]))

    dx = xidx - cx
    dy = yidx - cy
    r = np.sqrt(dx**2 + dy**2)

    normalized_r = r / radius
    scaling_factor = np.maximum(1 - normalized_r, 0)
  
    distorted_y = dy * (1 - strength * scaling_factor) + cy
    distorted_x = dx * (1 - strength * scaling_factor) + cx
    distorted_y = np.clip(distorted_y, 0, image.shape[0]-1).astype(int)
    distorted_x = np.clip(distorted_x, 0, image.shape[1]-1).astype(int)

    distorted_image = image[distorted_y, distorted_x]

    return distorted_image





def crystallize_distortion(image, crystal_size=10):
    '''
    Apply a crystallize distortion effect to an image using NumPy.

    Parameters:
    - image: numpy.ndarray
        The input image to be distorted, with shape (height, width, channels).
    - crystal_size: int
        The size of the "crystals" or blocks for the distortion effect.

    Returns:
    - distorted_image: numpy.ndarray
        The distorted image with the crystallize effect applied.
    '''

    img_copy = np.copy(image)

    height, width, channels = img_copy.shape

    for y in range(0, height, crystal_size):
        for x in range(0, width, crystal_size):
            y_end = min(y + crystal_size, height)
            x_end = min(x + crystal_size, width)
            block_average = img_copy[y:y_end, x:x_end].mean(axis=(0, 1), keepdims=True)
            img_copy[y:y_end, x:x_end] = block_average

    return img_copy




def honeycomb_distortion(image):
    '''Apply a honeycomb distortion effect to an image.

    Parameters:
    - image: np.ndarray, the original image array of shape (H, W, C) where
      H is height, W is width, and C is the number of color channels.

    Returns:
    - distorted_image: np.ndarray, the distorted image array with the same shape as the input.
    '''
    distorted_image = np.copy(image)
    height, width, channels = image.shape
    Y, X = np.indices((height, width))
    scale = 10
    intensity = 5
  
    X_distorted = X + np.sin(Y / scale) * intensity
    Y_distorted = Y + np.sin(X / scale) * intensity

    X_distorted = np.clip(X_distorted, 0, width - 1).astype(int)  # Changed np.int to int
    Y_distorted = np.clip(Y_distorted, 0, height - 1).astype(int)  # Changed np.int to int

    for c in range(channels):
        distorted_image[:, :, c] = image[Y_distorted, X_distorted, c]

    return distorted_image



def moving_blur(image, num_echoes, alpha_step, offset_step):
    '''
    Applies a "Moving Blur" effect to an input image with customizable parameters.

    Parameters:
        image (np.ndarray): The input image as a NumPy array of shape (H, W, C) where H is height,
                            W is width, and C is the number of channels (typically 3 for RGB).
        num_echoes (int): Number of echoes to apply.
        alpha_step (float): Step decrease in alpha for each echo. Determines the transparency of each echo.
        offset_step (int): Pixel offset for each echo. Determines how far each echo is staggered from the original.

    Returns:
        np.ndarray: The output image with the "Moving Blur" effect applied.
    '''

    # Ensure working on a copy of the image to preserve the original
    output_image = np.copy(image)

    # Loop over the echoes
    for i in range(1, num_echoes + 1):
        alpha = 1 - (i * alpha_step)  # Calculate the alpha (transparency) for this echo
        offset = i * offset_step  # Calculate the pixel offset for this echo

        # Create the staggered duplicate with the offset
        echo = np.zeros_like(output_image)
        if offset < output_image.shape[0] and offset < output_image.shape[1]:
            # Apply the offset only if it is within the image dimensions
            echo[offset:, offset:, :] = output_image[:-offset, :-offset, :]  # Offset the echo

            # Blend the echo back into the output image with the calculated alpha
            output_image = np.clip((1 - alpha) * output_image + alpha * echo, 0, 255).astype(np.uint8)

    return output_image


def warp_bubbles_effect(image, centers, radius, intensity):
    '''
    Applies a "warp bubbles" effect to an image.

    Parameters:
    - image: np.ndarray. The original image as a NumPy array of shape (H, W, C).
    - centers: list of tuples. Each tuple contains the (x, y) coordinates of the center of a bubble.
    - radius: int. The radius of the bubbles.
    - intensity: float. The intensity of the distortion effect.

    Returns:
    - np.ndarray. The image with the "warp bubbles" effect applied.
    '''

    # Ensure we work on a copy of the image to not alter the original
    output_image = np.copy(image)
    height, width = image.shape[:2]

    for center in centers:
        for y in range(height):
            for x in range(width):
                # Calculate the distance from the current pixel to the center of the bubble
                distance = np.sqrt((x - center[0])**2 + (y - center[1])**2)

                if distance < radius:
                    # Calculate the displacement based on the distance and intensity
                    displacement = (1 - distance / radius) ** 2 * intensity

                    # Calculate the source pixel position based on the displacement
                    source_x = int(x + displacement * (x - center[0]))
                    source_y = int(y + displacement * (y - center[1]))

                    # Clamp the source position to be within the image bounds
                    source_x = np.clip(source_x, 0, width - 1)
                    source_y = np.clip(source_y, 0, height - 1)

                    # Apply the displacement
                    output_image[y, x] = image[source_y, source_x]

    return output_image


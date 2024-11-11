from PIL import Image, ImageOps

def resize_image_for_id(photo_path, output_path, size='1inch'):
    # 定义一寸和两寸的标准尺寸，单位是像素 (根据标准证件照的300 DPI)
    sizes = {
        '1inch': (295, 413),  # 一寸照片尺寸：2.5x3.5 厘米（295x413 像素）
        '2inch': (413, 579),  # 两寸照片尺寸：3.5x4.9 厘米（413x579 像素）
    }
    
    # 检查用户输入的尺寸是否有效
    if size not in sizes:
        raise ValueError("Invalid size. Choose '1inch' or '2inch'")
    
    target_size = sizes[size]
    
    # 打开原始图片
    with Image.open(photo_path) as img:
        # # 按比例缩放，确保照片长宽比不变
        # img.thumbnail(target_size, Image.ANTIALIAS)
        
        # 使用 ImageOps.fit 将图片缩放和裁剪为完全覆盖目标尺寸
        img_resized = ImageOps.fit(img, target_size, Image.ANTIALIAS)

        # 保存调整后的图片
        img_resized.save(output_path)
        print(f"照片已成功裁剪并完全覆盖至 {target_size} 尺寸（无畸变）并保存到 {output_path}")
        

# 使用示例：
# 将路径 "input_photo.jpg" 的照片调整为一寸，并保存为 "output_1inch.jpg"
resize_image_for_id("input_photo.jpg", "output_1inch.jpg", size='1inch')

# 将路径 "input_photo.jpg" 的照片调整为两寸，并保存为 "output_2inch.jpg"
resize_image_for_id("input_photo.jpg", "output_2inch.jpg", size='2inch')

from typing import List, Union, Tuple
import os, fitz, shutil
from concurrent.futures import ThreadPoolExecutor
from ..information import gain
from ..path import paths
from other._convert_main import convert_main
from ._unit import *
from PIL import Image
from io import BytesIO

def ConvertPdf(
        img_paths: List[str],
        output_path: str,
        page_size: Tuple[Union[int, float], Union[int, float]] = A4,
        merge: bool = False,
        process: bool = True,
        max_workers: int = 10,
        dpi: int = 300
) -> None:
    """
    Converts a list of images to a PDF file with optional processing and merging.
    将图像列表转换为PDF文件，可选处理和合并功能。

    Args:
        img_paths (List[str]): List of image paths. 图像路径列表。
        output_path (str): Path to save the output PDF file. 保存输出PDF文件的路径。
        page_size (Tuple[Union[int, float], Union[int, float]], optional): Size of each page in the PDF. Defaults to A4. PDF中每页的大小，默认为A4。
        merge (bool, optional): If True, merges all images into a single PDF. Defaults to False. 如果为True，将所有图像合并为一个PDF，默认为False。
        process (bool, optional): If True, processes each image (resizing and resampling). Defaults to True. 如果为True，处理每个图像（调整大小和重采样），默认为True。
        max_workers (int, optional): Maximum number of worker threads. Defaults to 10. 最大工作线程数，默认为10。
        dpi (int, optional): Resolution of the images. Defaults to 300. 图像的分辨率，默认为300。

    Returns:
        None
    """

    def convert_and_process(img_path: str, page_size: Tuple[Union[int, float], Union[int, float]], process: bool,
                            dpi: int) -> Tuple[BytesIO, dict]:
        """
        Converts and processes a single image.
        转换并处理单个图像。

        Args:
            img_path (str): Path to the image file. 图像文件的路径。
            page_size (Tuple[Union[int, float], Union[int, float]]): Size of the page. 页面的大小。
            process (bool): If True, processes the image. 如果为True，处理图像。
            dpi (int): Resolution of the image. 图像的分辨率。

        Returns:
            Tuple[BytesIO, dict]: Processed image as a BytesIO object and image metadata. 处理后的图像作为BytesIO对象和图像元数据。
        """
        with Image.open(img_path) as orign_img:
            img = orign_img.copy()

        img = img.convert('RGBA')

        if process:
            document_dpi = img.info.get("dpi", (dpi, dpi))
            scale = dpi / document_dpi[0]
            resample = Image.Resampling.LANCZOS if scale <= 1 else Image.Resampling.BICUBIC
            img = img.resize((int(img.size[0] * scale), int(img.size[1] * scale)), resample)

        width, height = img.size
        if width > height:
            page_size = page_size[1], page_size[0]

        page_width, page_height = page_size
        scale_factor = min(page_width / width, page_height / height)
        final_size = int(width * scale_factor), int(height * scale_factor)
        x_offset = (page_width - final_size[0]) / 2
        y_offset = (page_height - final_size[1]) / 2

        rect = fitz.Rect(x_offset, y_offset, x_offset + final_size[0], y_offset + final_size[1])
        img_info = {'index': img_paths.index(img_path), 'page_size': page_size, 'rect': rect}
        img_info.update(img.info)

        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        img.close()

        return img_byte_arr, img_info

    def save_pdf(img_byte_arr: BytesIO, info: dict, output_path: str) -> str:
        """
        Saves a single image to a PDF file.
        将单个图像保存为PDF文件。

        Args:
            img_byte_arr (BytesIO): Processed image as a BytesIO object. 处理后的图像作为BytesIO对象。
            info (dict): Image metadata. 图像元数据。
            output_path (str): Path to save the output PDF file. 保存输出PDF文件的路径。

        Returns:
            str: Path to the saved PDF file. 保存的PDF文件路径。
        """
        pdf_document = fitz.open()
        page_width, page_height = info['page_size']
        rect = info['rect']
        index = info['index']

        page = pdf_document._newPage(width=page_width, height=page_height)
        page.insert_image(rect, stream=img_byte_arr)

        pdf_path = os.path.join(output_path, f'{index}.pdf')
        pdf_document.save(pdf_path)
        pdf_document.close()
        return pdf_path

    def merge_pdfs(output_path: str, input_paths: List[str]) -> None:
        """
        Merges multiple PDF files into a single PDF file.
        将多个PDF文件合并为一个PDF文件。

        Args:
            output_path (str): Path to save the merged PDF file. 保存合并后PDF文件的路径。
            input_paths (List[str]): List of PDF file paths to merge. 要合并的PDF文件路径列表。

        Returns:
            None
        """
        merged_pdf = fitz.open()
        for input_path in input_paths:
            with fitz.open(input_path) as pdf_document:
                merged_pdf.insert_pdf(pdf_document)
        merged_pdf.save(output_path)
        merged_pdf.close()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        image_datas = list(
            executor.map(lambda img_path: convert_and_process(img_path, page_size, process, dpi), img_paths))

    image_datas.sort(key=lambda x: x[1]['index'])

    temp_dir = os.path.join(os.path.dirname(output_path), 'temp')
    os.makedirs(temp_dir, exist_ok=True)

    if merge:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            pdf_paths = list(executor.map(lambda img_data: save_pdf(img_data[0], img_data[1], temp_dir), image_datas))
        merge_pdfs(output_path, pdf_paths)
    else:
        pdf_document = fitz.open()
        for img_data in image_datas:
            page_width, page_height = img_data[1]['page_size']
            rect = img_data[1]['rect']
            page = pdf_document._newPage(width=page_width, height=page_height)
            page.insert_image(rect, stream=img_data[0])
        pdf_document.save(output_path)
        pdf_document.close()

    shutil.rmtree(temp_dir)
def ConvertImage(pdf_path: str, output_dir: str, dpi: int = 300, image_format: str = "png",
                  max_workers: int = 8) -> None:
    """
    Converts PDF pages to images and sets image DPI.
    将PDF页面转换为图像并设置图像DPI。

    Args:
        pdf_path (str): Path to the PDF file. PDF文件的路径。
        output_dir (str): Directory to save the output images. 保存输出图像的目录。
        dpi (int, optional): Resolution of the output images. Defaults to 300. 输出图像的分辨率，默认为300。
        image_format (str, optional): Format of the output images (e.g., "png", "jpeg"). Defaults to "png". 输出图像的格式（例如，"png", "jpeg"），默认为 "png"。
        max_workers (int, optional): Maximum number of worker threads. Defaults to 8. 最大工作线程数，默认为8。
    """
    os.makedirs(output_dir, exist_ok=True)

    def set_image_dpi(image_path: str) -> None:
        """
        Sets the DPI of an image.
        设置图像的DPI。

        Args:
            image_path (str): Path to the image file. 图像文件的路径。
        """
        with Image.open(image_path) as img:
            img.save(image_path, dpi=(dpi, dpi))

    def process_pdf_page(doc: fitz.Document, page_num: int) -> None:
        """
        Processes a single PDF page and saves it as an image.
        处理单个PDF页面并将其保存为图像。

        Args:
            doc (fitz.Document): The PDF document object. PDF文档对象。
            page_num (int): The page number to process. 要处理的页面编号。
        """
        pixmap = doc.load_page(page_num).get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
        image_path = os.path.join(output_dir, f"page_{page_num + 1}.{image_format}")
        pixmap.save(image_path)
        set_image_dpi(image_path)

    with fitz.open(pdf_path) as doc:
        total_pages = len(doc)
        page_ranges = [(i, min(i + max_workers, total_pages)) for i in range(0, total_pages, max_workers)]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for start, end in page_ranges:
                executor.map(lambda page_num: process_pdf_page(doc, page_num), range(start, end))
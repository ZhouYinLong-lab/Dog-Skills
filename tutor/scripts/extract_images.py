#!/usr/bin/env python3
"""从 PDF 指定区域提取图片。

用法：
    python extract_images.py <pdf_path> <page_num> <x0> <y0> <x1> <y1> <output_path>

参数：
    pdf_path   : PDF 文件路径
    page_num   : 页码（从 1 开始）
    x0, y0     : 裁剪区域左上角坐标（单位：pt，PDF 坐标系）
    x1, y1     : 裁剪区域右下角坐标（单位：pt，PDF 坐标系）
    output_path: 输出图片路径（支持 .png / .jpg）

依赖：
    pip install pymupdf  （推荐，速度快）
    或
    pip install pdf2image pillow  （备选）

示例：
    python extract_images.py textbook.pdf 42 100 200 400 500 output/assets/ch05/fig_01.png

    # 提取整页（不推荐，仅用于预览定位）：
    python extract_images.py textbook.pdf 42 --full-page preview.png
"""

import sys
import os

PDF_COORD_SCALE = 2.0  # 渲染分辨率缩放因子


def extract_with_pymupdf(pdf_path, page_num, x0, y0, x1, y1, output_path):
    """使用 PyMuPDF (fitz) 提取指定区域。"""
    import fitz  # pip install pymupdf

    doc = fitz.open(pdf_path)
    if page_num < 1 or page_num > len(doc):
        doc.close()
        raise ValueError(f"页码 {page_num} 超出范围（1-{len(doc)}）")

    page = doc[page_num - 1]
    rect = fitz.Rect(x0, y0, x1, y1)
    mat = fitz.Matrix(PDF_COORD_SCALE, PDF_COORD_SCALE)

    pix = page.get_pixmap(matrix=mat, clip=rect)
    pix.save(output_path)
    doc.close()

    w, h = pix.width, pix.height
    print(f"[OK] 已提取 (PyMuPDF)：{output_path}（{w}x{h} px）")


def extract_with_pdf2image(pdf_path, page_num, x0, y0, x1, y1, output_path):
    """使用 pdf2image + PIL 提取指定区域。"""
    from pdf2image import convert_from_path
    from PIL import Image

    images = convert_from_path(
        pdf_path,
        first_page=page_num,
        last_page=page_num,
        dpi=int(72 * PDF_COORD_SCALE),
    )
    if not images:
        raise RuntimeError(f"无法从 {pdf_path} 第 {page_num} 页渲染图像")

    img = images[0]
    # pdf2image 的坐标原点在左上角，需要翻转 y 轴
    page_height_pt = img.height / PDF_COORD_SCALE
    y0_px = int((page_height_pt - y1) * PDF_COORD_SCALE)
    y1_px = int((page_height_pt - y0) * PDF_COORD_SCALE)
    x0_px = int(x0 * PDF_COORD_SCALE)
    x1_px = int(x1 * PDF_COORD_SCALE)

    cropped = img.crop((x0_px, y0_px, x1_px, y1_px))
    cropped.save(output_path)
    print(f"[OK] 已提取 (pdf2image)：{output_path}（{cropped.width}x{cropped.height} px）")


def extract_full_page(pdf_path, page_num, output_path):
    """导出整页（仅用于定位预览，不用于正式图片）。"""
    try:
        import fitz
        doc = fitz.open(pdf_path)
        page = doc[page_num - 1]
        mat = fitz.Matrix(PDF_COORD_SCALE, PDF_COORD_SCALE)
        pix = page.get_pixmap(matrix=mat)
        pix.save(output_path)
        doc.close()
        print(f"[OK] 整页预览：{output_path}（{pix.width}x{pix.height} px）")
        print("[WARN] 整页导出仅用于定位预览，正式图片请指定裁剪坐标。")
    except ImportError:
        from pdf2image import convert_from_path
        images = convert_from_path(
            pdf_path, first_page=page_num, last_page=page_num, dpi=150
        )
        images[0].save(output_path)
        print(f"[OK] 整页预览：{output_path}")
        print("[WARN] 整页导出仅用于定位预览，正式图片请指定裁剪坐标。")


def list_page_images(pdf_path, page_num):
    """列出 PDF 页面中嵌入的所有图像及其位置（用于定位）。"""
    try:
        import fitz
        doc = fitz.open(pdf_path)
        page = doc[page_num - 1]
        images = page.get_images(full=True)

        if not images:
            print(f"第 {page_num} 页没有嵌入图像。")
        else:
            print(f"第 {page_num} 页共有 {len(images)} 个嵌入图像：")
            for idx, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                w, h = base_image["width"], base_image["height"]
                # 获取图像在页面上的位置
                rects = page.get_image_rects(img)
                for r_idx, rect in enumerate(rects):
                    print(
                        f"  [{idx}] {w}x{h} px "
                        f"位置: ({rect.x0:.0f}, {rect.y0:.0f}) → "
                        f"({rect.x1:.0f}, {rect.y1:.0f})"
                    )

        doc.close()
    except ImportError:
        print("[ERROR] 需要安装 pymupdf：pip install pymupdf")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.exists(pdf_path):
        print(f"[ERROR] PDF 文件不存在：{pdf_path}")
        sys.exit(1)

    # --list mode
    if len(sys.argv) == 3 and sys.argv[2] == '--list':
        print("[ERROR] --list 需要指定页码，例如：python extract_images.py book.pdf 5 --list")
        sys.exit(1)

    if len(sys.argv) >= 4 and sys.argv[3] == '--list':
        page_num = int(sys.argv[2])
        list_page_images(pdf_path, page_num)
        sys.exit(0)

    # --full-page mode
    if len(sys.argv) >= 4 and sys.argv[2] == '--full-page':
        page_num = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        output_path = sys.argv[4] if len(sys.argv) > 4 else 'full_page.png'
        extract_full_page(pdf_path, page_num, output_path)
        sys.exit(0)

    # Crop mode: page x0 y0 x1 y1 output
    if len(sys.argv) < 8:
        print("[ERROR] 参数不足。用法：python extract_images.py <pdf> <page> <x0> <y0> <x1> <y1> <output>")
        sys.exit(1)

    page_num = int(sys.argv[2])
    x0, y0, x1, y1 = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
    output_path = sys.argv[7]

    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Try pymupdf first, fallback to pdf2image
    try:
        import fitz
        extract_with_pymupdf(pdf_path, page_num, x0, y0, x1, y1, output_path)
    except ImportError:
        try:
            extract_with_pdf2image(pdf_path, page_num, x0, y0, x1, y1, output_path)
        except ImportError:
            print("[ERROR] 需要安装以下任一依赖：")
            print("  pip install pymupdf")
            print("  或")
            print("  pip install pdf2image pillow")
            sys.exit(1)


if __name__ == '__main__':
    main()

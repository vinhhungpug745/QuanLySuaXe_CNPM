from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import current_app
from app.utils.calc_total_repairform import calc_total_VAT
import app.dao.dao as dao
import os

def export_receipt_pdf(receipt):
    font_bath=os.path.join(current_app.root_path,"fonts","DejaVuSans.ttf")
    pdfmetrics.registerFont(TTFont("DejaVuSans", font_bath))
    folder = os.path.join(current_app.root_path, "static/invoices")
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, f"receipt_{receipt.id}.pdf")

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    elements = []

    rf = receipt.repair_forms[0]
    reception = rf.reception_form

    # ===== TIÊU ĐỀ =====
    title = Paragraph(
        f"<b>HÓA ĐƠN SỬA CHỮA #{receipt.id}</b>",
        ParagraphStyle(
            name="Title",
            fontSize=16,
            fontName="DejaVuSans",
            alignment=1,  # center
            spaceAfter=20
        )
    )

    info_style = ParagraphStyle(
        name="Normal",
        fontName="DejaVuSans"
    )

    elements.append(title)

    # ===== THÔNG TIN CHUNG =====
    elements.append(Paragraph(f"<b>Phiếu #:</b> {receipt.id}", info_style))
    elements.append(Paragraph(
        f"<b>Ngày:</b> {receipt.created_date.strftime('%d/%m/%Y')}",
        info_style
    ))
    elements.append(Paragraph(
        f"<b>Khách hàng :</b> {reception.name}",
        info_style
    ))
    elements.append(Paragraph(
        f"<b>Biển số :</b> {reception.carnumber}",
        info_style
    ))
    elements.append(Paragraph(
        f"<b>Lỗi :</b> {reception.description}",
        info_style
    ))
    elements.append(Spacer(1, 12))

    # ===== BẢNG =====
    table_data = [[
        "Hạng mục", "Tiền công", "Linh kiện", "Đơn giá", "SL", "Thành tiền"
    ]]
    vat=dao.get_VAT()
    total = 0

    for rf in receipt.repair_forms:
        for comp in rf.components:
            thanh_tien = comp.component.price * comp.quantity
            total += thanh_tien + comp.cost

            table_data.append([
                Paragraph(str(comp.action),info_style),
                Paragraph( str(f"{comp.cost:,.0f}"), info_style),
                Paragraph(str(comp.component.name), info_style),
                Paragraph(str(f"{comp.component.price:,.0f}"), info_style),
                Paragraph(str(comp.quantity), info_style),
                Paragraph(str(f"{thanh_tien:,.0f}"), info_style)
            ])

    table = Table(
        table_data,
        colWidths=[140, 70, 120, 80, 30, 80]
    )

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "DejaVuSans"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # ===== TỔNG TIỀN =====
    elements.append(
        Paragraph(
            f"<b>TỔNG : {total:,.0f} VNĐ</b>",
            ParagraphStyle(
                name="Total",
                fontSize=12,
                fontName="DejaVuSans",
                alignment=2  # right
            )
        )
    )
    total=calc_total_VAT(receipt.repair_forms)
    elements.append(
        Paragraph(
            f"<b>TỔNG THANH TOÁN (VAT:{vat.VAT}%) : {total:,.0f} VNĐ</b>",
            ParagraphStyle(
                name="Total",
                fontSize=14,
                fontName="DejaVuSans",
                alignment=2  # right
            )
        )
    )

    doc.build(elements)
    return file_path

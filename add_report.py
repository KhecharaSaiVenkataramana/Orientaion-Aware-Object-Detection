content = open("app.py", encoding="utf-8").read()

if "download_report_csv" in content:
    print("Routes already exist")
else:
    routes = '''
@app.route("/download-report/csv")
def download_report_csv():
    import csv, io, json
    from urllib.parse import unquote
    stats_param = request.args.get("stats", "[]")
    try:
        stats = json.loads(unquote(stats_param))
    except Exception:
        stats = []
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["#","Filename","Model","Resolution","Objects","Density","Time(ms)","FPS","Output File"])
    for i, row in enumerate(stats, 1):
        writer.writerow([i, row.get("name",""), row.get("model",""), row.get("size",""),
                         row.get("objects",""), row.get("density",""), row.get("time",""),
                         row.get("fps",""), row.get("outfile","")])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode("utf-8")),
                     as_attachment=True, download_name="raven_report.csv", mimetype="text/csv")


@app.route("/download-report/pdf")
def download_report_pdf():
    import io as _io
    from datetime import datetime as dt
    files_param = request.args.get("files", "")
    filenames   = [f.strip() for f in files_param.split(",") if f.strip()]
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.units import cm
        from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                         Table, TableStyle, Image as RLImage, HRFlowable)
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
    except ImportError:
        return "Run: pip install reportlab", 500

    buf = _io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4,
                            topMargin=2*cm, bottomMargin=2*cm,
                            leftMargin=2*cm, rightMargin=2*cm)

    title_s = ParagraphStyle("T", fontSize=28, fontName="Helvetica-Bold",
                              textColor=colors.HexColor("#00cfff"), alignment=TA_CENTER, spaceAfter=6)
    sub_s   = ParagraphStyle("S", fontSize=11, fontName="Helvetica",
                              textColor=colors.HexColor("#8877cc"), alignment=TA_CENTER, spaceAfter=4)
    sec_s   = ParagraphStyle("H", fontSize=14, fontName="Helvetica-Bold",
                              textColor=colors.HexColor("#6644ff"), spaceBefore=18, spaceAfter=8)
    body_s  = ParagraphStyle("B", fontSize=10, fontName="Helvetica",
                              textColor=colors.HexColor("#cccccc"), spaceAfter=4)

    story = []
    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph("RAVEN", title_s))
    story.append(Paragraph("Detection Analysis Report", sub_s))
    story.append(Paragraph("Rotated-Annotation Vehicle and Entity Network", sub_s))
    story.append(Spacer(1, 0.4*cm))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#6644ff"), spaceAfter=12))
    story.append(Paragraph("Generated: " + dt.now().strftime("%d %B %Y, %H:%M"), sub_s))
    story.append(Paragraph("Total images: " + str(len(filenames)), sub_s))
    story.append(Spacer(1, 0.8*cm))

    story.append(Paragraph("Detection Results", sec_s))

    conn = get_db()
    outfile_stats = []
    try:
        with conn.cursor() as cur:
            for fname in filenames:
                safe = secure_filename(os.path.basename(fname))
                cur.execute("""SELECT filename,model_used,objects_found,inference_ms,fps,image_size
                               FROM detections WHERE output_path LIKE %s
                               ORDER BY detected_at DESC LIMIT 1""", ("%" + safe + "%",))
                row = cur.fetchone()
                if row:
                    outfile_stats.append(row)
    except Exception:
        pass
    finally:
        conn.close()

    if outfile_stats:
        tdata = [["Filename","Model","Objects","Time(ms)","FPS","Size"]]
        for r in outfile_stats:
            tdata.append([str(r.get("filename",""))[:22], str(r.get("model_used","")),
                          str(r.get("objects_found","")), str(round(r.get("inference_ms",0),1)),
                          str(round(r.get("fps",0),2)), str(r.get("image_size",""))])
        tbl = Table(tdata, repeatRows=1, colWidths=[4.5*cm,3.5*cm,2*cm,2.5*cm,2*cm,3*cm])
        tbl.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#6644ff")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
            ("FONTSIZE",(0,0),(-1,-1),8),
            ("TEXTCOLOR",(0,1),(-1,-1),colors.HexColor("#cccccc")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.HexColor("#0d0b22"),colors.HexColor("#100e28")]),
            ("GRID",(0,0),(-1,-1),0.3,colors.HexColor("#6644ff44")),
            ("ALIGN",(2,0),(-1,-1),"CENTER"),
            ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ]))
        story.append(tbl)
    else:
        story.append(Paragraph("No database records found for this session.", body_s))

    story.append(Spacer(1, 0.8*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#6644ff44"), spaceAfter=8))
    story.append(Paragraph("Output Images", sec_s))

    img_added = 0
    for fname in filenames:
        safe  = secure_filename(os.path.basename(fname))
        fpath = os.path.join(OUTPUT_FOLDER, safe)
        if os.path.exists(fpath):
            try:
                story.append(Paragraph(safe, body_s))
                story.append(RLImage(fpath, width=16*cm, height=10*cm, kind="proportional"))
                story.append(Spacer(1, 0.5*cm))
                img_added += 1
            except Exception:
                pass

    if img_added == 0:
        story.append(Paragraph("Output images expired (48h limit) or not found.", body_s))

    story.append(Spacer(1, 1*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#6644ff44"), spaceAfter=8))
    story.append(Paragraph("RAVEN - Detection that never blinks.", sub_s))

    def dark_bg(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor("#07051a"))
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=dark_bg, onLaterPages=dark_bg)
    buf.seek(0)
    return send_file(buf, as_attachment=True,
                     download_name="raven_report.pdf", mimetype="application/pdf")

'''
    old = 'if __name__ == "__main__":'
    content = content.replace(old, routes + old)
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Done! Report routes added.")
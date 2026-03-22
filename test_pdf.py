import io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

buf = io.BytesIO()
doc = SimpleDocTemplate(buf, pagesize=A4)
s = ParagraphStyle('t', fontSize=20, fontName='Helvetica-Bold')
doc.build([Paragraph('RAVEN Test PDF', s)])
with open('test_output.pdf', 'wb') as f:
    f.write(buf.getvalue())
print('PDF written OK, size:', len(buf.getvalue()), 'bytes')
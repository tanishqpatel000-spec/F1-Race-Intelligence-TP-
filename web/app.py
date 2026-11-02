from pathlib import Path
import io
import pandas as pd
from flask import Flask, request, render_template_string

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024
PAGE = '''<!doctype html><html><head><meta charset="utf-8"><title>F1 Data Explorer</title>
<style>body{font-family:Arial,sans-serif;max-width:1100px;margin:40px auto;padding:0 18px;background:#101820;color:#f4f6f8}h1{color:#e10600}section{background:#1d2a35;padding:20px;border-radius:12px;margin:18px 0}input,button{padding:10px}table{border-collapse:collapse;width:100%;font-size:13px}th,td{padding:8px;border-bottom:1px solid #52606b;text-align:left;overflow-wrap:anywhere}th{color:#ffb3b3}small{color:#cbd5dc}</style></head><body>
<h1>Formula 1 Race Intelligence</h1><p>Upload a CSV dataset to preview its structure and quality.</p>
<section><form method="post" enctype="multipart/form-data"><input type="file" name="file" accept=".csv" required><button type="submit">Profile CSV</button></form><small>Files are processed in memory for this request and are not saved by this demo app.</small></section>
{% if error %}<section>{{error}}</section>{% endif %}
{% if stats %}<section><h2>Dataset profile</h2><p>Rows: {{stats.rows}} | Columns: {{stats.cols}} | Duplicate rows: {{stats.duplicates}}</p><h3>Missing values</h3><ul>{% for k,v in stats.missing.items() %}<li>{{k}}: {{v}}</li>{% endfor %}</ul><h3>Preview (first 15 rows)</h3>{{table|safe}}</section>{% endif %}
</body></html>'''

@app.route('/', methods=['GET','POST'])
def index():
    stats = table = error = None
    if request.method == 'POST':
        f = request.files.get('file')
        try:
            if not f or not f.filename.lower().endswith('.csv'):
                raise ValueError('Please upload a CSV file.')
            df = pd.read_csv(io.BytesIO(f.read()))
            stats = {'rows': len(df), 'cols': len(df.columns), 'duplicates': int(df.duplicated().sum()), 'missing': {str(k): int(v) for k,v in df.isna().sum().items()}}
            table = df.head(15).to_html(index=False, escape=True, border=0)
        except Exception as exc:
            error = f'Could not process file: {exc}'
    return render_template_string(PAGE, stats=stats, table=table, error=error)

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)

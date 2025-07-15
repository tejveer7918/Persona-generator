def render_persona_html(data: dict) -> str:
    return f"""
<html>
<head>
<style>
    body {{
        font-family: 'Helvetica Neue', sans-serif;
        color: #111;
        padding: 30px;
        width: 800px;
    }}
    h1 {{ color: #ff5a00; }}
    h2 {{ color: #ff5a00; margin-top: 24px; }}
    .section {{ margin-bottom: 20px; }}
    .quote {{
        font-style: italic;
        color: #fff;
        background: #ff5a00;
        padding: 12px;
        border-radius: 6px;
        width: 300px;
    }}
    img {{
        width: 250px;
        border-radius: 6px;
        margin-right: 20px;
    }}
    .row {{ display: flex; }}
</style>
</head>
<body>
<div class="row">
    <img src="file://{data['avatar_path']}" alt="Profile Picture"/>
    <div>
        <h1>{data.get("persona_name", "Unnamed")}</h1>
        <p><strong>Demographics:</strong> {data.get("demographics", "N/A")}</p>
        <p><strong>Psychographics:</strong> {data.get("psychographics", "N/A")}</p>
        <p><strong>Reddit Usage:</strong> {data.get("reddit_usage", "N/A")}</p>
    </div>
</div>

<h2>Goals & Needs</h2>
<p>{data.get("goals", "N/A")}</p>

<h2>Frustrations</h2>
<p>{data.get("frustrations", "N/A")}</p>

<h2 class="section">Quote</h2>
<div class="quote">{data.get("quote", "")}</div>
</body>
</html>
"""

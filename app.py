import os
from flask import Flask, jsonify, request as flask_request
from datetime import datetime
from pydantic import BaseModel, ValidationError

app = Flask(__name__)

# מודל pydantic לאימות הנתונים שמתקבלים מהלקוח
class AgentRequest(BaseModel):
    query: str

# פונקציה המדמה "סוכן" – כאן אפשר לשלב לוגיקה מתקדמת או אינטגרציה עם LLM
def run_agent(agent_req: AgentRequest) -> dict:
    # לדוגמה: הסוכן פשוט מחזיר הודעה עם ה-query שקיבל
    response_text = (
        f"סוכן AI: קיבלתי את השאלה שלך: '{agent_req.query}'. "
        "עוד לא למדתי לענות בצורה חכמה, אבל אני בדרך!"
    )
    return {"response": response_text}

# נקודת קצה ראשית
@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'}), 200

# נקודת קצה המחזירה את הזמן הנוכחי
@app.route('/time')
def get_time():
    now = datetime.now().isoformat()
    return jsonify({'current_time': now}), 200

# נקודת קצה לקבלת ברכה עם שם
@app.route('/greet/<name>')
def greet(name):
    return jsonify({'greeting': f'Hello, {name}!'}), 200

# נקודת קצה לסוכן – מקבלת POST עם JSON המכיל את השדה "query"
@app.route('/agent', methods=['POST'])
def agent_endpoint():
    try:
        # קריאת הנתונים מהבקשה
        data = flask_request.get_json()
        # אימות הנתונים בעזרת pydantic
        agent_req = AgentRequest(**data)
    except ValidationError as ve:
        return jsonify({"error": ve.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # קריאה לפונקציית הסוכן
    result = run_agent(agent_req)
    return jsonify(result), 200

if __name__ == '__main__':
    # שימוש במשתנה סביבה PORT (לפריסה ב־Render) או 5000 כברירת מחדל
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

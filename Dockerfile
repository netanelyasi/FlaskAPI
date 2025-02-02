# בחירת תמונת בסיס רשמית של Python (גרסה 3.9 עם slim)
FROM python:3.9-slim

# משתני סביבה שמונעים כתיבת קבצי bytecode ומבטיחים הדפסה מיידית
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# הגדרת ספריית העבודה בתוך המכולה
WORKDIR /app

# העתקת קובץ הדרישות והתקנת התלויות
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# העתקת קוד הפרויקט לספריית העבודה
COPY . /app

# חשיפת הפורט שבו פועל השרת
EXPOSE 5000

# פקודה להרצת השרת
CMD ["python", "app.py"]

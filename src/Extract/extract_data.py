
"""
استخراج البيانات من ثلاثة مصادر: CSV + REST API + SQLite
مع التحقق من وجود البيانات في كل مصدر.
"""

import json
import sqlite3
import logging
from pathlib import Path

import pandas as pd
import requests


# =========================================================
# 1. إعداد Logging
# =========================================================
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("extract")


# =========================================================
# 2. دالة تحقق عامة
# =========================================================
def check_data(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """يتأكد أن البيانات موجودة وغير فارغة."""
    if df is None:
        raise ValueError(f"[{source_name}] الناتج None")
    if df.empty:
        raise ValueError(f"[{source_name}] البيانات فارغة")
    logger.info(f"[{source_name}] ✅ عدد السجلات: {len(df)}")
    return df


# =========================================================
# 3. استخراج CSV
# =========================================================
def extract_csv(path: str = "data/raw/students.csv") -> pd.DataFrame:
    logger.info("CSV extraction started")

    if not Path(path).exists():
        raise FileNotFoundError(f"ملف CSV غير موجود: {path}")

    df = pd.read_csv(path)
    return check_data(df, "CSV")


# =========================================================
# 4. استخراج API (مع Fallback محلي)
# =========================================================
def extract_api(url: str = None,
                local_file: str = "data/raw/api_students.json") -> pd.DataFrame:
    logger.info("API extraction started")

    # محاولة الاتصال بالـ API إن وُجد URL
    if url:
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            df = pd.DataFrame(resp.json())
            return check_data(df, "API")
        except Exception as e:
            logger.warning(f"فشل الاتصال بالـ API ({e}) — استخدام الملف المحلي")

    # Fallback: الملف المحلي
    if not Path(local_file).exists():
        raise FileNotFoundError(f"لا يوجد API ولا ملف محلي: {local_file}")

    with open(local_file, encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return check_data(df, "API (local)")


# =========================================================
# 5. استخراج SQLite
# =========================================================
def extract_database(
    db_path: str = "database/students.db",
    query: str = "SELECT student_id, course_id, semester, score FROM enrollments",
) -> pd.DataFrame:
    logger.info("Database extraction started")

    if not Path(db_path).exists():
        raise FileNotFoundError(f"قاعدة البيانات غير موجودة: {db_path}")

    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql_query(query, conn)
        return check_data(df, "Database")
    finally:
        conn.close()


# =========================================================
# 6. تشغيل الاستخراج الثلاثي
# =========================================================
def extract_all() -> dict:
    """يشغّل المصادر الثلاثة ويعيد قاموسًا بالنتائج."""
    logger.info("=" * 50)
    logger.info("بدء استخراج البيانات من المصادر الثلاثة")
    logger.info("=" * 50)

    csv_df = extract_csv()
    api_df = extract_api()
    db_df = extract_database()

    logger.info("=" * 50)
    logger.info("✅ انتهى الاستخراج بنجاح")
    logger.info("=" * 50)

    return {
        "csv": csv_df,
        "api": api_df,
        "database": db_df,
    }


# =========================================================
# 7. نقطة الدخول
# =========================================================
if __name__ == "__main__":
    try:
        data = extract_all()

        print("\n===== ملخص الاستخراج =====")
        print(f"CSV      : {len(data['csv'])} سجل")
        print(f"API      : {len(data['api'])} سجل")
        print(f"Database : {len(data['database'])} سجل")

        print("\n===== عيّنة من CSV =====")
        print(data["csv"].head())

        print("\n===== عيّنة من API =====")
        print(data["api"].head())

        print("\n===== عيّنة من Database =====")
        print(data["database"].head())

    except Exception as e:
        logger.error(f"❌ فشل الاستخراج: {e}")
        raise

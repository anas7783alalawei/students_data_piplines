مشروع دمج وتنظيف ومعالجة البيانات وتجهيزها لتعلم الآلة

📌 نبذة عن المشروع

يهدف هذا المشروع إلى بناء Data Pipeline باستخدام لغة Python لمعالجة البيانات القادمة من ثلاثة مصادر مختلفة:

- CSV
- JSON
- Database (DB)

يتم تمرير البيانات عبر ثلاث مراحل رئيسية:

CSV ──────┐
          │
JSON ─────┼──> Loading → Cleaning → Preprocessing → ML Ready Dataset
          │
DB ───────┘

حيث يتم في المرحلة الأولى تحميل البيانات، ثم تنظيفها، ثم معالجتها وتجهيزها لتكون مناسبة للاستخدام في تطبيقات وتدريب نماذج Machine Learning.

---

🎯 أهداف المشروع

يهدف المشروع إلى:

1. التعامل مع مصادر بيانات مختلفة.
2. استخدام Python لبناء Data Pipeline.
3. تحميل البيانات من CSV وJSON وDatabase.
4. تنظيف البيانات ومعالجة المشاكل الموجودة فيها.
5. توحيد شكل البيانات القادمة من المصادر المختلفة.
6. دمج البيانات عند الحاجة.
7. إجراء عمليات Data Preprocessing.
8. إنتاج Dataset جاهز للاستخدام في Machine Learning.
9. تطبيق مبادئ العمل الجماعي باستخدام Git وGitHub.
10. تطبيق Branches وCommits وPull Requests وCode Review.

---

🏗️ مراحل المشروع

يتكون المشروع من ثلاث مراحل رئيسية:

┌─────────────────────────┐
│      Data Sources       │
│ CSV / JSON / Database   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│        Loading          │
│      تحميل البيانات     │
│       Student 1         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│        Cleaning         │
│      تنظيف البيانات     │
│       Student 2         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     Preprocessing       │
│      معالجة البيانات    │
│       Student 3         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    ML Ready Dataset     │
└─────────────────────────┘

---

👥 فريق العمل

الطالب| المرحلة| الملف المسؤول عنه
الطالب الأول| تحميل البيانات Loading| "src/loading.py"
الطالب الثاني| تنظيف البيانات Cleaning| "src/cleaning.py"
الطالب الثالث| معالجة وتجهيز البيانات Preprocessing| "src/preprocessing.py"

«يتم تنفيذ المراحل بشكل مترابط، لذلك يجب الاتفاق بين الطلاب على شكل البيانات الداخلة والخارجة من كل مرحلة.»

---

👨‍💻 الطالب الأول — Loading

المسؤولية

الطالب الأول مسؤول عن تحميل البيانات من المصادر الثلاثة.

المصادر:

CSV
JSON
Database

والملف المسؤول عنه:

src/loading.py

سير العمل

CSV ──────┐
          │
JSON ─────┼──> loading.py → DataFrames
          │
DB ───────┘

المهام

- تحميل بيانات CSV.
- تحميل بيانات JSON.
- الاتصال بقاعدة البيانات.
- استخراج البيانات من قاعدة البيانات.
- تحويل البيانات إلى DataFrame.
- التحقق من إمكانية قراءة البيانات.
- التعامل مع أخطاء التحميل.
- إرجاع البيانات إلى المرحلة التالية.

Issues

LOADING-01 — تحميل بيانات CSV

إنشاء وظيفة تقوم بقراءة ملف CSV وتحويله إلى DataFrame.

LOADING-02 — تحميل بيانات JSON

إنشاء وظيفة تقوم بقراءة ملف JSON وتحويل بياناته إلى DataFrame.

LOADING-03 — تحميل بيانات Database

إنشاء وظيفة للاتصال بقاعدة البيانات واستخراج البيانات المطلوبة.

LOADING-04 — توحيد مخرجات التحميل

التأكد من أن البيانات الناتجة من CSV وJSON وDatabase يمكن تمريرها إلى مرحلة التنظيف بطريقة واضحة ومتفق عليها.

LOADING-05 — اختبار عملية التحميل

التأكد من أن جميع مصادر البيانات يتم تحميلها بنجاح ومعالجة أخطاء التحميل.

Branch

feature/loading

---

🧹 الطالب الثاني — Cleaning

المسؤولية

الطالب الثاني مسؤول عن تنظيف البيانات التي تم تحميلها.

الملف:

src/cleaning.py

لا يقوم هذا الطالب بتحميل البيانات من الملفات أو قاعدة البيانات، وإنما يستقبل البيانات الناتجة من مرحلة Loading.

سير العمل

Loaded Data
     │
     ▼
cleaning.py
     │
     ▼
Clean Data

المهام

1. معالجة القيم المفقودة

اكتشاف:

NaN
None
Empty Values

وتحديد الطريقة المناسبة للتعامل معها.

---

2. إزالة البيانات المكررة

اكتشاف السجلات المكررة ومعالجتها وفق قواعد المشروع.

---

3. تصحيح أنواع البيانات

التأكد من أن كل عمود يحتوي على النوع الصحيح، مثل:

Integer
Float
String
Date
Boolean

---

4. توحيد أسماء الأعمدة

مثلاً:

Student Name
studentName
student_name

يتم توحيدها إلى صيغة واحدة مثل:

student_name

---

5. توحيد القيم

إذا كانت نفس القيمة مكتوبة بأشكال مختلفة، يتم توحيدها.

مثلاً:

Male
male
M

يمكن توحيدها وفق قاعدة يحددها الفريق.

---

Issues

CLEANING-01 — معالجة القيم المفقودة

اكتشاف القيم المفقودة وتحديد طريقة التعامل معها.

CLEANING-02 — إزالة البيانات المكررة

اكتشاف السجلات المكررة وإزالتها حسب قواعد المشروع.

CLEANING-03 — تصحيح أنواع البيانات

التأكد من أن أنواع البيانات صحيحة ومتوافقة.

CLEANING-04 — توحيد أسماء الأعمدة والقيم

توحيد أسماء الأعمدة والقيم بين مصادر البيانات المختلفة.

CLEANING-05 — توحيد مخرجات التنظيف

التأكد من أن البيانات النظيفة لها شكل واضح يمكن تمريره إلى مرحلة المعالجة.

CLEANING-06 — اختبار عملية التنظيف

اختبار عمليات تنظيف البيانات والتأكد من صحة النتائج.

Branch

feature/cleaning

---

⚙️ الطالب الثالث — Preprocessing

المسؤولية

الطالب الثالث مسؤول عن معالجة البيانات بعد تنظيفها وتجهيزها للاستخدام في Machine Learning.

الملف:

src/preprocessing.py

سير العمل

Clean Data
     │
     ▼
preprocessing.py
     │
     ├── Integration
     ├── Feature Preparation
     ├── Encoding
     ├── Scaling
     └── Final Validation
     │
     ▼
ML Ready Dataset

المهام

1. دمج البيانات

دمج البيانات القادمة من المصادر المختلفة وفق الـSchema المتفق عليه.

---

2. معالجة القيم الشاذة

اكتشاف Outliers والتعامل معها حسب طبيعة البيانات.

---

3. تحويل البيانات الفئوية

تحويل البيانات النصية إلى شكل رقمي مناسب عند الحاجة.

مثال:

Male
Female

يمكن تحويلها إلى تمثيل رقمي مناسب باستخدام طريقة preprocessing مناسبة.

---

4. Scaling

تطبيق Scaling على المتغيرات الرقمية عندما يكون ذلك مطلوبًا لنموذج ML المستخدم.

---

5. تجهيز Features

تحديد وتجهيز المتغيرات التي سيتم استخدامها في نموذج Machine Learning.

---

6. التحقق النهائي

التأكد من أن Dataset النهائي:

- منظم.
- لا يحتوي على مشاكل غير معالجة.
- يحتوي على أنواع بيانات مناسبة.
- مناسب للانتقال إلى مرحلة Machine Learning.

---

Issues

PROCESSING-01 — دمج البيانات

دمج البيانات النظيفة القادمة من المصادر المختلفة.

PROCESSING-02 — معالجة Outliers

اكتشاف القيم الشاذة ومعالجتها وفق استراتيجية مناسبة.

PROCESSING-03 — Encoding

تحويل البيانات الفئوية إلى تمثيل مناسب لنماذج Machine Learning.

PROCESSING-04 — Scaling

تطبيق Scaling على المتغيرات الرقمية عند الحاجة.

PROCESSING-05 — تجهيز Features

تجهيز المتغيرات النهائية التي ستستخدم في Machine Learning.

PROCESSING-06 — إنشاء ML Ready Dataset

إنشاء Dataset النهائي وتجهيزه للحفظ.

PROCESSING-07 — اختبار المعالجة

التأكد من صحة البيانات بعد جميع عمليات preprocessing.

Branch

feature/preprocessing

---

🔗 شكل البيانات بين المراحل

من أهم قواعد المشروع أن يكون هناك Contract واضح بين الطلاب.

المرحلة الأولى

"loading.py"

تستقبل:

CSV
JSON
DB

وتخرج:

Loaded Data

---

المرحلة الثانية

"cleaning.py"

تستقبل:

Loaded Data

وتخرج:

Clean Data

---

المرحلة الثالثة

"preprocessing.py"

تستقبل:

Clean Data

وتخرج:

ML Ready Data

وبالتالي:

Loading
   │
   ▼
Loaded Data
   │
   ▼
Cleaning
   │
   ▼
Clean Data
   │
   ▼
Preprocessing
   │
   ▼
ML Ready Dataset

---

📂 هيكل المشروع

ml-data-pipeline/
│
├── data/
│   │
│   ├── raw/
│   │   ├── csv/
│   │   ├── json/
│   │   └── db/
│   │
│   └── processed/
│       └── ml_ready.csv
│
├── src/
│   │
│   ├── loading.py
│   ├── cleaning.py
│   └── preprocessing.py
│
├── tests/
│   │
│   ├── test_loading.py
│   ├── test_cleaning.py
│   └── test_preprocessing.py
│
├── notebooks/
│   └── exploration.ipynb
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

---

🔀 Git & GitHub Workflow

يستخدم الفريق Git وGitHub لإدارة المشروع والتعاون بين الطلاب.

لا يتم العمل مباشرة على "main".

يستخدم كل طالب Branch خاصًا به:

main
 │
 ├── feature/loading
 │
 ├── feature/cleaning
 │
 └── feature/preprocessing

سير العمل

Issue
  ↓
Branch
  ↓
Coding
  ↓
Testing
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Code Review
  ↓
Merge
  ↓
main

---

🌿 قواعد Branches

الطالب الأول

git switch -c feature/loading

الطالب الثاني

git switch -c feature/cleaning

الطالب الثالث

git switch -c feature/preprocessing

---

📝 Commit Convention

يجب أن تكون رسائل Commit واضحة.

أمثلة:

feat: add CSV loading
feat: add JSON loading
feat: add database loading

feat: handle missing values
feat: remove duplicate records
fix: correct data types

feat: add data preprocessing
feat: add categorical encoding
feat: add feature scaling

test: add loading tests
test: add cleaning tests
test: add preprocessing tests

docs: update README

---

🔃 Pull Requests

بعد انتهاء كل طالب من مهمته:

Branch
   ↓
Push
   ↓
Pull Request
   ↓
Review
   ↓
Merge

مثال:

feature/loading
       ↓
Pull Request
       ↓
main

ويجب أن تتم مراجعة الكود قبل الدمج.

---

🧪 الاختبارات

يحتوي المشروع على اختبارات لكل مرحلة:

tests/
│
├── test_loading.py
├── test_cleaning.py
└── test_preprocessing.py

تشمل الاختبارات:

- اختبار تحميل CSV.
- اختبار تحميل JSON.
- اختبار تحميل Database.
- اختبار القيم المفقودة.
- اختبار البيانات المكررة.
- اختبار أنواع البيانات.
- اختبار عمليات preprocessing.
- اختبار Dataset النهائي.

لتشغيل الاختبارات:

pytest

---

📦 المكتبات

المكتبات المستخدمة يتم تسجيلها في:

requirements.txt

ومن أمثلتها:

pandas
numpy
scikit-learn
pytest

لتثبيت المكتبات:

pip install -r requirements.txt

---

▶️ تشغيل المشروع

بعد تثبيت المتطلبات:

python main.py

يتم تنفيذ الـPipeline:

Loading
   ↓
Cleaning
   ↓
Preprocessing
   ↓
ML Ready Dataset

---

📊 المخرجات النهائية

الهدف النهائي هو إنتاج ملف:

data/processed/ml_ready.csv

ويجب أن يكون هذا الملف:

- موحد البنية.
- نظيفًا.
- معالجًا.
- جاهزًا للاستخدام في Machine Learning.

---

🤖 المرحلة التالية: Machine Learning

بعد إنتاج "ml_ready.csv" يمكن الانتقال إلى مرحلة تدريب نموذج ML:

ML Ready Dataset
       ↓
Train / Test Split
       ↓
Feature Selection
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Saving

هذه المرحلة تعتبر مرحلة لاحقة للمشروع الأساسي.

---

🎓 المهارات التي يطبقها المشروع

من خلال هذا المشروع يتم تطبيق:

- Python
- Pandas
- NumPy
- CSV
- JSON
- Database
- Data Loading
- Data Cleaning
- Data Preprocessing
- Data Integration
- Machine Learning Preparation
- Unit Testing
- Git
- GitHub
- Branching
- Commits
- Pull Requests
- Code Review
- Team Collaboration
- Software Engineering Practices

---

✅ Definition of Done

تعتبر المهمة مكتملة عندما:

- يتم تنفيذ الكود المطلوب.
- يتم اختبار الكود.
- تعمل الوظيفة بالشكل المطلوب.
- يتم عمل Commit واضح.
- يتم Push إلى GitHub.
- يتم إنشاء Pull Request.
- تتم مراجعة الكود.
- يتم معالجة ملاحظات المراجعة.
- يتم Merge إلى "main".

---

📌 ملاحظة مهمة

كل طالب مسؤول عن مرحلة محددة، ولكن المراحل الثلاث مترابطة:

Student 1
Loading
   ↓
Student 2
Cleaning
   ↓
Student 3
Preprocessing

لذلك يجب على الطلاب الاتفاق مسبقًا على شكل البيانات الداخلة والخارجة من كل مرحلة، حتى تستطيع كل مرحلة التعامل مع مخرجات المرحلة السابقة دون تعديل عشوائي في كود طالب آخر.

---

🚀 النتيجة النهائية

CSV ──────┐
          │
JSON ─────┼──> Loading
          │       │
DB ───────┘       ▼
               Cleaning
                  │
                  ▼
             Preprocessing
                  │
                  ▼
          ML Ready Dataset
                  │
                  ▼
            Machine Learning
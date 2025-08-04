<h1 align="center"> Data Cleaning and Preprocessing </h1>

## **📈 Objective**
To clean and preprocess a real-world healthcare dataset by addressing missing values, duplicates, formatting issues, and inconsistencies to make it ready for analysis.

---

## **📁 Dataset Details**
- **Name:** Medical Appointment No-Shows
- **Source:** Kaggle [Link](https://www.kaggle.com/datasets/joniarroba/noshowappointments?resource=download)
- **File:** `KaggleV2-May-2016.csv`
- **Rows:** 110,527 (before cleaning)
- **Columns:** 14

---

## **🛠️ Tools Used**
- Python
- Pandas

---

## **🔧 Cleaning Steps**
**1. Renamed Columns**
- All columns converted to lowercase.
- Spaces and hyphens replaced with underscores.
- Corrected handcap to handicap.

**2. Removed Duplicates**
- Checked and removed any fully duplicated rows.

**3. Handled Missing Values**
- Verified that no null values were present post-cleaning.

**4. Standardized Categorical Values**
- gender: Converted to uppercase.
- no_show: Changed 'Yes' to no_show, 'No' to show.

**5. Date Formatting**
- Converted scheduledday and appointmentday to datetime objects.

**6. Data Type Validation**
- Ensured age values are non-negative integers.
- Removed rows with negative age values.

---

## **📊 Summary of Changes**

| Task  | Description |
| ----- | ----- |
| Rows Before Cleaning | 110,527 |
| Rows After Cleaning | 110,526 |
| Duplicates Removed | 0 |
| Null Values Remaining | 0 |
| Renamed Columns | Yes |
| Standardized `gender/no_show` | Yes |
| Dates Converted | Yes |
| Negative Ages Removed | Yes |
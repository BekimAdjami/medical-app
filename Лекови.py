import streamlit as st

medication_data = {
    "Допамин": {
        "форми_на_дозирање": ["раствор за инфузија, во D5W", "инјектибилен раствор"],
        "јачини": ["80mg/100mL", "160mg/100mL", "320mg/100mL", "40mg/mL", "80mg/mL", "160mg/mL"],
        "хемодинамски_услови": {
            "низок_дозирачки_опсег": "1-5 mcg/kg/min IV: Може да зголеми излез од урина и бубрежна крвна потока",
            "среден_дозирачки_опсег": "5-15 mcg/kg/min IV: Може да зголеми бубрежна крвна потока, срцеви излез, брзина на срцевите и срцева контрактилност",
            "висок_дозирачки_опсег": "20-50 mcg/kg/min IV: Може да зголеми брзина на крвен притисок и стимулира вазоконстрикција; може да нема благосоптно влијание врз крвниот притисок; може да го зголеми ризикот од тахиаритмија"
        },
        "дозирачки_забелешки": {
            "бета1_ефекти": "2-10 mcg/kg/min",
            "алфа_ефекти": ">10 mcg/kg/min",
            "допаминска_ефекти": "0.5-2 mcg/kg/min"
        },
        "користење_за": {
            "хипотензија": "Лечење на хипотензија, низок срцеви излез, лоша перфузија на витални органи; користено за зголемување на среден крвен притисок кај септички шок пациенти кои остануваат хипотензија по адекватно волуменско проширување"
        }
    },
    "Добутамин": {
        "форми_на_дозирање": ["раствор за инфузија, во D5W", "инјектибилен раствор"],
        "јачини": ["100mg/100mL", "200mg/100mL", "400mg/100mL", "12.5mg/mL"],
        "кардиоваскуларен_декомпензација": "0.5-1 mcg/kg/min IV непрекината инфузија првично, потоа 2-20 mcg/kg/min; не треба да надмине 40 mcg/kg/min",
        "низок_срцеви_излез": "2-20 mcg/kg/min IV или IO; титрирајте кон желен ефект; не треба да надмине 40 mcg/kg/min",
        "користење_за": {
            "кардиоваскуларен_декомпензација": "0.5-1 mcg/kg/min IV непрекината инфузија првично, потоа 2-20 mcg/kg/min; не треба да надмине 40 mcg/kg/min",
            "низок_срцеви_излез": "2-20 mcg/kg/min IV или IO; титрирајте кон желен ефект; не треба да надмине 40 mcg/kg/min"
        }
    },
    "Норепинефрин": {
        "форми_на_дозирање": ["инјектибилен раствор"],
        "јачини": ["1mg/mL"],
        "акутна_хипотензија": {
            "почетна": "8-12 mcg/min IV инфузија; титрирајте кон ефект",
            "одржување": "2-4 mcg/min IV инфузија"
        },
        "срцеви_застој": {
            "почетна": "8-12 mcg/min IV инфузија; титрирајте кон ефект",
            "одржување": "2-4 mcg/min IV инфузија"
        },
        "сепсис_септички_шок": "0.01-3.3 mcg/kg/min IV инфузија",
        "ненормална_употреба": {
            "токсичност_на_бета_блокатори": "Треба да се титрира кон возраст-соодветен крвен притисок",
            "токсичност_на_калциумски_канали": "Треба да се титрира кон возраст-соодветен крвен притисок",
            "токсичност_на_трициклични_антидепресивни": "Треба да се титрира кон возраст-соодветен крвен притисок"
        },
        "користење_за": {
            "акутна_хипотензија": "Лечење на акутна хипотензија; треба да се титрира кон ефект",
            "срцеви_застој": "Лечење на срцеви застој; треба да се титрира кон ефект",
            "сепсис_септички_шок": "0.01-3.3 mcg/kg/min IV инфузија"
        }
    }
}

def calculate_dosage(patient_weight, desired_dose, dilution_ml):
    try:
        patient_weight = float(patient_weight)
        desired_dose = float(desired_dose)
        dilution_ml = float(dilution_ml)
        dosage = desired_dose * patient_weight
        ml_per_hour = dosage / dilution_ml
        return f"Пресметана Доза: {dosage} mg\nДоколку се дилуира во {dilution_ml} ml, потребно е да се подеси на {ml_per_hour:.2f} ml/h"
    except ValueError:
        return "Ве молиме внесете валидни броеви за тежина, доза, и дилуција."

def display_information(medication):
    if medication in medication_data:
        information = "\n".join([
            f"\nЛек: {medication}",
            "Форми на дозирање: " + ', '.join(medication_data[medication]["форми_на_дозирање"]),
            "Јачини: " + ', '.join(medication_data[medication]["јачини"]),
            "Користење за: " + ', '.join([f"{condition}: {use}" for condition, use in medication_data[medication]["користење_за"].items()]),
        ])
        return information
    else:
        return "Невалиден Лек. Ве молиме изберете помеѓу Допамин, Добутамин, или Норепинефрин."

def app():
    st.title("Пресметувач на Лекови")

    # Medication Selection
    medication = st.selectbox("Изберете Лек:", ["Допамин", "Добутамин", "Норепинефрин"])

    # Display Information Button
    if st.button("Прикажи Информации"):
        information = display_information(medication)
        st.text_area("Информации за Лекот", information, height=200)

    # Patient Weight and Desired Dose Entry
    patient_weight = st.text_input("Тежина на Пациентот (кг):")
    desired_dose = st.number_input("Доза (mcg/kg/min):", value=0.0, step=1.0)
    dilution_ml = st.number_input("Дилуција во (ml):", value=0.0, step=1.0)

    # Calculate Dosage Button
    if st.button("Пресметај Доза и ml/h"):
        result = calculate_dosage(patient_weight, desired_dose, dilution_ml)
        st.text(result)

    # Credit Line
    st.text("Made by B. Adjami")

if __name__ == "__main__":
    app()

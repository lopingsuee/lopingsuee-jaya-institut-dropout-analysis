
def select_with_labels(label, mapping, default_value=None, key=None):
    import streamlit as st

    values = list(mapping.keys())

    if default_value is None:
        default_value = values[0]

    try:
        default_index = values.index(default_value)
    except ValueError:
        default_index = 0

    return st.selectbox(
        label=label,
        options=values,
        index=default_index,
        format_func=lambda v: f"{mapping[v]} ({v})",
        key=key
    )


YES_NO_MAP = {
    1: "Yes",
    0: "No",
}

GENDER_MAP = {
    1: "Male",
    0: "Female",
}

ATTENDANCE_MAP = {
    1: "Daytime",
    0: "Evening",
}

MARITAL_STATUS_MAP = {
    1: "Single",
    2: "Married",
    3: "Widower",
    4: "Divorced",
    5: "Facto union",
    6: "Legally separated",
}

COURSE_MAP = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)",
}


APPLICATION_MODE_MAP = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99 (Different Plan)",
    27: "Ordinance No. 533-A/99 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)",
}


NATIONALITY_MAP = {
    1: "Portuguese",
    2: "German",
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Cape Verdean",
    24: "Guinean",
    25: "Mozambican",
    26: "Santomean",
    32: "Turkish",
    41: "Brazilian",
    62: "Romanian",
    100: "Moldova (Republic of)",
    101: "Mexican",
    103: "Ukrainian",
    105: "Russian",
    108: "Cuban",
    109: "Colombian",
}
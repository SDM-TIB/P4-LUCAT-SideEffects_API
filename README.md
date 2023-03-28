# P4-LUCAT-SideEffects_API

Retreive sideeffects based on the input variables



## Input Example
POST:
https://labs.tib.eu/sdm/p4lucat_sideeffects_api/exploration?topic=all&limit=10&page=0 
```
{
   "comorbidities":[
  	"C0242339",
  	"C0020538",
  	"C0149871"
   ],
   "biomarkers":[
  	"C0034802",
  	"C1332080",
  	"C0812281"
   ],
   "tumorType":[
  	"C0152013"
   ],
   "drugGroups":[
  	"C0002771",
  	"C0003232"
   ],
   "drugs":[
  	"C0000979",
  	"C0028978"
   ],
   "oncologicalTreatments":[
  	"C0021083",
  	"C3665472",
  	"C3899317",
  	"C0596087",
  	"C0034619",
  	"C0543467"
   ],
   "immunotherapyDrugs":[
  	"C3657270",
  	"C3658706",
  	"C1367202"
   ],
   "tkiDrugs":[
  	"C1135135",
  	"C2987648",
  	"C4058811",
  	"C1122962",
  	"C3853921",
  	"C3818721"
   ],
   "chemotherapyDrugs":[
  	"C0008838",
  	"C4082227",
  	"C0771375",
  	"C0015133",
  	"C0079083",
  	"C0045093",
  	"C0144576",
  	"C0210657",
  	"C0078257"
   ]
}
```

## Output Example
```
{
    "sideEffects": {
        "resultsTotal": 51,
        "results": {
            "Treprostinil": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Infusion site pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Infusion site reaction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Larynx pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pharyngolaryngeal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Throat irritation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain in limb",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Flushing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Jaw pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pruritus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypokalemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Shock",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Syncope",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Unconscious state",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abdominal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hematuria",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Epistaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anorexia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Decrease in appetite",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Melena",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angioedema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bone pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cellulitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Thrombocytopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Thrombophlebitis",
                    "group": "comorbidities"
                }
            ],
            "Bosentan": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Communicable diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Respiratory tract infections",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sensory discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vertigo",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Body fluid retention",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pulmonary hypertension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Upper respiratory infections",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Liver function tests abnormal finding",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Chest pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasopharyngitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Flushing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Shock",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Syncope",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Unconscious state",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspnea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arthralgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Musculoskeletal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sinusitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Palpitations",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bronchitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain in limb",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Back pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Muscle cramp",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Rectal hemorrhage",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Spasm",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urinary tract infection",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Epistaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension%2C orthostatic",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Blurred vision",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemoptysis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Lower respiratory tract infection",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasal congestion %28finding%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pruritus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Contusions",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Skin ulcer",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Wheezing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Acute bronchitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bladder pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cystitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Non-infectious cystitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pneumonia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tracheobronchitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abdominal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastrointestinal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hepatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypersensitivity",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Icterus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Thrombocytopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anaphylaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angioedema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Leukopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Liver cirrhosis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Liver failure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Neutropenia",
                    "group": "comorbidities"
                }
            ],
            "Clonidine": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension%2C orthostatic",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urinary tract infection",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Confusion",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Feeling abnormal",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Somnolence",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Upper abdominal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Asthenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fatigue",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Upper respiratory infections",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Xerostomia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Irritable mood",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Decrease in appetite",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Oropharyngeal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Oropharyngeal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sore throat",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nightmares",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasal congestion %28finding%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypoventilation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypoxia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Respiratory failure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Emotional disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleeplessness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fever",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Constipation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Chest pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hyperhidrosis disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sweating",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tinnitus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hallucinations",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Earache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tachycardia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasopharyngitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Aggressive behavior",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Asthma",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Influenza-like illness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abdominal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastrointestinal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Rhinorrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abnormal sleep-related event",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bradycardia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Crying",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Enuresis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Lower respiratory tract infection",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Thirst",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tremor",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Weepiness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Acute otitis media",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anxiety",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Enteritis due to specified virus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Epistaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Increased frequency of micturition",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Night terrors",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain in limb",
                    "group": "comorbidities"
                }
            ],
            "Iloprost": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Increasing frequency of cough",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Flushing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vasodilation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vasodilation procedure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Influenza",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Trismus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Shock",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleeplessness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Syncope",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Unconscious state",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Back pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Laboratory test result abnormal",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Palpitations",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gamma-glutamyltransferase increased",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Muscle cramp",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Spasm",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Alkaline phosphatase raised",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Blood alkaline phosphatase increased",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemoptysis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Glossalgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pneumonia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bronchospasm",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Drug interactions",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dysgeusia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Epistaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gingival hemorrhage",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Glossitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemoglobin measurement",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemorrhage",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypersensitivity",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasal congestion %28finding%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Thrombocytopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tongue irritation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Wheezing",
                    "group": "comorbidities"
                }
            ],
            "Losartan": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urinary tract infection",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypoglycemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bronchitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diabetic angiopathies",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Influenza",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Asthenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fatigue",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Communicable diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cellulitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Back pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Upper respiratory infections",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cataract",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Chest pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Muscle weakness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arthralgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastritis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypesthesia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Knee pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain in limb",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain in lower limb",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diabetic neuropathies",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fever",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Traumatic injury",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Weight gain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Wounds and injuries",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hyperkalemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sinusitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension%2C orthostatic",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspepsia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pharyngitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abdominal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastrointestinal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tachycardia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasal congestion %28finding%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Swelling",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Paranasal sinus disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleeplessness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Muscle cramp",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Palpitations",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Spasm",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Airway obstruction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anaphylaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angioedema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Blood urea increased",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dry cough",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dysgeusia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Essential hypertension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exfoliative dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Feeling abnormal",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Henoch-schoenlein purpura",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hepatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypersensitivity",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hyponatremia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Ill-defined disease",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Kidney failure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Lung diseases%2C obstructive",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Malaise",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nervous system disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Renal insufficiency",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Rhabdomyolysis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sensory discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Thrombocytopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vasculitis",
                    "group": "comorbidities"
                }
            ],
            "Perindopril": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Upper respiratory infections",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Asthenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Back pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Rhinitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain in limb",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Stomach ache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Upper abdominal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pharyngitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abdominal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urinary tract infection",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastrointestinal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angina pectoris",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleep disorders",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Chest pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sinusitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Electrocardiogram abnormal",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension%2C orthostatic",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Virus diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arm pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Muscle hypertonia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Protein urine present",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Proteinuria",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspepsia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Palpitations",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Shock",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Syncope",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Unconscious state",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fever",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Infection of ear",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cerebrovascular accident",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angioedema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Kidney failure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Purpura",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Renal insufficiency",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleep disturbances",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleeplessness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urticaria",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vascular purpura",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Acute coronary syndrome",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Acute pancreatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Agranulocytosis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anti-nuclear factor positive",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arthralgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arthritis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bullous pemphigoid",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cardiac arrest",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cardiac arrhythmia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Eosinophilia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Esr raised",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exfoliative dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hepatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypertensive %28finding%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypertensive disease",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hyponatremia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Icterus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Kidney failure%2C acute",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Leukocytosis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Leukopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Liver failure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Musculoskeletal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Myalgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Myocardial infarction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nephritis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Neutropenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pancytopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pemphigus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Psoriasis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pulmonary eosinophilia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pulmonary fibrosis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Serositis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Thrombocytopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vasculitis",
                    "group": "comorbidities"
                }
            ],
            "Riociguat": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspepsia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastritis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastroesophageal reflux disease",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Constipation",
                    "group": "comorbidities"
                }
            ],
            "Captopril": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pharyngitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anuria",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arthralgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Ataxia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Confusion",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Contracture",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Eosinophilia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Feeling abnormal",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fetal growth retardation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fever",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Irreversible renal failure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Kidney failure%2C chronic",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Microcephaly",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Muscle weakness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Musculoskeletal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Myalgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Myasthenias",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nephritis%2C interstitial",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nephritis%2C tubulointerstitial",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nervousness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Oligohydramnios",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Patent ductus arteriosus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pregnancy",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pulmonary eosinophilia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Rhinitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Skull hypoplasia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Somnolence",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vasculitis",
                    "group": "comorbidities"
                }
            ],
            "Sildenafil": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bronchitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Upper respiratory infections",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pharyngitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain in limb",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Back pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fever",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diarrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pneumonia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspepsia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Flushing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleeplessness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Musculoskeletal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Myalgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Epistaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspnoea exacerbated",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Influenza",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspnea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasopharyngitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Rhinorrhea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Visual disturbance",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abnormal vision",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Erythema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasal congestion %28finding%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Visual impairment",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Rhinitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastritis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Paresthesia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sinusitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urinary tract infection",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vertigo",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vision disorders",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Asthenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Chest pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Conjunctival diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Disorder of eye",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Eye/adnexa disease other",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fatigue",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hematuria",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemorrhage of penis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemospermia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypesthesia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Lacrimal apparatus diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Lacrimal structural disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Palpitations",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Somnolence",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tachycardia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tinnitus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Xerostomia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Acute coronary syndrome",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Amnesia%2C transient global",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anemia%2C sickle cell",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angina%2C unstable",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angina pectoris",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anxiety",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arteritic anterior ischemic optic neuropathy",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Atrial fibrillation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Blindness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Blindness%2C transient",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Blood and lymphatic system disorders",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Breast diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cardiac disease",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cardiovascular diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cerebral hemorrhage",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cerebrovascular accident",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Connective tissue diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Deafness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Detachment psychological",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Diplopia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Disorder of soft tissue",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dissociation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Erectile dysfunction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Erection increased",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Erection prolonged",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Erythema multiforme",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastrointestinal diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemoglobin measurement",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemoglobin ss disease with crisis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hemorrhage",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypersensitivity",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypertensive disease",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotensive",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Immune system diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Mediastinal diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Myocardial infarction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nervous system disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nonarteritic anterior ischemic optic neuropathy %28naion%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Optic neuropathy%2C ischemic",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Priapism",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pulmonary hemorrhage",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pulmonary hypertension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Raised intraocular pressure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Redness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Retinal edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Retinal vascular occlusion",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Scotoma",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Seizures",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Shock",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Stevens-johnson syndrome",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sudden cardiac death",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Swelling",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Syncope",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Toxic epidermal necrolysis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Transient ischemic attack",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Unconscious state",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Unspecified visual loss",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urethral diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urologic diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vascular diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vaso-occlusive crisis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Ventricular arrhythmia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vitreous detachment",
                    "group": "comorbidities"
                }
            ],
            "Nifedipine": [
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Lightheadedness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Headache",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Heartburn",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dizziness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Feels hot",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Heat sensation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Flushing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nasal congestion %28finding%29",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Oropharyngeal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Oropharyngeal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sore throat",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Asthenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Labile affect",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Mood swings",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tremor",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Palpitations",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Coughing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Wheezing",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nausea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nervousness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Fatigue",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspepsia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Muscle cramp",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Spasm",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cramps of lower extremities",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dyspnea",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Peripheral edema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exanthema",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Constipation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Sleeplessness",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Angina pectoris",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Erectile dysfunction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Flatulence",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Polyuria",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Urine output increased",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Abdominal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastrointestinal pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Tachycardia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Pruritus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Xerostomia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Somnolence",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypesthesia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Chest pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Agranulocytosis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Alanine aminotransferase increased",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Allergic hepatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anaphylactoid reaction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Anaphylaxis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Arthralgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Bezoar disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Blurred vision",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cardiac disease",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Cholestasis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Deglutition disorders",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Dermatitis%2C phototoxic",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Disorder of eye",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Esophagitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Exfoliative dermatitis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Eye pain",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gastrooesophageal sphincter insufficiency",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gingival diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Gynecomastia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Heart failure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hyperglycemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypotension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Hypovolemia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Icterus",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Intestinal obstruction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Intrahepatic cholestasis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Leukopenia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Malignant hypertension",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Malnutrition",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Mediastinal diseases",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Musculoskeletal discomfort",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Myalgia",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Nervous system disorder",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Palpable purpura",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Photosensitivity allergic reaction",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Primary ulcer of intestine",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Toxic epidermal necrolysis",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vasodilation",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vasodilation procedure",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Vomiting",
                    "group": "comorbidities"
                },
                {
                    "sideEffect": "http://research.tib.eu/p4-lucat/entity/Weight decreased",
                    "group": "comorbidities"
                }
            ]
        }
    }
}
```

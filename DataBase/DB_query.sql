CREATE TABLE IF NOT EXISTS HealthData (
    Gender TEXT,
    Age INTEGER,
    Height REAL,
    Weight REAL,
    family_history_with_overweight TEXT,
    FAVC TEXT,
    FCVC INTEGER,
    NCP REAL,
    CAEC TEXT,
    SMOKE TEXT,
    CH2O REAL,
    SCC TEXT,
    FAF REAL,
    TUE REAL,
    CALC TEXT,
    MTRANS TEXT,
    NObeyesdad TEXT
);

DELETE FROM HealthData;

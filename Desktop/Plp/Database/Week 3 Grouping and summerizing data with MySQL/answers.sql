USE hospital_db;

-- Question  1.1. Find the total number of patient admissions
SELECT COUNT(*) AS total_admissions
FROM admissions;

-- Question 1.2. Calculate the average length of stay for all patients
SELECT AVG(DATEDIFF(discharge_date, admission_date)) AS avg_length_of_stay
FROM admissions;

-- Question 2.1. Group admissions by primary_diagnosis and count the number of admissions
SELECT primary_diagnosis, COUNT(*) AS total_admissions
FROM admissions
GROUP BY primary_diagnosis;

-- Question 2.2. Group admissions by service and calculate the average length of stay
SELECT service, AVG(DATEDIFF(discharge_date, admission_date)) AS avg_length_of_stay
FROM admissions
GROUP BY service;

-- Question 2.3. Group discharges by discharge_disposition and count the number of discharges
SELECT discharge_disposition, COUNT(*) AS total_discharges
FROM discharges
GROUP BY discharge_disposition;

-- Question 3.1. Group admissions by service and filter where the total admissions is greater than 5
SELECT service, COUNT(*) AS total_admissions
FROM admissions
GROUP BY service
HAVING total_admissions > 5;

-- Question 3.2. Average length of stay for patients admitted with primary diagnosis of 'Stroke'
SELECT AVG(DATEDIFF(discharge_date, admission_date)) AS avg_length_of_stay
FROM admissions
WHERE primary_diagnosis = 'Stroke';

-- Question 4.1. Group emergency department visits by acuity and calculate the total number of visits
SELECT acuity, COUNT(*) AS total_visits
FROM ed_visits
GROUP BY acuity;

-- Question 4.2. Group admissions by primary_diagnosis and service, showing the total number of admissions
SELECT primary_diagnosis, service, COUNT(*) AS total_admissions
FROM admissions
GROUP BY primary_diagnosis, service;

-- Question 5.1. Group admissions by month and calculate the total admissions per month
SELECT MONTH(admission_date) AS month, COUNT(*) AS total_admissions
FROM admissions
GROUP BY month;

-- Question 5.2. Find the maximum length of stay for each primary_diagnosis
SELECT primary_diagnosis, MAX(DATEDIFF(discharge_date, admission_date)) AS max_length_of_stay
FROM admissions
GROUP BY primary_diagnosis;

-- Bonus Question. Calculate both total and average length of stay for each service, ordered by highest average stay
SELECT service, SUM(DATEDIFF(discharge_date, admission_date)) AS total_length_of_stay, 
       AVG(DATEDIFF(discharge_date, admission_date)) AS avg_length_of_stay
FROM admissions
GROUP BY service
ORDER BY avg_length_of_stay DESC;


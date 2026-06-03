# ANSI SQL Using MySQL – 25 SQL Practice Questions

This repository contains solutions for 25 ANSI SQL practice questions based on an Event Management Database schema consisting of:

- Users
- Events
- Sessions
- Registrations
- Feedback
- Resources

The exercises cover SQL concepts such as:

- Joins
- Aggregation
- GROUP BY
- HAVING
- Subqueries
- CTEs
- Date Functions
- Window Analysis
- Data Validation
- Reporting Queries

---

# Samlpe DataSet

## Crete Table:
### Code:
```


CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE Events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    city VARCHAR(100) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    status ENUM('upcoming','completed','cancelled'),
    organizer_id INT,
    FOREIGN KEY (organizer_id) REFERENCES Users(user_id)
);

CREATE TABLE Sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    title VARCHAR(200) NOT NULL,
    speaker_name VARCHAR(100) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_id INT,
    registration_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    feedback_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Resources (
    resource_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    resource_type ENUM('pdf','image','link'),
    resource_url VARCHAR(255) NOT NULL,
    uploaded_at DATETIME NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);
```
### Output:
<img width="1600" height="258" alt="WhatsApp Image 2026-06-03 at 9 31 02 PM" src="https://github.com/user-attachments/assets/38864013-1bbf-4004-b9e2-d1f83a887c6c" />

## Insert Data
### Code:
```
INSERT INTO Users (user_id, full_name, email, city, registration_date) VALUES
(1, 'Alice Johnson', 'alice@example.com', 'New York', '2024-12-01'),
(2, 'Bob Smith', 'bob@example.com', 'Los Angeles', '2024-12-05'),
(3, 'Charlie Lee', 'charlie@example.com', 'Chicago', '2024-12-10'),
(4, 'Diana King', 'diana@example.com', 'New York', '2025-01-15'),
(5, 'Ethan Hunt', 'ethan@example.com', 'Los Angeles', '2025-02-01');

INSERT INTO Events
(event_id, title, description, city, start_date, end_date, status, organizer_id)
VALUES
(1,
'Tech Innovators Meetup',
'A meetup for tech enthusiasts.',
'New York',
'2025-06-10 10:00:00',
'2025-06-10 16:00:00',
'upcoming',
1),

(2,
'AI & ML Conference',
'Conference on AI and ML advancements.',
'Chicago',
'2025-05-15 09:00:00',
'2025-05-15 17:00:00',
'completed',
3),

(3,
'Frontend Development Bootcamp',
'Hands-on training on frontend tech.',
'Los Angeles',
'2025-07-01 10:00:00',
'2025-07-03 16:00:00',
'upcoming',
2);

INSERT INTO Sessions
(session_id, event_id, title, speaker_name, start_time, end_time)
VALUES
(1,
1,
'Opening Keynote',
'Dr. Tech',
'2025-06-10 10:00:00',
'2025-06-10 11:00:00'),

(2,
1,
'Future of Web Dev',
'Alice Johnson',
'2025-06-10 11:15:00',
'2025-06-10 12:30:00'),

(3,
2,
'AI in Healthcare',
'Charlie Lee',
'2025-05-15 09:30:00',
'2025-05-15 11:00:00'),

(4,
3,
'Intro to HTML5',
'Bob Smith',
'2025-07-01 10:00:00',
'2025-07-01 12:00:00');

INSERT INTO Registrations
(registration_id, user_id, event_id, registration_date)
VALUES
(1, 1, 1, '2025-05-01'),
(2, 2, 1, '2025-05-02'),
(3, 3, 2, '2025-04-30'),
(4, 4, 2, '2025-04-28'),
(5, 5, 3, '2025-06-15');

INSERT INTO Feedback
(feedback_id, user_id, event_id, rating, comments, feedback_date)
VALUES
(1,
3,
2,
4,
'Great insights!',
'2025-05-16'),

(2,
4,
2,
5,
'Very informative.',
'2025-05-16'),

(3,
2,
1,
3,
'Could be better.',
'2025-06-11');

INSERT INTO Resources
(resource_id, event_id, resource_type, resource_url, uploaded_at)
VALUES
(1,
1,
'pdf',
'https://portal.com/resources/tech_meetup_agenda.pdf',
'2025-05-01 10:00:00'),

(2,
2,
'image',
'https://portal.com/resources/ai_poster.jpg',
'2025-04-20 09:00:00'),

(3,
3,
'link',
'https://portal.com/resources/html5_docs',
'2025-06-25 15:00:00');
```

# SQL Exercises

## 1. User Upcoming Events
### Problem Statement
List the top 5 users who have submitted the most feedback entries.
### Query
```
SELECT u.full_name, e.title, e.city, e.start_date
FROM Users u
JOIN Registrations r ON u.user_id = r.user_id
JOIN Events e ON r.event_id = e.event_id
WHERE e.status = 'upcoming'
AND u.city = e.city
ORDER BY e.start_date;
```
### Output
<img width="941" height="348" alt="WhatsApp Image 2026-06-03 at 2 08 23 PM" src="https://github.com/user-attachments/assets/8db1b83d-db35-4ea3-b429-0eb0edd85c69" />

## 2. Top Rated Events
### Problem Statement
Identify events with the highest average rating, considering only those that have received at 
least 10 feedback submissions.
### Query
```
SELECT e.event_id, e.title, AVG(f.rating) AS avg_rating
FROM Events e
JOIN Feedback f ON e.event_id = f.event_id
GROUP BY e.event_id, e.title
HAVING COUNT(f.feedback_id) >= 10
ORDER BY avg_rating DESC;
```
### Output
Empty Set
<img width="942" height="357" alt="WhatsApp Image 2026-06-03 at 2 08 49 PM" src="https://github.com/user-attachments/assets/1615ac40-3d59-414a-9690-ccd4669ec8a6" />

## 3. Inactive Users
### Problem Statement
Retrieve users who have not registered for any events in the last 90 days.
### Query
```
SELECT u.*
FROM Users u
LEFT JOIN Registrations r
ON u.user_id = r.user_id
AND r.registration_date >= CURDATE() - INTERVAL 90 DAY
WHERE r.registration_id IS NULL;
```
### Output
<img width="931" height="328" alt="WhatsApp Image 2026-06-03 at 2 10 33 PM" src="https://github.com/user-attachments/assets/fe82cf71-5307-4e33-bde8-cc6cc851de29" />

## 4. Peak Session Hours
### Problem Statement
Count how many sessions are scheduled between 10 AM to 12 PM for each event. 
### Query
```
SELECT e.title,
COUNT(s.session_id) AS session_count
FROM Events e
LEFT JOIN Sessions s
ON e.event_id = s.event_id
WHERE TIME(s.start_time) BETWEEN '10:00:00' AND '12:00:00'
GROUP BY e.event_id, e.title;
```
### Output
<img width="935" height="341" alt="WhatsApp Image 2026-06-03 at 2 27 34 PM" src="https://github.com/user-attachments/assets/2443300d-6bde-400b-aa61-75bacb43bcf0" />

## 5. Most Active Cities
### Problem Statement
List the top 5 cities with the highest number of distinct user registrations.
### Query
```
SELECT u.city,
COUNT(DISTINCT r.user_id) AS registrations
FROM Users u
JOIN Registrations r
ON u.user_id = r.user_id
GROUP BY u.city
ORDER BY registrations DESC
LIMIT 5;
```
### Output
<img width="931" height="324" alt="WhatsApp Image 2026-06-03 at 2 37 22 PM" src="https://github.com/user-attachments/assets/d82d19e8-ce58-4d25-8dc3-7d779a1f87c7" />

## 6. Event Resource Summary
### Problem Statement
### Query
```
SELECT e.title,
SUM(CASE WHEN r.resource_type='pdf' THEN 1 ELSE 0 END) AS pdf_count,
SUM(CASE WHEN r.resource_type='image' THEN 1 ELSE 0 END) AS image_count,
SUM(CASE WHEN r.resource_type='link' THEN 1 ELSE 0 END) AS link_count
FROM Events e
LEFT JOIN Resources r
ON e.event_id = r.event_id
GROUP BY e.event_id, e.title;
```
### Output
<img width="931" height="324" alt="WhatsApp Image 2026-06-03 at 2 37 22 PM" src="https://github.com/user-attachments/assets/5d98b7d3-e6d8-413f-96e3-04cb6f6a4973" />






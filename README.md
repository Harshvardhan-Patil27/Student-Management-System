Student Management System (Backend)
Overview:
A robust backend system built with Python and SQLite to manage student enrollments, course data, and financial reporting.

This project simulates a real-world relational database environment, moving beyond simple single-table storage to handle complex Many-to-Many relationships between Students and Courses.

Key Features:
Relational Database Design: Designed a normalized schema with 3 tables: Students, Courses, and a junction table Enrollments.

Data Integrity: Implemented Foreign Key Constraints and enabled PRAGMA foreign_keys = ON to prevent invalid data entry and orphan records.

Advanced SQL Queries: Used INNER JOINs to connect three distinct tables and generate readable reports (e.g., "Which student is taking which course?").

Business Logic: Implemented SQL Aggregations (SUM, COUNT) to calculate business metrics like Total Revenue from course fees.

Tech Stack

Language: Python 3.x

Database: SQLite3 (Built-in)

Concepts: CRUD, Normalization, JOINS, Aggregation, ACID Properties.

# Feedback-System
The Feedback Management System is designed to collect, manage, and control access to feedback within an educational environment. It ensures that different users (students, teachers, and directors) interact with the system according to their roles and privileges.

🎯 Objectives

Provide students with a simple and anonymous way to submit feedback.
Allow teachers to access only the feedback relevant to them.
Enable directors/administrators to monitor and analyze all feedback for decision-making.
Ensure proper security and access control using Django’s built-in and custom permission system.

👥 User Roles & Access Control

Students
Can submit feedback about a teacher.
Feedback is anonymous to maintain student privacy.
Students cannot view or modify previously submitted feedback.

Teachers
Can log in securely.
Can view only their own feedback using a custom permission (view_own_feedback).
Cannot view feedback about other teachers.

Directors / Administrators
Can log in securely.
Have a custom permission (view_all_feedback) that allows them to view feedback for all teachers.
Can generate reports or summaries from feedback data.
Director logs in → System shows all feedback records with summary tools.

Admin manages users → Assigns teachers, and directors to appropriate groups with permissions.

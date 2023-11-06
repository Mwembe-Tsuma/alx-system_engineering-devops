
# Postmortem: Web Service Outage on November 6, 2023

![image](https://github.com/Mwembe-Tsuma/alx-system_engineering-devops/assets/49154717/09b02e00-75f3-4e35-ba4f-26e1ac1f7bed)

## Issue Summary:

* Duration: November 6, 2023, 08:00 AM — 10:30 AM
* Impact: The outage affected our e-commerce platform, resulting in a 2.5-hour downtime for approximately 20% of our users.
* Root Cause: The outage was caused by a misconfigured web server that disrupted traffic.

## Timeline:

* 08:00 AM : Issue detected by an automated monitoring alert indicating increased error rates on our e-commerce platform.
* 08:05 AM : The on-call engineer was notified and began investigating.
* 08:20 AM : Initial assumption was that a sudden increase in user traffic was causing the issues.
* 08:45 AM : After investigating the web server logs, it was suspected that the issue might be related to misconfiguration.
* 09:15 AM : The incident was escalated to the network operations team for web server
* 10:00 AM : After thorough analysis, the misconfigured web server was identified as the root cause.
* 10:30 AM : The issue was resolved by reconfiguring the web server to its default settings.

## Root Cause and Resolution:

* Root Cause: The misconfigured web server was set to server traffic erroneously , causing some serious issues, resulting in high latencies and errors for users.
* Resolution: The web server configuration was reverted to its default settings, ensuring traffics request are served properly. Further analysis confirmed that the platform was performing as expected.
Corrective and Preventative Measures:

## Improvements/Fixes:

* Implement automated configuration validation to prevent future misconfigurations.
* Enhance web server monitoring and alerting to quickly detect anomalies.
* Develop a rollback plan for critical configurations to ensure rapid recovery.

## Tasks to Address the Issue:

* Create and implement an automated configuration validation script.
* Enhance web server monitoring with alerting for uneven traffic distribution.
* Document a rollback plan for critical configurations.
* Conduct a post-incident review with the engineering and network operations teams to share lessons learned.
By following these corrective measures and implementing the outlined tasks, we aim to minimize the risk of similar incidents in the future and maintain the reliability of our e-commerce platform. We apologize for any inconvenience this outage may have caused our users and appreciate your understanding as we continue to improve our services.

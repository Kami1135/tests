# Problem
You are given a list of services, each defined with metadata including:
1) service name
2) owning team
3) criticality
4) git repo URL
5) environments it is deployed on (deploy-on)
6) tech leads
7) managers

task1:
Print services that are deployed only on prod and is critical?

task2:
Given the service data, count how many services each tech lead is involved in (regardless of criticality or environment).
Output the result as a mapping:
tech-lead-email -> number-of-services.

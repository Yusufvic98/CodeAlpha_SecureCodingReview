# CodeAlpha Secure Coding Review

## Project Overview

This project demonstrates a practical secure coding review of a small Python Secure Notes Manager. It identifies a file path traversal weakness, implements a remediation, and validates the change with automated regression tests.

## Objectives

- Identify insecure file path handling.
- Reproduce the weakness using a harmless local test file.
- Implement path containment validation.
- Verify legitimate and invalid file access.
- Document findings, remediation, and limitations.

## Vulnerability Identified

**Finding ID:** SCR-001  
**Category:** Path Traversal / Improper File Path Validation  
**Severity:** Medium (provisional)

The initial application accepted a user-supplied filename without verifying that its resolved path remained inside the intended notes directory. A controlled test confirmed that a file outside that directory could be read.

## Remediation

The updated implementation resolves the requested path and checks that it remains within the notes directory before reading it. Invalid paths are rejected with a controlled error.

## Testing

Automated tests were executed using Python's built-in `unittest` framework.

- Valid note access — passed
- Path traversal rejection — passed
- Missing note handling — passed

**Result:** 3 tests passed.

## Project Structure

- `app/` — Application source code and sample notes
- `tests/` — Automated security regression tests
- `findings/` — Security findings and remediation report
- `evidence/` — Project screenshots and supporting evidence

## Limitations

This is a local educational code review, not a comprehensive security audit. The test results validate the documented cases but do not establish the absence of all vulnerabilities. Production deployments may require additional filesystem protections.

## Technologies

- Python 3
- `pathlib`
- `unittest`
- Kali Linux
- Git

## Author

Developed as part of the CodeAlpha Cybersecurity Internship.

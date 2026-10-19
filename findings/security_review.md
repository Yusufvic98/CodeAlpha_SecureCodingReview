
# Secure Coding Review — Security Findings

## Project Overview

**Project:** CodeAlpha Secure Coding Review  
**Application:** Python Secure Notes Manager  
**Finding ID:** SCR-001  
**Category:** Path Traversal / Improper File Path Validation  
**Severity:** Medium (provisional)

## 1. Finding Description

The initial application joined a user-supplied filename to the
notes directory without verifying that the resolved path remained
inside the intended directory.

## 2. Evidence and Reproduction

A controlled test file was created outside the notes directory
but inside the project application directory.

Test input:

`../test_outside_note.txt`

Initial result:

The application returned the contents of the outside test file,
confirming that it could read beyond its intended notes directory.

No sensitive system files were accessed.

## 3. Potential Impact

Depending on deployment and filesystem permissions, an attacker
could potentially read files outside the intended notes directory.

The actual impact depends on accessible files, application
privileges, and the surrounding deployment environment.

## 4. Root Cause

The initial implementation used a path constructed directly
from user-controlled input without a containment check.

## 5. Remediation

The updated implementation resolves the requested path and uses
`Path.is_relative_to()` to verify that it remains inside the
resolved notes directory before reading the file.

Invalid paths are rejected with a controlled error.

## 6. Verification

- Python syntax compilation completed successfully.
- A valid note remained readable after remediation.
- The controlled path traversal input was rejected.
- Three automated regression tests passed:
  - Valid note access
  - Path traversal rejection
  - Missing note handling

## 7. Limitations

This was a local, controlled code review and test exercise.
The tests do not constitute a comprehensive security audit.
Additional filesystem race-condition protections may be required
for production deployments.

## 8. Conclusion

The review identified and reproduced a file path traversal
weakness. A path containment check was implemented, and the
documented functional and regression tests passed.

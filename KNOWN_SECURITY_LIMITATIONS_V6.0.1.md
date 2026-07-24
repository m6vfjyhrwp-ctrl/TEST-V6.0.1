# Known Security Limitations

A static open-source PWA cannot prevent copying or modification. An attacker controlling hosting can replace both assets and integrity metadata. Meta CSP is weaker than response-header CSP. Local storage is origin-scoped but not encrypted. Checksums provide integrity, while publisher authenticity requires a trusted detached signature or attestation.

libCertifier() -
- Utility for Linux class IoT devices to request and receive operational certificate.
- Creates a key pair (ECC 256v1)
- Creates CSR (signed)
- Creates Certificate Request Token (signed with Attestation private key)
- Request and receives certificate chain
- Stores it is pkcs12 bundle
- Written in Python
- Shared library and command-line executable.
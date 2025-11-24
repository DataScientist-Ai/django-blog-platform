# Security Policy

## Supported Versions

We actively support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 5.2.x   | :white_check_mark: |
| 5.1.x   | :white_check_mark: |
| < 5.1   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in BlogBuster, please help us by reporting it responsibly.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by emailing [INSERT YOUR EMAIL HERE] with the subject line "Security Vulnerability Report".

### What to Include

When reporting a security vulnerability, please include:

1. A clear description of the vulnerability
2. Steps to reproduce the issue
3. Potential impact of the vulnerability
4. Any suggested fixes or mitigations
5. Your contact information for follow-up questions

### Our Response Process

1. **Acknowledgment**: We'll acknowledge receipt of your report within 48 hours
2. **Investigation**: We'll investigate the issue and work on a fix
3. **Updates**: We'll keep you informed of our progress
4. **Disclosure**: We'll coordinate disclosure timing with you
5. **Fix**: We'll release a security fix as soon as possible

### Recognition

We appreciate security researchers who help keep our users safe. With your permission, we'll acknowledge your contribution in our security advisory.

## Security Best Practices

When deploying BlogBuster, please follow these security best practices:

### Environment Variables
- Never commit sensitive information to version control
- Use environment variables for secrets
- Generate strong, unique secret keys

### Database Security
- Use strong passwords for database users
- Regularly backup your database
- Keep database software updated

### Server Security
- Keep Django and all dependencies updated
- Use HTTPS in production
- Configure proper firewall rules
- Regularly monitor logs for suspicious activity

### Django Security Settings
- Set `DEBUG = False` in production
- Use strong `SECRET_KEY`
- Configure `ALLOWED_HOSTS` properly
- Enable security middleware
- Use secure cookies and sessions

## Contact

For security-related questions or concerns, please contact [INSERT YOUR EMAIL HERE].



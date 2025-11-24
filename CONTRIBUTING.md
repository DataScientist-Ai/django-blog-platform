# Contributing to BlogBuster

Thank you for your interest in contributing to BlogBuster! We welcome contributions from developers of all skill levels. This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## 🤝 Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Set up the development environment** (see below)
4. **Create a feature branch** for your changes
5. **Make your changes** following the guidelines
6. **Test your changes** thoroughly
7. **Submit a pull request**

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/blogbuster.git
   cd blogbuster
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for testing admin features)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 🤝 How to Contribute

### Types of Contributions

- **🐛 Bug fixes**: Fix existing issues
- **✨ New features**: Add new functionality
- **📚 Documentation**: Improve docs or add examples
- **🎨 UI/UX improvements**: Enhance design and user experience
- **🔧 Performance**: Optimize code and improve speed
- **🧪 Tests**: Add or improve test coverage

### Finding Issues to Work On

- Check the [Issues](https://github.com/yourusername/blogbuster/issues) tab
- Look for issues labeled `good first issue` or `help wanted`
- Comment on issues you'd like to work on to avoid duplication

## 📝 Pull Request Process

1. **Update the README.md** if your changes affect usage or installation
2. **Update documentation** for any new features
3. **Add tests** for new functionality
4. **Ensure all tests pass**
5. **Follow the coding standards** (see below)

### PR Template

When submitting a pull request, please include:

- **Description**: What changes were made and why
- **Type of change**: Bug fix, new feature, documentation, etc.
- **Testing**: How the changes were tested
- **Screenshots**: For UI changes (if applicable)
- **Breaking changes**: Any breaking changes and migration steps

## 💻 Coding Standards

### Python Code

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black formatter default)
- Use descriptive variable and function names
- Add docstrings to classes and functions

### Django-Specific Guidelines

- Use Django's class-based views when appropriate
- Follow Django's naming conventions for models, views, and URLs
- Use Django's built-in authentication and authorization
- Optimize database queries (use `select_related` and `prefetch_related`)
- Use Django's form validation and error handling

### HTML/CSS/JavaScript

- Use semantic HTML5 elements
- Follow BEM methodology for CSS class naming
- Ensure responsive design works on all screen sizes
- Minimize JavaScript for better performance
- Use Tailwind CSS utility classes consistently

### Git Commit Messages

Use clear, descriptive commit messages:

```
feat: add user authentication system
fix: resolve mobile menu toggle issue
docs: update installation instructions
style: format code with black
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test blog_buster

# Run with coverage
coverage run manage.py test
coverage report
```

### Writing Tests

- Write unit tests for models, views, and utility functions
- Write integration tests for user workflows
- Use Django's `TestCase` for database-related tests
- Aim for at least 80% test coverage

## 📚 Documentation

### Code Documentation

- Add docstrings to all classes, methods, and functions
- Use Google-style docstrings
- Document parameters, return values, and exceptions

### User Documentation

- Update `README.md` for new features
- Update `ADMIN_GUIDE.md` for admin panel changes
- Add screenshots for UI changes
- Create tutorials for complex features

## 🎯 Development Workflow

1. **Choose an issue** or create one describing the feature/bug
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make changes** following the coding standards
4. **Write tests** for new functionality
5. **Test thoroughly** - both automated and manual testing
6. **Update documentation** if needed
7. **Commit changes** with clear messages
8. **Push to your fork**: `git push origin feature/your-feature-name`
9. **Create a Pull Request** with detailed description

## 📞 Getting Help

If you need help or have questions:

- Check existing [Issues](https://github.com/YOUR_USERNAME/blogbuster/issues) and [Discussions](https://github.com/YOUR_USERNAME/blogbuster/discussions)
- Create a new issue for bugs or feature requests
- Ask questions in the discussions section

## 🙏 Recognition

Contributors will be recognized in:
- The project's contributor list
- Release notes for significant contributions
- Special mentions for major features

Thank you for contributing to BlogBuster! 🎉

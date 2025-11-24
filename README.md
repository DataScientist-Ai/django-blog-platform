# BlogBuster 📰

A modern, feature-rich Django blog platform inspired by Lifewire.com, built with Tailwind CSS and designed for professional content management.

![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4+-38B2AC.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎨 **Modern Design**
- **Lifewire-inspired UI** with clean, professional aesthetics
- **Responsive design** that works perfectly on all devices
- **Tailwind CSS** for modern, maintainable styling
- **Custom color scheme** with brand-consistent theming

### 📝 **Content Management**
- **Multiple content types**: Posts, Buying Guides, Product Reviews, How-To Series
- **Rich text editing** with featured images and categories
- **SEO-optimized** URLs and meta information
- **Draft/Published** workflow with scheduling

### 🎛️ **Admin-Controlled Widgets**
- **Homepage widgets**: Hero section, trending posts, quick tips, newsletter signup
- **Sidebar widgets**: Popular posts, related content, author bio, social sharing
- **Dynamic content blocks** that can be toggled on/off via admin
- **Customizable layouts** for different page types

### 🔍 **Advanced Features**
- **Search functionality** across all content
- **Category and tag filtering**
- **Pagination** for large content lists
- **Reading time estimation**
- **View tracking** and analytics

### 🛍️ **E-commerce Ready**
- **Buying guides** with product comparisons and affiliate links
- **Product reviews** with structured scoring and pros/cons
- **Affiliate link management**
- **Verdict-based recommendations**

### 📱 **Developer-Friendly**
- **Well-documented code** with comprehensive admin guide
- **Management commands** for seeding demo content
- **Modular architecture** for easy customization
- **Docker-ready** setup (optional)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/blogbuster.git
   cd blogbuster
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Seed demo content (optional)**
   ```bash
   python manage.py seed_demo_content
   python manage.py seed_sidebar_widgets
   python manage.py assign_dummy_images
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - **Homepage**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

## 📖 Usage Guide

### Admin Panel Overview

The admin panel provides comprehensive control over all aspects of your blog:

#### Content Management
- **Posts**: Create and manage blog articles
- **Categories**: Organize content into topics
- **Tags**: Add searchable keywords to posts
- **Buying Guides**: Curate product recommendations
- **Product Reviews**: Write detailed product analyses
- **How-To Series**: Create step-by-step tutorials

#### Widget Management
- **Homepage Settings**: Control hero section and newsletter
- **Quick Tips**: Manage homepage tip cards
- **Sidebar Widgets**: Configure post page sidebars

### Content Types

#### Posts
Standard blog posts with rich content, categories, tags, and featured images.

#### Buying Guides
Curated lists of product recommendations with:
- Product comparisons
- Affiliate links
- Price ranges
- Pros/cons analysis
- Verdict badges

#### Product Reviews
Comprehensive product evaluations featuring:
- Overall scoring (0-10 scale)
- Category-specific ratings
- Pros and cons lists
- "Why Trust Us" credibility sections
- Affiliate integration

#### How-To Series
Step-by-step tutorial guides with:
- Difficulty levels
- Prerequisites
- Estimated completion time
- Progress tracking

## 🏗️ Project Structure

```
blogbuster/
├── blog_buster/              # Main Django app
│   ├── management/commands/  # Custom management commands
│   ├── migrations/           # Database migrations
│   ├── models.py            # Data models
│   ├── views.py             # View functions
│   ├── admin.py             # Admin configuration
│   ├── urls.py              # URL routing
│   └── context_processors.py # Template context processors
├── templates/               # HTML templates
│   └── blog_buster/
│       ├── base.html
│       ├── index.html
│       ├── post_detail.html
│       └── partials/
├── static/                  # Static assets
│   ├── css/
│   └── js/
├── media/                   # User-uploaded files
├── blogbuster/              # Django project settings
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🎨 Customization

### Themes and Styling
- Built with **Tailwind CSS** for easy customization
- CSS variables for consistent theming
- Responsive breakpoints for all screen sizes

### Widget Configuration
All widgets are configurable through the admin panel:
- Enable/disable individual widgets
- Set display limits and ordering
- Customize text and links

### Content Types
Add new content types by extending the existing models or creating new Django apps.

## 🔧 Development

### Management Commands

```bash
# Seed demo data
python manage.py seed_demo_content
python manage.py seed_sidebar_widgets
python manage.py assign_dummy_images

# Django standard commands
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### Testing

```bash
# Run tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production (Example with Gunicorn)
```bash
pip install gunicorn
gunicorn blogbuster.wsgi:application --bind 0.0.0.0:8000
```

### Docker (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "blogbuster.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive docstrings
- Add tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the clean design and comprehensive content strategy of [Lifewire.com](https://www.lifewire.com/)
- Built with [Django](https://www.djangoproject.com/) web framework
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- Icons and UI components inspired by modern web design patterns

## 📞 Support

For questions or support:
- Open an issue on GitHub
- Check the [Admin Guide](ADMIN_GUIDE.md) for detailed usage instructions
- Review the code comments for technical details

---

**Made with ❤️ by developers, for developers and content creators.**

⭐ Star this repo if you find it helpful!

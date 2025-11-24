# BlogBuster Admin Guide

## Overview

BlogBuster is a comprehensive blog platform with multiple content types and admin-controlled widgets. This guide covers all administrative functionality.

---

# Content Management

## Step 1: Create a Superuser (Admin Account)

If you haven't created an admin account yet, run this command in your terminal:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- Username (e.g., `admin`)
- Email address (optional)
- Password (enter twice)

## Step 2: Start the Development Server

Make sure your server is running:

```bash
python manage.py runserver
```

## Step 3: Access the Admin Panel

1. Open your browser and go to: **http://localhost:8000/admin/**
2. Log in with the superuser credentials you just created

## Step 4: Add Categories (Recommended First)

Before creating posts, it's good to have categories set up:

1. In the admin panel, click on **"Categories"** under "BLOG_BUSTER"
2. Click **"Add Category"** button (top right)
3. Fill in:
   - **Name**: e.g., "Technology", "Tutorials", "News"
   - **Slug**: Will auto-generate from name (or customize it)
   - **Description**: Optional description of the category
4. Click **"Save"**

## Step 5: Add Tags (Optional but Recommended)

1. Click on **"Tags"** under "BLOG_BUSTER"
2. Click **"Add Tag"** button
3. Fill in:
   - **Name**: e.g., "Python", "Django", "Web Development"
   - **Slug**: Will auto-generate
4. Click **"Save"**

## Step 6: Create Your First Post

1. Click on **"Posts"** under "BLOG_BUSTER"
2. Click **"Add Post"** button (top right)

### Fill in the Post Details:

**Content Section:**
- **Title**: Your post title (e.g., "Getting Started with Django")
- **Slug**: Auto-generates from title (URL-friendly version)
- **Author**: Select your user account from dropdown
- **Excerpt**: Short description (appears in post previews) - max 300 characters
- **Content**: Your full blog post content (supports line breaks)
- **Featured image**: Upload an image (optional but recommended)

**Categorization Section:**
- **Category**: Select a category from dropdown
- **Tags**: Select one or more tags (hold Ctrl/Cmd to select multiple)

**Publishing Section:**
- **Status**: 
  - Choose **"Published"** to make it visible on the site
  - Choose **"Draft"** to save it for later
- **Featured**: Check this box to feature the post on homepage
- **Published at**: Leave blank (auto-fills when you save as "Published")

**Statistics Section:**
- Views, Created at, Updated at are auto-managed

3. Click **"Save"** or **"Save and add another"** or **"Save and continue editing"**

## Step 7: View Your Post

After saving a published post:
- Go to: **http://localhost:8000/** (homepage)
- Or: **http://localhost:8000/posts/** (all posts)
- Click on your post to view the full article

## Tips:

1. **Featured Posts**: Check "Featured" to show on homepage
2. **Drafts**: Use "Draft" status to work on posts before publishing
3. **Images**: Upload featured images for better visual appeal
4. **Excerpts**: Write compelling excerpts (they appear in post cards)
5. **Tags**: Use relevant tags to help readers find related content
6. **Categories**: Organize posts into logical categories

## Quick Access URLs:

- Admin Panel: http://localhost:8000/admin/
- Homepage: http://localhost:8000/
- All Posts: http://localhost:8000/posts/
- Admin Posts: http://localhost:8000/admin/blog_buster/post/

---

# Advanced Content Types

## Buying Guides

Buying guides help readers make informed purchase decisions with curated product recommendations.

### Creating a Buying Guide

1. Go to **"Buying Guides"** in admin
2. Click **"Add Buying Guide"**
3. Fill in:
   - **Title**: e.g., "Best Wireless Earbuds of 2025"
   - **Slug**: Auto-generated from title
   - **Summary**: Overview paragraph
   - **Category**: Select relevant category
   - **Hero Quote**: Optional quote to display prominently
   - **Published**: Check to make live
   - **Featured**: Check to highlight on homepage

### Adding Guide Picks

After creating the guide, add individual product recommendations:

1. In the guide admin, use the **"Guide Picks"** inline form
2. Add each product:
   - **Title**: Product name
   - **Verdict**: e.g., "Best Overall", "Best Budget", "Best Premium"
   - **Tagline**: Short selling point
   - **Pros**: One per line (press Enter for each)
   - **Cons**: One per line
   - **Price Range**: e.g., "$50-$100"
   - **Affiliate URL**: Optional affiliate link
   - **Rating**: 1-5 stars
   - **Sort Order**: Controls display order

## Product Reviews

Full product review articles with structured scoring and editorial content.

### Creating a Product Review

1. Go to **"Product Reviews"** in admin
2. Click **"Add Product Review"**
3. Fill in:
   - **Product Name**: The product being reviewed
   - **Slug**: Auto-generated
   - **Summary**: Brief overview
   - **Verdict**: Final recommendation statement
   - **Affiliate URL**: Optional affiliate link
   - **Hero Image**: Product image
   - **Overall Score**: 0-10 scale
   - **Pros/Cons**: One per line
   - **Why Trust Us**: Editorial credibility statement
   - **Methodology**: How the review was conducted
   - **Published/Featured**: Visibility controls

### Adding Review Scores

Use the **"Review Scores"** inline form to add category-specific ratings:
- **Label**: e.g., "Design", "Performance", "Value"
- **Score**: 0-10 scale

## How-To Series

Step-by-step tutorial series with prerequisites and difficulty levels.

### Creating a How-To Series

1. Go to **"How-To Series"** in admin
2. Click **"Add How-To Series"**
3. Fill in:
   - **Title**: Tutorial name
   - **Slug**: Auto-generated
   - **Intro**: Introduction/overview
   - **Difficulty**: Beginner/Intermediate/Advanced
   - **Estimated Time**: e.g., "30 minutes"
   - **Prerequisites**: One item per line
   - **Published/Featured**: Visibility controls

### Adding Tutorial Steps

Use the **"How-To Steps"** inline form:
- **Step Number**: Order (1, 2, 3...)
- **Title**: Step headline
- **Instructions**: Detailed instructions
- **Tip**: Optional additional advice

---

# Widget Management

## Homepage Widgets

### Homepage Settings

Control hero section and newsletter signup:

1. Go to **"Homepage settings"** (under Blog_buster)
2. Edit:
   - **Hero section**: Heading, subheading, CTA buttons
   - **Newsletter**: Description, button text, disclaimer

### Quick Tips

Manage homepage tip cards:

1. Go to **"Quick Tips"** in admin
2. Add/edit tips with title, description, and display order
3. Toggle **"Is active"** to show/hide

## Sidebar Widgets

Control post detail page sidebars via **"Sidebar Widgets"**:

### Widget Types Available:

1. **Popular Posts**: Shows most-viewed posts (configurable time period and count)
2. **Related Posts**: Shows posts from same category/tags (configurable count)
3. **Author Bio**: Author information with optional avatar and social links
4. **Social Share**: Share buttons for Facebook, Twitter, LinkedIn, Pinterest, Email
5. **Newsletter**: Sidebar signup form with custom text
6. **Categories**: Category list with optional post counts
7. **Recent Posts**: Latest published posts
8. **Quick Tips**: Editorial tips from database
9. **Buying Guides**: Featured buying guides

### Managing Sidebar Widgets:

1. Go to **"Sidebar Widgets"** in admin
2. **Enable/disable** widgets with the **"Is active"** checkbox
3. **Reorder** widgets by editing **"Sort order"** (lower numbers appear first)
4. **Configure** each widget type by clicking on the widget and editing its specific settings

### Widget-Specific Configuration:

- **Popular Posts**: Set post count and time period (days)
- **Related Posts**: Set post count and enable category/tag matching
- **Author Bio**: Add biography text, avatar image, social links toggle
- **Social Share**: Enable/disable individual social platforms
- **Newsletter**: Customize description, button text, privacy disclaimer
- **Categories**: Set max categories and toggle post count display
- **Recent Posts**: Set post count
- **Quick Tips**: Set tip count to display
- **Buying Guides**: Set guide count to display

---

# Utility Commands

## Content Seeding

```bash
# Seed demo posts and user
python manage.py seed_demo_content

# Seed sidebar widgets with default configs
python manage.py seed_sidebar_widgets

# Generate dummy images for posts
python manage.py assign_dummy_images
```

## Development

```bash
# Run development server
python manage.py runserver

# Access admin panel
# http://localhost:8000/admin/

# Create superuser if needed
python manage.py createsuperuser
```

---

# Content Strategy Tips

## Post Categories
- **Technology**: Hardware, software, gadgets
- **Tutorials**: How-to guides, programming, tools
- **Reviews**: Product reviews, comparisons
- **News**: Industry updates, announcements

## Widget Strategy
- **Homepage**: Focus on engagement - featured content, quick tips, newsletter
- **Post Sidebars**: Balance promotion (newsletter, related content) with utility (social share, categories)

## Editorial Workflow
1. Create categories first
2. Write and publish posts
3. Create buying guides for evergreen content
4. Add reviews for current products
5. Build how-to series for educational content
6. Configure widgets to surface content appropriately

---

# Technical Notes

- All content types support **draft/published** status and **featured** flags
- **SEO-friendly** slugs auto-generate from titles
- **Image handling** for featured images and hero graphics
- **Responsive design** works on all devices
- **Admin customization** allows full content and widget control
- **Performance optimized** with database indexes and efficient queries


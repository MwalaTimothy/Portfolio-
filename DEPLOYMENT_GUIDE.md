# 🚀 GitHub Pages Deployment Guide

This guide will walk you through hosting your portfolio website on GitHub Pages for free.

## 📋 Prerequisites

- A GitHub account (create one at [github.com](https://github.com) if you don't have one)
- Your portfolio files (already created ✅)
- Git repository initialized (already done ✅)

## 🎯 Step-by-Step Deployment

### Step 1: Create a GitHub Repository

1. **Go to GitHub.com** and sign in to your account
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Choose a repository name:**
   - **Option A**: `portfolio` (simple name)
   - **Option B**: `yourusername.github.io` (where yourusername is your GitHub username)
5. **Make sure the repository is PUBLIC** (required for free GitHub Pages)
6. **Do NOT initialize with README** (we already have files)
7. **Click "Create repository"**

### Step 2: Connect Local Repository to GitHub

Open PowerShell in your portfolio folder and run these commands:

```bash
# Navigate to your portfolio folder (if not already there)
cd "c:\Users\USER\OneDrive\Portfolio"

# Add your GitHub repository as the remote origin
# Replace 'yourusername' and 'repository-name' with your actual values
git remote add origin https://github.com/yourusername/repository-name.git

# Rename the default branch to main
git branch -M main

# Push your code to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. **Go to your repository** on GitHub.com
2. **Click on "Settings"** tab (at the top of the repository)
3. **Scroll down to "Pages"** in the left sidebar
4. **Under "Source"**, select **"Deploy from a branch"**
5. **Select branch**: Choose **"main"**
6. **Select folder**: Choose **"/ (root)"**
7. **Click "Save"**

### Step 4: Access Your Live Website

After 5-10 minutes, your website will be available at:
- **If repository name is `portfolio`**: `https://yourusername.github.io/portfolio`
- **If repository name is `yourusername.github.io`**: `https://yourusername.github.io`

## 🔧 Important Customizations Before Going Live

### 1. Update Personal Information

Edit `index.html` and replace:
- **"Your Name"** → Your actual name
- **Email address** → your.email@example.com
- **Phone number** → Your phone number
- **Location** → Your city/country
- **Social media links** → Your actual profiles

### 2. Add Your Images

Place these images in the `images/` folder:
- **`profile.jpg`** - Your professional headshot (350x350px or larger)
- **`about.jpg`** - About section image (600x400px or larger)  
- **`project1.jpg`** - First project screenshot (600x300px or larger)
- **`project2.jpg`** - Second project screenshot
- **`project3.jpg`** - Third project screenshot

### 3. Update Project Information

In `index.html`, modify the projects section with:
- **Real project titles and descriptions**
- **Actual GitHub repository links**
- **Live demo links**
- **Correct technology tags**

### 4. Customize Content

- **About section**: Write your actual bio and experience
- **Skills section**: Update with your real technical skills
- **Statistics**: Update the numbers (projects completed, years experience, etc.)

## 📱 Testing Your Website

### Local Testing
1. Open `index.html` in your browser
2. Test on different screen sizes (resize browser window)
3. Check all links and functionality

### After Deployment
1. Visit your GitHub Pages URL
2. Test on mobile devices
3. Check loading speed
4. Verify all images display correctly

## 🔄 Updating Your Website

After making changes:

```bash
# Add changes to git
git add .

# Commit changes
git commit -m "Update portfolio content"

# Push to GitHub
git push origin main
```

Your website will automatically update within a few minutes.

## 🎨 Advanced Customizations

### Custom Domain (Optional)
1. Buy a domain name
2. Create a `CNAME` file in your repository root with your domain
3. Configure DNS settings with your domain provider
4. Update GitHub Pages settings to use custom domain

### Analytics (Optional)
Add Google Analytics code before closing `</body>` tag in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

## 🐛 Troubleshooting

### Website Not Loading
- Check if repository is public
- Verify GitHub Pages is enabled in settings
- Wait 10-15 minutes for first deployment

### Images Not Showing
- Ensure image files are in the correct `images/` folder
- Check file names match exactly (case-sensitive)
- Verify images were committed and pushed to GitHub

### CSS/JavaScript Not Working
- Check file paths in `index.html`
- Ensure all files were uploaded to GitHub
- Clear browser cache and refresh

## 📞 Need Help?

If you encounter issues:
1. Check the [GitHub Pages documentation](https://docs.github.com/en/pages)
2. Verify all files are committed and pushed
3. Check repository settings
4. Wait for deployment (can take up to 10 minutes)

## 🎉 Congratulations!

Your portfolio website is now live and accessible to the world! Share your URL with potential employers, clients, and on your social media profiles.

**Remember to**:
- Keep your portfolio updated with new projects
- Regularly commit and push changes
- Monitor your website for any issues
- Update your resume with the portfolio URL
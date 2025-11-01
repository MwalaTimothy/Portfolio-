# Deploy Portfolio to GitHub Pages
# PowerShell script to set up the repository and deploy

Write-Host "Setting up Timothy Mwala Portfolio for GitHub Pages deployment..." -ForegroundColor Green

# Initialize Git repository if not already done
if (-not (Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Yellow
    git init
}

# Add all files
Write-Host "Adding files to Git..." -ForegroundColor Yellow
git add .

# Commit changes
Write-Host "Committing changes..." -ForegroundColor Yellow
git commit -m "Initial portfolio deployment - Timothy Mwala M.Sc. Electronics & Instrumentation"

# Add remote origin (replace with your actual repository URL)
Write-Host "Adding remote origin..." -ForegroundColor Yellow
git branch -M main

# Push to GitHub
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "Please run the following commands to complete deployment:" -ForegroundColor Cyan
Write-Host ""
Write-Host "git remote add origin https://github.com/MwalaTimothy/Portfolio-.git" -ForegroundColor White
Write-Host "git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "Then go to your GitHub repository settings and:" -ForegroundColor Cyan
Write-Host "1. Navigate to Settings > Pages" -ForegroundColor White
Write-Host "2. Set Source to 'GitHub Actions'" -ForegroundColor White
Write-Host "3. The site will be available at: https://mwalatimothy.github.io/Portfolio-/" -ForegroundColor White
Write-Host ""
Write-Host "Portfolio deployment setup complete! 🚀" -ForegroundColor Green
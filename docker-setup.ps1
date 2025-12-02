# Quick Start Script for AI Image Generator
# Run this to test your Docker setup

Write-Host "🎨 AI Image Generator - Docker Setup" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is installed
Write-Host "Checking Docker installation..." -ForegroundColor Yellow
try {
    $dockerVersion = docker --version
    Write-Host "✅ Docker found: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker not found! Please install Docker Desktop first." -ForegroundColor Red
    Write-Host "Download from: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Choose an option:" -ForegroundColor Cyan
Write-Host "1. Build and run with Docker Compose (Recommended)" -ForegroundColor White
Write-Host "2. Build Docker image only" -ForegroundColor White
Write-Host "3. Run existing image" -ForegroundColor White
Write-Host "4. Stop and remove containers" -ForegroundColor White
Write-Host "5. View logs" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter your choice (1-5)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "🚀 Building and starting with Docker Compose..." -ForegroundColor Yellow
        docker-compose up -d --build
        Write-Host ""
        Write-Host "✅ Done! App should be running at http://localhost:8501" -ForegroundColor Green
        Write-Host "📊 View logs with: docker-compose logs -f" -ForegroundColor Cyan
    }
    "2" {
        Write-Host ""
        Write-Host "🔨 Building Docker image..." -ForegroundColor Yellow
        docker build -t ai-image-generator .
        Write-Host ""
        Write-Host "✅ Image built successfully!" -ForegroundColor Green
        Write-Host "🚀 Run with: docker run -p 8501:8501 ai-image-generator" -ForegroundColor Cyan
    }
    "3" {
        Write-Host ""
        Write-Host "🚀 Starting container..." -ForegroundColor Yellow
        docker run -d -p 8501:8501 --name ai-image-gen ai-image-generator
        Write-Host ""
        Write-Host "✅ Container started!" -ForegroundColor Green
        Write-Host "🌐 Open http://localhost:8501 in your browser" -ForegroundColor Cyan
    }
    "4" {
        Write-Host ""
        Write-Host "🛑 Stopping containers..." -ForegroundColor Yellow
        docker-compose down
        Write-Host "✅ Containers stopped and removed" -ForegroundColor Green
    }
    "5" {
        Write-Host ""
        Write-Host "📊 Showing logs (Ctrl+C to exit)..." -ForegroundColor Yellow
        docker-compose logs -f
    }
    default {
        Write-Host "❌ Invalid choice" -ForegroundColor Red
    }
}

# 🚀 Quick Reference - AI Image Generator

## 📦 Your Configuration

- **Docker Hub**: `parthibanktech3/ai-image-generator`
- **GitHub**: (Your repository)
- **Render**: (Will be created when you deploy)

## ⚡ Quick Commands

### Local Development
```bash
# Run the app
streamlit run app.py

# Access at: http://localhost:8501
```

### Docker Local
```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Git Commands
```bash
# Initial setup
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main

# Regular updates
git add .
git commit -m "Your message"
git push
```

### Docker Hub
```bash
# Build
docker build -t parthibanktech3/ai-image-generator .

# Login
docker login

# Push
docker push parthibanktech3/ai-image-generator

# Pull (from any machine)
docker pull parthibanktech3/ai-image-generator
docker run -p 8501:8501 parthibanktech3/ai-image-generator
```

## 🎯 Deployment Options

### Option 1: Render (Easiest)
1. Push to GitHub
2. Go to https://dashboard.render.com/
3. New + → Blueprint
4. Select your repo
5. Click "Apply"
6. Done! ✅

### Option 2: Docker Hub + GitHub Actions
1. Add `DOCKERHUB_TOKEN` to GitHub Secrets
2. Push to GitHub
3. Auto-builds to `parthibanktech3/ai-image-generator`
4. Pull and run anywhere

### Option 3: Local Docker
```bash
docker-compose up -d
```

## 📁 Important Files

| File | Purpose |
|------|---------|
| `START_HERE.md` | Main navigation |
| `DEPLOYMENT_CHECKLIST.md` | Step-by-step deployment |
| `RENDER_DEPLOY.md` | Render quick guide |
| `render.yaml` | Render configuration |
| `Dockerfile` | Container config |
| `docker-compose.yml` | Local deployment |
| `.github/workflows/docker-build.yml` | CI/CD |

## 🔑 GitHub Secrets Needed

For auto-build to Docker Hub:
- `DOCKERHUB_TOKEN` - Get from https://hub.docker.com/settings/security

(Username `parthibanktech3` is already configured)

## 🌐 URLs After Deployment

### Render
- Will be: `https://ai-image-generator-xxxx.onrender.com`
- You'll get this after deployment

### Docker Hub
- Image: `parthibanktech3/ai-image-generator`
- URL: https://hub.docker.com/r/parthibanktech3/ai-image-generator

### Local
- Always: `http://localhost:8501`

## ✅ What Works

- ✅ Text-to-Image (all modes)
- ✅ Background Removal
- ✅ Quality Presets
- ✅ Docker Deployment
- ⚠️ Image Editing (limited on free APIs)

## 🆘 Quick Troubleshooting

### App won't start
```bash
# Check if port is in use
netstat -ano | findstr :8501

# Kill process if needed
taskkill /PID <PID> /F
```

### Docker issues
```bash
# Clean up
docker-compose down
docker system prune -a

# Rebuild
docker-compose up --build
```

### Git issues
```bash
# Check status
git status

# Reset if needed
git reset --hard HEAD
```

## 📞 Need Help?

1. **Deployment**: See `DEPLOYMENT_CHECKLIST.md`
2. **Image Editing**: See `IMG2IMG_ISSUES.md`
3. **General**: See `README.md`
4. **Render**: See `RENDER_DEPLOY.md`

## 🎯 Next Steps

1. ✅ Read `START_HERE.md`
2. ✅ Follow `DEPLOYMENT_CHECKLIST.md`
3. ✅ Push to GitHub
4. ✅ Deploy to Render
5. ✅ Share your app!

---

**Everything is configured and ready to deploy!** 🚀

Your Docker Hub: `parthibanktech3/ai-image-generator`

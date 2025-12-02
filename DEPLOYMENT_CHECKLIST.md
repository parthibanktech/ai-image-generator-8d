# 📋 Deployment Checklist

## ✅ Pre-Deployment

- [ ] All files are saved
- [ ] Test locally: `streamlit run app.py`
- [ ] Test Docker: `docker-compose up`
- [ ] Review `.gitignore` (don't commit secrets!)
- [ ] Update README if needed

## 🐙 GitHub Setup

### 1. Initialize Git (if not done)
```bash
cd c:\study\python\irctc-app\ai_image_generator
git init
git add .
git commit -m "Initial commit: AI Image Generator"
```

### 2. Create GitHub Repository
- Go to https://github.com/new
- Name: `ai-image-generator`
- Don't initialize with README (you already have one)
- Click "Create repository"

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/ai-image-generator.git
git branch -M main
git push -u origin main
```

### 4. Setup GitHub Actions (for Docker Hub auto-build)
- Go to repository Settings → Secrets and variables → Actions
- Add secrets:
  - `DOCKERHUB_USERNAME`: Your Docker Hub username (e.g., `parthibanktech3`)
  - `DOCKERHUB_TOKEN`: Your Docker Hub access token (get from https://hub.docker.com/settings/security)
- Next push will trigger auto-build to `YOUR_USERNAME/ai-image-generator`

## 🚀 Render Deployment

### Option A: Using render.yaml (Easiest)
- [ ] Push code to GitHub (see above)
- [ ] Go to https://dashboard.render.com/
- [ ] Click "New +" → "Blueprint"
- [ ] Select your GitHub repository
- [ ] Render detects `render.yaml` automatically
- [ ] Click "Apply"
- [ ] Wait for deployment (~5 minutes)
- [ ] Access your app at the provided URL

### Option B: Manual Render Setup
- [ ] Go to https://dashboard.render.com/
- [ ] Click "New +" → "Web Service"
- [ ] Connect GitHub repository
- [ ] Configure:
  - Name: `ai-image-generator`
  - Environment: `Docker`
  - Plan: `Free` (or `Starter` for $7/month)
  - Dockerfile Path: `./Dockerfile`
  - Port: `8501`
- [ ] Add environment variables (optional):
  - `HF_TOKEN`
  - `OPENROUTER_API_KEY`
- [ ] Click "Create Web Service"

## 🐳 Docker Hub (Optional)

### If using GitHub Actions:
- [ ] Create Docker Hub account: https://hub.docker.com/
- [ ] Create access token: https://hub.docker.com/settings/security
- [ ] Add to GitHub Secrets (see above)
- [ ] Push to GitHub → Auto-builds to Docker Hub

### Manual Docker Push:
```bash
docker build -t parthibanktech3/ai-image-generator .
docker login
docker push parthibanktech3/ai-image-generator
```

## 🧪 Post-Deployment Testing

### Test Your Deployed App
- [ ] Visit your Render URL
- [ ] Test Text-to-Image generation
- [ ] Test Background Removal (if image uploaded)
- [ ] Try different quality presets
- [ ] Check all deployment modes work

### Monitor Performance
- [ ] Check Render dashboard for logs
- [ ] Monitor response times
- [ ] Check for errors in logs

## 📝 Documentation Updates

- [ ] Update README with your Render URL
- [ ] Add screenshots if desired
- [ ] Update any custom instructions

## 🎯 Optional Enhancements

- [ ] Set up custom domain on Render
- [ ] Enable Render auto-deploy on push
- [ ] Set up monitoring/alerts
- [ ] Add analytics (if needed)

## 🔒 Security Checklist

- [ ] Never commit `.env` file
- [ ] API keys are in environment variables only
- [ ] `.gitignore` is properly configured
- [ ] Secrets are in Render environment variables

## 📊 Files Checklist

Make sure these files exist:
- [ ] `app.py` - Main application
- [ ] `Dockerfile` - Container config
- [ ] `docker-compose.yml` - Local deployment
- [ ] `render.yaml` - Render deployment
- [ ] `requirements.txt` - Dependencies
- [ ] `.gitignore` - Git ignore rules
- [ ] `.dockerignore` - Docker ignore rules
- [ ] `README.md` - Documentation
- [ ] `DEPLOYMENT.md` - Deployment guide
- [ ] `RENDER_DEPLOY.md` - Render quick guide
- [ ] `.github/workflows/docker-build.yml` - CI/CD

## 🎉 Success Criteria

Your deployment is successful when:
- [ ] App loads at Render URL
- [ ] Text-to-Image works
- [ ] No errors in Render logs
- [ ] All modes are selectable
- [ ] Background removal works (with uploaded image)

## 🆘 If Something Goes Wrong

1. **Check Render Logs**
   - Dashboard → Your Service → Logs
   
2. **Common Issues**
   - Port mismatch: Ensure port 8501
   - Build fails: Check Dockerfile syntax
   - App crashes: Check Python dependencies
   
3. **Get Help**
   - See `DEPLOYMENT.md`
   - See `IMG2IMG_ISSUES.md`
   - Check Render documentation
   - Open GitHub issue

## 📞 Quick Commands Reference

```bash
# Local testing
streamlit run app.py

# Docker testing
docker-compose up

# Git commands
git add .
git commit -m "Update"
git push

# Docker build
docker build -t ai-image-generator .
```

---

**Ready to deploy? Start with the GitHub Setup section above!** 🚀

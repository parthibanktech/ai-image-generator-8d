# 🚀 Quick Deploy to Render

## Step-by-Step Guide

### Prerequisites
- GitHub account
- Render account (free): https://render.com/

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to https://dashboard.render.com/
   - Click "New +" → "Blueprint"
   - Select your repository
   - Render will detect `render.yaml` automatically
   - Click "Apply"

3. **Add Environment Variables (Optional)**
   - In Render dashboard, go to your service
   - Click "Environment"
   - Add:
     - `HF_TOKEN` = your_huggingface_token
     - `OPENROUTER_API_KEY` = your_openrouter_key

4. **Access Your App**
   - Render will provide a URL like: `https://ai-image-generator-xxxx.onrender.com`
   - First load may take 1-2 minutes (cold start on free tier)

## 🎯 What's Included in render.yaml

- ✅ Docker-based deployment
- ✅ Free tier compatible
- ✅ Health check configured
- ✅ Auto-deploy on git push
- ✅ Environment variables support

## 💡 Tips

### Free Tier
- ✅ Good for testing and demos
- ⚠️ Spins down after 15 minutes of inactivity
- ⚠️ Cold start takes ~1 minute

### Paid Tier ($7/month)
- ✅ No cold starts
- ✅ Always available
- ✅ Better performance
- ✅ More resources

## 🔧 Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Ensure all files are committed
- Check Render build logs

### App Won't Start
- Check port is 8501
- Verify health check path: `/_stcore/health`
- Check environment variables

### Slow Performance
- Free tier has limited resources
- Upgrade to Starter plan
- Or use Docker on your own server

## 📝 render.yaml Explained

```yaml
services:
  - type: web              # Web service type
    name: ai-image-generator
    runtime: docker        # Use Docker
    plan: free            # Free tier (change to 'starter' for paid)
    dockerfilePath: ./Dockerfile
    dockerContext: .
    envVars:              # Environment variables
      - key: PORT
        value: 8501       # Streamlit port
      - key: HF_TOKEN
        sync: false       # Don't sync, set manually
      - key: OPENROUTER_API_KEY
        sync: false
    healthCheckPath: /_stcore/health  # Streamlit health endpoint
    autoDeploy: true      # Auto-deploy on git push
```

## 🎉 That's It!

Your app is now deployed and accessible worldwide!

**Next Steps:**
- Share your Render URL
- Monitor usage in Render dashboard
- Upgrade to paid tier if needed
- Set up custom domain (optional)

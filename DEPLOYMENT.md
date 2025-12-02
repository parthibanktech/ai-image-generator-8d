# AI Image Generator - Deployment Guide

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Docker Deployment

#### Option 1: Docker Compose (Recommended)
```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

#### Option 2: Docker CLI
```bash
# Build image
docker build -t ai-image-generator .

# Run container
docker run -p 8501:8501 \
  -e HF_TOKEN=your_token_here \
  ai-image-generator
```

## 🌐 Cloud Deployment

### Deploy to Render

#### Option 1: Using render.yaml (Recommended)
1. Fork/push this repository to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New +" → "Blueprint"
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml`
6. Add environment variables (optional):
   - `HF_TOKEN`
   - `OPENROUTER_API_KEY`
7. Click "Apply" to deploy

#### Option 2: Manual Setup
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: ai-image-generator
   - **Environment**: Docker
   - **Plan**: Free or Starter
   - **Dockerfile Path**: ./Dockerfile
   - **Port**: 8501
5. Add environment variables if needed
6. Click "Create Web Service"

**Note**: Free tier may have cold starts. Upgrade to Starter ($7/month) for better performance.

### Deploy to Railway
1. Fork this repository
2. Go to [Railway](https://railway.app/)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variables if needed
6. Deploy!

### Deploy to Fly.io
```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Launch app
flyctl launch

# Deploy
flyctl deploy
```

## 📦 GitHub Actions CI/CD

### Setup Docker Hub Integration
1. Go to your GitHub repository → Settings → Secrets and variables → Actions
2. Add the following secrets:
   - `DOCKERHUB_USERNAME`: Your Docker Hub username
   - `DOCKERHUB_TOKEN`: Your Docker Hub access token
     - Get token from: https://hub.docker.com/settings/security

3. Push to main/master branch to trigger automatic build and push

### Pull the Docker Image
```bash
# Pull from Docker Hub
docker pull YOUR_USERNAME/ai-image-generator:latest

# Run
docker run -p 8501:8501 YOUR_USERNAME/ai-image-generator:latest
```

## 🔧 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `HF_TOKEN` | No | Hugging Face API token (for cloud mode) |
| `OPENROUTER_API_KEY` | No | OpenRouter API key (for OpenRouter mode) |

## 🛠️ Troubleshooting

### Image Editing Not Working
The image-to-image feature has known reliability issues with free APIs. Recommendations:
1. Use **Local GPU mode** for best results (requires NVIDIA GPU)
2. Try **Pollinations mode** with lower strength values (0.3-0.5)
3. Use simple, clear prompts without quality enhancers for img2img

### Background Removal
If background removal fails:
1. Restart the Streamlit app after first installation
2. Check that `rembg` and `onnxruntime` are installed
3. First use will download a ~180MB model

### Connection Issues
If you see "Failed to resolve" errors:
- Check your internet connection
- Try switching deployment modes
- Hugging Face servers may be temporarily down

## 📝 Notes
- Free tier APIs have rate limits and may be slow
- For production use, consider using Local GPU mode or paid APIs
- Background removal model downloads on first use (~180MB)

# 🎨 8D Ultra-Realistic AI Image Generator

![Python](https://img.shields.io/badge/Python-3.11+-green?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange?logo=github)

Generate **8D Ultra-Realistic** images using cutting-edge AI models with **3 deployment options**:
- ☁️ **Cloud (Hugging Face)** - Fast, no setup
- 🌐 **Cloud (OpenRouter)** - Multi-provider access
- 🏠 **Private (Local GPU)** - 100% private, runs on YOUR hardware

---

## 🚀 Quick Start

### 1. Install Base Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run app.py
```

### 3. Choose Your Mode
Select your deployment mode in the sidebar and follow the setup instructions.

---

## 📋 Deployment Modes Comparison

| Feature | ☁️ Hugging Face | 🌐 OpenRouter | 🏠 Local GPU |
|---------|----------------|---------------|--------------|
| **GPU Location** | Hugging Face servers | Partner providers | YOUR machine |
| **Model Download** | ❌ No | ❌ No | ✅ Yes (~6-13GB) |
| **Privacy** | ⚠️ Data sent to HF | ⚠️ Data sent to provider | ✅ 100% private |
| **Setup** | API key only | API key only | GPU + CUDA required |
| **Cost** | Free tier + paid | Pay per use | Free (your electricity) |
| **Speed** | Fast | Fast | Depends on your GPU |
| **Best For** | Demos, public data | Multi-model access | Sensitive data, full control |

---

## ☁️ Mode 1: Hugging Face Cloud

### Setup
1. Get a free API token: [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Enter it in the app sidebar (or set `HF_TOKEN` environment variable)

### Features
- ✅ No GPU required
- ✅ Fast generation (10-30 seconds)
- ✅ Multiple models available (SDXL, FLUX, etc.)
- ⚠️ Data is processed on Hugging Face servers

### Models Available
- Stable Diffusion XL (Best for 8D quality)
- Realistic Vision XL (Ultra photorealistic)
- DreamShaper XL (Artistic style)
- FLUX.1-schnell (Fast premium)
- And more...

---

## 🌐 Mode 2: OpenRouter Cloud

### Setup
1. Get an API key: [OpenRouter Keys](https://openrouter.ai/keys)
2. Enter it in the app sidebar (or set `OPENROUTER_API_KEY` environment variable)

### Features
- ✅ Access to multiple providers (OpenAI, Anthropic, etc.)
- ⚠️ Primarily for text models (image support limited)
- ⚠️ Data passes through OpenRouter + provider

---

## 🏠 Mode 3: Private (Local GPU)

### Requirements
- ✅ NVIDIA GPU with **8GB+ VRAM** (16GB recommended for SDXL)
- ✅ CUDA installed ([Download](https://developer.nvidia.com/cuda-downloads))
- ✅ ~20GB free disk space (for models)

### Setup
1. Install additional dependencies:
   ```bash
   pip install -r requirements-local.txt
   ```
2. Verify CUDA installation:
   ```bash
   python -c "import torch; print(torch.cuda.is_available())"
   ```
   Should print `True`.
3. Select "🏠 Private (Local GPU)" in the app.

### Features
- ✅ **100% Private** - Never leaves your machine
- ✅ No API costs
- ✅ Full control over models
- ✅ Unlimited generations

---

## 🚢 Deployment

### Docker Deployment

#### Quick Start with Docker Compose
```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

#### Docker CLI
```bash
# Build
docker build -t ai-image-generator .

# Run
docker run -p 8501:8501 ai-image-generator
```

### Cloud Platforms

- **Render**: See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions
- **Railway**: One-click deploy from GitHub
- **Fly.io**: Use `flyctl launch`

### CI/CD with GitHub Actions

The project includes automated Docker builds:
1. Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` to GitHub Secrets
2. Push to main/master branch
3. Docker image automatically builds and pushes to Docker Hub

For complete deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🎯 Quality Presets

All modes support these quality presets:

1. **🌟 8D Ultra-Realistic** (50 steps, guidance 9.0)
   - Maximum quality, photorealistic
   - Best for: Professional photos, portraits
2. **🎬 Cinematic 8D** (45 steps, guidance 8.5)
   - Film-quality with dramatic lighting
   - Best for: Movie scenes, artistic shots
3. **🎨 Artistic 8D** (40 steps, guidance 8.0)
   - Award-winning art style
   - Best for: Creative artwork, illustrations
4. **⚡ Balanced Quality** (30 steps, guidance 7.5)
   - Good quality, faster generation
   - Best for: Quick iterations
5. **🚀 Fast Generation** (20 steps, guidance 7.0)
   - Quick results
   - Best for: Testing prompts

---

## 🔒 Privacy & Security

### When to use each mode:

| Data Type | Recommended Mode |
|-----------|------------------|
| Public/marketing images | ☁️ Any cloud mode |
| Internal business data | ⚠️ Review ToS carefully |
| Customer PII | 🏠 **Local GPU ONLY** |
| Medical/financial data | 🏠 **Local GPU ONLY** |
| Prototypes/demos | ☁️ Cloud modes fine |

---

## 🛠️ Troubleshooting

### "No CUDA GPU detected"
- Install NVIDIA CUDA drivers
- Verify with: `nvidia-smi`
- Ensure PyTorch CUDA version matches

### "Model loading failed"
- Check disk space (~20GB needed)
- Clear cache: `rm -rf ~/.cache/huggingface/`
- Try a different model

### "API Error 404"
- Model may be loading (wait 30s, retry)
- Check API token is valid
- Try a different model

---

## 📦 Project Structure

```
ai_image_generator/
├── app.py                      # Main Streamlit app
├── requirements.txt            # Base dependencies
├── requirements-local.txt      # Local GPU dependencies
├── Dockerfile                  # Container config
├── docker-compose.yml          # Local deployment
├── render.yaml                 # Render deployment
├── .github/workflows/          # CI/CD
└── README.md                   # This file
```

---

## 📧 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review model documentation on Hugging Face
3. Open an issue on GitHub

---

**Made with ❤️ by Parthi**
*Generate stunning 8D images with the power of AI!* 🎨✨
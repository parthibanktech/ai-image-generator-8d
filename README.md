# 🎨 8D AI Image Generator - Multi-Mode Deployment

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
1. Get a free API token: https://huggingface.co/settings/tokens
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
1. Get an API key: https://openrouter.ai/keys
2. Enter it in the app sidebar (or set `OPENROUTER_API_KEY` environment variable)

### Features
- ✅ Access to multiple providers (OpenAI, Anthropic, etc.)
- ⚠️ Primarily for text models (image support limited)
- ⚠️ Data passes through OpenRouter + provider

### Note
OpenRouter is **primarily designed for text/chat models**. For image generation, we recommend **Hugging Face** or **Local GPU** mode.

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
Should print `True`

3. Select "🏠 Private (Local GPU)" in the app

### First Run
- Models will download automatically (~6-13GB per model)
- Stored in: `~/.cache/huggingface/`
- Subsequent runs will use cached models

### Features
- ✅ **100% Private** - Never leaves your machine
- ✅ No API costs
- ✅ Full control over models
- ✅ Unlimited generations
- ⚠️ Requires powerful GPU
- ⚠️ Slower on first run (model download)

### Recommended GPUs
| GPU | VRAM | SDXL Support | Speed |
|-----|------|--------------|-------|
| RTX 3060 | 12GB | ✅ Good | Medium |
| RTX 3080 | 10GB | ✅ Good | Fast |
| RTX 4070 | 12GB | ✅ Excellent | Fast |
| RTX 4080 | 16GB | ✅ Excellent | Very Fast |
| RTX 4090 | 24GB | ✅ Perfect | Ultra Fast |

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

### Data Flow

**Cloud Modes:**
```
Your Computer → API Provider → Back to You
```
⚠️ Data is processed on third-party servers

**Local Mode:**
```
Your Computer (100% local processing)
```
✅ Data never leaves your machine

---

## 💡 Tips & Best Practices

### For Best Quality:
1. Use "8D Ultra-Realistic" preset
2. Increase inference steps (50-100)
3. Use detailed prompts
4. Let negative prompts filter out artifacts

### For Speed:
1. Use "Fast Generation" preset
2. Reduce inference steps (20-30)
3. Use smaller resolutions
4. Try SDXL Turbo (local mode)

### For Privacy:
1. Use Local GPU mode
2. Ensure firewall is active
3. Models are cached locally
4. No internet needed after download

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

### "Out of memory"
- Reduce resolution
- Use SDXL Turbo instead of SDXL
- Close other GPU applications
- Enable attention slicing (already enabled)

---

## 📦 Project Structure

```
ai_image_generator/
├── app.py                      # Main Streamlit app
├── requirements.txt            # Base dependencies
├── requirements-local.txt      # Local GPU dependencies
├── README.md                   # This file
└── venv/                       # Virtual environment
```

---

## 🔧 Environment Variables

Optional - set these to avoid entering keys in the UI:

```bash
# Hugging Face
export HF_TOKEN="your_hf_token_here"

# OpenRouter
export OPENROUTER_API_KEY="your_openrouter_key_here"
```

---

## 📝 License

This project uses models from Hugging Face. Each model has its own license:
- Stable Diffusion XL: CreativeML Open RAIL++-M License
- Check individual model cards for specific licenses

---

## 🤝 Contributing

Feel free to submit issues or pull requests!

---

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

## 📧 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review model documentation on Hugging Face
3. Open an issue on GitHub

---

**Made with ❤️ by Parthi**

*Generate stunning 8D images with the power of AI!* 🎨✨

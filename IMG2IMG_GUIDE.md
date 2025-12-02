# 🎨 Image-to-Image (Img2Img) Guide

## Overview
The AI Image Generator now supports **Image-to-Image transformation**, allowing you to upload an existing image and modify it based on your text prompt.

## 🚀 How to Use

### Step 1: Upload an Image
1. Click on the **"📤 Upload an image to modify"** section
2. Select a PNG, JPG, or JPEG file (max 200MB)
3. The image will be automatically resized to 768x768 for optimal processing

### Step 2: Adjust Transformation Strength
- A **"Transformation Strength"** slider will appear after uploading
- **0.0** = Minimal changes (keeps most of the original image)
- **0.5** = Balanced transformation
- **0.75** = Recommended default (good balance)
- **1.0** = Complete transformation (almost like text-to-image)

### Step 3: Write Your Prompt
Describe how you want to modify the image. Examples:
- "Make him as superhero"
- "Turn this into a cyberpunk scene"
- "Add dramatic lighting and cinematic effects"
- "Convert to oil painting style"

### Step 4: Generate!
Click **"🚀 Generate 8D Image"** and wait for the AI to transform your image.

---

## 📋 Model Compatibility

### ☁️ Hugging Face Cloud Mode
**✅ Img2Img Compatible Models:**
- **Instruct Pix2Pix** (🎨 Best for Image Editing) - RECOMMENDED
- **Stable Diffusion v1.5** (Img2Img Compatible)

**❌ Text2Img Only (Won't work for img2img):**
- Stable Diffusion XL
- Realistic Vision XL
- DreamShaper XL
- FLUX.1-schnell

**Important:** The Hugging Face Inference API has limited img2img support. If you get an error, switch to one of the compatible models above.

### 🌸 Pollinations.ai Mode
- ✅ **Fully supports Img2Img**
- No model selection needed
- Automatically uses the best available model

### 🌐 OpenRouter Mode
- ⚠️ Limited image generation support
- Primarily designed for text models
- Not recommended for img2img

### 🏠 Local GPU Mode
- ✅ **ALL models support Img2Img**
- Best quality and most control
- Requires NVIDIA GPU with 8GB+ VRAM
- Models automatically download on first use

---

## 💡 Tips for Best Results

### 1. **Choose the Right Strength**
- **Low (0.2-0.4)**: Subtle changes, style transfer, color adjustments
- **Medium (0.5-0.7)**: Moderate transformations, adding elements
- **High (0.8-1.0)**: Dramatic changes, complete reimagining

### 2. **Write Clear Prompts**
- Be specific about what you want to change
- Use descriptive adjectives
- Mention style, lighting, mood, etc.

### 3. **Use Negative Prompts**
- Describe what you DON'T want
- Helps avoid unwanted artifacts
- Examples: "blurry, distorted, low quality"

### 4. **Quality Presets**
- **8D Ultra-Realistic**: Best for photorealistic transformations
- **Cinematic 8D**: Great for dramatic, movie-like effects
- **Artistic 8D**: Perfect for artistic style transfers

---

## 🔧 Troubleshooting

### Error: "Task 'image-to-image' not supported"
**Solution:**
1. Switch to **Instruct Pix2Pix** or **Stable Diffusion v1.5**
2. OR switch to **Local GPU mode** (all models work)
3. OR switch to **Pollinations.ai mode**

### Image Quality is Poor
**Solution:**
- Increase **Inference Steps** (40-50 for best quality)
- Use **8D Ultra-Realistic** preset
- Adjust **Guidance Scale** (7-9 recommended)
- Try a lower **Transformation Strength** to preserve more detail

### Generation is Too Slow
**Solution:**
- Use **Fast Generation** preset
- Reduce **Inference Steps** to 20-30
- Switch to **Pollinations.ai** (very fast)
- Use **Local GPU** with **SDXL Turbo** model

### Image Looks Too Different from Original
**Solution:**
- Lower the **Transformation Strength** to 0.3-0.5
- Use more specific prompts
- Try **Instruct Pix2Pix** model (better at following instructions)

---

## 📊 Comparison Table

| Mode | Img2Img Support | Speed | Quality | Cost |
|------|----------------|-------|---------|------|
| **Hugging Face** | ⚠️ Limited models | Fast | Good | FREE |
| **Pollinations.ai** | ✅ Full support | Very Fast | Good | FREE |
| **OpenRouter** | ❌ Not recommended | Medium | Varies | Paid |
| **Local GPU** | ✅ Full support | Medium-Fast | Excellent | FREE (requires GPU) |

---

## 🎯 Use Cases

### 1. **Photo Enhancement**
- Strength: 0.3-0.5
- Prompt: "enhance quality, professional photography, sharp details"

### 2. **Style Transfer**
- Strength: 0.6-0.8
- Prompt: "oil painting style, impressionist, vibrant colors"

### 3. **Character Transformation**
- Strength: 0.7-0.9
- Prompt: "superhero costume, dramatic pose, cinematic lighting"

### 4. **Scene Modification**
- Strength: 0.5-0.7
- Prompt: "cyberpunk city background, neon lights, futuristic"

### 5. **Artistic Reimagining**
- Strength: 0.8-1.0
- Prompt: "fantasy art, magical atmosphere, ethereal glow"

---

## 🎓 Best Practices

1. **Start with Lower Strength**: Begin at 0.5 and adjust up/down
2. **Use Reference Images**: Upload high-quality source images
3. **Experiment with Models**: Try different models for different effects
4. **Combine with Quality Presets**: Use presets to auto-enhance prompts
5. **Iterate**: Generate multiple versions with different settings

---

## 🆘 Need Help?

If you encounter issues:
1. Check the error message for specific guidance
2. Try switching to a different model
3. Reduce image size (upload smaller images)
4. Switch to Local GPU mode for maximum compatibility
5. Use Pollinations.ai for quick, reliable results

---

**Happy Image Transforming! 🎨✨**

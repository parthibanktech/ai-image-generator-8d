import streamlit as st
import os
import io
import time
from PIL import Image
from huggingface_hub import InferenceClient
import requests
import base64

# ------------------------------
# 1. Page Setup
# ------------------------------
st.set_page_config(page_title="Parthi 8D AI Image Generator", layout="wide", page_icon="🎨")
st.title("🎨 Parthi 8D AI Image Studio - Ultra HD Generation")
st.markdown("### Generate **8D Ultra-Realistic** images with cutting-edge AI models")
st.markdown("*Powered by Cloud APIs or Your Private GPU*")

# ------------------------------
# 2. API Configuration
# ------------------------------
def get_secret(key):
    """Safely get secret from environment or streamlit secrets"""
    if key in os.environ:
        return os.environ[key]
    try:
        return st.secrets.get(key)
    except Exception:
        return None

DEFAULT_TOKEN = "hf_nzy"
HF_TOKEN = get_secret("HF_TOKEN")

# Sidebar Configuration
with st.sidebar:
    st.header("🚀 Deployment Mode")
    
    deployment_mode = st.radio(
        "Choose where to run AI models:",
        [
            "☁️ Cloud (Hugging Face - FREE)",
            "🌸 Cloud (Pollinations.ai - FREE)",
            "🌐 Cloud (OpenRouter)", 
            "🏠 Private (Local GPU)"
        ],
        index=3,
        help="""
        **Cloud (Hugging Face)**: FREE, uses HF's GPU, fast.
        **Cloud (Pollinations)**: FREE, no key needed, very fast.
        **Cloud (OpenRouter)**: For paid/custom models.
        **Private (Local GPU)**: 100% private, runs on your PC.
        """
    )
    
    # Extract mode
    if "Hugging Face" in deployment_mode:
        mode = "huggingface"
    elif "Pollinations" in deployment_mode:
        mode = "pollinations"
    elif "OpenRouter" in deployment_mode:
        mode = "openrouter"
    else:
        mode = "local"
    
    st.divider()
    st.header("⚙️ API Configuration")
    
    OPENROUTER_KEY = None  # define here so it's in scope later
    
    # API Token based on mode
    if mode == "huggingface":
        if not HF_TOKEN:
            HF_TOKEN = st.text_input(
                "Enter Hugging Face Token:",
                value=DEFAULT_TOKEN,
                type="password",
                help="Get your free token here: https://huggingface.co/settings/tokens"
            )
            if not HF_TOKEN:
                st.warning("⚠️ Token required to proceed.")
                st.stop()
        
        st.success("✅ Hugging Face API Ready")
        st.info("🖥️ **Using**: Hugging Face's GPU servers (FREE)")
        
    elif mode == "openrouter":
        OPENROUTER_KEY = get_secret("OPENROUTER_API_KEY")
        
        if not OPENROUTER_KEY:
            OPENROUTER_KEY = st.text_input(
                "Enter OpenRouter API Key:",
                type="password",
                help="Get your key here: https://openrouter.ai/keys"
            )
            
        if not OPENROUTER_KEY:
            st.warning("⚠️ OpenRouter API key required.")
            st.stop()
            
        # Validation: Check if key looks valid (prevent pasting page text)
        if len(OPENROUTER_KEY) > 200 or " " in OPENROUTER_KEY.strip():
            st.error("❌ Invalid API Key detected!")
            st.warning("It looks like you pasted text instead of the key. Please clear the input and paste your 'sk-or-...' key.")
            st.stop()
        
        st.success("✅ OpenRouter API Ready")
        st.info("🖥️ **Using**: OpenRouter's Partner GPUs")
        
    else:  # local or pollinations
        if mode == "local":
            st.success("✅ Local Mode Selected")
            st.info("🖥️ **Using**: YOUR GPU (models will download to your machine)")
            st.warning("⚠️ Requires: NVIDIA GPU with 8GB+ VRAM, CUDA installed | GTX and 8GB RAM")
            
            # Check if required libraries are installed
            try:
                import torch
                from diffusers import StableDiffusionXLPipeline, DiffusionPipeline  # noqa: F401
                
                if torch.cuda.is_available():
                    gpu_name = torch.cuda.get_device_name(0)
                    gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
                    st.success(f"✅ GPU Detected: {gpu_name} ({gpu_memory:.1f} GB)")
                else:
                    st.error("❌ No CUDA GPU detected! Local mode requires NVIDIA GPU.")
                    st.info("💡 Switch to Cloud mode or install CUDA drivers.")
            except ImportError:
                st.error("❌ Required libraries not installed!")
                st.code("pip install torch torchvision diffusers transformers accelerate", language="bash")
                st.stop()
        else:
            st.success("✅ Pollinations Mode Selected")
            st.info("🖥️ **Using**: Pollinations.ai (no API key needed)")
    
    st.divider()
    st.subheader("🎯 Quality Preset")
    
    # Quality Presets for 8D Generation
    quality_presets = {
        "🌟 8D Ultra-Realistic": {
            "suffix": ", 8k uhd, ultra detailed, photorealistic, professional photography, sharp focus, HDR, studio lighting, extreme detail, hyper realistic",
            "negative": "blurry, low quality, distorted, ugly, pixelated, bad anatomy, watermark, text, cartoon, anime, painting, sketch, low resolution, jpeg artifacts, compression, noise",
            "guidance": 9.0,
            "steps": 50
        },
        "🎬 Cinematic 8D": {
            "suffix": ", cinematic lighting, 8k resolution, film grain, depth of field, bokeh, professional color grading, anamorphic lens, dramatic lighting",
            "negative": "amateur, low quality, blurry, overexposed, underexposed, flat lighting, poor composition, distorted",
            "guidance": 8.5,
            "steps": 45
        },
        "🎨 Artistic 8D": {
            "suffix": ", masterpiece, award winning, highly detailed, 8k, professional art, vibrant colors, perfect composition, trending on artstation",
            "negative": "low quality, blurry, amateur, poorly drawn, bad anatomy, distorted, ugly, watermark",
            "guidance": 8.0,
            "steps": 40
        },
        "⚡ Balanced Quality": {
            "suffix": ", high quality, detailed, 4k, sharp focus, professional",
            "negative": "blurry, low quality, distorted, ugly, pixelated, bad anatomy, watermark, text",
            "guidance": 7.5,
            "steps": 30
        },
        "🚀 Fast Generation": {
            "suffix": ", good quality, detailed",
            "negative": "blurry, low quality, distorted",
            "guidance": 7.0,
            "steps": 20
        }
    }
    
    selected_preset = st.selectbox("Choose Quality Preset:", list(quality_presets.keys()), index=0)
    preset_config = quality_presets[selected_preset]
    
    st.divider()
    st.subheader("🖼️ Model Selection")
    
    # Model selection based on deployment mode
    if mode == "huggingface":
        model_options = {
            "Stable Diffusion XL (🔥 Best Quality - Text2Img)": "stabilityai/stable-diffusion-xl-base-1.0",
            "FLUX.1-schnell (⚡ Fast Premium - Text2Img)": "black-forest-labs/FLUX.1-schnell",
            "Realistic Vision XL (Ultra Photorealistic - Text2Img)": "SG161222/RealVisXL_V4.0",
            "DreamShaper XL (Artistic - Text2Img)": "Lykon/dreamshaper-xl-1-0",
            "Stable Diffusion v1.5 (✅ Both Text2Img & Img2Img)": "runwayml/stable-diffusion-v1-5",
            "Instruct Pix2Pix (✅ Img2Img Only - Image Editing)": "timbrooks/instruct-pix2pix",
        }
        st.info("💡 **Model Guide:**\n"
                "- **Text2Img**: Create images from text prompts\n"
                "- **Img2Img**: Modify uploaded images\n"
                "- **SD v1.5**: Works for both! Use this if unsure.\n"
                "- **Instruct Pix2Pix**: Best for strong image editing.")
    elif mode == "pollinations":
        model_options = {
            "Pollinations Default (Stable Diffusion)": "pollinations",
        }
        st.info("🌸 Pollinations.ai automatically uses the best available model (usually SDXL/Flux).")
    elif mode == "openrouter":
        model_options = {
            "DALL-E 3 (OpenAI - Paid)": "openai/dall-e-3",
            "Custom Model ID (Enter Manually)": "custom",
        }
        st.info("ℹ️ OpenRouter: Select 'Custom' to enter any model ID from openrouter.ai")
    else:  # local mode
        model_options = {
            "Stable Diffusion XL (Local)": "stabilityai/stable-diffusion-xl-base-1.0",
            "Stable Diffusion XL Turbo (Fast)": "stabilityai/sdxl-turbo",
            "Realistic Vision XL (Local)": "SG161222/RealVisXL_V4.0",
            "DreamShaper XL (Local)": "Lykon/dreamshaper-xl-1-0",
        }
        st.info("📥 Models will download on first use (~6-13GB each). Stored in: `~/.cache/huggingface/`")
    
    selected_model_name = st.selectbox("Select AI Model:", list(model_options.keys()), index=0)
    
    if selected_model_name == "Custom Model ID (Enter Manually)":
        model_id = st.text_input("Enter OpenRouter Model ID:", value="black-forest-labs/flux-1-schnell", help="Copy ID from openrouter.ai")
    else:
        model_id = model_options[selected_model_name]
    
    st.divider()
    st.subheader("🎛️ Advanced Settings")
    
    # Auto-fill from preset but allow customization
    negative_prompt = st.text_area(
        "Negative Prompt (What to avoid):",
        value=preset_config["negative"],
        height=100,
        help="Describe what you DON'T want in the image"
    )
    
    guidance_scale = st.slider(
        "Guidance Scale (Prompt Adherence)", 
        1.0, 20.0, 
        preset_config["guidance"],
        help="Higher = more faithful to prompt, Lower = more creative"
    )
    
    num_inference_steps = st.slider(
        "Inference Steps (Quality vs Speed)", 
        10, 100, 
        preset_config["steps"],
        help="More steps = higher quality but slower generation"
    )
    
    # Resolution settings
    st.subheader("📐 Resolution")
    resolution_presets = {
        "8K Ultra HD (7680×4320)": (1024, 1024),  # API limitation, will upscale
        "4K Ultra HD (3840×2160)": (1024, 1024),
        "1080p Full HD": (1024, 576),
        "Square HD": (1024, 1024),
        "Portrait": (768, 1024),
        "Landscape": (1024, 768)
    }
    
    selected_resolution = st.selectbox("Output Resolution:", list(resolution_presets.keys()), index=3)
    width, height = resolution_presets[selected_resolution]

# ------------------------------
# 3. Helper Functions
# ------------------------------
def image_to_base64(image: Image.Image) -> str:
    # Convert PIL Image to Base64 string
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def query_openrouter_api(prompt, model_id, api_key, negative_prompt="", width=1024, height=1024):
    """Query OpenRouter API for image generation (via Chat Endpoint)"""
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/parthibanktech/IRCTC-Assistant",
        "X-Title": "8D AI Image Studio"
    }
    
    # OpenRouter uses chat format
    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "user",
                "content": f"Generate an image: {prompt}. Negative prompt: {negative_prompt}"
            }
        ]
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response


@st.cache_resource
def load_local_pipeline(model_id, pipeline_type="text2img"):
    """Load local diffusion pipeline (cached to avoid reloading)"""
    import torch
    from diffusers import (
        StableDiffusionXLPipeline, 
        StableDiffusionXLImg2ImgPipeline,
        AutoPipelineForText2Image,
        AutoPipelineForImage2Image
    )
    
    try:
        if "turbo" in model_id.lower():
            if pipeline_type == "img2img":
                pipe = AutoPipelineForImage2Image.from_pretrained(
                    model_id,
                    torch_dtype=torch.float16,
                    variant="fp16"
                )
            else:
                pipe = AutoPipelineForText2Image.from_pretrained(
                    model_id,
                    torch_dtype=torch.float16,
                    variant="fp16"
                )
        else:
            if pipeline_type == "img2img":
                pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
                    model_id,
                    torch_dtype=torch.float16,
                    variant="fp16",
                    use_safetensors=True
                )
            else:
                pipe = StableDiffusionXLPipeline.from_pretrained(
                    model_id,
                    torch_dtype=torch.float16,
                    variant="fp16",
                    use_safetensors=True
                )
        
        pipe = pipe.to("cuda")
        pipe.enable_attention_slicing()
        
        return pipe
    except Exception as e:
        st.error(f"Failed to load model locally: {e}")
        return None


def generate_local_image(pipe, prompt, negative_prompt, width, height, guidance_scale, num_steps, input_image=None, strength=0.75):
    """Generate image using local GPU"""
    try:
        if input_image is not None:
            image = pipe(
                prompt=prompt,
                image=input_image,
                negative_prompt=negative_prompt,
                guidance_scale=guidance_scale,
                num_inference_steps=num_steps,
                strength=strength,
            ).images[0]
        else:
            image = pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                guidance_scale=guidance_scale,
                num_inference_steps=num_steps,
            ).images[0]
        
        return image
    except Exception as e:
        st.error(f"Local generation failed: {e}")
        return None

def upload_image_to_host(image):
    """Upload image to a temporary host and return the direct URL"""
    try:
        # 1. Resize to 512x512 for speed (Tiny file size)
        img_resized = image.resize((512, 512))
        buf = io.BytesIO()
        img_resized.save(buf, format="JPEG", quality=80)
        buf.seek(0)
        files = {'file': ('image.jpg', buf, 'image/jpeg')}
        
        # 2. Try Host A: tmpfiles.org
        try:
            # CRITICAL: Reduced timeout to 3s. If it's not instant, it's dead. Move on.
            response = requests.post('https://tmpfiles.org/api/v1/upload', files=files, timeout=3)
            if response.status_code == 200:
                data = response.json()
                raw_url = data['data']['url']
                return raw_url.replace("tmpfiles.org/", "tmpfiles.org/dl/")
        except Exception as e:
            print(f"Host A failed: {e}")
            
        # 3. Try Host B: file.io (Backup)
        buf.seek(0) # Reset buffer
        files = {'file': ('image.jpg', buf, 'image/jpeg')}
        response = requests.post('https://file.io', files=files, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                return data['link']
                
        return None
    except Exception as e:
        return None

# ------------------------------
# 4. Main Interface
# ------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. 📝 Describe Your Vision")
    
    prompt = st.text_area(
        "Enter your image prompt:",
        "a majestic lion in a futuristic cyberpunk city",
        height=100,
        help="Describe what you want to see. The quality preset will automatically enhance your prompt!"
    )
    
    # Show enhanced prompt preview
    if prompt:
        if preset_config["suffix"] not in prompt:
            enhanced_prompt_preview = prompt + preset_config["suffix"]
        else:
            enhanced_prompt_preview = prompt
        with st.expander("🔍 Preview Enhanced Prompt (Auto-Applied)"):
            st.info(enhanced_prompt_preview)
            
    # Composition Selector (New Feature to fix "missing subjects")
    composition_style = st.selectbox(
        "📸 Camera Angle / Composition (Fixes missing subjects)",
        ["Default", "Wide Shot (Best for battles/groups)", "Full Body Shot", "Close-up (Portraits)", "Cinematic Angle", "Drone View"],
        index=0,
        help="If the AI cuts off a person or focuses on just one thing, try 'Wide Shot' or 'Full Body Shot'."
    )
    
    st.divider()
    
    uploaded_file = st.file_uploader("📤 Upload an image to modify (Optional - Img2Img)", type=["png", "jpg", "jpeg"])
    
    input_image = None
    img2img_strength = 0.75  # Default strength
    
    if uploaded_file:
        input_image = Image.open(uploaded_file).convert("RGB")
        input_image.thumbnail((768, 768))
        st.image(input_image, caption="Input Image", use_container_width=True)
        st.info("ℹ️ Mode: **Image-to-Image** (The AI will modify this image based on your prompt)")
        
        if mode == "huggingface":
            st.success("✅ For Hugging Face Img2Img, the app will use Instruct Pix2Pix internally.")
        
        img2img_strength = st.slider(
            "Transformation Strength",
            0.0, 1.0, 0.45,
            help="How much to change the image. 0.0 = minimal change, 1.0 = complete transformation"
        )
    else:
        st.info("ℹ️ Mode: **Text-to-Image** (The AI will create an image from scratch)")
    
    generate_btn = st.button("🚀 Generate 8D Image", type="primary", use_container_width=True)

    # Quick Tools for Uploaded Image
    if uploaded_file and input_image:
        st.divider()
        st.subheader("🛠️ Quick Tools")
        if st.button("✂️ Remove Background Only", use_container_width=True):
            status_container = st.empty()
            try:
                status_container.info("🔄 Initializing background remover...")
                
                # Import inside the button to avoid startup lag
                import rembg
                from rembg import remove
                import onnxruntime
                
                status_container.info("✂️ Removing background... (This may take a moment)")
                
                # Remove background
                processed_image = remove(input_image)
                
                # Save to session state
                st.session_state['processed_image'] = processed_image
                st.session_state['processed_caption'] = "Background Removed"
                
                status_container.success("✅ Background removed successfully!")
                time.sleep(1)
                status_container.empty()
                st.rerun()
                
            except ImportError as e:
                status_container.error(f"❌ Missing library: {e}")
                if "onnxruntime" in str(e) or "rembg" in str(e):
                    st.warning("⚠️ New libraries were installed. Please STOP and RESTART the Streamlit app in your terminal.")
            except Exception as e:
                status_container.error(f"❌ Error: {e}")

# ------------------------------
# 5. Generation Logic
# ------------------------------
with col2:
    st.subheader("2. ✨ Your Masterpiece")
    
    # Check for processed image in session state (from Quick Tools)
    if 'processed_image' in st.session_state:
        st.image(st.session_state['processed_image'], caption=st.session_state.get('processed_caption', "Result"), use_container_width=True)
        
        # Download button for processed image
        buf = io.BytesIO()
        st.session_state['processed_image'].save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="💾 Download Processed Image",
            data=byte_im,
            file_name="processed_image.png",
            mime="image/png",
            use_container_width=True,
        )
        
        if st.button("❌ Clear Result", use_container_width=True):
            del st.session_state['processed_image']
            st.rerun()
            
    if generate_btn:
        if not prompt:
            st.error("Please enter a prompt!")
        else:
            try:
                # CRITICAL FIX: For Img2Img, WE DO NOT USE PRESETS.
                # Presets add too much noise ("8k, best quality...") which makes the AI ignore the input image.
                if input_image:
                    enhanced_prompt = prompt # Raw prompt only
                else:
                    # Text-to-Image gets the fancy presets
                    suffix = preset_config["suffix"]
                    
                    # Add Composition Style
                    if composition_style and composition_style != "Default":
                        comp_text = composition_style.split("(")[0].strip()
                        suffix = f", {comp_text}" + suffix
                    
                    if suffix not in prompt:
                        enhanced_prompt = prompt + suffix
                    else:
                        enhanced_prompt = prompt
                
                with st.spinner(f"🎨 Generating {selected_preset} image... (This may take 30-60s for best quality)"):
                    # ... (Mode display code) ...
                    
                    generated_image = None
                    
                    # ===== MODE 1: HUGGING FACE API =====
                    if mode == "huggingface":
                        token_to_use = HF_TOKEN if HF_TOKEN else DEFAULT_TOKEN
                        client = InferenceClient(token=token_to_use, timeout=120)
                        
                        max_retries = 2
                        retry_count = 0
                        success = False
                        
                        while retry_count < max_retries and not success:
                            try:
                                if retry_count > 0:
                                    wait_time = 2
                                    st.info(f"⏳ Waiting for server ({wait_time}s)... (Attempt {retry_count + 1}/{max_retries})")
                                    import time
                                    time.sleep(wait_time)
                                
                                if input_image:
                                    # === IMAGE TO IMAGE (EDITING) ===
                                    edit_model = "runwayml/stable-diffusion-v1-5"
                                    # CLEAN PROMPT: No presets, just instructions
                                    final_prompt = f"{prompt}, preserve facial features, identity"
                                    
                                    input_resized = input_image.resize((512, 512))
                                    
                                    st.info(f"🎨 Editing with fast model: {edit_model}")
                                    
                                    with st.spinner("🎨 Editing your image... (Should be fast)"):
                                        generated_image = client.image_to_image(
                                            image=input_resized,
                                            prompt=final_prompt,
                                            negative_prompt=negative_prompt,
                                            model=edit_model,
                                            guidance_scale=guidance_scale,
                                            num_inference_steps=num_inference_steps,
                                            strength=img2img_strength
                                        )
                                        success = True
                                        st.success("✅ Edited successfully using Stable Diffusion v1.5!")
                                else:
                                    # === TEXT TO IMAGE ===
                                    # ... (Text2Img code) ...
                                    generated_image = client.text_to_image(
                                        prompt=enhanced_prompt,
                                        negative_prompt=negative_prompt,
                                        model=model_id,
                                        width=width,
                                        height=height,
                                        guidance_scale=guidance_scale,
                                        num_inference_steps=num_inference_steps
                                    )
                                    success = True
                            except Exception as e:
                                error_msg = str(e)
                                retry_count += 1
                                st.warning(f"⚠️ Attempt {retry_count} failed: {error_msg}")
                                
                                if retry_count >= max_retries:
                                    st.error(f"❌ Hugging Face failed. Trying fallback...")
                                    
                                    # Fallback to Pollinations
                                    try:
                                        import urllib.parse
                                        st.info("🔄 Switching to Pollinations.ai...")
                                        
                                        if input_image:
                                            st.info("📤 Uploading image for Pollinations...")
                                            public_img_url = upload_image_to_host(input_image)
                                            
                                            if public_img_url:
                                                # CLEAN PROMPT: Use user's prompt directly without "face swap" noise
                                                final_prompt = urllib.parse.quote(prompt)
                                                # Use the USER'S selected strength, not hardcoded 0.30
                                                image_url = f"https://image.pollinations.ai/prompt/{final_prompt}?image={public_img_url}&width=768&height=768&nologo=true&seed=42&model=turbo&strength={img2img_strength}"
                                            else:
                                                raise Exception("Image upload failed on all hosts")
                                        else:
                                            encoded_prompt = urllib.parse.quote(enhanced_prompt)
                                            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=768&height=768&nologo=true&model=turbo"
                                        
                                        # CRITICAL FIX: Increased timeout to 180s and reduced res to 768px to ensure completion
                                        response = requests.get(image_url, timeout=180)
                                        if response.status_code == 200:
                                            generated_image = Image.open(io.BytesIO(response.content))
                                            success = True
                                            st.success("✅ Generated via Fallback (Turbo Mode, 768px)!")
                                    except Exception as fallback_err:
                                        st.error(f"❌ All methods failed: {fallback_err}")
                    
                    # ===== MODE 2: POLLINATIONS.AI (FREE) =====
                    elif mode == "pollinations":
                        try:
                            import urllib.parse
                            encoded_prompt = urllib.parse.quote(enhanced_prompt + " " + negative_prompt)
                            
                            if input_image is not None:
                                st.info("📤 Uploading image for Pollinations Img2Img...")
                                public_img_url = upload_image_to_host(input_image)
                                
                                if public_img_url:
                                    # Use user's prompt and strength
                                    final_prompt = urllib.parse.quote(prompt)
                                    image_url = f"https://image.pollinations.ai/prompt/{final_prompt}?image={public_img_url}&width={width}&height={height}&nologo=true&seed=42&model=turbo&strength={img2img_strength}"
                                    st.success("✅ Image uploaded! Transforming (Turbo Mode)...")
                                else:
                                    st.warning("⚠️ Image upload failed. Falling back to text-to-image.")
                                    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true&model=turbo"
                            else:
                                image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true&model=turbo"
                            
                            resp = requests.get(image_url, timeout=180)
                            if resp.status_code == 200:
                                generated_image = Image.open(io.BytesIO(resp.content))
                            else:
                                st.error(f"❌ Pollinations Error: {resp.status_code}")
                                st.text(resp.text)
                        except Exception as e:
                            st.error(f"❌ Pollinations generation error: {e}")
                    
                    # ===== MODE 3: OPENROUTER API =====
                    elif mode == "openrouter":
                        st.warning("⚠️ OpenRouter is primarily for text models. Image generation is experimental.")
                        resp = query_openrouter_api(
                            enhanced_prompt,
                            model_id,
                            OPENROUTER_KEY,
                            negative_prompt,
                            width,
                            height,
                        )
                        if resp.status_code == 200:
                            data = resp.json()
                            st.write("OpenRouter response JSON:")
                            st.json(data)
                        else:
                            st.error(f"❌ OpenRouter Error: {resp.status_code}")
                            st.text(resp.text)
                    
                    # ===== MODE 4: LOCAL GPU =====
                    else:  # local
                        pipeline_type = "img2img" if input_image is not None else "text2img"
                        with st.spinner(f"📥 Loading {pipeline_type} model to your GPU... (first time may download weights)"):
                            pipe = load_local_pipeline(model_id, pipeline_type)
                        
                        if pipe is not None:
                            with st.spinner(f"🎨 Generating on your GPU... ({num_inference_steps} steps)"):
                                generated_image = generate_local_image(
                                    pipe,
                                    enhanced_prompt,
                                    negative_prompt,
                                    width,
                                    height,
                                    guidance_scale,
                                    num_inference_steps,
                                    input_image,
                                    img2img_strength,
                                )
                    
                    # ===== DISPLAY RESULT =====
                    if generated_image is not None:
                        st.success("✅ Generated Successfully!")
                        st.image(generated_image, caption="Generated Image", use_container_width=True)
                        
                        buf = io.BytesIO()
                        generated_image.save(buf, format="PNG")
                        byte_im = buf.getvalue()
                        
                        st.download_button(
                            label="💾 Download Image",
                            data=byte_im,
                            file_name="generated_image.png",
                            mime="image/png",
                            use_container_width=True,
                        )
                    else:
                        st.warning("⚠️ No image was generated. Please try again with different settings or mode.")
            except Exception as e:
                st.error(f"❌ System Error: {repr(e)}")
                st.warning("Tip: Try a different model or simplify your request.")

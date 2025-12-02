# 🤖 GitHub Actions CI/CD - Explained

## What is This Workflow?

The `.github/workflows/docker-build.yml` file is a **CI/CD pipeline** that automatically:
1. Builds your Docker image
2. Pushes it to Docker Hub
3. Makes it available for deployment anywhere

## 🎯 When Does It Run?

The workflow triggers automatically when you:
- ✅ Push code to `main` or `master` branch
- ✅ Create a pull request to `main` or `master`
- ✅ Manually trigger it from GitHub Actions tab

## 📋 Step-by-Step Explanation

### Step 1: Checkout Repository
```yaml
- name: Checkout repository
  uses: actions/checkout@v4
```
**What it does**: Downloads your code from GitHub so the workflow can access it.

**Why**: The workflow runs on GitHub's servers, not your computer, so it needs to download your code first.

---

### Step 2: Set up Docker Buildx
```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3
```
**What it does**: Installs Docker Buildx, an advanced Docker builder.

**Why**: 
- Faster builds with caching
- Can build for multiple platforms (Linux, Windows, ARM)
- Better optimization

---

### Step 3: Log in to Docker Hub
```yaml
- name: Log in to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}
```
**What it does**: Logs into your Docker Hub account.

**Why**: You need to be logged in to push images to Docker Hub.

**Secrets Used**:
- `DOCKERHUB_USERNAME`: Your Docker Hub username (`parthibanktech3`)
- `DOCKERHUB_TOKEN`: Your Docker Hub access token (from https://hub.docker.com/settings/security)

---

### Step 4: Extract Metadata
```yaml
- name: Extract metadata
  id: meta
  uses: docker/metadata-action@v5
  with:
    images: parthibanktech3/ai-image-generator
    tags: |
      type=ref,event=branch
      type=ref,event=pr
      type=semver,pattern={{version}}
      type=raw,value=latest,enable={{is_default_branch}}
```
**What it does**: Creates tags for your Docker image.

**Tags Created**:
- `latest` - Always points to the newest version from main/master
- `main` or `master` - Tagged with branch name
- `pr-123` - If from a pull request
- Version numbers - If you use semantic versioning

**Example**: If you push to main, the image gets tagged as:
- `parthibanktech3/ai-image-generator:latest`
- `parthibanktech3/ai-image-generator:main`

---

### Step 5: Build and Push Docker Image
```yaml
- name: Build and push Docker image
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: ${{ steps.meta.outputs.tags }}
    labels: ${{ steps.meta.outputs.labels }}
    cache-from: type=registry,ref=parthibanktech3/ai-image-generator:buildcache
    cache-to: type=registry,ref=parthibanktech3/ai-image-generator:buildcache,mode=max
```
**What it does**: 
1. Builds your Docker image using the `Dockerfile`
2. Pushes it to Docker Hub
3. Uses caching for faster builds

**Parameters Explained**:
- `context: .` - Build from current directory
- `push: true` - Upload to Docker Hub (set to `false` to test without pushing)
- `tags` - Use the tags from Step 4
- `cache-from/cache-to` - Speed up builds by reusing layers

**Result**: Your image is now at `docker.io/parthibanktech3/ai-image-generator`

---

### Step 6: Display Image Digest
```yaml
- name: Image digest
  run: echo ${{ steps.meta.outputs.digest }}
```
**What it does**: Shows the SHA256 digest (unique fingerprint) of the built image.

**Why**: This digest uniquely identifies your image. You can use it to verify the exact version deployed.

**Example output**: `sha256:abc123def456...`

---

## 🔐 Required GitHub Secrets

You need to add these secrets to your GitHub repository:

### How to Add Secrets:
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret:

| Secret Name | Value | Where to Get It |
|-------------|-------|-----------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username (e.g., `parthibanktech3`) | Your Docker Hub account |
| `DOCKERHUB_TOKEN` | Your access token | https://hub.docker.com/settings/security |

### Getting Your Docker Hub Token:
1. Go to https://hub.docker.com/settings/security
2. Click **New Access Token**
3. Name it: `GitHub Actions`
4. Permissions: **Read, Write, Delete**
5. Click **Generate**
6. **Copy the token** (you can't see it again!)
7. Add it to GitHub Secrets as `DOCKERHUB_TOKEN`

---

## 🚀 How to Use This Workflow

### First Time Setup:
1. **Add GitHub Secrets** (see above)
2. **Push your code** to GitHub:
   ```bash
   git add .
   git commit -m "Add CI/CD workflow"
   git push origin main
   ```
3. **Watch it run**:
   - Go to your GitHub repo
   - Click **Actions** tab
   - You'll see the workflow running

### Every Time You Push:
1. Make changes to your code
2. Commit and push:
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```
3. GitHub Actions automatically:
   - Builds new Docker image
   - Pushes to Docker Hub
   - Tags as `latest`

---

## 📊 What Happens After the Workflow Runs?

### 1. Image is on Docker Hub
Your image is available at:
```
docker.io/parthibanktech3/ai-image-generator:latest
```

### 2. Anyone Can Pull It
```bash
docker pull parthibanktech3/ai-image-generator:latest
docker run -p 8501:8501 parthibanktech3/ai-image-generator:latest
```

### 3. You Can Deploy Anywhere
- Render
- Railway
- AWS
- Google Cloud
- Your own server
- Anywhere that supports Docker!

---

## 🔍 Monitoring the Workflow

### View Workflow Runs:
1. Go to your GitHub repository
2. Click **Actions** tab
3. Click on any workflow run to see details

### Check Build Logs:
- Click on a workflow run
- Click on the job name (`build-and-push`)
- Expand each step to see logs

### If Build Fails:
- Check the error message in logs
- Common issues:
  - Missing GitHub Secrets
  - Dockerfile syntax error
  - Network issues

---

## 💡 Advanced Tips

### Test Without Pushing:
Change `push: true` to `push: false` to test builds without uploading.

### Manual Trigger:
1. Go to **Actions** tab
2. Click **Build and Push Docker Image**
3. Click **Run workflow**
4. Select branch and click **Run workflow**

### Build for Specific Platforms:
Add to the build step:
```yaml
platforms: linux/amd64,linux/arm64
```

---

## 🎯 Summary

**What This Workflow Does**:
1. ✅ Automatically builds Docker image on every push
2. ✅ Pushes to `parthibanktech3/ai-image-generator`
3. ✅ Tags as `latest` and branch name
4. ✅ Uses caching for faster builds
5. ✅ Makes your app deployable anywhere

**What You Need to Do**:
1. Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` to GitHub Secrets
2. Push your code
3. That's it! Everything else is automatic

**Result**:
Your app is automatically built and ready to deploy anywhere that supports Docker!

---

## 📞 Troubleshooting

### "Error: Username and password required"
- Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` to GitHub Secrets

### "Error: denied: requested access to the resource is denied"
- Check your Docker Hub token has write permissions
- Verify the username is correct: `parthibanktech3`

### "Build failed"
- Check Dockerfile syntax
- Ensure all files are committed
- Check build logs for specific error

### "Workflow doesn't run"
- Ensure file is at `.github/workflows/docker-build.yml`
- Check you pushed to `main` or `master` branch
- Verify workflow syntax is correct

---

**Your CI/CD pipeline is ready! Just add the secrets and push your code!** 🚀
